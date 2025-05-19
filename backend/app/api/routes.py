from fastapi import APIRouter
from pydantic import BaseModel
from uuid import UUID, uuid4

router = APIRouter()


class Signal(BaseModel):
    id: UUID
    symbol: str
    side: str  # 'buy' or 'sell'
    confidence: float


fake_signal = Signal(id=uuid4(), symbol="AAPL", side="buy", confidence=0.8)


@router.get("/signals/next", response_model=Signal)
async def get_signal() -> Signal:
    """Return the next trading signal (mock)."""
    return fake_signal


@router.post("/trades/approve/{signal_id}")
async def approve_trade(signal_id: UUID) -> dict[str, str]:
    """Approve execution of a trade."""
    # TODO: integrate risk manager and execution
    return {"status": f"signal {signal_id} approved"}


@router.get("/settings")
async def list_settings() -> dict[str, str]:
    # TODO: fetch from DB
    return {"auto_trade": "false"}
