# Generated by Django 4.0.2 on 2022-02-28 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('greeting', '0002_film_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='image',
            field=models.ImageField(default=1, upload_to='uploads/'),
            preserve_default=False,
        ),
    ]
