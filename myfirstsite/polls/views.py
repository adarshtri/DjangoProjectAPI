from django.http import HttpResponse
from rest_framework import generics
from .models import Questions, Choice
from .serializers import QuestionSerializer, ChoiceSerializer
from .serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework import permissions


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


def index(request):
    return HttpResponse("Hi there, you are seeing polls index.")


class CreateView(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Questions.objects.all()
    serializer_class = QuestionSerializer

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user.id)


class CreateChoice(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer

    def perform_create(self, serializer):
        serializer.save()