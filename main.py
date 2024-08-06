from contextlib import asynccontextmanager
from fastapi import FastAPI
from routers import include_routers
import logging

from action.create_super_user import create_superuser

app = FastAPI()
include_routers(app)
logging.basicConfig(
    level=logging.DEBUG,
    filename='kingdom.log',
    datefmt="%Y-%m-%d %H:%M:%S",
    format="[%(asctime)s.%(msecs)03d] %(module)10s:%(lineno)-3d %(levelname)-7s - %(message)s",
)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_superuser()
    yield
