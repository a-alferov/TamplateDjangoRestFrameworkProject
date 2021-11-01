from django.contrib.contenttypes.models import ContentType
from django_filters import FilterSet, ChoiceFilter, NumberFilter

from api.models import TaggedItem, TaggedObjectType


class ContentTypeChoiceFilter(ChoiceFilter):
    def filter(self, qs, value):
        if value != '':
            content_type = ContentType.objects.get(model=value, app_label='api')
            return qs.filter(content_type=content_type)
        return super().filter(qs, value)


class TagFilterSet(FilterSet):
    content_type = ContentTypeChoiceFilter(choices=TaggedObjectType.choices)
    tagged_object = NumberFilter(field_name='object_id', label='Tagged object id')

    class Meta:
        model = TaggedItem
        fields = (
            'id',
            'content_type',
            'tagged_object',
            'created_date',
            'updated_date',
        )
