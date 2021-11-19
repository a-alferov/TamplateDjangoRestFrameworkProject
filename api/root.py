from rest_framework import permissions, routers


class API(routers.APIRootView):
    permission_classes = (permissions.AllowAny,)
    api_root_dict = {
        'v1': 'v1',
        'v2': 'v2',
        'v3': 'v3',
        'v4': 'v4',
        'schema': 'schema',
    }
