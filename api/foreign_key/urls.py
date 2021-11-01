from django.urls import path
from rest_framework.routers import DefaultRouter

from .root import ForeignKeyRoot
from .views import ReporterView, ArticleView

router = DefaultRouter()

router.register(r'reporter', ReporterView, basename='reporter')
router.register(r'article', ArticleView, basename='article')

urlpatterns = [
    path(r'', ForeignKeyRoot.as_view(), name='foreign-key')
]

urlpatterns.extend(router.urls)
