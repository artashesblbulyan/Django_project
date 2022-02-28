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
    is_published = models.BooleanField()
    text = models.TextField()
    status = models.CharField(max_length=3)
    geeks_field = models.URLField(max_length=200)

    def __str__(self):
        return f"{self.name} : {self.rate} : {self.created_at} : {self.is_published} : {self.status}"


