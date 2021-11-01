from django.urls import path, include
from rest_framework.schemas import get_schema_view

from .root import APIRoot

urlpatterns = [
    path(r'', APIRoot.as_view(), name='api-root'),
    path(r'generic-key/', include('api.generic_key.urls')),
    path(r'many-to-many/', include('api.many_to_many.urls')),
    path(r'foreign-key/', include('api.foreign_key.urls')),
    path(r'schema/', get_schema_view(
        title='Template Django Rest Framework Project',
        description='API schema',
        version='1.0.0',
    ), name='openapi-schema'),
]
