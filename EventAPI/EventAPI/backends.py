from django.contrib.auth.backends import BaseBackend 
from django.contrib.auth import get_user_model
from django.db.models import Q

User = get_user_model()
print("User", User)


class CustomLoginView(BaseBackend):
    def authenticate(self, request, username = None, password = None, **kwargs):
        try:
            user=User.objects.get(Q(username=username))
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            user = User.objects.get(id=user_id)
            return user
        except User.DoesNotExist:
            return None