from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="User Profile Api",
        default_version='v1'
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('profileProj.profileApi.urls')),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-ui'),

]
