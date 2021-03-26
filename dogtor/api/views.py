from rest_framework import viewsets

from vet.models import PetOwner, Pet, PetDate
from .serializers import OwnersSerializer, DatesSerializer, PetsSerializer

# Create your views here.
class OwnersViewSet(viewsets.ModelViewSet):
    """
    ViewSet del modelo PetOwners.
    """

    queryset = PetOwner.objects.all()
    serializer_class = OwnersSerializer

class PetsViewSet(viewsets.ModelViewSet):
    """
    ViewSet del modelo PetOwners.
    """

    queryset = Pet.objects.all()
    serializer_class = PetsSerializer

class PetsDateViewSet(viewsets.ModelViewSet):
    """
    ViewSet del modelo PetOwners.
    """

    queryset = PetDate.objects.all()
    serializer_class = DatesSerializer