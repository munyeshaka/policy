from django.urls import re_path


from .import views

app_name = 'policyAPI'

urlpatterns = [
    re_path(r'^$', views.home),
    re_path(r'^selah/', views.selah, name="selah"),
    re_path(r'^green/', views.green, name="green"),
]