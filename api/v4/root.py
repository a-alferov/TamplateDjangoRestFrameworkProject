from rest_framework import permissions, routers


class V4(routers.APIRootView):
    permission_classes = (permissions.AllowAny,)
    api_root_dict = {
        'foreign-key': 'v4-foreign-key',
        'many-to-many': 'v4-many-to-many',
    }
