from django.urls import path
from rest_framework_extensions.routers import ExtendedDefaultRouter as DefaultRouter

from .root import ManyToManyRoot
from .views import PizzaViewSet, ToppingViewSet, PizzaToppingViewSet

router = DefaultRouter()

pizza = router.register(r'pizza', PizzaViewSet, basename='pizza')
pizza.register(r'topping', PizzaToppingViewSet, basename='pizza-topping',
               parents_query_lookups=['pizza'])
topping = router.register(r'topping', ToppingViewSet, basename='topping')

urlpatterns = [
    path(r'', ManyToManyRoot.as_view(), name='many-to-many')
]

urlpatterns.extend(router.urls)
