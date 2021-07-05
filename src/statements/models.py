from django.db import models

# Create your models here.
class Statement(models.Model):
    title = models.CharField(max_length=120)
    sub_title = models.TextField(default='N/A')
    likes = models.IntegerField()
    draft = models.BooleanField(default=True)
