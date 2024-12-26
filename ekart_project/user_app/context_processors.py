from user_app.models import Cart,Orders

def cart_count(request):
    if request.user.is_authenticated:
        count = Cart.objects.filter(user = request.user,status = 'in-cart').count()
        return {'count':count}
    else:
        return {'count':0}
    
def order_count(request):
    if request.user.is_authenticated:
        order_count = Orders.objects.filter(user = request.user,status = 'order-placed').count()
        return {'order_count':order_count}
    else:
        return {'order_count':0}


# def ordercount(request):
#     if request.user.is_authenticated:
#         ordercount = Orders.objects.all(user = request.user,status = 'order-placed ,delivered, dispatched,cancelled' ).count()
#         return {'ordercount':ordercount}
#     else:
#         return {'ordercount':0}   thought of this but not working
