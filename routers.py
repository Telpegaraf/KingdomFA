from fastapi import APIRouter
from apps.gods.views import gods_router

router = APIRouter
router.include_router(gods_router)
