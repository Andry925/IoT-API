import json
from aiohttp import web
from aiohttp_security import AbstractAuthorizationPolicy, remember, forget, check_authorized
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
                return user.email
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
        return web.Response(text="User created successfully", status=200)

    except Exception as e:
        response_obj = {"failed": str(e)}
        return web.Response(text=json.dumps(response_obj), status=500)


async def login(request) -> web.Response:
    try:
        data = await request.json()
        password = data.get("password")
        email = data.get("email")
        user = await objects.get(User, email=email)
        if user and user.check_password(password):
            await remember(request, web.Response(), email)
            response_obj = {"user": "some"}
            return web.Response(text=json.dumps(response_obj), status=200)

    except Exception as e:
        response_obj = {"reason": str(e)}
        return web.Response(text=json.dumps(response_obj), status=500)


async def logout(request) -> web.Response:
    try:
        await check_authorized(request)
        response = web.Response(text="You are logged out")
        await forget(request, response)
        return response

    except Exception as e:
        response_obj = {"message": str(e)}
        return web.Response(text=json.dumps(response_obj), status=401)
