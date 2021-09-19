from .serializers import ImageSerializer
from .models import Image
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, BasePermission, SAFE_METHODS
from django.conf import settings
User = settings.AUTH_USER_MODEL


# Create your views here.

class ImagePermission(BasePermission):
    message = 'Only author can delete their post.'

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user


class ImageList(generics.ListCreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class ImageDetail(generics.RetrieveUpdateAPIView, ImagePermission):
    permission_classes = [ImagePermission]
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
