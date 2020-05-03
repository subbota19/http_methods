from django.shortcuts import render, HttpResponse
from django.views import View


class MethodView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('<h1>Hello</h1>')
