from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    app_name: str = "SentinelLocker"
    env: str = "dev"
    cors_origins: list[str] = ["http://localhost:3000"]

    postgres_dsn: str = Field(
        default="postgresql+asyncpg://locker:locker@localhost:5432/locker"
    )
    redis_url: str = "redis://localhost:6379/0"

    jwt_secret: str = "replace-in-production"
    jwt_algorithm: str = "HS256"
    access_token_ttl_seconds: int = 900
    refresh_token_ttl_seconds: int = 1209600

    s3_bucket: str = "sentinel-locker-docs"
    aws_region: str = "us-east-1"


settings = Settings()
