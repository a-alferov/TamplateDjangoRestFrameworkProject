from django.contrib.contenttypes.models import ContentType
from rest_flex_fields.serializers import FlexFieldsSerializerMixin
from rest_framework import serializers
from rest_framework import viewsets

from api.models import TaggedItem, Bookmark, Note, TaggedObjectType
from .filters import TagFilterSet


class TaggedObjectTypeField(serializers.ChoiceField):
    def to_representation(self, value):
        return super().to_representation(value.model)

    def to_internal_value(self, data):
        data = super().to_internal_value(data)
        return ContentType.objects.get(model=data, app_label='api')


class TaggedObjectSerializer(serializers.Serializer):
    class BookmarkSerializer(serializers.ModelSerializer):
        class Meta:
            model = Bookmark
            fields = '__all__'

    class NoteSerializer(serializers.ModelSerializer):
        class Meta:
            model = Note
            fields = '__all__'

    def to_representation(self, instance):
        if isinstance(instance, Bookmark):
            serializer = self.BookmarkSerializer(instance)
        elif isinstance(instance, Note):
            serializer = self.NoteSerializer(instance)
        else:
            raise Exception('Unexpected type of tagged object')
        return serializer.data


class TagView(viewsets.ModelViewSet):
    class TaggedSerializer(FlexFieldsSerializerMixin, serializers.HyperlinkedModelSerializer):
        content_type = TaggedObjectTypeField(TaggedObjectType.choices)
        tagged_object = serializers.IntegerField(source='object_id')
        url = serializers.HyperlinkedIdentityField(view_name='tag-detail')

        class Meta:
            model = TaggedItem
            fields = (
                'id',
                'tag',
                'content_type',
                'created_date',
                'updated_date',
                'tagged_object',
                'url',
            )
            expandable_fields = {
                'tagged_object': TaggedObjectSerializer
            }

    queryset = TaggedItem.objects.all()
    serializer_class = TaggedSerializer
    filterset_class = TagFilterSet
    ordering_fields = '__all__'


class BookmarkView(viewsets.ModelViewSet):
    class BookmarkSerializer(FlexFieldsSerializerMixin, serializers.HyperlinkedModelSerializer):
        tags = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

        class Meta:
            model = Bookmark
            fields = ('id', 'uri', 'tags', 'url')
            expandable_fields = {
                'tags': (TagView.TaggedSerializer, {'many': True})
            }

    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer
    filterset_fields = '__all__'
    ordering_fields = '__all__'


class NoteView(viewsets.ModelViewSet):
    class NoteSerializer(FlexFieldsSerializerMixin, serializers.HyperlinkedModelSerializer):
        tags = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

        class Meta:
            model = Note
            fields = ('id', 'text', 'tags', 'url')
            expandable_fields = {
                'tags': (TagView.TaggedSerializer, {'many': True})
            }

    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    filterset_fields = '__all__'
    ordering_fields = '__all__'
