from contextlib import asynccontextmanager
from fastapi import FastAPI
from routers import include_routers
import logging

from config_logs import configure_logging
from action.create_super_user import create_superuser

app = FastAPI()
include_routers(app)

configure_logging()
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_superuser()
    yield
