from Accounts.models import Profile
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializer import ProfileSerializer, UserSerializer

# Create your views here.

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


# class ExampleView(APIView):
#     authentication_classes = [SessionAuthentication, BasicAuthentication]
#     permission_classes = [IsAuthenticated]

#     def get(self, request, format=None):
#         content = {
#             "user": str(request.user),  # `django.contrib.auth.User` instance.
#             "auth": str(request.auth),  # None
#         }
#         return Response(content)
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
