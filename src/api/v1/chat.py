from fastapi import APIRouter

from src.helper_functions.chat_openai import get_chat_response_from_openail

chat_router = APIRouter(prefix="/v1/chat", tags=["chat"])


@chat_router.post(
    "/",
    status_code=200,
)
async def get_chat_response(
        message: str,
):
    response_text = get_chat_response_from_openail(message)
    return response_text
