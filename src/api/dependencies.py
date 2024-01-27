from src.repositories.all_repositories import UserRepository, ApplicationRepository
from src.services.application import ApplicationService
from src.services.user import UserService


def user_service():
    return UserService(UserRepository())


def application_service():
    return ApplicationService(ApplicationRepository())