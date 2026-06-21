from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Products(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField()
    date = models.DateField(default=timezone.now)
    

    def __str__(self):
        return self.name
    