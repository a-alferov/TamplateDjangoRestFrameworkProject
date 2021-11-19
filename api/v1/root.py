from rest_framework import permissions, routers


class V1(routers.APIRootView):
    permission_classes = (permissions.AllowAny,)

    api_root_dict = {
        'foreign-key': 'v1-foreign-key',
        # 'generic-key': 'generic-key',
        'many-to-many': 'v1-many-to-many',
    }
