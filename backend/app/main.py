from fastapi import FastAPI
from .core.logging import logger  # noqa
from .api.routes import router as api_router


def create_app() -> FastAPI:
    app = FastAPI(title="Alpaca AI Bot")

    @app.get("/health")
    async def health() -> dict[str, str]:
        return {"status": "ok"}

    app.include_router(api_router, prefix="/api")
    return app


app = create_app()
