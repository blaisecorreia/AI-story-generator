import uuid
from fastapi import APIRouter, Depends, HTTPException, cookies, Response, BackgroundTasks
from typing import Optional
from sqlalchemy.orm import Session
from datetime import datetime, timedelta

from backend.db.database import get_db, SessionLocal
from backend.models.story import Story, StoryNode
from backend.models.job import StoryJob
from backend.schemas.story import {
    CompleteStoryRequest, CompleteStoryResponse,CompleteStoryNodeResponse
}
from backend.schemas.job import StoryJobResponse

router = APIRouter(
    prefix="/story",
    tags=["story"]
)

def get_session_id(session_id: Optional[str] = cookies.Cookie(None)):
    if session_id is None:
        session_id = str(uuid.uuid4())
    return session_id


@router.post("/create", response_model=StoryJobResponse)
def create_story(
    background_tasks: BackgroundTasks,
    request: CompleteStoryRequest,
    response: Response,
    db: Session = Depends(get_db),
    session_id: str = Depends(get_session_id)
):
    response.set_cookie(key="session_id", value=session_id, httponly=True, max_age=3600)

    
