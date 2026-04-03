from django.contrib import admin
from .models import Product, Order, OrderItem, DailyRevenue

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at')
    inlines = [OrderItemInline]

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')

admin.site.register(Order, OrderAdmin)

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity', 'price_at_order')

@admin.register(DailyRevenue)
class DailyRevenueAdmin(admin.ModelAdmin):
    list_display = ('date', 'total_orders', 'total_revenue')

