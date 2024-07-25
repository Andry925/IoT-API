from aiohttp import web
from .routes import setup_routes


async def create_app() -> web.Application:
    app = web.Application()
    setup_routes(app)
    return app
