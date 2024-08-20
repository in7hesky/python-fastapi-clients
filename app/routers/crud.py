from fastapi import APIRouter, Body, status
from ..database import Database
from ..models import ClientModel

TARGET_COLLECTION_NAME = "clients"

database = Database()
target_collection = database.db.get_collection(TARGET_COLLECTION_NAME)

router = APIRouter()

@router.get("/")
def root():
    return {"mes": "FastAPI is running"}


@router.post("/clients",
             response_model=ClientModel,
             status_code=status.HTTP_201_CREATED,
             )
async def create_client(client: ClientModel = Body(...)):
    new_client = await target_collection.insert_one(
        client.model_dump(by_alias=True, exclude={"id"})
    )

    created_client = await target_collection.find_one(
        {"_id": new_client.inserted_id}
    )

    return created_client


