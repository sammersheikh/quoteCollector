from django.db import models

# Create your models here.

class Quote(models.Model):
    category = models.CharField(max_length=100)
    quote = models.TextField(max_length=250)
    by = models.CharField(max_length=100)

    def __str__(self):
        return self.quote

