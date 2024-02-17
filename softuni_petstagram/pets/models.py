from django.db import models
from django.template.defaultfilters import slugify
# Create your models here.
class Pet(models.Model):
    MAX_LENGTH = 30
    name = models.CharField(max_length=MAX_LENGTH, null=False, blank=False,)
    pet_photo = models.URLField(null=False, blank=False,)

    date_of_birth = models.DateField(null=True, blank=True,)

    slug = models.SlugField(
        unique=True,
        null=False,
        blank=True,
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.name}-{self.pk}")

        super().save(*args, **kwargs)

