from django.urls import path
from .views import ImageList, ImageDetail


urlpatterns = [
    path('post', ImageList.as_view(), name='image_list'),
    path('post/<int:pk>/', ImageDetail.as_view(), name='image_detail')
]
