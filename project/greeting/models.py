from django.db import models

# Create your models here.
STATUS_CHOICES = (
    (1, 'new'),
    (2, 'doing'),
    (3, 'done'),
)

class Film(models.Model):
    name = models.CharField(max_length=25)
    rate = models.IntegerField(choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    is_punlished = models.BooleanField()
    status = models.CharField(max_length=3)

    def __str__(self):
        return f"{self.name}{self.rate}"


