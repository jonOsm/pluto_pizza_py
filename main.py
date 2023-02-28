from fastapi import Depends, FastAPI
from fastapi import Depends, FastAPI

from api import auth
from api.routers import users, products

app = FastAPI()

app.include_router(users.router)
app.include_router(products.router)
app.include_router(auth.router)


@app.get("/health")
async def health_check() -> dict[str, str]:
    return {"status": "online"}
