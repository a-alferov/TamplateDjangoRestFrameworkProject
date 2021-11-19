from rest_framework import permissions, routers


class ManyToMany(routers.APIRootView):
    permission_classes = (permissions.AllowAny,)

    api_root_dict = {
        'pizza': 'v1-pizza-list',
        'topping': 'v1-topping-list',
    }
