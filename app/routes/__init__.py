# app/routes/__init__.py

from fastapi import APIRouter
from app.routes.auth import router as auth_router

router = APIRouter()
router.include_router(auth_router, tags=["auth"])
