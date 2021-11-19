from rest_flex_fields.serializers import FlexFieldsSerializerMixin
from rest_framework import serializers
from rest_framework import viewsets
from rest_framework.schemas.openapi import AutoSchema
from rest_framework.viewsets import ModelViewSet
from rest_framework_extensions.mixins import NestedViewSetMixin

from api.models import Pizza, Topping


class ToppingView(NestedViewSetMixin, ModelViewSet):
    class ToppingSerializer(FlexFieldsSerializerMixin, serializers.HyperlinkedModelSerializer):
        class Meta:
            model = Topping
            fields = ('id', 'name', 'created_date', 'url')
            extra_kwargs = {
                'url': {'view_name': 'v1-topping-detail'}
            }

    queryset = Topping.objects.all()
    serializer_class = ToppingSerializer
    filterset_fields = '__all__'
    ordering_fields = '__all__'
    schema = AutoSchema(
        tags=['V1-Topping'],
        component_name='V1-Topping',
        operation_id_base='V1-Topping',
    )


class PizzaView(NestedViewSetMixin, viewsets.ModelViewSet):
    class PizzaSerializer(FlexFieldsSerializerMixin, serializers.HyperlinkedModelSerializer):
        class Meta:
            model = Pizza
            fields = ('id', 'name', 'created_date', 'toppings', 'url')
            extra_kwargs = {
                'url': {'view_name': 'v1-pizza-detail'},
                'toppings': {'view_name': 'v1-topping-detail', 'many': True}
            }
            expandable_fields = {
                'toppings': (ToppingView.ToppingSerializer, {'many': True}),
            }

    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer
    filterset_fields = '__all__'
    ordering_fields = '__all__'
    schema = AutoSchema(
        tags=['V1-Pizza'],
        component_name='V1-Pizza',
        operation_id_base='V1-Pizza',
    )
