from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/customer/', include('customer.urls')),
    path('api/orders/', include('orders.urls')),
    path('api/products/', include('products.urls')),
    path('api/seller/', include('seller.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
