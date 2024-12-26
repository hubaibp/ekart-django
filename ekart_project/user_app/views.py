from django.shortcuts import render,redirect
from django.views.generic import TemplateView,CreateView,FormView,DetailView,ListView
from admin_app.models import Products
from django.contrib.auth.models import User
from django.contrib import messages
from user_app.forms import SignUpForm,SignInForm,CartForm,OrderForm
from django.views import View
from django.contrib.auth import login,logout,authenticate
from user_app.models import Cart,Orders
from django.core.mail import send_mail,settings
from user_app.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.

class Home(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # print(self.request.user.emal)  #to access the email
        context['products'] = Products.objects.all()
        return context

class SignUpView(CreateView):
    form_class = SignUpForm
    model = User
    template_name = 'signup1.html'

    def form_valid(self, form):
        User.objects.create_user(**form.cleaned_data)
        messages.success(self.request,'Registration successful')
        return redirect('Home_view')
    
    def form_invalid(self, form):
        messages.warning(self.request,'Invalid inputs')
        return super().form_invalid(form)
    
class SignInView(FormView):
    form_class = SignInForm
    template_name = 'signin.html'

    def post(self, request, *args, **kwargs):
        uname = request.POST.get("username")
        pswd = request.POST.get("password")
        user = authenticate(request,username = uname,password = pswd)
        if user:
            if user.is_superuser == 1:
                count = Orders.objects.filter(status = 'order-placed').count()
                return render(request,"dashboard.html",{'count_order':count})
            else:
                login(request,user)
                messages.success(request,'Login Successful')
                return redirect('Home_view')
        else:
            messages.warning(request,'Invalid inputs')
            return redirect('signin_view')
        
class SignOutView(View):
    def get(self,request):
        logout(request)
        return redirect('signin_view')
        
class ProductDetailView(DetailView):
    model = Products
    pk_url_kwarg = 'id'
    template_name = 'productdetail.html'
    context_object_name = 'product'


@method_decorator(login_required, name = 'dispatch')
class AddToCartView(TemplateView):
    model = Cart
    template_name = 'add_to_cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product'] = Products.objects.get(id = kwargs.get('id'))
        context['form'] = CartForm()
        return context
    
    def post(self,request,*args,**kwargs):
        quantity = request.POST.get('quantity')
        user = request.user
        product = Products.objects.get(id=kwargs.get('id'))
        # cart_object = Cart.objects.filter(user = user,product = product,status = 'in-cart')
        cart_object = Cart.objects.filter(user = user,product = product).exclude(status = 'order-placed')
        if cart_object:
            cart_data = cart_object[0]
            cart_data.quantity += int(quantity)
            cart_data.save()
            messages.success(request,'Product added !')
            return redirect('Home_view')


        else:
            Cart.objects.create(user = user,product = product,quantity = quantity)
            messages.success(request,'Product added !')
            return redirect('Home_view')
        
@method_decorator(login_required,name='dispatch')
class CartList(ListView):
    model = Cart
    template_name = 'list_cart.html'
    context_object_name = 'cart'

    def get_queryset(self):
        return Cart.objects.filter(user = self.request.user,status = 'in-cart')
    
class PlaceOrder(TemplateView):
    template_name = 'place_order.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = OrderForm()
        context['product'] = Cart.objects.get(id = kwargs.get('id'))
        return context
    
    def post(self,request,*args,**kwargs):
        address = request.POST.get('address')
        email = request.POST.get('email')
        user = request.user
        cart_obj = Cart.objects.get(id = kwargs.get('id'))
        Orders.objects.create(user = user,product = cart_obj,address = address,email = email)
        messages.success(request,"order placed successfully")
        send_mail("Ekart","Order placed successfully",settings.EMAIL_HOST_USER,[email])
        cart_obj.status = 'order-placed'
        cart_obj.save()
        return redirect('Home_view')

@method_decorator(login_required,name='dispatch')
class OrderList(ListView):
    model = Orders
    template_name = 'list_orders.html'
    context_object_name = 'order'

    def get_queryset(self):
        return Orders.objects.filter(user = self.request.user,status = 'order-placed')