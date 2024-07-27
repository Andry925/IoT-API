from src.users.views import test_view,create_user, login, logout
from src.devices.views import create_new_device, obtain_my_devices, edit_device, delete_device


def setup_routes(app):
    app.router.add_route('GET', '/', test_view)
    app.router.add_route('POST', '/register', create_user)
    app.router.add_route('POST', '/login', login)
    app.router.add_route('POST', '/logout', logout )
    app.router.add_route('POST', '/new-device', create_new_device)
    app.router.add_route('GET', '/devices', obtain_my_devices)
    app.router.add_route('PUT', '/edit-device/{device_id}', edit_device),
    app.router.add_route('DELETE', '/delete-device/{device_id}', delete_device)
