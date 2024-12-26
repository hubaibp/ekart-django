from django.urls import path
from user_app import views

urlpatterns=[
    path('',views.Home.as_view(),name = 'Home_view'),
    path('signup1',views.SignUpView.as_view(),name = 'signup_view'),
    path('signin',views.SignInView.as_view(),name = 'signin_view'),
    path('signout',views.SignOutView.as_view(),name = 'signout_view'),
    path('detail/<int:id>',views.ProductDetailView.as_view(),name = 'detail_view'),
    path('add/cart/<int:id>',views.AddToCartView.as_view(),name = 'addcart_view'),
    path('list/cart',views.CartList.as_view(),name = 'listcart_view'),
    path('place/order/<int:id>',views.PlaceOrder.as_view(),name = 'placeorder_view'),
    path('list/orders',views.OrderList.as_view(),name = 'listorders_view'),

]