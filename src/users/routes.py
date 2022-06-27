from typing import List

from beanie import PydanticObjectId
from fastapi import APIRouter, HTTPException
from src.users.models import User, UserUpdate, UserCreate

router = APIRouter(tags=["Users"], prefix="/users")


@router.get("/", response_description="User records retrieved", response_model=List[User])
async def get_users() -> List[User]:
    return await User.find_all().to_list()


@router.get("/{id}", response_description="User record retrieved", response_model=User)
async def get_user_record(id: PydanticObjectId) -> User:
    user = await User.get(id)
    if not user:
        raise HTTPException(status_code=404, detail="User record not found!")
    return user


@router.post("/", response_description="User added to the database", response_model=User)
async def add_user(user: UserCreate) -> User:
    return await User(**user.dict()).create()


@router.put("/{id}", response_description="User record updated", response_model=User)
async def update_user_data(id: PydanticObjectId, user_update: UserUpdate) -> User:
    user_dict = {k: v for k, v in user_update.dict().items() if v is not None}
    update_query = {"$set": {field: value for field, value in user_dict.items()}}

    user = await User.get(id)
    if not user:
        raise HTTPException(status_code=404, detail="User record not found!")

    await user.update(update_query)
    return await get_user_record(id)


@router.delete("/{id}", response_description="User record deleted from the database")
async def delete_user_data(id: PydanticObjectId) -> dict:
    record = await User.get(id)
    if not record:
        raise HTTPException(status_code=404, detail="User record not found!")

    await record.delete()
    return {"message": "User deleted successfully"}
