# Generated by Django 4.2.1 on 2023-06-06 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='articls',
            name='photo',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
