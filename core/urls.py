
from django.contrib import admin
from django.urls import path,include
from . import views
# from api import urls as api_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('api/',include('api.urls')),
]
