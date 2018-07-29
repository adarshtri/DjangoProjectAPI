from rest_framework import serializers
from .models import SiteUser


class SignUpSerializer(serializers.ModelSerializer):

    class Meta:
        model = SiteUser
        fields = ('id', 'username', 'useremail', 'userpassword')