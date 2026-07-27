"""Root URL configuration for Pinzo."""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.http import JsonResponse
from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)


def healthcheck(_request):
    return JsonResponse({"status": "ok", "service": "pinzo-backend"})


api_v1_patterns = [
    path("health/", healthcheck, name="health"),
    path("auth/", include("apps.accounts.urls")),
    path("products/", include("apps.products.urls")),
    path("campaigns/", include("apps.campaigns.urls")),
    path("groupbuy/", include("apps.groupbuy.urls")),
    path("cart/", include("apps.cart.urls")),
    path("orders/", include("apps.orders.urls")),
    path("payments/", include("apps.payments.urls")),
    path("referral/", include("apps.referral.urls")),
    path("notifications/", include("apps.notifications.urls")),
]

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include((api_v1_patterns, "v1"))),
    # API docs
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("api/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
    path("", healthcheck, name="root"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
