from django.db import models

from softuni_petstagram.photos.models import PetPhoto

'''
The field Comment Text is required:
•	Comment Text - it should consist of a maximum of 300 characters.
An additional field should be created:
•	Date and Time of Publication - when a comment is created (only), the date of publication is automatically generated.
One more thing we should keep in mind is that the comment should relate to the photo (as in social apps users comment on a specific photo/post, i.e., the comment object is always connected to the photo object).
Open the common/models.py file and let us create the model: 
'''
class PhotoComment(models.Model):
    MAX_TEXT_LENGTH = 300

    text = models.TextField(
        max_length=MAX_TEXT_LENGTH,
        null=False,
        blank=False,
    )

    created_at = models.DateTimeField(auto_now_add=True,)

    modified_at = models.DateTimeField(auto_now=True, )

    pet_photo = models.ForeignKey(PetPhoto, on_delete=models.DO_NOTHING)

class PhotoLike(models.Model):
    pet_photo = models.ForeignKey(PetPhoto, on_delete=models.DO_NOTHING)
