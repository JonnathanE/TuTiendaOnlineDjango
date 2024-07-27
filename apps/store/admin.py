from django.contrib import admin

from .models import Product, ProductCateory


# Register your models here.
class ProductCategoryAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at")


class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at")


admin.site.register(ProductCateory, ProductCategoryAdmin)
admin.site.register(Product, ProductAdmin)
