from rest_framework import permissions, routers


class V3(routers.APIRootView):
    permission_classes = (permissions.AllowAny,)
    api_root_dict = {
        'foreign-key': 'v3-foreign-key',
        'many-to-many': 'v3-many-to-many',
    }
