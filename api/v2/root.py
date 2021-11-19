from rest_framework import permissions, routers


class V2(routers.APIRootView):
    permission_classes = (permissions.AllowAny,)
    api_root_dict = {
        'foreign-key': 'v2-foreign-key',
        'many-to-many': 'v2-many-to-many',
    }
