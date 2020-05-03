from django.contrib import admin
from django.urls import path, include
from method import urls as method_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(method_urls))
]
