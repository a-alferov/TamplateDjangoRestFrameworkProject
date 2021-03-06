from rest_flex_fields.serializers import FlexFieldsSerializerMixin
from rest_framework import serializers
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.schemas.openapi import AutoSchema
from rest_framework.viewsets import ModelViewSet

from api.models import Article, Reporter
from .services import article_create


class ReporterView(ModelViewSet):
    class ReporterSerializer(FlexFieldsSerializerMixin, serializers.HyperlinkedModelSerializer):
        class Meta:
            model = Reporter
            fields = ('id', 'first_name', 'last_name', 'email', 'url')
            extra_kwargs = {
                'url': {'view_name': 'v1-reporter-detail'}
            }

    class CreateArticleSerializer(serializers.HyperlinkedModelSerializer):
        class Meta:
            model = Article
            fields = ('id', 'headline', 'pub_date', 'reporter', 'url')
            read_only_fields = ('reporter',)

    queryset = Reporter.objects.all()
    serializer_class = ReporterSerializer
    filterset_fields = '__all__'
    ordering_fields = '__all__'
    schema = AutoSchema(
        tags=['V1-Reporter'],
        component_name='V1-Reporter',
        operation_id_base='V1-Reporter'
    )

    @action(
        detail=True,
        methods=['post'],
        serializer_class=CreateArticleSerializer,
        schema=AutoSchema(
            tags=['V1-CreateArticle'],
            component_name='V1-CreateArticle',
            operation_id_base='V1-CreateArticle',
        )
    )
    def create_article(self, request, pk):
        reporter = self.get_object()
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)

        article = article_create(reporter, **serializer.validated_data)

        return Response(self.serializer_class(article, context={'request': request}).data,
                        status=status.HTTP_201_CREATED)


class ArticleView(ModelViewSet):
    class ArticleSerializer(FlexFieldsSerializerMixin, serializers.HyperlinkedModelSerializer):
        class Meta:
            model = Article
            fields = ('id', 'headline', 'pub_date', 'reporter', 'url')
            extra_kwargs = {
                'reporter': {'view_name': 'v1-reporter-detail'},
                'url': {'view_name': 'v1-article-detail'}
            }
            expandable_fields = {
                'reporter': ReporterView.ReporterSerializer
            }

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filterset_fields = '__all__'
    ordering_fields = '__all__'
    schema = AutoSchema(
        tags=['V1-Article'],
        component_name='V1-Article',
        operation_id_base='V1-Article',
    )
