import pytest
from backend.app.risk.manager import Signal, risk_manager, ApprovedSignal, RejectedSignal

@pytest.mark.asyncio
async def test_validate_approves_within_risk():
    s = Signal(symbol="AAPL", side="buy", qty=1, price=10)
    result = risk_manager.validate(s)
    assert isinstance(result, ApprovedSignal)

@pytest.mark.asyncio
async def test_validate_rejects_excess_risk():
    s = Signal(symbol="AAPL", side="buy", qty=200, price=10)
    result = risk_manager.validate(s)
    assert isinstance(result, RejectedSignal)
    assert result.reason == "exceeds max risk"
