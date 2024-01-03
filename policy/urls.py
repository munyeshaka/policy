
from django.contrib import admin
from django.urls import include, path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('policyPro/', admin.site.urls),
    path('', include('policyAPI.urls')),
    path('api/', include('testAPI.urls')),
]
urlpatterns += staticfiles_urlpatterns()
