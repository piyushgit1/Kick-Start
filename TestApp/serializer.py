from rest_framework.serializers import ModelSerializer
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.hashers import make_password


from TestApp.models import UserProfile


class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id','username','email','password','is_staff','is_superuser','is_active']

    def validate_password(self, password):
        validate_password(password=password)
        return make_password(password)
