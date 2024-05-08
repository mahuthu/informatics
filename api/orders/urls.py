from django.urls import path
from. import views
from .views import CreateCustomer, CreateOrder, order_detail

urlpatterns = [
    path('home1', views.home1, name="home1"),
    # path('customer', CustomerListCreateAPIView.as_view(), name='customer-list-create'),
    # path('orders/', OrderListCreateAPIView.as_view(), name='order-list-create'),
    # path('success/<int:pk>', views.success, name='success'),
    path("create_customer", views.CreateCustomer, name = "create_customer"),
    path("create_order", views.CreateOrder, name = "create_order"),
    path('order_detail/<int:pk>', views.order_detail, name='order_detail')
]