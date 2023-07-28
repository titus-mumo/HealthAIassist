from django.contrib.auth.backends import ModelBackend

class UserSiteAuthBackend(ModelBackend):
    def get_user(self, user_id):
        return super().get_user(user_id)