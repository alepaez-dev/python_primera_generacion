from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy

from .models import PetOwner, Pet
from .forms import OwnerForm, PetForm

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

class OwnersList(ListView):
    model = PetOwner
    template_name = "vet/owners/list.html"
    context_object_name = "owners"

def test(request):
    print(request.__dict__)
    return HttpResponse("Hello world!!")

class OwnersDetail(DetailView):
    model = PetOwner
    template_name = "vet/owners/detail.html"
    context_object_name = "owner"

#clases
class Test(View):

    def get(self, request):
        return HttpResponse("Hello world from class view!!")

###Pet

class PetsList(ListView):
    model = Pet
    template_name = "vet/pets/list.html"
    context_object_name = "pets"
# class PetsList(TemplateView):
#     template_name = "vet/pets/list.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['pets'] = Pet.objects.all()
#         return context

class PetsDetail(DetailView):
    model = Pet
    template_name = "vet/pets/detail.html"
    context_object_name = "pet"

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

class OwnersCreate(CreateView):
    model = PetOwner
    template_name = "vet/owners/create.html"
    form_class = OwnerForm
    success_url = reverse_lazy("vet:owners_list")

class PetsCreate(CreateView):
    model = Pet
    template_name = "vet/pets/create.html"
    form_class = PetForm
    success_url = reverse_lazy("vet:pets_list")

    def get_initial(self):
        initial = {}
        for queryparam in self.request.GET:
            initial[queryparam] = self.request.GET[queryparam]
        return initial
      
class OwnersUpdate(UpdateView):
    model = PetOwner
    template_name = "vet/owners/update.html"
    form_class = OwnerForm
    success_url = reverse_lazy("vet:owners_list")

          
class PetsUpdate(UpdateView):
    model = Pet
    template_name = "vet/pets/update.html"
    form_class = PetForm
    success_url = reverse_lazy("vet:pets_list")