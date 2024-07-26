from src.users.views import test_view,create_user, login, logout


def setup_routes(app):
    app.router.add_route('GET', '/', test_view)
    app.router.add_route('POST', '/users', create_user)
    app.router.add_route('POST', '/login', login)
    app.router.add_route('POST', '/protected', logout )
