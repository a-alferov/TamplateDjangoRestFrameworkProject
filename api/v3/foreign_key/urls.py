from django.urls import path
from rest_framework.routers import DefaultRouter

from .root import ForeignKey
from .views import ReporterView, ArticleView

router = DefaultRouter()

router.register(r'reporter', ReporterView, basename='v3-reporter')
router.register(r'article', ArticleView, basename='v3-article')

urlpatterns = [
    path(r'', ForeignKey.as_view(), name='v3-foreign-key'),
]

urlpatterns.extend(router.urls)
