from django.contrib import admin
from marts.models import Signin_model,contact_model,Product,OrderItem,Order
class SigninAdmin(admin.ModelAdmin):
    list_display=('name','email')
admin.site.register(Signin_model,SigninAdmin)


class contactInfo(admin.ModelAdmin):
    list_display=('name','sub','email')
admin.site.register(contact_model,contactInfo)
class productAdmin(admin.ModelAdmin):
    list_display=('id','image','name','price','category')
admin.site.register(Product,productAdmin)


# Register your models here.
class OrderItemInline(admin.TabularInline):
    model=OrderItem
class OrderAdmin(admin.ModelAdmin):
    list_display=('id','total_price','created_at')
    inlines=[OrderItemInline]
admin.site.register(Order,OrderAdmin)
admin.site.register(OrderItem)
