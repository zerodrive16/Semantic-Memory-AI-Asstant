from openai import OpenAI 
from dotenv import load_dotenv
from fastapi import FastAPI

load_dotenv()  # Load environment variables from .env file

client = OpenAI()
app = FastAPI()

@app.post("/chat")
def chats_from_chatgpt(chat_input: str): 
    response = client.responses.create(
        model = "gpt-4.1-mini",
        input = chat_input
    )
    return response.output_text