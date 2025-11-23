from . import views
from django.urls import path

urlpatterns = [
    path('home/',views.home,name="home"),
    path('products/',views.products,name="products"),
    path('categories/',views.categories,name="categories"),
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact"),
    path('dashboard/',views.dashboard,name="dashboard"),
]
