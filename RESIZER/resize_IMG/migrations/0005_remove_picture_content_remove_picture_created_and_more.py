# Generated by Django 4.0 on 2022-02-18 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resize_IMG', '0004_alter_picture_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='picture',
            name='content',
        ),
        migrations.RemoveField(
            model_name='picture',
            name='created',
        ),
        migrations.RemoveField(
            model_name='picture',
            name='updated',
        ),
        migrations.AlterField(
            model_name='picture',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
