from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi_pagination import add_pagination
from api import auth
from api.routers import users, products, addresses, toppings

app = FastAPI()

origins = [
    "http://localhost:5173",
    "https://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(products.router)
app.include_router(addresses.router)
app.include_router(toppings.router)

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/health")
async def health_check() -> dict[str, str]:
    return {"status": "online"}


add_pagination(app)
