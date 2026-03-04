# Backend API Design (v1)

## Auth
- `POST /api/v1/auth/register`: register via email/password (+ optional mobile)
- `POST /api/v1/auth/login`: login with email/password + OTP in production
- `POST /api/v1/auth/refresh`: rotate refresh token and issue new token pair

## Documents
- `GET /api/v1/documents`: list current user's docs
- `POST /api/v1/documents/upload`: upload doc; encrypted + AI-tagged
- `POST /api/v1/documents/share`: create expiring share link with optional password

## Admin
- `GET /api/v1/admin/metrics`: security/storage/usage metrics

## Security API Patterns
- OAuth2/JWT bearer for protected routes
- MFA step-up required for high-risk actions (share/download/delete)
- Rate limiting at API gateway + login endpoints
- Idempotency keys for critical writes
