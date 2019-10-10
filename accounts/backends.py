from .models import UserRegistrationModel

class EmailAuth:
    def authenticate(self, request, username=None, password=None):
        try:
            user = UserRegistrationModel.objects.get(email=username)
            if user.check_password(password):
                return user

            return None
        except UserRegistrationModel.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            user = UserRegistrationModel.objects.get(pk=user_id)

            if user.is_active:
                return user

            return None
        except UserRegistrationModel.DoesNotExist:
            return None