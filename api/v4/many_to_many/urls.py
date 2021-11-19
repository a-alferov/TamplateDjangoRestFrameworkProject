from django.urls import path
from rest_framework_extensions.routers import ExtendedDefaultRouter as DefaultRouter

from .root import ManyToMany
from .views import PizzaView, ToppingView, PizzaToppingView

router = DefaultRouter()

pizza = router.register(r'pizza', PizzaView, basename='v4-pizza')
pizza.register(r'topping', PizzaToppingView, basename='v4-pizza-topping',
               parents_query_lookups=['pizza'])
topping = router.register(r'topping', ToppingView, basename='v4-topping')

urlpatterns = [
    path(r'', ManyToMany.as_view(), name='v4-many-to-many'),
]

urlpatterns.extend(router.urls)
