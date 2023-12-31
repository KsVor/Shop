from django.contrib import admin

from products.models import Basket, Product, ProductCategory

# Register your models here.

admin.site.register(ProductCategory)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'quantity')
    fields = ('name', 'dascription', 'price', 'quantity', 'image', 'category')
    search_fields = ('name',)
    ordering = ('name',)


class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantity', 'created_datestamp')
    readonly_fields = ('created_datestamp',)
    extra = 0
