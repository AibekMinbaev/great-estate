# Generated by Django 4.1.5 on 2023-02-06 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_my_profile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='my_profile',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='my_profile',
            name='phone_number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
