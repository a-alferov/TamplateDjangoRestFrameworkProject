from rest_flex_fields.serializers import FlexFieldsSerializerMixin
from rest_framework import serializers
from rest_framework import viewsets
from rest_framework.schemas.openapi import AutoSchema
from rest_framework.viewsets import ModelViewSet
from rest_framework_extensions.mixins import NestedViewSetMixin

from api.models import Pizza, Topping


class ToppingView(NestedViewSetMixin, ModelViewSet):
    class ToppingSerializer(FlexFieldsSerializerMixin, serializers.ModelSerializer):
        url = serializers.HyperlinkedIdentityField(view_name='v2-topping-detail')

        class Meta:
            model = Topping
            fields = ('id', 'name', 'created_date', 'url')

    queryset = Topping.objects.all()
    serializer_class = ToppingSerializer
    filterset_fields = '__all__'
    ordering_fields = '__all__'
    schema = AutoSchema(
        tags=['V2-Topping'],
        component_name='V2-Topping',
        operation_id_base='V2-Topping',
    )


class PizzaView(NestedViewSetMixin, viewsets.ModelViewSet):
    class PizzaSerializer(FlexFieldsSerializerMixin, serializers.ModelSerializer):
        url = serializers.HyperlinkedIdentityField(view_name='v2-pizza-detail')

        class Meta:
            model = Pizza
            fields = ('id', 'name', 'created_date', 'toppings', 'url')
            expandable_fields = {
                'toppings': (ToppingView.ToppingSerializer, {'many': True}),
            }

    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer
    filterset_fields = '__all__'
    ordering_fields = '__all__'
    schema = AutoSchema(
        tags=['V2-Pizza'],
        component_name='V2-Pizza',
        operation_id_base='V2-Pizza',
    )
