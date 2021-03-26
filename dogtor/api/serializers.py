 
from rest_framework import serializers

from vet.models import PetOwner, Pet, PetDate

# Serializers define the API representation.

class OwnersListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetOwner
        fields = ["id", "first_name","last_name"]

class OwnersSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetOwner
        fields = "__all__"

class PetsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = ["id", "name","type"]

class PetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = "__all__"

class OwnerPetsSerializer(serializers.ModelSerializer):
    # llave foranea
    pets = PetsListSerializer(many=True)
    class Meta:
        model = PetOwner
        fields = [
            "id",
            "first_name",
            "last_name",
            "email",
            "phone",
            "address",
            "created_at",
            "pets",
        ]

class PetOwnerSerializer(serializers.ModelSerializer):
    #llave foranea
    owner = OwnersListSerializer()
    class Meta:
        model = Pet
        fields = [
            "id",
            "name",
            "type",
            "created_at",
            "owner",
        ]
