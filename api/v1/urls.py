from django.urls import path, include

from .root import V1

urlpatterns = [
    path(r'', V1.as_view(), name='v1'),
    path(r'foreign-key/', include('api.v1.foreign_key.urls')),
    # path(r'generic-key/', include('api.v1.generic_key.urls')),
    path(r'many-to-many/', include('api.v1.many_to_many.urls')),

]
