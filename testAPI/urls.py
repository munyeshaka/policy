
from django.urls import include, path
from rest_framework import routers
from .views import *
# from mkAPI import views

router_mk = routers.DefaultRouter()


router_mk.register(r'songs', SongViewSet)


urlpatterns = [
    path('', include(router_mk.urls)),
]
