from openai import OpenAI 
from dotenv import load_dotenv
from fastapi import FastAPI
from app.schemas import ChatInput, ChatResponse
from app.embedding import get_embedding

load_dotenv()  # Load environment variables from .env file

client = OpenAI()
app = FastAPI()

@app.post("/chat", response_model=ChatResponse)
def chats_from_chatgpt(chat_input: ChatInput):
    embedding = get_embedding(chat_input.message)
    print(embedding)

    response = client.responses.create(
        model = "gpt-4.1-mini",
        input = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": chat_input.message},
        ],
    )
    return ChatResponse(response=response.output_text)