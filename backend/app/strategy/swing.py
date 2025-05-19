from .base import Strategy
from ..core.logging import logger


class SwingStrategy(Strategy):
    name = "swing"

    async def on_event(self, event: dict) -> None:
        logger.info("swing event", extra=event)
        # TODO: implement logic
