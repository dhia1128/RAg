# AI Document Q&A with FastAPI, PostgreSQL, and Ollama

This project is a simple AI-powered document Q&A application built with FastAPI and PostgreSQL. It allows you to upload text-based documents, store them in PostgreSQL, and ask questions about them using a local LLM powered by Ollama.

## Features

- Upload `.txt`, `.pdf`, and `.docx` documents
- Extract text from uploaded files
- Store document metadata and content chunks in PostgreSQL
- Ask natural-language questions about uploaded files
- Use a local LLM with Ollama instead of a paid API key
- Access a browser-based UI to upload files and test the app
- Use FastAPI Swagger UI for API testing

## Tech Stack

- FastAPI
- PostgreSQL
- SQLAlchemy
- Python
- Ollama (local LLM)
- HTML / JavaScript frontend

## Project Structure

- `.env` — environment variables
- `requirements.txt` — Python dependencies
- `app/` — FastAPI application code
- `static/index.html` — browser UI
- `README.md` — setup and usage guide

## Prerequisites

Before running the project, make sure you have:

- Python 3.10+
- PostgreSQL installed and running
- Ollama installed and configured

## Setup

### 1. Create and activate a virtual environment

On Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 2. Install dependencies

```powershell
pip install -r requirements.txt
```

### 3. Configure environment variables

Edit the `.env` file with your local PostgreSQL settings.

Example:

```env
APP_NAME=AI Document Q&A
APP_ENV=development
SECRET_KEY=change-me-in-production
HOST=0.0.0.0
PORT=8000

POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=docqa_db
POSTGRES_USER=postgres
POSTGRES_PASSWORD=your_password
DATABASE_URL=postgresql+psycopg://postgres:your_password@localhost:5432/docqa_db

OPENAI_API_KEY=
OPENAI_MODEL=llama3.2
```

### 4. Start PostgreSQL

Make sure PostgreSQL is running locally and that the database `docqa_db` exists.

### 5. Pull the local model with Ollama

```powershell
ollama pull llama3.2
```

### 6. Run the application

```powershell
uvicorn app.main:app --reload
```

### 7. Open the app

Browser UI:

```text
http://127.0.0.1:8000/
```

API docs:

```text
http://127.0.0.1:8000/docs
```

## How it works

1. Upload a document from the browser page.
2. The backend extracts the text from the file.
3. The text is split into chunks and stored in PostgreSQL.
4. You ask a question about the uploaded document.
5. The system sends the document context to Ollama.
6. The LLM generates an answer based only on the document content.

## Current API Endpoints

- `GET /health`
- `GET /documents`
- `POST /documents/upload`
- `POST /ask`

## Notes

- This version uses a local Ollama model, so no OpenAI API key is required.
- The browser UI is served from the `static` folder.
- The project is a good starting point for a document Q&A or RAG-style application.

## Optional Next Improvements

- Add chat history
- Add document deletion and update features
- Add user authentication
- Add a real frontend framework such as React or Next.js
