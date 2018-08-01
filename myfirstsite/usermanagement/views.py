from rest_framework import generics
from .models import User
from .userserializer import UserSerializer
from rest_framework.response import Response
from django.db.models import Q
from django.utils import timezone
import random


# Signup and list users.
class UserViewCreate(generics.CreateAPIView):

    serializer_class = UserSerializer
    request = None

    def create(self, request, *args, **kwargs):

        self.request = request

        serializer = self.get_serializer(data=self.request.data)
        if serializer.is_valid():
            if self.check_signin_details():
                serializer.save()
                return Response(data={"message": "User created successfully.", "status": "ok", "response_code": 222},
                                status=201)
            else:
                return Response(
                    data={"message": "User already exists with same username or useremail.", "status": "error",
                          "response_code": 444}, status=400)

    def get_queryset(self):
        return User.objects.filter(
            Q(username=self.request.data["username"]) | Q(useremail=self.request.data["useremail"]))

    def check_signin_details(self):

        query_set = self.get_queryset()

        return not bool(query_set)


# Login and logout
class LogActivity(generics.RetrieveUpdateAPIView):

    serializer_class = UserSerializer
    request = None

    def get_queryset(self):
        return User.objects.filter(Q(username=self.request.data["username"])
                                   & Q(userpassword=self.request.data["userpassword"]))


class LogoutActivity(LogActivity):

    def update(self, request, *args,  **kwargs):
        self.request = request
        query_set = self.get_queryset()

        if bool(query_set):
            query_set.filter(username=self.request.data["username"],
                             userpassword=self.request.data["userpassword"],
                             logintoken=self.request.data["logintoken"]).update(logintoken=None, lastlogout=timezone.now())
            return Response(data={"message": "User logged out successfully.", "response_code": 222}, status=201)
        else:
            return Response(
                data={"message": "User not found or logintoken doesn't match.", "response_code": 444},
                status=201)


class LoginActivity(LogActivity):

    def update(self, request, *args,  **kwargs):
        self.request = request
        query_set = self.get_queryset()

        if bool(query_set):
            logintoken = random.randint(1, 10000)
            query_set.filter(username=self.request.data["username"])\
                .filter(userpassword=self.request.data["userpassword"])\
                .update(lastlogin=timezone.now(), logintoken=logintoken)
            return Response(
                data={"message": "User logged in successfully.", "logintoken": logintoken, "response_code": 222},
                status=201)
        else:
            return Response(data={"message": "User not found.", "response_code": 444}, status=201)
