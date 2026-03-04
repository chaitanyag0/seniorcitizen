from sqlalchemy.ext.asyncio import AsyncSession

from app.models.audit_log import AuditLog


async def record_audit_event(
    db: AsyncSession,
    *,
    actor_id: str | None,
    action: str,
    resource_type: str,
    resource_id: str,
    ip_address: str,
    user_agent: str,
    metadata: dict | None = None,
) -> None:
    event = AuditLog(
        actor_id=actor_id,
        action=action,
        resource_type=resource_type,
        resource_id=resource_id,
        ip_address=ip_address,
        user_agent=user_agent,
        metadata=metadata or {},
    )
    db.add(event)
    await db.commit()
