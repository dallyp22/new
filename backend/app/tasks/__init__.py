from celery import Celery
from ..core.config import get_settings

settings = get_settings()
celery_app = Celery(
    "alpaca_tasks",
    broker=settings.rabbit_url,
    backend=settings.redis_url,
)


@celery_app.task
def nightly_etl() -> str:
    # TODO: implement data retrieval and model retraining
    return "ok"
