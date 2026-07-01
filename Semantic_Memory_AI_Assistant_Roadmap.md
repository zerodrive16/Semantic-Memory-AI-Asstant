# Semantic Memory AI Assistant

## Projektziel

Ein KI-Assistent mit Kurzzeit- und Langzeitgedächtnis, der relevante
Informationen dauerhaft speichert, situationsabhängig wiederfindet,
reflektiert und unwichtige Informationen vergisst.

## Mehrwert

-   Praktisches End-to-End-KI-Projekt
-   Verbindet LLMs, Retrieval, Memory und Agenten
-   Lernt moderne Architekturkonzepte statt nur RAG
-   Sehr gutes Portfolio-Projekt

## Technologien

-   Python
-   FastAPI
-   LLM (OpenAI oder Ollama)
-   Embeddings
-   Qdrant
-   Redis
-   LangGraph (später)
-   Graph Memory
-   Docker
-   Git/GitHub

## Zielarchitektur

``` text
User
  │
FastAPI
  │
Conversation Manager
 ├── Short-Term Memory (Redis)
 ├── Long-Term Memory (Qdrant)
 ├── Retrieval
 └── LLM
        │
     Antwort
```

# Roadmap

## Phase 1 -- Chatbot

### Lernen

-   Python
-   FastAPI
-   LLM API
-   Prompting \### Teilprojekt
-   Einfacher Chatbot mit API

## Phase 2 -- Embeddings

### Lernen

-   Embeddings
-   Cosine Similarity \### Teilprojekt
-   Jede Nachricht als Embedding erzeugen

## Phase 3 -- Vector Database

### Lernen

-   Qdrant
-   Similarity Search \### Teilprojekt
-   Embeddings dauerhaft speichern und abrufen

## Phase 4 -- Memory-System

### Lernen

-   Redis
-   Kurzzeit-/Langzeitgedächtnis \### Teilprojekt
-   Memory Manager

## Phase 5 -- Importance Scoring

### Lernen

-   Klassifikation
-   LLM-basierte Bewertung \### Teilprojekt
-   Nur wichtige Erinnerungen speichern

## Phase 6 -- Retrieval

### Lernen

-   Hybrid Search
-   BM25
-   Re-Ranking \### Teilprojekt
-   Retrieval-Pipeline verbessern

## Phase 7 -- Memory Compression

### Lernen

-   Summarization \### Teilprojekt
-   Erinnerungen verdichten

## Phase 8 -- Reflection

### Lernen

-   Reflection Pattern \### Teilprojekt
-   Erkenntnisse aus Gesprächen ableiten

## Phase 9 -- Forgetting

### Lernen

-   Scoring
-   Retention \### Teilprojekt
-   Veraltete Erinnerungen löschen

## Phase 10 -- Graph Memory

### Lernen

-   Wissensgraphen \### Teilprojekt
-   Beziehungen zwischen Entitäten speichern

## Phase 11 -- Multi-Agent

### Lernen

-   LangGraph
-   Agenten \### Teilprojekt
-   Memory-, Search- und Planning-Agent kombinieren

## Abschluss

Am Ende entsteht **ein einziges Projekt**, das in jeder Phase erweitert
wird. Jede Phase sollte in Git versioniert werden, sodass der
Entwicklungsfortschritt nachvollziehbar bleibt.
