from pydantic import BaseModel


class ChatInput(BaseModel):
    message: str

class ChatResponse(BaseModel):
    response: str

class EmbeddingResponse(BaseModel):
    embedding: list[float]

class UpsertPointRequest(BaseModel):
    text: str
