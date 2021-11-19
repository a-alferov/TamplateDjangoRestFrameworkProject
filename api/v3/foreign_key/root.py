from rest_framework import permissions, routers


class ForeignKey(routers.APIRootView):
    permission_classes = (permissions.AllowAny,)
    api_root_dict = {
        'reporter': 'v3-reporter-list',
        'article': 'v3-article-list',
    }
