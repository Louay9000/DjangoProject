# Generated by Django 5.1.1 on 2024-10-02 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evenements', '0004_venue_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='evenement',
            name='approved',
            field=models.BooleanField(default=False, verbose_name='Approved'),
        ),
    ]
