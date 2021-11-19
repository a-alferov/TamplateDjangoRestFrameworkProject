from django.urls import path, include

from .root import V2

urlpatterns = [
    path(r'', V2.as_view(), name='v2'),
    path(r'foreign-key/', include('api.v2.foreign_key.urls')),
    path(r'many-to-many/', include('api.v2.many_to_many.urls')),
]
