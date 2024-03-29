from sre_parse import State
from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User

class Barber(models.Model):
    name = models.CharField(max_length = 100)
    state = models.CharField(max_length = 100, default = 'N/A')
    city = models.CharField(max_length = 100, default = 'N/A')
    ratings = ArrayField(models.IntegerField())
    price = models.CharField(max_length = 100)
    description = models.TextField()
    profile_image = models.TextField(default = 'N/A')
    haircut_images = ArrayField(models.TextField(default = 'N/A'), default = ['order_status_changed', 'new_signal'])
    website = models.TextField(default = 'N/A')
    contact = models.TextField(default = 'N/A')

    def __str__(self):
        return self.name

class Comment(models.Model):
    author = models.ForeignKey(User, related_name='comment', on_delete=models.CASCADE)
    content = models.CharField(max_length = 250)

    def __str__(self):
        return self.author