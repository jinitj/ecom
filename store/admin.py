from django.contrib import admin
from store.models import Customer,Product,Cart,CartElement
# Register your models here.
admin.site.register(Customer)
admin.site.register(Product)

class CartElementInline(admin.TabularInline):
    model = CartElement
    extra = 2

class CartAdmin(admin.ModelAdmin):
    fieldsets = [(None,{'fields':['cart_identifier','total']}) ,]
    inlines = [CartElementInline]

admin.site.register(Cart , CartAdmin)