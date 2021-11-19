from rest_flex_fields.serializers import FlexFieldsSerializerMixin
from rest_framework import serializers
from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.reverse import reverse
from rest_framework.schemas.openapi import AutoSchema
from rest_framework_extensions.mixins import NestedViewSetMixin

from api.models import Pizza, Topping


class ToppingView(NestedViewSetMixin, viewsets.ModelViewSet):
    class ToppingSerializer(FlexFieldsSerializerMixin, serializers.ModelSerializer):
        url = serializers.HyperlinkedIdentityField(view_name='v4-topping-detail')

        class Meta:
            model = Topping
            fields = ('id', 'name', 'created_date', 'url')

    queryset = Topping.objects.all()
    serializer_class = ToppingSerializer
    filterset_fields = '__all__'
    ordering_fields = '__all__'
    schema = AutoSchema(
        tags=['V4-Topping'],
        component_name='V4-Topping',
        operation_id_base='V4-Topping',
    )


class PizzaView(NestedViewSetMixin, viewsets.ModelViewSet):
    class PizzaSerializer(FlexFieldsSerializerMixin, serializers.ModelSerializer):
        url = serializers.HyperlinkedIdentityField(view_name='v4-pizza-detail')
        toppings_url = serializers.HyperlinkedRelatedField(
            view_name='v4-pizza-topping-list',
            read_only=True,
            source='*',
            lookup_field='pk',
            lookup_url_kwarg='parent_lookup_pizza',
        )

        class Meta:
            model = Pizza
            fields = ('id', 'name', 'created_date', 'toppings', 'toppings_url', 'url')
            expandable_fields = {
                'toppings': (ToppingView.ToppingSerializer, {'many': True}),
            }

    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer
    filterset_fields = ('id', 'name', 'created_date', 'toppings')
    ordering_fields = ('id', 'name', 'created_date')
    schema = AutoSchema(
        tags=['V4-Pizza'],
        component_name='V4-Pizza',
        operation_id_base='V4-Pizza',
    )


class PizzaToppingView(NestedViewSetMixin, viewsets.ReadOnlyModelViewSet):
    class PizzaToppingSerializer(FlexFieldsSerializerMixin, serializers.ModelSerializer):
        id = serializers.PrimaryKeyRelatedField(queryset=Topping.objects.all())
        url = serializers.SerializerMethodField()

        class Meta:
            model = Topping
            fields = ('id', 'name', 'created_date', 'url')

        def get_url(self, obj):
            kwargs = {'parent_lookup_pizza': self.context['pizza'].id, 'pk': obj.id}
            return reverse(
                'v4-pizza-topping-detail',
                kwargs=kwargs,
                request=self.context['request'],
                format=self.context['format'],
            )

    queryset = Topping.objects.all()
    serializer_class = PizzaToppingSerializer
    filterset_fields = '__all__'
    ordering_fields = '__all__'
    schema = AutoSchema(
        tags=['V4-PizzaTopping'],
        component_name='V4-PizzaTopping',
        operation_id_base='V4-PizzaTopping',
    )

    def get_serializer_context(self):
        context = super().get_serializer_context()
        pizza_id = self.kwargs.get('parent_lookup_pizza')
        if pizza_id is not None:
            context.update({'pizza': get_object_or_404(Pizza.objects.all(), id=pizza_id)})
        return context
