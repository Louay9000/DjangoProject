# Generated by Django 5.1.1 on 2024-11-19 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evenements', '0006_evenementadmin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evenementadmin',
            name='approved',
            field=models.BooleanField(default=False, verbose_name='Approved'),
        ),
    ]
