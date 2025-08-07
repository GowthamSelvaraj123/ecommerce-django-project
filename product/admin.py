from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Product, Category, Review

@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    list_display = ('title', 'brand', 'price', 'stock', 'availability_status')
    search_fields = ('title', 'brand', 'sku')
    list_filter = ('category', 'availability_status', 'brand')

admin.site.register(Category)
admin.site.register(Review)