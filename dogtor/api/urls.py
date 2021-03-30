from django.urls import path, include
from rest_framework import routers
from .views import (
    ListOwnersAPIView, 
    RetrieveOwnersAPIView, 
    CreateOwnersAPIView, 
    UpdateOwnersAPIView, 
    ListPetsAPIView, 
    CreatePetsAPIView, 
    RetrievePetsAPIView, 
    UpdatePetsAPIView,
    DestroyOwnersAPIView, 
    DestroyPetsAPIView,
    RetrieveOwnerPetsAPIView,
    RetrievePetsOwnerDateAPIView,
    ListDatesAPIView,
    CreateDatesAPIView,
    RetrieveDatesAPIView,
    UpdateDatesAPIView,
    DestroyDatesAPIView,
    RetrieveDatesPetAPIView,
    ListOfficesAPIView,
    CreateOfficesAPIView,
    RetrieveOfficesDateAPIView,
    RetrieveOwnerPetsDatesAPIView,
    RetrieveOfficesFilterIsAvailableAPIView,
    #Users
    CreateUsersAPIView,
)



urlpatterns = [
    path("owners/", ListOwnersAPIView.as_view(), name="list_owners"),
    path("owners/<int:pk>/", RetrieveOwnersAPIView.as_view(), name="retrieve_owners"),
    path("owners/create/", CreateOwnersAPIView.as_view(), name="create_owners"),
    path("owners/<int:pk>/update/", UpdateOwnersAPIView.as_view(), name="update_owners"),
    path("owners/<int:pk>/destroy/", DestroyOwnersAPIView.as_view(), name="destroy_owners"),
    path("owners/<int:pk>/pets/", RetrieveOwnerPetsAPIView.as_view(), name="retrieve-owner-pets"),
    path("owners/<int:pk>/pets_dates/", RetrieveOwnerPetsDatesAPIView.as_view(), name="retrieve-owner-pets-dates"),
    path("pets/", ListPetsAPIView.as_view(), name="list_pets"),
    path("pets/<int:pk>/", RetrievePetsAPIView.as_view(), name="retrieve_pets"),
    path("pets/create/", CreatePetsAPIView.as_view(), name="create_pets"),
    path("pets/<int:pk>/update/", UpdatePetsAPIView.as_view(), name="update_pets"),
    path("pets/<int:pk>/destroy/", DestroyPetsAPIView.as_view(), name="destroy_pets"),
    path("pets/<int:pk>/owner/", RetrievePetsOwnerDateAPIView.as_view(), name="retrieve-pets-owner"),
    path("dates/", ListDatesAPIView.as_view(), name="list_dates"),
    path("dates/<int:pk>/", RetrieveDatesAPIView.as_view(), name="retrieve_dates"),
    path("dates/create/", CreateDatesAPIView.as_view(), name="create_dates"),
    path("dates/<int:pk>/update", UpdateDatesAPIView.as_view(), name="update_dates"),
    path("dates/<int:pk>/destroy", DestroyDatesAPIView.as_view(), name="destroy_dates"),
    path("dates/<int:pk>/pet", RetrieveDatesPetAPIView.as_view(), name="retrieve-dates-pet"),
    path("offices/", ListOfficesAPIView.as_view(), name="list_offices"),
    path("offices/create/", CreateOfficesAPIView.as_view(), name="create_offices"),
    path("offices/<int:pk>/", RetrieveOfficesDateAPIView.as_view(), name="retrieve_offices"),
    path("offices/isAvailable/<str:pk>/",RetrieveOfficesFilterIsAvailableAPIView.as_view(), name="retrieve_offices_isAvailable"),
    #Users
    path("users/create/",CreateUsersAPIView.as_view(), name="create_users"),
]