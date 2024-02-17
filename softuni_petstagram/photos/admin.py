from django.contrib import admin

from softuni_petstagram.photos.models import PetPhoto


@admin.register(PetPhoto)
class PetPhotoAdmin(admin.ModelAdmin):
    list_display = ('short_description', 'pk', 'location', 'created_at', 'tagged_pets')

    def short_description(self, obj):
        return obj.description[:25]

    def tagged_pets(self, obj):
        return ', '.join(pet.name for pet in obj.pets.all())

