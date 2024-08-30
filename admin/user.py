from sqladmin import ModelView

from kingdom.models import User


class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.username]
    column_searchable_list = [User.username]
    name = "User"
    name_plural = "Users"
    icon = "fa-solid fa-user"
    form_columns = [User.username, User.password, User.email]
