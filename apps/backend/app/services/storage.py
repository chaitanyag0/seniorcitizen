import uuid

import boto3

from app.core.config import settings


class StorageService:
    def __init__(self) -> None:
        self.client = boto3.client("s3", region_name=settings.aws_region)

    def put_encrypted_document(self, payload: bytes, owner_id: str) -> str:
        key = f"documents/{owner_id}/{uuid.uuid4()}.bin"
        self.client.put_object(Bucket=settings.s3_bucket, Key=key, Body=payload)
        return key
