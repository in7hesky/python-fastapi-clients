from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def root():
    return {"mes": "FastAPI is running"}