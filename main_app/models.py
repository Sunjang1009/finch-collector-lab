from django.db import models

# Create your models here.
class Corgi(models.Model):
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


class Dog(models.Model):
    name = models.CharField(max_length=100)
    weight = models.IntegerField(default=10)
    color = models.CharField(max_length=100)
    Female = "Female"
    Male = "Male"
    DOG_GENDER_CHOICES = [
        (Female,"Female"),
        (Male, "Male"),
    ]
    gender = models.CharField(max_length=10,
    choices=DOG_GENDER_CHOICES,
    default="female",
    )
    corgi = models.ForeignKey(Corgi, on_delete=models.CASCADE, related_name="dogs")
    def __str__(self):
        return self.name

