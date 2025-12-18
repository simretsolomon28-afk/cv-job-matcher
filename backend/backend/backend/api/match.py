from fastapi import APIRouter
from pydantic import BaseModel
from services.matcher import calculate_match

router = APIRouter()

class MatchRequest(BaseModel):
    cv_text: str
    job_text: str

@router.post("/match")
def match_cv_job(data: MatchRequest):
    return calculate_match(data.cv_text, data.job_text)
