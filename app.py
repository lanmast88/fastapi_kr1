from fastapi import FastAPI
from fastapi.responses import FileResponse
from models import User, Feedback
app = FastAPI()

me = User(name="Глеб Ушаков", age=19)
feadbacks = []

@app.get("/", response_class=FileResponse)
def root():
    return FileResponse("index.html")

@app.post("/calculate")
def calculate(num1: int, num2:int):
    return {"result": num1 + num2}

@app.get("/users")
def get_users():
    return [me]

@app.post("/user")
def is_18_user(user: User):
    adult = user.age >= 18
    return {
        "name": user.name,
        "age": user.age,
        "is_adult": adult
    }

@app.post("/feedback")
def add_feedback(feedback: Feedback):
    feadbacks.append(feedback)
    return {"message": f"Спасибо, {feedback.name}! Ваш отзыв сохранён."}