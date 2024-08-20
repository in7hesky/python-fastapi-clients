from fastapi import APIRouter, Body, status, HTTPException
from fastapi.responses import Response
from ..database import Database
from ..models import ClientModel, UpdateClientModel
from bson import ObjectId
from pymongo import ReturnDocument


TARGET_COLLECTION_NAME = "clients"

database = Database()
target_collection = database.db.get_collection(TARGET_COLLECTION_NAME)

router = APIRouter()

@router.get("/")
def get_app_status():
    return {"mes": "FastAPI is running"}


@router.get(
    "/clients/{id}",
    response_model=ClientModel,
    status_code=status.HTTP_200_OK,
)
async def get_client(id: str):
    if (
        client := await target_collection.find_one({"_id": ObjectId(id)})
    ) is not None:
        return client

    raise HTTPException(status_code=404, detail=f"Client {id} not found")


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


@router.put(
    "/clients/{id}",
    response_model=ClientModel,
    status_code=status.HTTP_200_OK,
)
async def update_client(id: str, client: UpdateClientModel = Body(...)):
    client = {
        k: v for k, v in client.model_dump(by_alias=True).items() if v is not None
    }

    if len(client) >= 1:
        update_result = await target_collection.find_one_and_update(
            {"_id": ObjectId(id)},
            {"$set": client},
            return_document=ReturnDocument.AFTER,
        )
        if update_result is not None:
            return update_result
        else:
            raise HTTPException(status_code=404, detail=f"Client {id} not found")

    if (existing_client := await target_collection.find_one({"_id": id})) is not None:
        return existing_client

    raise HTTPException(status_code=404, detail=f"Client {id} not found")


@router.delete("/clients/{id}")
async def delete_client(id: str):
    delete_result = await target_collection.delete_one({"_id": ObjectId(id)})

    if delete_result.deleted_count == 1:
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    raise HTTPException(status_code=404, detail=f"Client {id} not found")
