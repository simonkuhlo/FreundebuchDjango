from fastapi import APIRouter
from crud import user as crud_user
from schemas.user import UserCreate, UserUpdate

prefix: str = "/users"

router = APIRouter(prefix=prefix)

@router.get("/hello")
async def hello():
    return {"hello": "world"}

@router.get("/{user_id}")
async def read_user(user_id:int):
    user = crud_user.get(user_id)
    return {"user": user}

@router.post("/")
async def create_user(user:UserCreate):
    user = crud_user.create(user)
    return {"user": user}

@router.put("/{user_id}")
async def update_user(user:UserUpdate, user_id:int):
    user = crud_user.update(user_id, user)
    return {"user": user}

@router.delete("/{user_id}")
async def delete_user(user_id:int):
    crud_user.delete(user_id)
    return {"User deleted"}