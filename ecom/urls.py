from django.urls import path
from .views import register_user, login_user, customer_view, seller_view, admin_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("register/", register_user, name="register"),
    path("login/", login_user, name="login"),
    path("customer/", customer_view, name="customer-view"),
    path("seller/", seller_view, name="seller-view"),
    path("admin/", admin_view, name="admin-view"),
]

# Serving media files in debug mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
