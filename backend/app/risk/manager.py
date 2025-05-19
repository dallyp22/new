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
    reason: str = ""


class RiskManager:
    max_risk_per_trade: float = 1000  # dollars

    def validate(self, signal: Signal) -> ApprovedSignal | RejectedSignal:
        risk = signal.qty * signal.price
        if risk > self.max_risk_per_trade:
            logger.warning("signal rejected", extra={"risk": risk})
            r = RejectedSignal(reason="exceeds max risk", **signal.__dict__)
            return r
        return ApprovedSignal(**signal.__dict__)


risk_manager = RiskManager()
