import requests
from app.embedding import get_embedding

response = requests.get("https://localhost:8000/chat")

print(response.status_code)
response_json = response.json()
print(get_embedding(response_json["response"]))