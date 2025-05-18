import asyncio
from collections.abc import AsyncIterator


class MarketEventBus:
    _subscribers: list[asyncio.Queue] = []

    @classmethod
    async def publish(cls, event: dict) -> None:
        for q in cls._subscribers:
            await q.put(event)

    @classmethod
    async def subscribe(cls) -> AsyncIterator[dict]:
        q: asyncio.Queue = asyncio.Queue()
        cls._subscribers.append(q)
        try:
            while True:
                yield await q.get()
        finally:
            cls._subscribers.remove(q)
