from fastapi import APIRouter
from app.api.routes.user import router as hedgehogs_router


router = APIRouter()
router.include_router(hedgehogs_router, prefix="/user", tags=["user"])
