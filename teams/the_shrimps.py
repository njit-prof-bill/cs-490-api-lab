from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

question = "What is your name"
answer = "The Shrimps"


class AnswerRequest(BaseModel):
    answer: str


@router.get("/question")
def get_question():
    return {
        "question": question
    }


@router.post("/answer")
def post_answer(request: AnswerRequest):
    correct = request.answer.strip().lower() == answer.lower()
    return {
        "correct": correct,
        "message": "You are correct!" if correct else "Sorry, that's not correct."
    }
