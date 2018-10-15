from django.contrib.auth.models import User

class EmailAuth:
    """User authentication using an exact match on their email and password"""

    def authenticate(self, username=None, password=None):
        """Finds the user with their email and verified password"""
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
            return None
        except User.DoesNotExist:
            return None
    
    def get_user(self, user_id):
        try:
            user = User.objects.get(pk=user_id)
            if user.is_authenticated():
                return user
            return None
        except User.DoesNotExist:
            return None