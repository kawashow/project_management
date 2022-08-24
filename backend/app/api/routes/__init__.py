from fastapi import APIRouter
from app.api.routes.user import router as user_router
from app.api.routes.issue import router as issue_router

router = APIRouter()
router.include_router(user_router, prefix="/user", tags=["user"])
router.include_router(issue_router, prefix="/issue", tags=["issue"])

