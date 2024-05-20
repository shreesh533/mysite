from django.db import models

# Create your models here.


class Urls(models.Model):
    full_url = models.TextField()
    short_url = models.CharField(max_length=128, null=True)
    hit_count = models.IntegerField(default=0)
