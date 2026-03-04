import uuid
from datetime import UTC, datetime, timedelta

from jose import jwt

from app.core.config import settings


def _build_token(subject: str, ttl_seconds: int, token_type: str) -> tuple[str, str, datetime]:
    now = datetime.now(UTC)
    expires = now + timedelta(seconds=ttl_seconds)
    jti = str(uuid.uuid4())
    payload = {
        "sub": subject,
        "jti": jti,
        "iat": int(now.timestamp()),
        "exp": int(expires.timestamp()),
        "typ": token_type,
    }
    token = jwt.encode(payload, settings.jwt_secret, algorithm=settings.jwt_algorithm)
    return token, jti, expires


def issue_access_token(subject: str) -> str:
    token, _, _ = _build_token(subject, settings.access_token_ttl_seconds, "access")
    return token


def issue_refresh_token(subject: str) -> tuple[str, str, datetime]:
    return _build_token(subject, settings.refresh_token_ttl_seconds, "refresh")
