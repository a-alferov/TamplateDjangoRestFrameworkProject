from rest_flex_fields.serializers import FlexFieldsSerializerMixin
from rest_framework import serializers
from rest_framework import viewsets
from rest_framework.reverse import reverse
from rest_framework.schemas.openapi import AutoSchema

from api.models import Reporter, Article


class ReporterView(viewsets.ModelViewSet):
    class ReporterSerializer(FlexFieldsSerializerMixin, serializers.ModelSerializer):
        url = serializers.HyperlinkedIdentityField(view_name='v3-reporter-detail')

        class Meta:
            model = Reporter
            fields = ('id', 'first_name', 'last_name', 'email', 'url')

    queryset = Reporter.objects.all()
    serializer_class = ReporterSerializer
    filterset_fields = '__all__'
    ordering_fields = '__all__'
    schema = AutoSchema(
        tags=['V4-Reporter'],
        component_name='V4-Reporter',
        operation_id_base='V4-Reporter',
    )


class ArticleReporterView(viewsets.ReadOnlyModelViewSet):
    class ArticleReporterSerializer(serializers.ModelSerializer):
        url = serializers.SerializerMethodField()

        class Meta:
            model = Reporter
            fields = ('id', 'first_name', 'last_name', 'email', 'url')

        def get_url(self, obj):
            kwargs = {'parent_lookup_article': self.context['article'].id, 'pk': obj.id}
            return reverse(
                viewname='v4-article-reporter-detail',
                kwargs=kwargs,
                request=self.context['request'],
                format=self.context['format']
            )

    queryset = Reporter.objects.all()
    serializer_class = ArticleReporterSerializer
    filterset_fields = '__all__'
    ordering_fields = '__all__'
    schema = AutoSchema(
        tags=['V4-ArticleReporter'],
        component_name='V4-ArticleReporter',
        operation_id_base='V4-ArticleReporter',
    )

    def get_serializer_context(self):
        context = super().get_serializer_context()
        article_id = self.kwargs.get('parent_lookup_article')
        if article_id is not None:
            context.update({'article': Article.objects.get(id=article_id)})
        return context


class ArticleView(viewsets.ModelViewSet):
    class ArticleSerializer(FlexFieldsSerializerMixin, serializers.ModelSerializer):
        url = serializers.HyperlinkedIdentityField(view_name='v4-article-detail')
        reporter_url = serializers.SerializerMethodField()

        class Meta:
            model = Article
            fields = ('id', 'headline', 'pub_date', 'reporter', 'reporter_url', 'url')

        def get_reporter_url(self, obj):
            kwargs = {'parent_lookup_article': obj.id, 'pk': obj.reporter.id}
            return reverse(
                viewname='v4-article-reporter-detail',
                kwargs=kwargs,
                request=self.context['request'],
                format=self.context['format']
            )

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filterset_fields = '__all__'
    ordering_fields = '__all__'
    schema = AutoSchema(
        tags=['V4-Article'],
        component_name='V4-Article',
        operation_id_base='V4-Article',
    )
