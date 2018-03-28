from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User

from django.contrib.auth.backends import ModelBackend


class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None):
        try:
            user = User.objects.get(email=username)
        except User.DoesNotExist:
            return None
        else:
            pwd_valid = user.check_password(password)
            can_auth = self.user_can_authenticate(user)
            if pwd_valid and can_auth:
                return user
            else:
                return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
