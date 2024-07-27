from aiohttp import web
from peewee_async import Manager
from aiohttp_security import check_authorized, authorized_userid
from .models import Location, Device, User, db

objects = Manager(db)


async def create_new_device(request) -> web.Response:
    await check_authorized(request)
    current_user = await authorized_userid(request)
    data = await request.json()
    location_obj, created = await objects.get_or_create(Location, name=data.get('location_id'))
    data['api_user_id'] = current_user
    data['location_id'] = location_obj
    device = await objects.create(Device, **data)
    device.set_password(data.get('password'))
    await objects.update(device)

    response_obj = {
        "id": device.id,
        "name": device.name,
        "type": device.type,
        "login": device.login,
        "location": device.location_id.name,
        "user": device.api_user_id.email}
    return web.json_response(response_obj, status=201)


async def obtain_my_devices(request) -> web.Response:
    await check_authorized(request)
    current_user = await authorized_userid(request)
    user_devices = await objects.execute(Device.select(Device, User).join(User).where(Device.api_user_id == current_user))
    response_obj = [{
        "id": device.id,
        "name": device.name,
        "type": device.type,
        "login": device.login,
        "location": device.location_id.name,
        "user": device.api_user_id.email
    } for device in user_devices]
    return web.json_response(response_obj, status=200)
