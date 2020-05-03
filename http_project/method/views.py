from django.views import View
from . import services


class MethodView(View):
    http_method_names = ['get', 'post', 'delete', 'put', 'head']

    def get(self, request, *args, **kwargs):
        return services.get_user(request.GET)

    def post(self, request, *args, **kwargs):
        return services.create_user(request.POST)

    def delete(self, request, *args, **kwargs):
        return services.delete_user(request.GET)

    def put(self, request, *args, **kwargs):
        request.method = "POST"
        request._load_post_and_files()
        return services.updated_user(request.POST)

    def head(self, request, *args, **kwargs):
        return services.last_modified_user(request.GET)
