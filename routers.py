from fastapi import APIRouter
from apps.gods.router import gods_router

router = APIRouter
router.include_router(gods_router)
