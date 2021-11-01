from rest_framework import permissions, routers


class GenericRoot(routers.APIRootView):
    permission_classes = (permissions.AllowAny,)
    api_root_dict = {
        'tag': 'tag-list',
        'bookmark': 'bookmark-list',
        'note': 'note-list',
    }
