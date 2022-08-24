from fastapi import APIRouter
from typing import List

router = APIRouter()

@router.get("/")
async def get_all_issues() -> List[dict]:
    """
    retrun all issue
    """
    issues = [
        {"id": 1, "description": "memo", "title": "test title", "createdby": "test user"}
    ]

    return issues

@router.post("/")
async def create_issue():
    pass
