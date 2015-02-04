from rest_framework import serializers
from apps.default.models import *

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
