from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class AnswerRequest(BaseModel):
    answer: str


@router.get("/question")
def get_question():
    return { "question": "What is your quest?" }

ANSWER="I seek the holy grail"

@router.post("/answer")
def post_answer(request: AnswerRequest):
    correct = request.answer.strip().lower() == ANSWER.strip().lower()
    return { 
        "correct": correct,
        "message": "yea u do" if correct else "hell nah",
    }
