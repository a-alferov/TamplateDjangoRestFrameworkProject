from rest_framework import permissions, routers


class GenericKey(routers.APIRootView):
    permission_classes = (permissions.AllowAny,)
    api_root_dict = {
        'tag': 'tag-list',
        'bookmark': 'bookmark-list',
        'note': 'note-list',
    }
