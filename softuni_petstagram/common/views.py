from django.shortcuts import render

from softuni_petstagram.photos.models import PetPhoto


def index(request):
    context = {
        'pet_photos': PetPhoto.objects.all(),

    }
    return render(request, 'common/index.html', context)
