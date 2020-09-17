from rest_framework import serializers
from .models import *
from accounts.models import User


class FieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Field
        fields = '__all__'

class OptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Options
        fields = '__all__'

class FormSerializer(serializers.ModelSerializer):
    field = FieldSerializer(many=True)
    class Meta:
        model = Form
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'