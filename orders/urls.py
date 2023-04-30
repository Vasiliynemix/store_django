from django.urls import path

from orders.views import OrderCreateView, CanceledTemplateView, SuccessTemplateView, OrderListView
app_name = 'orders'

urlpatterns = [
    path('order-create/', OrderCreateView.as_view(), name='order_create'),
    path('', OrderListView.as_view(), name='orders_list'),
    path('order-success/', SuccessTemplateView.as_view(), name='order_success'),
    path('order_canceled/', CanceledTemplateView.as_view(), name='order_canceled'),
]
