from django.urls import path
from rest_framework.routers import DefaultRouter

from .root import GenericKey
from .views import TagView, BookmarkView, NoteView

router = DefaultRouter()

router.register(r'tag', TagView, basename='tag')
router.register(r'bookmark', BookmarkView, basename='bookmark')
router.register(r'note', NoteView, basename='note')

urlpatterns = [
    path(r'', GenericKey.as_view(), name='generic-key'),
]

urlpatterns.extend(router.urls)
