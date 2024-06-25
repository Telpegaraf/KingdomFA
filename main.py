from contextlib import asynccontextmanager
from fastapi import FastAPI

from api_v1.routers import domain, god, user, auth, general, character_class, equipment

app = FastAPI()
app.include_router(domain.domain_router)
app.include_router(god.god_router)
app.include_router(user.user_router)
app.include_router(general.general_router)
app.include_router(auth.auth_router)
app.include_router(character_class.character_class_router)
app.include_router(equipment.equipment_router)


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
