# Database Schema (PostgreSQL)

## users
- id (UUID, PK)
- email (unique)
- mobile_number (unique nullable)
- password_hash
- full_name
- is_active
- mfa_enabled
- created_at

## documents
- id (UUID, PK)
- owner_id (FK users.id)
- filename, mime_type
- encrypted_object_key
- encrypted_data_key
- tags (JSONB)
- ai_summary (TEXT)
- created_at

## refresh_tokens
- id (UUID)
- user_id (FK users.id)
- jti (unique)
- is_revoked
- expires_at

## audit_logs
- id (UUID)
- actor_id (UUID nullable)
- action
- resource_type, resource_id
- ip_address, user_agent
- metadata (JSONB)
- created_at
