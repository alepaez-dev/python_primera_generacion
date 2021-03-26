from django import forms 

from .models import PetOwner, Pet, PetDate

class OwnerForm(forms.ModelForm):

    class Meta:
        model = PetOwner
        fields = ["first_name","last_name", "address", "email","phone"]
        # widgets = {
        #     "email": forms.EmailInput()
        # }

class PetForm(forms.ModelForm):

    class Meta:
        model = Pet
        fields = ["name", "type", "owner"]


class PetsDateForm(forms.ModelForm):

    class Meta:
        model = PetDate
        fields = ["datetime", "type", "pet"]
