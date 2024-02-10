from django.urls import path

from softuni_petstagram.common.views import index

urlpatterns = (
    path('', index, name='index'),
)
