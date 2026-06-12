from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class AnswerRequest(BaseModel):
    answer: str


@router.get("/question")
def get_question():
 return{
        "question": "What is the capital of Assyria?"
    }

ANSWER = "Nineveh"
    
@router.post("/answer")
def post_answer(request: AnswerRequest):
    correct = request.answer.strip().lower() == ANSWER.strip().lower()

    return {
        "correct": correct,
        "message": "You may pass." if correct else "Into the Gorge of Eternal Peril!",
    }