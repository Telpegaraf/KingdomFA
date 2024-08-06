from contextlib import asynccontextmanager
from fastapi import FastAPI
from routers import include_routers

from action.create_super_user import create_superuser

app = FastAPI()
include_routers(app)


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_superuser()
    yield
