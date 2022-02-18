from rest_framework import serializers
from .models import Picture


class PictureSerializer(serializers.ModelSerializer):
    image_large = serializers.ImageField(read_only=True)
    image_medium = serializers.ImageField(read_only=True)
    image_small = serializers.ImageField(read_only=True)

    class Meta:
        model = Picture
        fields = [
            'picture',
            'image_large',
            'image_medium',
            'image_small',
        ]