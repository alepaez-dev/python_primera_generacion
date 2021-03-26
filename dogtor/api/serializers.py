 
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

class DatesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetDate
        fields = [
            "datetime",
            "type",
        ]

class DatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetDate
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

class PetOwnerDateSerializer(serializers.ModelSerializer):
    #llave foranea
    owner = OwnersListSerializer()
    dates = DatesListSerializer(many=True)
    class Meta:
        model = Pet
        fields = [
            "id",
            "name",
            "type",
            "created_at",
            "owner",
            "dates",
        ]

class DatePetsSerializers(serializers.ModelSerializer):
    #llave foranea
    pet = PetsListSerializer()
    class Meta:
        model = PetDate
        fields = [
            "datetime",
            "type",
            "created_at",
            "pet",
        ]
