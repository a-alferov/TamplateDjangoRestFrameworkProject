from rest_framework import permissions, routers


class ManyToMany(routers.APIRootView):
    permission_classes = (permissions.AllowAny,)

    api_root_dict = {
        'pizza': 'v3-pizza-list',
        'topping': 'v3-topping-list',
    }
