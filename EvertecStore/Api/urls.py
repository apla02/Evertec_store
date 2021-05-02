from django.urls import path
from . import views

urlpatterns = [
    path("create/", views.create_order, name='create_order'),
    path("create/new/", views.new_order, name='new_order'),
    path("<int:id>/", views.order_detail, name='order_detail'),
    path("<int:id>/status/", views.order_detail, name='status'), #?
    path("", views.list_orders, name='list_orders'),
]


