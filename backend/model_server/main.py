from fastapi import FastAPI

app = FastAPI(title="Model Server")


@app.get("/predict/price")
async def predict_price() -> dict[str, float]:
    # TODO: load model and return prediction
    return {"prob_up": 0.5}


@app.post("/llm/sentiment")
async def llm_sentiment(text: str) -> dict[str, float]:
    # TODO: call openai or local model
    return {"score": 0.0}
