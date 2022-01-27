from django.contrib.auth.models import User


def user_str(user: User) -> str:
    if user.first_name:
        if user.last_name:
            return f"{user.first_name} {user.last_name}"
        return user.first_name
    return user.username

User.add_to_class("__str__", user_str)
