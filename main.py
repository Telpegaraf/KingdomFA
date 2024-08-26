from contextlib import asynccontextmanager
from fastapi import FastAPI
from routers import include_routers
import logging
from config_logs import configure_logging
from action.create_super_user import create_superuser
from sqladmin import Admin
from database import db_helper
from admin.admin_panel import UserAdmin, AdminAuth
from core.config import settings

configure_logging()
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_superuser()
    yield

app = FastAPI(lifespan=lifespan)
include_routers(app)


def create_admin(app):
    authentication_backend = AdminAuth(secret_key=settings.get_secret_key)
    admin = Admin(app=app, engine=db_helper.engine, authentication_backend=authentication_backend)
    admin.add_view(UserAdmin)

    return admin


create_admin(app)
