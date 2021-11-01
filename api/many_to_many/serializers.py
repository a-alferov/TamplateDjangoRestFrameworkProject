from rest_flex_fields.serializers import FlexFieldsSerializerMixin
from rest_framework import serializers
from rest_framework.reverse import reverse

from api.models import Pizza, Topping


class ToppingSerializer(FlexFieldsSerializerMixin, serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Topping
        fields = ('id', 'name', 'created_date', 'url')


class PizzaSerializer(FlexFieldsSerializerMixin, serializers.HyperlinkedModelSerializer):
    toppings = serializers.HyperlinkedRelatedField(
        view_name='pizza-topping-list',
        read_only=True,
        source='*',
        lookup_field='pk',
        lookup_url_kwarg='parent_lookup_pizza',
    )

    class Meta:
        model = Pizza
        fields = ('id', 'name', 'created_date', 'toppings', 'url')
        expandable_fields = {
            'toppings': (ToppingSerializer, {'many': True}),
        }


class PizzaToppingSerializer(FlexFieldsSerializerMixin, serializers.HyperlinkedModelSerializer):
    id = serializers.PrimaryKeyRelatedField(queryset=Topping.objects.all())
    url = serializers.SerializerMethodField()

    class Meta:
        model = Topping
        fields = ('id', 'name', 'created_date', 'url')
        read_only_fields = ('name', 'created_date', 'url')

    def get_url(self, obj):
        kwargs = {'parent_lookup_pizza': self.context['pizza'].id, 'pk': obj.id}
        return reverse(
            'pizza-topping-detail',
            kwargs=kwargs,
            request=self.context['request'],
            format=self.context['format'],
        )
