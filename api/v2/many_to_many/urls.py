from django.urls import path
from rest_framework.routers import DefaultRouter

from .root import ManyToMany
from .views import PizzaView, ToppingView

router = DefaultRouter()

router.register(r'pizza', PizzaView, basename='v2-pizza')
router.register(r'topping', ToppingView, basename='v2-topping')

urlpatterns = [
    path(r'', ManyToMany.as_view(), name='v2-many-to-many'),
]

urlpatterns.extend(router.urls)
