from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('product/<int:id>/', views.product_detail, name='product_detail'),
    re_path(r'^product/(?P<slug>[a-z0-9-]+)/$', views.product_slug_view, name='product_slug'),
    path('add-to-cart/<int:id>/', views.add_to_cart, name='add_to_cart'),
]
