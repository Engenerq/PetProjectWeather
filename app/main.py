from fastapi import FastAPI

from app.routers.api.weather import router_w

app = FastAPI()
app.include_router(router_w)
