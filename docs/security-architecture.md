# Zero-Trust Security Architecture

## Architecture Logic
1. Client performs local pre-encryption (optional strong mode) and transmits TLS 1.3.
2. API Gateway enforces WAF, bot mitigation, geo/risk checks, and rate limiting.
3. Identity service verifies JWT + refresh rotation + MFA claims.
4. Policy Decision Point (PDP) evaluates RBAC/ABAC risk signals.
5. Document service encrypts payload with per-file DEK and stores wrapped DEK metadata.
6. Object storage persists encrypted blobs only; no plaintext at rest.
7. Audit service logs immutable action events to append-only sink.

## Threat Controls
- SQLi: ORM + validated schemas + no raw SQL by default.
- XSS: CSP + escaped rendering + strict content types.
- CSRF: SameSite=strict + double submit token for browser forms.
- Brute force: adaptive rate limits + account lock + risk scoring.

## Enterprise Enhancements
- Hardware-backed key management (AWS KMS / Cloud KMS / HSM)
- Device binding + biometric WebAuthn assertions
- SIEM integration for anomaly detection
- Backup & DR: multi-region encrypted replicas
