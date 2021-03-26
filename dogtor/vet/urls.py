from django.urls import path
from .views import list_pet_owners, Test, Owners, OwnersList, OwnersDetail, PetsList, PetsDetail, OwnersCreate, PetsCreate, OwnersUpdate, PetsUpdate,PetsDateList,PetsDateUpdate, PetsDetail, PetsDateCreate

urlpatterns = [
  path("owners/", OwnersList.as_view(), name="owners_list"),
  path("owners/add", OwnersCreate.as_view(), name="owners_create"),
  path("owners/<int:pk>/", OwnersDetail.as_view(), name="owners_detail"),
  path("owners/<int:pk>/update", OwnersUpdate.as_view(), name="owners_update"),
  path("pets/", PetsList.as_view(), name="pets_list"),
  path("pets/add", PetsCreate.as_view(), name="pets_create"),
  path("pets/<int:pk>/", PetsDetail.as_view(), name="pets_detail"),
  path("pets/<int:pk>/update", PetsUpdate.as_view(), name="pets_update"),
  path("petsdate/", PetsDateList.as_view(), name="petsdate_list"),
  path("petsdate/add", PetsDateCreate.as_view(), name="petsdate_create"),
  path("petsdate/<int:pk>/", PetsDetail.as_view(), name="petsdate_detail"),
  path("petsdate/<int:pk>/update", PetsDateUpdate.as_view(), name="petsdate_update"),
  path("test/", Test.as_view()),
]