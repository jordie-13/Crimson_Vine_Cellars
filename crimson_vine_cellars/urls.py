from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('products/', include('products.urls')),
    path('summernote/', include('django_summernote.urls')),
    path('bag/', include('bag.urls')),
    path('checkout/', include('checkout.urls'),)
]
