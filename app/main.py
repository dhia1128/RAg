from pathlib import Path

from fastapi import FastAPI, File, HTTPException, UploadFile
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session

from app.database import SessionLocal, init_db
from app.schemas import AskRequest, AskResponse, DocumentItem, UploadResponse
from app.services import DocumentService

app = FastAPI(title="AI Document Q&A", version="0.1.0")

BASE_DIR = Path(__file__).resolve().parent.parent
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")


@app.get("/")
async def root() -> FileResponse:
    return FileResponse(BASE_DIR / "static" / "index.html")


@app.on_event("startup")
def startup_event() -> None:
    init_db()


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/documents", response_model=list[DocumentItem])
def get_documents() -> list[DocumentItem]:
    db: Session = SessionLocal()
    try:
        service = DocumentService(db)
        documents = service.list_documents()
        return documents
    finally:
        db.close()


@app.post("/documents/upload", response_model=UploadResponse)
async def upload_document(file: UploadFile = File(...)) -> UploadResponse:
    if not file.filename:
        raise HTTPException(status_code=400, detail="A file is required.")

    content = await file.read()
    db: Session = SessionLocal()
    try:
        service = DocumentService(db)
        extracted_text = service.extract_text(content, file.filename)
        if not extracted_text.strip():
            raise HTTPException(status_code=400, detail="No readable text found in the uploaded file.")

        document = service.create_document(
            title=file.filename,
            file_name=file.filename,
            content_type=file.content_type or "application/octet-stream",
            content=extracted_text,
        )

        chunks_created = len(service.chunk_text(extracted_text))
        return UploadResponse(
            message="Document uploaded successfully.",
            document_id=document.id,
            chunks_created=chunks_created,
        )
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    finally:
        db.close()


@app.post("/ask", response_model=AskResponse)
async def ask_question(payload: AskRequest) -> AskResponse:
    db: Session = SessionLocal()
    try:
        service = DocumentService(db)
        result = service.ask_question(payload.question, payload.document_id)
        return AskResponse(
            document_id=result["document_id"],
            question=result["question"],
            answer=result["answer"],
        )
    except RuntimeError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    finally:
        db.close()


@app.exception_handler(Exception)
async def global_exception_handler(_, exc: Exception) -> JSONResponse:
    return JSONResponse(status_code=500, content={"detail": str(exc)})
