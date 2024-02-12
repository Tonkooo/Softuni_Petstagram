from django.db import models

# Create your models here.
class Pet(models.Model):
    MAX_LENGTH = 30
    name = models.CharField(max_length=MAX_LENGTH, null=False, blank=False)
    pet_photo = models.URLField(null=False, blank=False)

    date_of_birth = models.DateField(null=False, blank=False)

    slug = models.SlugField(
        unique=True,
        null=False,
        bland=True,
    )
