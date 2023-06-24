from django.db import models

# Create your models here.
class Corgis(models.Model):
    name = models.CharField(max_length=100)
    mixes = models.CharField(max_length=250)
    image = models.CharField(max_length=250)
    bio = models.CharField(max_length=500)
    verified_corgi = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


