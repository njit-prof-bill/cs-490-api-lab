from fastapi import APIRouter
from pydantic import BaseModel


router = APIRouter()

QUESTION = "What is your name"
ANSWER = "The Shrimps"


class AnswerRequest(BaseModel):
    answer: str


@router.get("/question")
def get_question():
    return {"question": QUESTION}


@router.post("/answer")
def post_answer(request: AnswerRequest):
    correct = request.answer.strip().lower() == ANSWER.lower()
    return {
        "correct": correct,
        "message": "You are correct!" if correct else "Sorry, that's not correct."
    }
