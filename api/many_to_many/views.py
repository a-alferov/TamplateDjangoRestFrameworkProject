from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.mixins import (
    ListModelMixin,
    CreateModelMixin,
    RetrieveModelMixin,
    DestroyModelMixin,
)
from rest_framework.response import Response
from rest_framework.schemas.openapi import AutoSchema
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework_extensions.mixins import NestedViewSetMixin

from api.models import Pizza, Topping
from .serializers import PizzaSerializer, ToppingSerializer, PizzaToppingSerializer
from .services import topping_add, topping_remove


class PizzaViewSet(NestedViewSetMixin, ModelViewSet):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer
    filterset_fields = ('id', 'name', 'created_date', 'toppings')
    ordering_fields = ('id', 'name', 'created_date')


class PizzaToppingViewSet(
    NestedViewSetMixin,
    ListModelMixin,
    RetrieveModelMixin,
    CreateModelMixin,
    DestroyModelMixin,
    GenericViewSet
):
    queryset = Topping.objects.all()
    serializer_class = PizzaToppingSerializer
    filterset_fields = ('id', 'name', 'created_date')
    ordering_fields = ('id', 'name', 'created_date')
    schema = AutoSchema(
        tags=['PizzaTopping'],
        component_name='PizzaTopping',
        operation_id_base='PizzaTopping'
    )

    def get_serializer_context(self):
        context = super().get_serializer_context()
        pizza_id = self.kwargs.get('parent_lookup_pizza')
        if pizza_id is not None:
            context.update({'pizza': get_object_or_404(Pizza.objects.all(), id=pizza_id)})
        return context

    def create(self, request, *args, **kwargs):
        pizza = get_object_or_404(Pizza.objects.all(), id=kwargs.get('parent_lookup_pizza'))
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        topping = serializer.validated_data['id']

        topping_add(pizza, topping)

        return Response(self.get_serializer(topping).data, status=status.HTTP_201_CREATED)

    def destroy(self, request, *args, **kwargs):
        pizza = get_object_or_404(Pizza.objects.all(), id=kwargs.get('parent_lookup_pizza'))
        topping = self.get_object()

        topping_remove(pizza, topping)

        return Response(status=status.HTTP_204_NO_CONTENT)


class ToppingViewSet(NestedViewSetMixin, ModelViewSet):
    queryset = Topping.objects.all()
    serializer_class = ToppingSerializer
    filterset_fields = ('id', 'name', 'created_date')
    ordering_fields = ('id', 'name', 'created_date')
