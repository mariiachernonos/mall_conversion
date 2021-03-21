import rest_framework
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ads/', include('ads.urls')),
    # path('api-auth/', include('rest_framework.urls'))
    ]
