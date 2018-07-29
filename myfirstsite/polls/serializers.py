from rest_framework import serializers
from .models import Questions, Choice
from django.contrib.auth.models import User


class QuestionSerializer(serializers.ModelSerializer):
    """Serializer to map the Question model instance to JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Questions
        user_id = serializers.ReadOnlyField(source='user_id.id')
        fields = ('id', 'question_text', 'pub_date', 'user_id')


class ChoiceSerializer(serializers.ModelSerializer):
    """Serializer to map the Choice model instance to JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Choice
        fields = ('id', 'question', 'choice_text', 'votes')


class UserSerializer(serializers.ModelSerializer):
    questions = serializers.PrimaryKeyRelatedField(many=True, queryset=Questions.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'questions')
