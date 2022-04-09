from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("basics.urls")),
    path('admin/', admin.site.urls),
    path("auth/", include("django.contrib.auth.urls")),
]
