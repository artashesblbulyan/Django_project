# Generated by Django 4.0.2 on 2022-02-25 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('deskription', models.TextField()),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField()),
            ],
        ),
    ]
