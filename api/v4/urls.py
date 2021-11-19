from django.urls import path, include

from .root import V4

urlpatterns = [
    path(r'', V4.as_view(), name='v4'),
    path(r'foreign-key/', include('api.v4.foreign_key.urls')),
    path(r'many-to-many/', include('api.v4.many_to_many.urls')),
]
