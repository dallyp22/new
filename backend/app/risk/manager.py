from dataclasses import dataclass
from ..core.logging import logger


@dataclass
class Signal:
    symbol: str
    side: str
    qty: int
    price: float


class ApprovedSignal(Signal):
    pass


class RejectedSignal(Signal):
    reason: str


class RiskManager:
    """Very small risk manager to demonstrate rejection logic."""

    def __init__(self, max_risk_per_trade: float = 1000) -> None:
        self.max_risk_per_trade = max_risk_per_trade

    def validate(self, signal: Signal) -> ApprovedSignal | RejectedSignal:
        """Validate a trading signal and return an approved or rejected copy."""
        risk = signal.qty * signal.price
        if risk > self.max_risk_per_trade:
            logger.warning("signal rejected", extra={"risk": risk})
            r = RejectedSignal(**signal.__dict__)
            r.reason = "exceeds max risk"
            return r
        return ApprovedSignal(**signal.__dict__)


risk_manager = RiskManager()
