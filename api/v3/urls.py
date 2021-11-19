from django.urls import path, include

from .root import V3

urlpatterns = [
    path(r'', V3.as_view(), name='v3'),
    path(r'foreign-key/', include('api.v3.foreign_key.urls')),
    path(r'many-to-mant/', include('api.v3.many_to_many.urls')),
]
