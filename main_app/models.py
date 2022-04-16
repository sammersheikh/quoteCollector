from django.db import models
from django.urls import reverse

# Create your models here.

class Quote(models.Model):
    category = models.CharField(max_length=100)
    quote = models.TextField(max_length=250)
    by = models.CharField(max_length=100)

    def __str__(self):
        return self.quote

    def get_absolute_url(self):
        return reverse('detail', kwargs={'quote_id': self.id})
