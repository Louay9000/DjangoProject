# Generated by Django 5.1.1 on 2024-12-03 16:32

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evenements', '0009_venue_image'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='evenement',
            name='attendees',
            field=models.ManyToManyField(blank=True, null=True, related_name='attendees', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='venue',
            name='image',
            field=models.ImageField(blank=True, upload_to='venues/'),
        ),
    ]