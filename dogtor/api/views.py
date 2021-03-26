from rest_framework import generics

from vet.models import PetOwner, Pet, PetDate

from .serializers import (
    OwnersListSerializer, 
    OwnersSerializer, 
    PetsListSerializer, 
    PetsSerializer,
    OwnerPetsSerializer,
    PetOwnerSerializer,
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


#vista especial
class RetrieveOwnerPetsAPIView(generics.RetrieveAPIView):
    queryset = PetOwner.objects.all()
    serializer_class = OwnerPetsSerializer


class RetrievePetsOwnerAPIView(generics.RetrieveAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetOwnerSerializer