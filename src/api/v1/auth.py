from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from src.api.dependencies import user_service
from src.helper_functions.auth_handler import get_current_user, bcrypt_context, create_access_token, \
    create_refresh_token
from src.schemas.user import UserCreate
from src.services.user import UserService

from sqlalchemy.exc import IntegrityError

auth_router = APIRouter(prefix="/v1/auth", tags=["auth"])



@auth_router.post(
    "/signup/",
    status_code=201,
    summary="Регистрация пользователя.",
)
async def add_user(
        user: UserCreate,
        users_service: Annotated[UserService, Depends(user_service)],
):
    try:
        user_id = await users_service.add_user(user)
        return user_id
    except IntegrityError as e:
        if "duplicate key value" in str(e):
            raise HTTPException(status_code=400, detail="Пользователь с таким email уже существует")
        else:
            raise HTTPException(status_code=400, detail="Неверные данные")



@auth_router.post(
    "/login/",
    status_code=200,
    summary="Вход в систему. можно использовать email",
)
async def login(
        form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
        users_service: Annotated[UserService, Depends(user_service)],
):
    try:
        user = await users_service.get_user(email=form_data.username)

        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        if not bcrypt_context.verify(form_data.password, user.hashed_password):
            raise HTTPException(status_code=404, detail="Неправильный пароль")
        data = {'email': user.email, 'id': user.id}
        try:
            token = create_access_token(data=data)
            refresh_token = create_refresh_token(data=data)
        except Exception as token_creation_error:
            # token creation error
            raise HTTPException(status_code=500, detail=f"Token creation error: {str(token_creation_error)}")
        return {'access_token': token, 'refresh_token': refresh_token}

    except HTTPException as e:
        raise e

    except IntegrityError:
        raise HTTPException(status_code=500, detail="Internal Server Error")

    except Exception as e:
        # Other errors
        print(f"Unexpected error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")



@auth_router.post(
    "/current-user/",
    status_code=200,
    summary="Возвращает пользователя.",
    description="Возвращает пользователя.",
)
async def get_user(
    user: Annotated[dict, Depends(get_current_user)],
):
    try:
        return user
    except HTTPException as e:
        # Handle specific HTTPExceptions
        if e.status_code == 401:
            # Token-related error handling
            return HTTPException(status_code=401, detail="Invalid token")
    except Exception as e:
        # Handle other exceptions
        return {"error": "Internal server error", "detail": str(e)}