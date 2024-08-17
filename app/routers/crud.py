from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def root():
    return {"mes": "FastAPI is running"}

@router.get("/clients")
def clients_get():
    return "Some client data"

@router.post("/clients")
def clients_post():
    return {"data_posted": True}

