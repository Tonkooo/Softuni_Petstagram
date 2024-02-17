from django.contrib import admin

from softuni_petstagram.photos.models import PetPhoto


@admin.register(PetPhoto)
class PetPhotoAdmin(admin.ModelAdmin):
    #list_display = ('photo', 'description', 'location')
    pass