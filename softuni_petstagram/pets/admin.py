from django.contrib import admin

from softuni_petstagram.pets.models import  Pet

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_of_birth', 'slug')