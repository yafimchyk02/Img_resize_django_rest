from django.shortcuts import render
from .models import Picture
from .serializers import PictureSerializer
from rest_framework import generics


def home(request):
    return render(request, 'home.html', locals())


class resize_picture(generics.ListCreateAPIView):
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer
