# Full Folder Structure

```text
seniorcitizen/
├── apps/
│   ├── backend/
│   │   ├── app/
│   │   │   ├── api/v1/            # Versioned API routers
│   │   │   ├── core/              # Configuration and logging
│   │   │   ├── db/                # Database session/base
│   │   │   ├── middleware/        # Security headers + request context
│   │   │   ├── models/            # SQLAlchemy entities
│   │   │   ├── schemas/           # Request/response DTOs
│   │   │   ├── security/          # JWT, password hashing, encryption
│   │   │   ├── services/          # Audit, storage, AI helpers
│   │   │   └── workers/           # Async processors (thumbnail, OCR)
│   │   └── requirements.txt
│   └── frontend/
│       ├── app/                   # Next.js App Router screens
│       ├── components/            # Shared UI components
│       ├── lib/                   # Theme + helpers
│       └── tailwind.config.ts
├── docs/
│   ├── folder-structure.md
│   ├── api-design.md
│   ├── database-schema.md
│   └── security-architecture.md
├── infra/
│   ├── docker-compose.yml
│   └── nginx.conf
└── README.md
```
