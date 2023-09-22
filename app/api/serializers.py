from rest_framework import serializers

from .models import Libraries


class LibrariesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libraries
        depth = 1
        fields = '__all__'