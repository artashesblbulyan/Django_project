# Generated by Django 4.0.2 on 2022-02-28 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('greeting', '0003_film_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='film',
            name='image',
        ),
        migrations.AddField(
            model_name='film',
            name='geeks_field',
            field=models.URLField(default=1),
            preserve_default=False,
        ),
    ]