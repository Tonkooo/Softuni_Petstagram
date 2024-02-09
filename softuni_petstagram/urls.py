from django.contrib import admin
from django.urls import path, include

from softuni_petstagram.accounts.urls import details_profile

urlpatterns = (
    path('admin/', admin.site.urls),
    path('accounts/', include('softuni_petstagram.accounts.urls')),
    path('', include('softuni_petstagram.common.urls')),
    path('pets/', include('softuni_petstagram.pets.urls')),
    path('photos/', include('softuni_petstagram.photos.urls')),

)
