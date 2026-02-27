from pydantic import BaseModel, Field, field_validator

class User(BaseModel):
    name: str
    age: int

class Feedback(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    message: str = Field(min_length=10, max_length=500)

    @field_validator("message")
    def validate_message(cls, message: str):
        banned_words = ["кринж", "рофл", "вайб"]
        message_lower = message.lower()
        for word in banned_words:
            if word in message_lower:
                raise ValueError("Использование недопустимых слов")
        return message