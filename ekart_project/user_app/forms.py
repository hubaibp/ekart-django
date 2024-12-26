from django import forms
from django.contrib.auth.models import User
from user_app.models import Cart,Orders

class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields =['username','email','password']
        widgets ={
            'username':forms.TextInput(attrs={'class':"form-control",'placeholder':'Enter the username'}),
            'email':forms.EmailInput(attrs={'class':"form-control",'placeholder':'Enter your email'}),
            'password':forms.PasswordInput(attrs={'class':"form-control",'placeholder':'Enter your password'}),
        }

class SignInForm(forms.ModelForm):
    class Meta:
        fields = ['username','password']
        model = User
        widgets ={
            'username':forms.TextInput(attrs={'class':"form-control",'placeholder':'Enter the username'}),
            'password':forms.PasswordInput(attrs={'class':"form-control",'placeholder':'Enter your password'}),
        }

class CartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields =['quantity']
        widgets ={
            'quantity':forms.NumberInput(attrs={'class':'form-control','placeholder':'Quantity'})
        }

class OrderForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = ['address','email']
        widgets ={
            'address':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your address'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter your email','type':'email'})
        }