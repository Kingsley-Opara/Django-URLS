from django.db import models

from django.conf import settings
from django.urls import reverse

user = settings.AUTH_USER_MODEL
# Create your models here.
class Recieps(models.Model):
    Owner = models.ForeignKey(user, on_delete=models.SET_NULL, null=True)
    About = models.TextField()
    Ingredient = models.TextField(max_length=1000)
    Preperation = models.TextField()
    Price = models.DecimalField(decimal_places=2, max_digits=100000)
    Featured = models.BooleanField(default=True)

    def __str__(self):
        return self.About

    def get_absolute_url(self, *args, **kwargs):
        return reverse('detail', kwargs={'id':self.id})
