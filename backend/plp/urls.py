from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    path("admin/", admin.site.urls),
]
# API URLS
urlpatterns += [
    # API base url
    path("api/", include("plp.api_router")),
    # DRF auth token
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    # API documentation
    path("api/schema/", SpectacularAPIView.as_view(), name="api-schema"),
    path(
        "",
        SpectacularSwaggerView.as_view(url_name="api-schema"),
        name="api-docs",
    ),
]
