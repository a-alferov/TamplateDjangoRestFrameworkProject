from rest_framework import permissions, routers


class ForeignKey(routers.APIRootView):
    permission_classes = (permissions.AllowAny,)
    api_root_dict = {
        'reporter': 'v1-reporter-list',
        'article': 'v1-article-list',
    }
