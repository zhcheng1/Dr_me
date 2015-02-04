from django.shortcuts import render
from rest_framework import generics
from apps.default.serializers import *


class DoctorList(generics.ListAPIView):
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()

class DoctorDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()

class UserInfoList(generics.ListAPIView):
    serializer_class = UserInfoSerializer
    queryset = UserInfo.objects.all()
