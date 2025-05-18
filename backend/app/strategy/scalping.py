from .base import Strategy
from ..core.logging import logger


class ScalpingStrategy(Strategy):
    name = "scalping"

    async def on_event(self, event: dict) -> None:
        logger.info("scalping event", extra=event)
        # TODO: implement logic and emit signals
