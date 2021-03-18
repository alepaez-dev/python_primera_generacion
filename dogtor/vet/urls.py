from django.urls import path
from .views import list_pet_owners, Test, Owners, OwnersList, OwnersDetail, PetsList, PetsDetail

urlpatterns = [
  path("owners/", OwnersList.as_view()),
  path("pets/", PetsList.as_view()),
  path("owners/<int:pk>/", OwnersDetail.as_view()),
  path("pets/<int:id>/", PetsDetail.as_view()),
  path("test/", Test.as_view()),
]