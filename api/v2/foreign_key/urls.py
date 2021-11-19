from django.urls import path
from rest_framework.routers import DefaultRouter

from .root import ForeignKey
from .views import ReporterView, ArticleView

router = DefaultRouter()

router.register(r'reporter', ReporterView, basename='v2-reporter')
router.register(r'article', ArticleView, basename='v2-article')

urlpatterns = [
    path(r'', ForeignKey.as_view(), name='v2-foreign-key')
]

urlpatterns.extend(router.urls)
