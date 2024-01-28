from sqladmin import ModelView

from src.models.application import Application
from src.models.user import User


class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.email, User.phone_number, User.firstname, User.lastname]


class ApplicationAdmin(ModelView, model=Application):
    column_list = [Application.id, Application.user_id, Application.insurance_sum, Application.total_insurance_premium,
                   Application.main_coverage_premium, Application.ns_premium, Application.disability_premium,
                   Application.tt_premium, Application.created_at]


