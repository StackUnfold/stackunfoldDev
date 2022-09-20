from .models import jee_mains
from rest_framework import serializers


class JeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = jee_mains
        fields = '__all__'