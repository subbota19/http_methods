from .views import MethodView
from django.urls import path

urlpatterns = [
    path('method', MethodView.as_view(), name='method'),
]
