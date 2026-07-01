from openai import OpenAI 
from dotenv import load_dotenv


load_dotenv()  # Load environment variables from .env file
client = OpenAI()

def get_embedding(text: str) -> list[float]:
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )
    return response.data[0].embedding