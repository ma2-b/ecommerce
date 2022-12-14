from django.urls import path, include
from . import views

app_name = "market"

urlpatterns = [
    path('', views.home, name="home"),
    path('shop/', views.ShopListView.as_view(), name="shop"),
    path('cart/', views.cart, name="cart"),
    path('about/', views.AboutView.as_view(), name="about"),
    path('contanct/', views.ContanctView.as_view(), name="contanct"),
    path('cart/checkout', views.checkout, name="checkout"),
    path('update_item/', views.updateItem, name="updateItem"),
    path('process_order/', views.process_order, name="updateItem"),

]
