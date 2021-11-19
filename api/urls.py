from django.urls import path, include
from rest_framework.schemas import get_schema_view

from .root import API

urlpatterns = [
    path(r'', API.as_view(), name='api-root'),
    path(r'v1/', include('api.v1.urls')),
    path(r'v2/', include('api.v2.urls')),
    path(r'v3/', include('api.v3.urls')),
    path(r'v4/', include('api.v4.urls')),
    path(r'schema/', get_schema_view(
        title='Template Django Rest Framework Project',
        description='API schema',
        version='1.0.0',
    ), name='schema'),
]
