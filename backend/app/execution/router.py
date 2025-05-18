"""Simple execution router for Alpaca trades."""

from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce

from ..core.logging import logger
from ..core.config import get_settings
from ..risk.manager import ApprovedSignal


settings = get_settings()


async def execute(signal: ApprovedSignal) -> None:
    """Execute an approved trading signal via Alpaca REST API."""
    logger.info("executing order", extra=signal.__dict__)

    client = TradingClient(
        settings.alpaca_key,
        settings.alpaca_secret,
        paper=True,
    )

    order = MarketOrderRequest(
        symbol=signal.symbol,
        qty=signal.qty,
        side=OrderSide.BUY if signal.side.lower() == "buy" else OrderSide.SELL,
        time_in_force=TimeInForce.DAY,
    )

    try:
        response = client.submit_order(order)
        logger.info("order submitted", extra={"order_id": response.id})
    except Exception as exc:  # pragma: no cover - network
        logger.error("order failed", exc_info=exc)
