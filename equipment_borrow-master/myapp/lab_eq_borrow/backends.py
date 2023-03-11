from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from .models import User

class EmailBackend(ModelBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        
        users = User.objects.filter(u_email=email)

        for user in users:
            if user.check_password(password):
                return user

    def get_user(self, user_id):
        UserModel = get_user_model()
        try:
            return UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None
