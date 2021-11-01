from rest_framework import permissions, routers


class ForeignKeyRoot(routers.APIRootView):
    permission_classes = (permissions.AllowAny,)
    api_root_dict = {
        'reporter': 'reporter-list',
        'article': 'article-list',
    }
