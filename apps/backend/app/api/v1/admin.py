from fastapi import APIRouter

router = APIRouter(prefix="/admin", tags=["admin"])


@router.get("/metrics")
async def metrics() -> dict:
    return {
        "active_users_24h": 1204,
        "uploads_24h": 9821,
        "security_incidents": 0,
        "storage_utilization_gb": 421.7,
    }
