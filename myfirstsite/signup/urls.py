from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import SignUp

urlpatterns = [
    path('', SignUp.as_view(), name='create'),
    ]

urlpatterns = format_suffix_patterns(urlpatterns)
