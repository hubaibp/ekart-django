from django.shortcuts import render,redirect
from django.views.generic import ListView,DetailView
from user_app.models import Orders
from django.views import View
from django.http import HttpResponse
from django.core.mail import send_mail
from django.contrib import messages
from .forms import OrderUpdateForm
from django.contrib.auth.models import User   #order  table ll email id  ilell  take  from user  table


# Create your views here.
class NewOrderList(ListView):
    template_name = 'dashboard.html'
    model = Orders
    context_object_name = 'order_list'

    def get_queryset(self):
        return Orders.objects.filter(status = 'order-placed')


class OrderConfirm(View):
    def get (self,request,*args,**kwargs):
        order=Orders.objects.get(id=kwargs.get('id'))
        to=order.email
        send_mail('Order Confirmation',f'Your order has been placed', 'shaheemzubair8750@gmail.com',[to])
        messages.success(request,'Order Confirmed')
        return redirect('orderlist_view')
    



class NewOrderList(ListView):
    template_name = 'allorder.html'
    model = Orders
    context_object_name = 'orderall'
    def get_queryset(self):
        return Orders.objects.all().exclude(status="delivered")          #.exclude(status = 'order-placed')


#to see  all  oder details
class OrderdetailView(DetailView):
    template_name = 'orderdetail.html'
    model = Orders
    context_object_name = 'orderdetailview'
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['form']=OrderUpdateForm()
        return context
    
    def post(self,request,*args,**kwargs):
        status1=request.POST.get('status')
        exp_date1=request.POST.get('exp_date')
        orderk=Orders.objects.get(id=kwargs.get('id'))  #to get the order for getting user id
        orderk.status=status1
        orderk.exp_date=exp_date1
        orderk.save()
       # user=User.objects.get(id=orderk.user.id)  # order  table ll email id  ilatha  case  take  it  from  User table
       # to=user.email
        # send_mail("ekart",f"expected delivery date is {exp_date1}",'shaheemzubair8750@gmail.com',[to])
        # messages.success(request,'Order Updated')
        send_mail("ekart",f"expected delivery date is {orderk.exp_date}",'shaheemzubair8750@gmail.com',[orderk.email])
        messages.success(request,'Order Updated')
        return redirect('orderlist_view')
