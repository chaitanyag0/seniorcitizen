from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class DocumentOut(BaseModel):
    id: UUID
    filename: str
    mime_type: str
    tags: dict
    ai_summary: str | None
    created_at: datetime


class ShareLinkRequest(BaseModel):
    document_id: UUID
    expires_in_minutes: int = 30
    password: str | None = None
