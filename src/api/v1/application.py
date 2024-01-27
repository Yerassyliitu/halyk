from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException

from src.api.dependencies import application_service
from src.helper_functions.auth_handler import get_current_user
from src.schemas.application import ApplicationCreate
from src.services.application import ApplicationService

application_router = APIRouter(prefix="/v1/application", tags=["application"])


@application_router.get(
    "/",
    status_code=200
)
async def get_applications(
        applications_service: Annotated[ApplicationService, Depends(application_service)],
):
    applications = await applications_service.get_applications()
    if applications:
        return applications
    else:
        raise HTTPException(status_code=404, detail="Нет заявок")


@application_router.post(
    "/",
    status_code=201,
)
async def add_application(
        application: ApplicationCreate,
        applications_service: Annotated[ApplicationService, Depends(application_service)],
        user: Annotated[dict, Depends(get_current_user)],
):
    try:
        application_id = await applications_service.add_application(application)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    return application_id
