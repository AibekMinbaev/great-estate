# Generated by Django 4.1.5 on 2023-02-15 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0005_alter_listing_property_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='property_image',
            field=models.ImageField(blank=True, default='defaultproperty.jpg', null=True, upload_to=''),
        ),
    ]
