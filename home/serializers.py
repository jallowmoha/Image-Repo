from .models import Image
from rest_framework import serializers
from .models import Image


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('id', 'title', 'image', 'author', 'date_created')
