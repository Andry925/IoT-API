from aiohttp import web


async def test_view(request) -> web.Response:
    return web.Response(text="Initial config")
