from django.urls import path, include

from softuni_petstagram.accounts.views import (signup_user, signin_user, delete_profile,
                                               details_profile, edit_profile, signout_user)

urlpatterns = (
    path('signup/', signup_user, name='signup'),
    path('signin/', signin_user, name='signin'),
    path('signout/', signout_user, name='sign_out'),
    path(
        "profile/<int:pk>/", include([
            path("", details_profile, name="details_profile"),
            path("edit/", edit_profile, name="edit_profile"),
            path("delete/", delete_profile, name="delete_profile")
        ]),
    )
)
