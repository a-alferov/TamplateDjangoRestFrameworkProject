from rest_framework import permissions, routers


class ForeignKey(routers.APIRootView):
    permission_classes = (permissions.AllowAny,)
    api_root_dict = {
        'reporter': 'v2-reporter-list',
        'article': 'v2-article-list',
    }
