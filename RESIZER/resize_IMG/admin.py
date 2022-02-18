from django.contrib import admin
from resize_IMG.models import *
from django.contrib import admin
from imagekit.admin import AdminThumbnail


class PictureAdmin(admin.ModelAdmin):
    list_display = ('id', 'picture', 'thumbnail')
    thumbnail = AdminThumbnail(image_field='thumbnail')

    class Meta:
        model = Picture


admin.site.register(Picture, PictureAdmin)

# Register your models here.
