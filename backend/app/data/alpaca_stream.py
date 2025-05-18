import asyncio
import websockets
from .pubsub import MarketEventBus
from ..core.config import get_settings

settings = get_settings()


async def connect():
    url = "wss://stream.data.alpaca.markets/v2/sip"
    async with websockets.connect(url) as ws:
        await ws.send({"action": "auth", "key": settings.alpaca_key, "secret": settings.alpaca_secret})
        # TODO: subscribe to channels and forward events
        async for msg in ws:
            await MarketEventBus.publish(msg)
