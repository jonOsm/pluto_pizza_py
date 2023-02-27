from fastapi import FastAPI
from api.routers import users, products
from db import models

app = FastAPI()

app.include_router(users.router)
app.include_router(products.router)


@app.get("/health")
async def health_check() -> dict[str, str]:
    return {"status": "online"}


@app.get("/test")
async def health_check():
    return models.testing()
