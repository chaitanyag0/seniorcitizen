# SentinelLocker - Government-Grade Digital Document Locker

SentinelLocker is a cloud-native, zero-trust digital document locker inspired by DigiLocker, designed for enterprise/government-grade security, premium UX, and microservice-ready scalability.

## Monorepo Structure

- `apps/frontend`: Next.js 14 + TailwindCSS + Framer Motion premium UI
- `apps/backend`: FastAPI service with JWT rotation, MFA hooks, audit logs, document encryption pipeline
- `infra`: Docker Compose, deployment and infra templates
- `docs`: API design, architecture, security model, schema and workflows

## Quick Start (Local)

```bash
# Backend
cd apps/backend
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000

# Frontend
cd ../frontend
npm install
npm run dev
```

## Security Highlights

- Envelope encryption (DEK per file + KEK from KMS)
- JWT access + refresh token rotation with JTI tracking in Redis
- MFA-ready login (OTP, OAuth2, biometric assertion hooks)
- Signed, expiring share links with optional password gate
- Audit trail on every sensitive action
- Strict input validation + parameterized DB access + CSP headers

See `docs/security-architecture.md` for the zero-trust model.
