import base64
import os

from cryptography.hazmat.primitives.ciphers.aead import AESGCM


class EnvelopeEncryptionService:
    """
    Security architecture logic:
    1) Generate random Data Encryption Key (DEK) per file.
    2) Encrypt bytes client-side or at API edge with AES-256-GCM using DEK.
    3) Wrap DEK with KMS-managed Key Encryption Key (KEK) (simulated here).
    4) Store encrypted blob in S3 and wrapped DEK in PostgreSQL metadata.
    5) Decrypt only after policy + authZ checks (zero-trust decision point).
    """

    @staticmethod
    def encrypt_bytes(raw: bytes) -> tuple[bytes, str]:
        dek = AESGCM.generate_key(bit_length=256)
        aes = AESGCM(dek)
        nonce = os.urandom(12)
        encrypted = nonce + aes.encrypt(nonce, raw, None)
        wrapped_dek = base64.b64encode(dek).decode("utf-8")
        return encrypted, wrapped_dek

    @staticmethod
    def decrypt_bytes(ciphertext: bytes, wrapped_dek: str) -> bytes:
        dek = base64.b64decode(wrapped_dek)
        nonce = ciphertext[:12]
        payload = ciphertext[12:]
        aes = AESGCM(dek)
        return aes.decrypt(nonce, payload, None)
