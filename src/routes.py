from src.users.views import test_view,create_user, login, logout
from src.devices.views import create_new_device, obtain_my_devices


def setup_routes(app):
    app.router.add_route('GET', '/', test_view)
    app.router.add_route('POST', '/users', create_user)
    app.router.add_route('POST', '/login', login)
    app.router.add_route('POST', '/protected', logout )
    app.router.add_route('POST', '/new-device', create_new_device)
    app.router.add_route('GET', '/devices', obtain_my_devices)
