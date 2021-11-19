from django.urls import path
from rest_framework.routers import DefaultRouter

from .root import ManyToMany
from .views import PizzaView, ToppingView

router = DefaultRouter()

router.register(r'pizza', PizzaView, basename='v3-pizza')
router.register(r'topping', ToppingView, basename='v3-topping')

urlpatterns = [
    path(r'', ManyToMany.as_view(), name='v3-many-to-many'),
]

urlpatterns.extend(router.urls)
