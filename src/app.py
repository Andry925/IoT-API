import aiohttp_security
import aiohttp_session
from aiohttp import web
from aiohttp_security import SessionIdentityPolicy
from aiohttp_session.cookie_storage import EncryptedCookieStorage
from cryptography import fernet
from .routes import setup_routes
from src.users.views import AuthorizationPolicy


async def create_app() -> web.Application:
    app = web.Application()
    fernet_key = fernet.Fernet.generate_key()
    secret_key = fernet.Fernet(fernet_key)
    aiohttp_session.setup(app, EncryptedCookieStorage(secret_key))
    policy = SessionIdentityPolicy()
    auth_policy = AuthorizationPolicy()
    aiohttp_security.setup(app, policy, auth_policy)
    setup_routes(app)
    return app