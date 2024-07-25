from src.users.views import test_view


def setup_routes(app):
    app.router.add_route('GET', '/', test_view)
