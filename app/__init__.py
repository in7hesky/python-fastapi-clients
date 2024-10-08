from fastapi import FastAPI
from .routers.crud import router
from .config import get_settings

def create_app():
    app = FastAPI()
    
    app.include_router(router)

    return app
    