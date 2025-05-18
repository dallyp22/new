import pytest
from backend.app.risk.manager import RiskManager, Signal, ApprovedSignal, RejectedSignal


@pytest.mark.asyncio
async def test_risk_manager_rejects_large_trade():
    rm = RiskManager(max_risk_per_trade=100)
    sig = Signal(symbol="AAPL", side="buy", qty=10, price=20.0)
    result = rm.validate(sig)
    assert isinstance(result, RejectedSignal)
    assert result.reason == "exceeds max risk"


@pytest.mark.asyncio
async def test_risk_manager_approves_small_trade():
    rm = RiskManager(max_risk_per_trade=1000)
    sig = Signal(symbol="AAPL", side="buy", qty=1, price=10.0)
    result = rm.validate(sig)
    assert isinstance(result, ApprovedSignal)


