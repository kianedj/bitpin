from django.urls import path, include
from django.contrib import admin
from accounts import urls as accounts_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("api/post/", include('post.urls')),
    path('api/accounts/', include(accounts_urls)),
    path('accounts/profile/', include('post.urls'))
]
