from .base import Strategy
from ..core.logging import logger


class OptionsStrategy(Strategy):
    name = "options"

    async def on_event(self, event: dict) -> None:
        logger.info("options event", extra=event)
        # TODO: implement logic
