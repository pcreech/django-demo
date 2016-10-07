from django.db import models

# Create your models here.
class AddRequest(models.Model):
    left = models.IntegerField()
    right = models.IntegerField()
    total = models.IntegerField(null=True)


