# Generated by Django 4.0.5 on 2022-06-24 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0003_alter_trip_category_alter_trip_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='top_offer',
            field=models.BooleanField(default=False),
        ),
    ]
