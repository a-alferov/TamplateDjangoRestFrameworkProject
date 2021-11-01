from rest_framework import permissions, routers


class APIRoot(routers.APIRootView):
    permission_classes = (permissions.AllowAny,)
    api_root_dict = {
        'generic-key': 'generic-key',
        'many-to-many': 'many-to-many',
        'foreign-key': 'foreign-key',
    }
