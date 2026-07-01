import uuid 
from qdrant_client import QdrantClient
from qdrant_client.http.models import PointStruct, VectorParams, Distance
from app.embedding import get_embedding
from app.schemas import EmbeddingResponse, UpsertPointRequest

qdrant_client = QdrantClient(host="localhost", port = 6333)

EMBED_DIM = 1024
COLLECTION_NAME = "semantic_memory"

if not qdrant_client.collection_exists(collection_name=COLLECTION_NAME): 
    qdrant_client.create_collection(
        collection_name=COLLECTION_NAME,
        vectors_config = VectorParams(size=EMBED_DIM, distance=Distance.COSINE)
    )

def upsert_point(text: UpsertPointRequest, embedding: EmbeddingResponse) -> None:
    points = [
        PointStruct(
            id=str(uuid.uuid4()), 
            vector=embedding.embedding, 
            payload = {"text": text.text}
        ) for text, embedding in zip([text], [embedding])
    ]
    qdrant_client.upsert(
        collection_name=COLLECTION_NAME,
        points=points
    )

def ingest(): 
    pass