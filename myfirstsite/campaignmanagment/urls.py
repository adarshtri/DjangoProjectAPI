from django.urls import path
from .views import CreateCampaign, UpdateCampaign
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('createcampaign/', CreateCampaign.as_view(), name='create'),
    path('updatecampaign/', UpdateCampaign.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
