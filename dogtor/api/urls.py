from django.urls import path, include
from rest_framework import routers
from .views import ListOwnersAPIView, RetrieveOwnersAPIView, CreateOwnersAPIView, UpdateOwnersAPIView, ListPetsAPIView, CreatePetsAPIView, RetrievePetsAPIView, UpdatePetsAPIView, DestroyOwnersAPIView, DestroyPetsAPIView

urlpatterns = [
    path("owners/", ListOwnersAPIView.as_view(), name="list_owners"),
    path("owners/<int:pk>/", RetrieveOwnersAPIView.as_view(), name="retrieve_owners"),
    path("owners/create/", CreateOwnersAPIView.as_view(), name="create_owners"),
    path("owners/<int:pk>/update/", UpdateOwnersAPIView.as_view(), name="update_owners"),
    path("owners/<int:pk>/destroy/", DestroyOwnersAPIView.as_view(), name="destroy_owners"),
    path("pets/", ListPetsAPIView.as_view(), name="list_pets"),
    path("pets/<int:pk>/", RetrievePetsAPIView.as_view(), name="retrieve_pets"),
    path("pets/create/", CreatePetsAPIView.as_view(), name="create_pets"),
    path("pets/<int:pk>/update/", UpdatePetsAPIView.as_view(), name="update_pets"),
    path("pets/<int:pk>/destroy/", DestroyPetsAPIView.as_view(), name="destroy_pets"),
]