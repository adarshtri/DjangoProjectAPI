from django.urls import path
from .views import UserViewCreate,  LoginActivity, LogoutActivity
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('signup/', UserViewCreate.as_view(), name='create'),
    path('login/', LoginActivity.as_view()),
    path('logout/', LogoutActivity.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
