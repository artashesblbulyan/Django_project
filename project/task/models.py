from django.db import models
from django.contrib.auth.models import User
# Create your models here.

STATUS_CHOICES = (
    (1, 'new'),
    (2, 'doing'),
    (3, 'done'),
)


class Type(models.Model):
    name = models.CharField(max_length=10)
    desc = models.TextField()


class Task(models.Model):
    name = models.CharField(max_length=20)
    deskription = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"
