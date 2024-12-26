from django.urls import path
from admin_app import views

urlpatterns=[
    path('order/list',views.NewOrderList.as_view(),name = 'orderlist_view'),
    path('order/confirm/<int:id>',views.OrderConfirm.as_view(),name = 'orderconfirm'),
    path('order/list/all',views.NewOrderList.as_view(),name = 'allorder'),
    path('order/detail/<int:id>',views.OrderdetailView.as_view(),name = 'orderdetail_view'),
    
    
    
]