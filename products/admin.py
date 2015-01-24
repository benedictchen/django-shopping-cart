from django.contrib import admin

from .models import Product, ProductImage, Variation


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'active', 'updated_at']
    list_editable = ['active', 'price']
    list_filter = ['price', 'active', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']
    prepopulated_fields = {'slug': ('title',)}

    class Meta():
        model = Product


class ProductImageAdmin(admin.ModelAdmin):
    class Meta():
        model = ProductImage


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage, ProductImageAdmin)
admin.site.register(Variation)