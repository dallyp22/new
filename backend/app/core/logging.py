import logging
from logging.config import dictConfig


def setup_logging() -> None:
    dictConfig(
        {
            "version": 1,
            "formatters": {
                "default": {
                    "()": "pythonjsonlogger.jsonlogger.JsonFormatter",
                    "format": "%(asctime)s %(levelname)s %(name)s %(message)s",
                }
            },
            "handlers": {
                "default": {
                    "class": "logging.StreamHandler",
                    "formatter": "default",
                    "level": "INFO",
                }
            },
            "root": {"handlers": ["default"], "level": "INFO"},
        }
    )


setup_logging()
logger = logging.getLogger("alpaca-ai-bot")
