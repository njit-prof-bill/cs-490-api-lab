from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class AnswerRequest(BaseModel):
    answer: str


@router.get("/question")
def get_question():
    return {
        "question": "What is the air speed of unladen swallow?"
    }

ANSWER = "African or European?"

@router.post("/answer")
def post_answer(request: AnswerRequest):
    correct = request.answer.strip().lower() == ANSWER.strip().lower()

    return {
        "correct": correct,
        "message": "You may pass." if correct else "Into the Gorge of Eternal Peril!",
    }
