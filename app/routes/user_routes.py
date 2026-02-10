from fastapi import APIRouter, HTTPException
from controllers.user_controller import *
from models.user_model import user

router = APIRouter()

nuevo_user = UserController()


@router.post("/create_user")
async def create_user(user: user):
    rpta = nuevo_user.create_user(user)
    return rpta


@router.get("/get_user/{user_id}",response_model=user)
async def get_user(user_id: int):
    rpta = nuevo_user.get_user(user_id)
    return rpta

@router.get("/get_usuarios/")
async def get_usuarios():
    rpta = nuevo_user.get_usuarios()
    return rpta