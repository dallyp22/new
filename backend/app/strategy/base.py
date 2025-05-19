import abc
from ..data.pubsub import MarketEventBus
from ..core.logging import logger


class Strategy(abc.ABC):
    name: str = "base"

    async def run(self) -> None:
        async for event in MarketEventBus.subscribe():
            await self.on_event(event)

    @abc.abstractmethod
    async def on_event(self, event: dict) -> None:
        pass
