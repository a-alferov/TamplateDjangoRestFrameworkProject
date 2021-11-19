from rest_flex_fields.serializers import FlexFieldsSerializerMixin
from rest_framework import serializers
from rest_framework import viewsets
from rest_framework.schemas.openapi import AutoSchema

from api.models import Pizza, Topping
from api.utils import IdHyperlinkedModelSerializer


class ToppingView(viewsets.ModelViewSet):
    class ToppingSerializer(FlexFieldsSerializerMixin, serializers.ModelSerializer):
        url = serializers.HyperlinkedIdentityField(view_name='v3-topping-detail')

        class Meta:
            model = Topping
            fields = ('id', 'name', 'created_date', 'url')

    queryset = Topping.objects.all()
    serializer_class = ToppingSerializer
    filterset_fields = '__all__'
    ordering_fields = '__all__'
    schema = AutoSchema(
        tags=['V3-Topping'],
        component_name='V3-Topping',
        operation_id_base='V3-Topping',
    )


class PizzaToppingSerializer(serializers.Serializer):
    id = serializers.PrimaryKeyRelatedField(queryset=Topping.objects.all())
    url = serializers.HyperlinkedIdentityField(view_name='v3-topping-detail')


class PizzaView(viewsets.ModelViewSet):
    class PizzaSerializer(FlexFieldsSerializerMixin, IdHyperlinkedModelSerializer):
        url = serializers.HyperlinkedIdentityField(view_name='v3-pizza-detail')

        # toppings = PizzaToppingSerializer(many=True)

        class Meta:
            model = Pizza
            fields = (
                'id',
                'name',
                'created_date',
                'toppings',
                'url',
            )
            extra_kwargs = {
                'toppings': {'many': True, 'view_name': 'v3-topping-detail'}
            }
            expandable_fields = {
                'toppings': (ToppingView.ToppingSerializer, {'many': True})
            }

    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer
    filterset_fields = '__all__'
    ordering_fields = '__all__'
    schema = AutoSchema(
        tags=['V3-Pizza'],
        component_name='V3-Pizza',
        operation_id_base='V3-Pizza',
    )
