from django.urls import path
from . import views
from .views import CreateView, CreateChoice
from .views import index
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('createPoll/', CreateView.as_view(), name='create'),
    path('createChoice/', CreateChoice.as_view(), name='create'),
    path('users/', views.UserList.as_view()),
    path('users/(?P<pk>[0-9]+)/', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
