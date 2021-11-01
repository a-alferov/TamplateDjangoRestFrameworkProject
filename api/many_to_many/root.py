from rest_framework import permissions, routers


class ManyToManyRoot(routers.APIRootView):
    permission_classes = (permissions.AllowAny,)

    api_root_dict = {
        'pizza': 'pizza-list',
        'topping': 'topping-list',
    }
