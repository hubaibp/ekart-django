from django.contrib import admin
from admin_app.models import Category,Products

from user_app.models import Orders

# Register your models here.
admin.site.register(Category)
admin.site.register(Products)

admin.site.register(Orders)
