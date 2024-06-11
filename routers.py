from fastapi import APIRouter
from api_v1.gods.views import gods_router

router = APIRouter
router.include_router(gods_router)
