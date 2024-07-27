import json
from aiohttp import web
from aiohttp_security import AbstractAuthorizationPolicy, remember, forget, check_authorized
from peewee import DoesNotExist, IntegrityError
from peewee_async import Manager
from .models import User, db

objects = Manager(db)


async def test_view(request) -> web.Response:
    return web.Response(text="Initial config")


class AuthorizationPolicy(AbstractAuthorizationPolicy):

    async def authorized_userid(self, identity):
        try:
            user = await objects.get(User, email=identity)
            if user:
                return user.id
            return None

        except Exception as e:
            response_obj = {"failed": str(e)}
            return web.Response(text=json.dumps(response_obj), status=500)

    async def permits(self, identity, permission, context=None):
        return True


async def create_user(request) -> web.Response:
    try:
        data = await request.json()
        if not data:
            return web.Response(text="Missing user data", status=400)

        user = await objects.create(User, **data)
        user.set_password(data.get("password"))
        await objects.update(user)
        return web.Response(text="User created successfully", status=201)
    except IntegrityError:
        return web.Response(text="User creation failed due to integrity error", status=400)
    except Exception as e:
        return web.Response(text=json.dumps({"failed": str(e)}), status=500)

async def login(request) -> web.Response:
    try:
        data = await request.json()
        email = data.get("email")
        password = data.get("password")

        if not email or not password:
            return web.Response(text="Email and password must be provided", status=400)

        user = await objects.get(User, email=email)
        if user and user.check_password(password):
            response = web.Response(text=json.dumps({"user": "some"}))
            await remember(request, response, email)
            return response
        return web.Response(text="Invalid email or password", status=400)
    except DoesNotExist:
        return web.Response(text="Invalid email or password", status=400)
    except Exception as e:
        return web.Response(text=json.dumps({"reason": str(e)}), status=500)

async def logout(request) -> web.Response:
    try:
        await check_authorized(request)
        response = web.Response(text="You are logged out")
        await forget(request, response)
        return response
    except web.HTTPUnauthorized:
        return web.Response(text=json.dumps({"message": "Unauthorized"}), status=401)
    except Exception as e:
        return web.Response(text=json.dumps({"message": str(e)}), status=500)
