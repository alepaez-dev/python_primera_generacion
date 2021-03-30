from rest_framework import generics

from django.contrib.auth.models import User

from vet.models import PetOwner, Pet, PetDate, Office

from .serializers import (
    OwnersListSerializer, 
    OwnersSerializer, 
    PetsListSerializer, 
    PetsSerializer,
    OwnerPetsSerializer,
    PetOwnerDateSerializer,
    DatesListSerializer,
    DatesSerializer,
    DatePetsSerializers,
    OfficesListSerializer,
    OfficesSerializer,
    OfficesDateSerializer,
    OwnerPetsDatesSerializer,
    #Users
    UsersSerializer,
)
    

# Create your views here.

class ListOwnersAPIView(generics.ListAPIView):
    queryset = PetOwner.objects.all().order_by("created_at")
    serializer_class = OwnersListSerializer

class CreateOwnersAPIView(generics.CreateAPIView):
    queryset = PetOwner.objects.all()
    serializer_class = OwnersSerializer


class RetrieveOwnersAPIView(generics.RetrieveAPIView):
    queryset = PetOwner.objects.all()
    serializer_class = OwnersSerializer

class UpdateOwnersAPIView(generics.UpdateAPIView):
    queryset = PetOwner.objects.all()
    serializer_class = OwnersSerializer

class DestroyOwnersAPIView(generics.DestroyAPIView):
    queryset = PetOwner.objects.all()
    serializer_class = OwnersSerializer

# pets
class ListPetsAPIView(generics.ListAPIView):
    queryset = Pet.objects.all().order_by("created_at")
    serializer_class = PetsListSerializer

class CreatePetsAPIView(generics.CreateAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetsSerializer


class RetrievePetsAPIView(generics.RetrieveAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetsSerializer

class UpdatePetsAPIView(generics.UpdateAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetsSerializer

class DestroyPetsAPIView(generics.DestroyAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetsSerializer

# dates
class ListDatesAPIView(generics.ListAPIView):
    queryset = PetDate.objects.all().order_by("created_at")
    serializer_class = DatesListSerializer

class CreateDatesAPIView(generics.CreateAPIView):
    queryset = PetDate.objects.all()
    serializer_class = DatesSerializer

class RetrieveDatesAPIView(generics.RetrieveAPIView):
    queryset = PetDate.objects.all()
    serializer_class = DatesSerializer

class UpdateDatesAPIView(generics.UpdateAPIView):
    queryset = PetDate.objects.all()
    serializer_class = DatesSerializer

class DestroyDatesAPIView(generics.DestroyAPIView):
    queryset = PetDate.objects.all()
    serializer_class = DatesSerializer


#vista especial
class RetrieveOwnerPetsAPIView(generics.RetrieveAPIView):
    queryset = PetOwner.objects.all()
    serializer_class = OwnerPetsSerializer


class RetrievePetsOwnerDateAPIView(generics.RetrieveAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetOwnerDateSerializer

class RetrieveDatesPetAPIView(generics.RetrieveAPIView):
    queryset = PetDate.objects.all()
    serializer_class = DatePetsSerializers

#Sucursal
class ListOfficesAPIView(generics.ListAPIView):
    queryset = Office.objects.all().order_by("created_at")
    serializer_class = OfficesListSerializer

class CreateOfficesAPIView(generics.CreateAPIView):
    queryset = Office.objects.all()
    serializer_class = OfficesSerializer

class RetrieveOfficesDateAPIView(generics.RetrieveAPIView):
    queryset = Office.objects.all()
    serializer_class = OfficesDateSerializer

class RetrieveOwnerPetsDatesAPIView(generics.RetrieveAPIView):
    queryset = PetOwner.objects.all()
    serializer_class = OwnerPetsDatesSerializer

#Vista para regresar el filter de IsAvailable
class RetrieveOfficesFilterIsAvailableAPIView(generics.ListAPIView):
    serializer_class = OfficesSerializer

    def get_queryset(self):
        """Filtering with the URL"""
        isAvailable = self.kwargs["pk"]
        return Office.objects.filter(isAvailable=isAvailable)


# Users

class CreateUsersAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UsersSerializer