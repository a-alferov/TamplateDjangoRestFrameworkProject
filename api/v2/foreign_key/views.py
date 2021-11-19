from rest_flex_fields.serializers import FlexFieldsSerializerMixin
from rest_framework import serializers
from rest_framework import viewsets
from rest_framework.schemas.openapi import AutoSchema

from api.models import Reporter, Article


class ReporterView(viewsets.ModelViewSet):
    class ReporterSerializer(FlexFieldsSerializerMixin, serializers.ModelSerializer):
        url = serializers.HyperlinkedIdentityField(view_name='v2-reporter-detail')

        class Meta:
            model = Reporter
            fields = ('id', 'first_name', 'last_name', 'email', 'url')

    queryset = Reporter.objects.all()
    serializer_class = ReporterSerializer
    filterset_fields = '__all__'
    ordering_fields = '__all__'
    schema = AutoSchema(
        tags=['V2-Reporter'],
        component_name='V2-Reporter',
        operation_id_base='V2-Reporter',
    )


class ArticleView(viewsets.ModelViewSet):
    class ArticleSerializer(FlexFieldsSerializerMixin, serializers.ModelSerializer):
        url = serializers.HyperlinkedIdentityField(view_name='v2-article-detail')

        class Meta:
            model = Article
            fields = (
                'id',
                'headline',
                'pub_date',
                'reporter',
                'url',
            )
            expandable_fields = {
                'reporter': ReporterView.ReporterSerializer
            }

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filterset_fields = '__all__'
    ordering_fields = '__all__'
    schema = AutoSchema(
        tags=['V2-Article'],
        component_name='V2-Article',
        operation_id_base='V2-Article'
    )
