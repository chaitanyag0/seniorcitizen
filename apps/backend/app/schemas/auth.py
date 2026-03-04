from pydantic import BaseModel, EmailStr, Field


class RegisterRequest(BaseModel):
    full_name: str = Field(min_length=2, max_length=120)
    email: EmailStr
    password: str = Field(min_length=12, max_length=128)
    mobile_number: str | None = Field(default=None, min_length=10, max_length=20)


class LoginRequest(BaseModel):
    email: EmailStr
    password: str
    otp_code: str | None = Field(default=None, min_length=6, max_length=8)


class TokenPair(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"
