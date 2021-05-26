from .views import *
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('', get_routes, name='routes'),
    path('products/', GetProducts.as_view(), name='products'),
    path('products/<str:pk>', GetProduct.as_view(), name='product')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
