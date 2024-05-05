from django.urls import path
from. import views
from .views import CustomerListCreateAPIView, OrderListCreateAPIView

urlpatterns = [
    path('home', views.home, name="home"),
    path('customer', CustomerListCreateAPIView.as_view(), name='customer-list-create'),
    path('orders/', OrderListCreateAPIView.as_view(), name='order-list-create'),
    path('success/<int:pk>', views.success, name='success'),
]