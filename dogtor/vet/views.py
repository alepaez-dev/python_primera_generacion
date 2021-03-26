from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import PetOwner, Pet, PetDate
from .forms import OwnerForm, PetForm, PetsDateForm

# Create your views here.
def list_pet_owners(request):
    """List owners."""
    owners = PetOwner.objects.all()
    context = {"owners": owners}

    template = loader.get_template("vet/owners/list.html")
    return HttpResponse(template.render(context, request))

class Owners(View):
    def get(self, request):
        owners = PetOwner.objects.all()
        context = {"owners": owners}

        template = loader.get_template("vet/owners/list.html")
        return HttpResponse(template.render(context, request))

# class OwnersList(TemplateView):
#     template_name = "vet/owners/list.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['owners'] = PetOwner.objects.all()
#         return context

class OwnersList(LoginRequiredMixin, ListView):
    model = PetOwner
    template_name = "vet/owners/list.html"
    context_object_name = "owners"
    login_url = reverse_lazy("login")

def test(request):
    print(request.__dict__)
    return HttpResponse("Hello world!!")

class OwnersDetail(LoginRequiredMixin, DetailView):
    model = PetOwner
    template_name = "vet/owners/detail.html"
    context_object_name = "owner"
    login_url = reverse_lazy("login")

#clases
class Test(View):

    def get(self, request):
        return HttpResponse("Hello world from class view!!")

###Pet

class PetsList(LoginRequiredMixin, ListView):
    model = Pet
    template_name = "vet/pets/list.html"
    context_object_name = "pets"
    login_url = reverse_lazy("login")
# class PetsList(TemplateView):
#     template_name = "vet/pets/list.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['pets'] = Pet.objects.all()
#         return context

class PetsDetail(LoginRequiredMixin, DetailView):
    model = Pet
    template_name = "vet/pets/detail.html"
    context_object_name = "pet"
    login_url = reverse_lazy("login")

# class PetsDetail(TemplateView):
#     template_name = "vet/pets/detail.html"

#     def get_context_data(self, id, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['pet'] = Pet.objects.get(id=id)
#         return context

# class PetsDetail(View):
#     def get(self, request, id):
#         pet = Pet.objects.get(id=id)
#         context = {"pet": pet}
#         template = loader.get_template("vet/pets/detail.html")
#         return HttpResponse(template.render(context, request))

class OwnersCreate(LoginRequiredMixin, CreateView):
    model = PetOwner
    template_name = "vet/owners/create.html"
    form_class = OwnerForm
    success_url = reverse_lazy("vet:owners_list")
    login_url = reverse_lazy("login")

class PetsCreate(LoginRequiredMixin, CreateView):
    model = Pet
    template_name = "vet/pets/create.html"
    form_class = PetForm
    success_url = reverse_lazy("vet:pets_list")
    login_url = reverse_lazy("login")

    def get_initial(self):
        initial = {}
        for queryparam in self.request.GET:
            initial[queryparam] = self.request.GET[queryparam]
        return initial
      
class OwnersUpdate(LoginRequiredMixin, UpdateView):
    model = PetOwner
    template_name = "vet/owners/update.html"
    form_class = OwnerForm
    success_url = reverse_lazy("vet:owners_list")
    login_url = reverse_lazy("login")

          
class PetsUpdate(LoginRequiredMixin, UpdateView):
    model = Pet
    template_name = "vet/pets/update.html"
    form_class = PetForm
    success_url = reverse_lazy("vet:pets_list")
    login_url = reverse_lazy("login")

#PetDate

class PetsDateList(LoginRequiredMixin, ListView):
    model = PetDate
    template_name = "vet/petsdate/list.html"
    context_object_name = "petsdate"
    login_url = reverse_lazy("login")

class PetsDateCreate(LoginRequiredMixin, CreateView):
    model = PetDate
    template_name = "vet/petsdate/create.html"
    form_class = PetsDateForm
    success_url = reverse_lazy("vet:petsdate_list")
    login_url = reverse_lazy("login")


class PetsDetail(LoginRequiredMixin, DetailView):
    model = PetDate
    template_name = "vet/petsdate/detail.html"
    context_object_name = "petdate"
    login_url = reverse_lazy("login")
          
class PetsDateUpdate(LoginRequiredMixin, UpdateView):
    model = PetDate
    template_name = "vet/petsdate/update.html"
    form_class = PetsDateForm
    success_url = reverse_lazy("vet:petsdate_list")
    login_url = reverse_lazy("login")