from django.urls import path
from rest_framework_extensions.routers import ExtendedDefaultRouter as DefaultRouter

from .root import ForeignKey
from .views import ReporterView, ArticleView, ArticleReporterView

router = DefaultRouter()

router.register(r'reporter', ReporterView, basename='v4-reporter')
article = router.register(r'article', ArticleView, basename='v4-article')
article.register(r'reporter', ArticleReporterView, basename='v4-article-reporter',
                 parents_query_lookups=['article'])

urlpatterns = [
    path(r'', ForeignKey.as_view(), name='v4-foreign-key'),
]

urlpatterns.extend(router.urls)
