# Generated by Django 4.1.5 on 2023-02-13 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_listing_property_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing_rent',
            name='property_image',
            field=models.ImageField(blank=True, default='defaultproperty.jpg', null=True, upload_to=''),
        ),
    ]