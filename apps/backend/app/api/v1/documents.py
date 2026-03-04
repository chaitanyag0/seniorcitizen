from uuid import UUID

from fastapi import APIRouter, Depends, File, Form, HTTPException, Request, UploadFile, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.deps import get_current_user_id
from app.db.session import get_db
from app.models.document import Document
from app.schemas.document import DocumentOut, ShareLinkRequest
from app.security.encryption import EnvelopeEncryptionService
from app.services.ai import infer_document_tags
from app.services.audit import record_audit_event

router = APIRouter(prefix="/documents", tags=["documents"])


@router.get("", response_model=list[DocumentOut])
async def list_documents(
    user_id: str = Depends(get_current_user_id), db: AsyncSession = Depends(get_db)
) -> list[DocumentOut]:
    rows = await db.scalars(select(Document).where(Document.owner_id == UUID(user_id)))
    return [DocumentOut.model_validate(r, from_attributes=True) for r in rows.all()]


@router.post("/upload", response_model=DocumentOut)
async def upload_document(
    request: Request,
    file: UploadFile = File(...),
    folder: str = Form(default="root"),
    user_id: str = Depends(get_current_user_id),
    db: AsyncSession = Depends(get_db),
) -> DocumentOut:
    data = await file.read()
    encrypted, wrapped_dek = EnvelopeEncryptionService.encrypt_bytes(data)
    tags = infer_document_tags(file.filename, file.content_type or "application/octet-stream")

    document = Document(
        owner_id=UUID(user_id),
        filename=file.filename,
        mime_type=file.content_type or "application/octet-stream",
        encrypted_object_key=f"vault/{user_id}/{file.filename}",
        encrypted_data_key=wrapped_dek,
        tags={**tags, "folder": folder, "size": len(encrypted)},
    )
    db.add(document)
    await db.flush()

    await record_audit_event(
        db,
        actor_id=user_id,
        action="document.upload",
        resource_type="document",
        resource_id=str(document.id),
        ip_address=request.client.host if request.client else "unknown",
        user_agent=request.headers.get("user-agent", "unknown"),
    )
    return DocumentOut.model_validate(document, from_attributes=True)


@router.post("/share")
async def generate_share_link(
    payload: ShareLinkRequest,
    user_id: str = Depends(get_current_user_id),
    db: AsyncSession = Depends(get_db),
) -> dict:
    document = await db.scalar(select(Document).where(Document.id == payload.document_id))
    if not document or str(document.owner_id) != user_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Document not found")

    # In production: sign URL using dedicated share-token service with one-time scope.
    return {
        "url": f"https://locker.example/share/{document.id}",
        "expires_in_minutes": payload.expires_in_minutes,
        "password_protected": bool(payload.password),
    }
