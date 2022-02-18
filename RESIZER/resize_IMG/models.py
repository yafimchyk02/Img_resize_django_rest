from django.db import models
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill


class Picture(models.Model):
    picture = models.ImageField(upload_to='pictures', null=True, blank=True)
    image_large = ImageSpecField(source='picture', processors=[ResizeToFill(512, 512)], format='PNG',
                                 options={'quality': 70})
    image_medium = ImageSpecField(source='picture', processors=[ResizeToFill(256, 256)], format='PNG',
                                  options={'quality': 70})
    image_small = ImageSpecField(source='picture', processors=[ResizeToFill(128, 128)], format='PNG',
                                 options={'quality': 70})
# Create your models here.
