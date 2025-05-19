import hashlib
import json
import asyncio
import redis.asyncio as redis
from ..core.config import get_settings
from ..core.logging import logger
from openai import AsyncOpenAI

settings = get_settings()
redis_client = redis.from_url(settings.redis_url)
openai_client = AsyncOpenAI(api_key=settings.openai_api_key)


async def headline_sentiment(text: str) -> float:
    key = "sent:" + hashlib.md5(text.encode()).hexdigest()
    cached = await redis_client.get(key)
    if cached:
        return float(cached)

    prompt = f"What is the sentiment score -1 to 1 for: {text}"
    try:
        resp = await openai_client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
        )
        score = float(resp.choices[0].message.content.strip())
    except Exception as exc:
        logger.error("llm error", exc_info=exc)
        score = 0.0
    await redis_client.set(key, score, ex=3600)
    return score
