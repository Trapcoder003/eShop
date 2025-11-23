from shop.views import MyLoginView
from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('',MyLoginView.as_view(),name='dashboard'),
    path('',include('shop.urls')),
    path('admin/', admin.site.urls),
]
