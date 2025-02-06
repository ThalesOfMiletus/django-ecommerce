from django.contrib import admin
from .models import Product, Customer, Order, Category, Profile
from django.contrib.auth.models import User

admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Category)
admin.site.register(Profile)

class ProfileInline(admin.StackedInline):
    model = Profile
    verbose_name_plural = 'profiles'
    
class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ['username', 'first_name', 'last_name', 'email']
    inlines = [ProfileInline]
    
admin.site.unregister(User)
admin.site.register(User, UserAdmin) 