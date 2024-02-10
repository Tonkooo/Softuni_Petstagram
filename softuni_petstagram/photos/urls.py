from softuni_petstagram.photos.views import create_photo, details_photo, edit_photo
from django.urls import path, include

urlpatterns = (
    path("create/", create_photo, name="create_photo"),
    path("<int:pk>/", include([
            path("", details_photo, name="details_photo"),
            path("edit/", edit_photo, name="edit_photo"),

        ]),
    ),
)