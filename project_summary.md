# AI Document Q&A Project Summary

## Overview
This project is a small document-based question-answering application built with FastAPI, PostgreSQL, SQLAlchemy, and Ollama. It allows users to upload text-based files, store them in a database, split the content into chunks, and ask natural-language questions about the uploaded document.

## Main Components
- `app/main.py`: FastAPI API entry point and route definitions.
- `app/services.py`: business logic for extracting text, chunking content, retrieving data, and calling Ollama.
- `app/models.py`: SQLAlchemy models for `Document`, `DocumentChunk`, and `Conversation`.
- `app/database.py`: database engine and initialization logic.
- `app/config.py`: environment-driven configuration loader.
- `static/index.html`: browser-based frontend for uploading documents and asking questions.
- `docker-compose.yml`: orchestration for the app, PostgreSQL, and Ollama.
- `Dockerfile`: container build instructions for the backend.

## How It Works
1. The user uploads a supported file from the browser.
2. The backend extracts readable text from the file.
3. The text is split into chunks and saved in PostgreSQL.
4. The user asks a question.
5. The backend retrieves the relevant document chunks and sends them to Ollama.
6. Ollama returns an answer grounded in the uploaded document context.

## Strengths
- Easy to understand and run locally.
- Clean separation between frontend, backend, services, and persistence.
- Works without requiring a paid API key through local Ollama usage.
- Suitable for learning and prototype development.

## Possible Improvements
- Add semantic search using embeddings.
- Improve the frontend with a modern framework.
- Add support for more file types.
- Implement authentication, deletion, and richer chat features.
