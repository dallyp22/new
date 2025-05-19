import asyncio
import json
import websockets
from .pubsub import MarketEventBus
from ..core.config import get_settings

settings = get_settings()


async def connect():
    url = "wss://stream.data.alpaca.markets/v2/sip"
    async with websockets.connect(url) as ws:
        payload = {"action": "auth", "key": settings.alpaca_key, "secret": settings.alpaca_secret}
        await ws.send(json.dumps(payload))
        # TODO: subscribe to channels and forward events
        async for msg in ws:
            await MarketEventBus.publish(msg)
