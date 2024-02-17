from django.core.exceptions import ValidationError
from django.db import models
from django.core.validators import MinLengthValidator, BaseValidator

from softuni_petstagram.pets.models import Pet


def random_validator(value):
    # if invalid, raise validation error
    # else, if valid, do nothing
    pass


SIZE_5MB = 5 * 1024 * 1024


class MaxFileSizeValidator(BaseValidator):
    def clean(self, x):
        return x.size

    def compare(self, file_size, max_size):
        return max_size < file_size


def validate_image_size_less_than_5mb(value):
    if value.size > SIZE_5MB:
        raise ValidationError('Image size must be less than 5MB')


class PetPhoto(models.Model):
    MIN_DESCRIPTION_LENGTH = 10
    MAX_DESCRIPTION_LENGTH = 300

    MAX_LOCATION_LENGTH = 30

    photo = models.ImageField(
        upload_to='pet_photos/',
        null=False,
        blank=False,
        validators=(
            # validate_image_size_less_than_5mb,
            MaxFileSizeValidator(limit_value=SIZE_5MB),
        )
    )

    description = models.TextField(
        blank=True,
        null=True,
        max_length=MAX_DESCRIPTION_LENGTH,
        validators=(
            MinLengthValidator(MIN_DESCRIPTION_LENGTH),
        )
    )

    location = models.CharField(
        max_length=MAX_LOCATION_LENGTH,
        blank=True,
        null=True,
    )

    pets = models.ManyToManyField(Pet)

    created_at = models.DateTimeField(
        auto_now_add=True,  # done only on create
    )

    modified_at = models.DateTimeField(
        auto_now=True,  # done on every save
    )
