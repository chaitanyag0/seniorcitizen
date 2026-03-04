from datetime import UTC, datetime

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.models.refresh_token import RefreshToken
from app.models.user import User
from app.schemas.auth import LoginRequest, RegisterRequest, TokenPair
from app.security.password import hash_password, verify_password
from app.core.config import settings
from app.security.tokens import issue_access_token, issue_refresh_token

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register", response_model=TokenPair)
async def register(payload: RegisterRequest, db: AsyncSession = Depends(get_db)) -> TokenPair:
    existing = await db.scalar(select(User).where(User.email == payload.email))
    if existing:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Email already exists")

    user = User(
        email=payload.email,
        full_name=payload.full_name,
        password_hash=hash_password(payload.password),
        mobile_number=payload.mobile_number,
    )
    db.add(user)
    await db.flush()

    access = issue_access_token(str(user.id))
    refresh, jti, expires = issue_refresh_token(str(user.id))
    db.add(RefreshToken(user_id=user.id, jti=jti, expires_at=expires))
    await db.commit()
    return TokenPair(access_token=access, refresh_token=refresh)


@router.post("/login", response_model=TokenPair)
async def login(payload: LoginRequest, db: AsyncSession = Depends(get_db)) -> TokenPair:
    user = await db.scalar(select(User).where(User.email == payload.email))
    if not user or not verify_password(payload.password, user.password_hash):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    access = issue_access_token(str(user.id))
    refresh, jti, expires = issue_refresh_token(str(user.id))
    db.add(RefreshToken(user_id=user.id, jti=jti, expires_at=expires))
    await db.commit()
    return TokenPair(access_token=access, refresh_token=refresh)


@router.post("/refresh", response_model=TokenPair)
async def refresh_token(refresh_token: str, db: AsyncSession = Depends(get_db)) -> TokenPair:
    from jose import jwt

    payload = jwt.decode(refresh_token, settings.jwt_secret, algorithms=[settings.jwt_algorithm])
    jti = payload["jti"]
    token = await db.scalar(select(RefreshToken).where(RefreshToken.jti == jti))
    if not token or token.is_revoked or token.expires_at < datetime.now(UTC):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid refresh token")

    token.is_revoked = True
    new_access = issue_access_token(payload["sub"])
    new_refresh, new_jti, expires = issue_refresh_token(payload["sub"])
    db.add(RefreshToken(user_id=token.user_id, jti=new_jti, expires_at=expires))
    await db.commit()
    return TokenPair(access_token=new_access, refresh_token=new_refresh)
