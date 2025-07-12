from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

api_urlpatterns = [
    path("users/", include("users.api.urls")),
    path("predictions/", include("predictor.api.urls")),
]
docs_urlpatterns = [
    path("docs/", SpectacularAPIView.as_view(), name="docs"),
    path(
        "docs/swagger/",
        SpectacularSwaggerView.as_view(url_name="docs"),
        name="swagger-ui",
    ),
]
urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(api_urlpatterns + docs_urlpatterns)),
]
