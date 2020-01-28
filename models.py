from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    created_date=models.DateField(default=timezone.now)
    text=models.TextField(null=True ,blank =True)

    def __str__(self):
        return self.title