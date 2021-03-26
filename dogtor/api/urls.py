from django.urls import path, include
from rest_framework import routers
from .views import OwnersViewSet, PetsDateViewSet, PetsViewSet

router = routers.DefaultRouter()
router.register(r"owners", OwnersViewSet)
router.register(r"pets", PetsViewSet)
router.register(r"dates", PetsDateViewSet)

urlpatterns = [
    #ViewSets
    path("", include(router.urls)),
]
