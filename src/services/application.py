from src.schemas.application import ApplicationCreate

from src.repositories.repository import AbstractRepository

class ApplicationService:
    def __init__(self, applications_repo: AbstractRepository):
        self.applications_repo: AbstractRepository = applications_repo

    async def add_application(self, application: ApplicationCreate):
        application_dict = application.model_dump()
        application_id = await self.applications_repo.add_one(data=application_dict)
        return application_id

    async def get_applications(self):
        applications = await self.applications_repo.get_all()
        return applications
    async def get_application(self, **filters):
        application = await self.applications_repo.get_one(**filters)
        return application

    async def delete_application(self, **filters):
        application = await self.applications_repo.delete_one(**filters)
        return application



