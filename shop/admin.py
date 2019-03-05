from django.contrib import admin
from .models import Category,Product
# Register your models here.

@admin.register(Category)
class CategoryModel(admin.ModelAdmin):
    list_display=['name','slug']
    prepopulated_fields={'slug':('name',)}

@admin.register(Product)
class ProductModel(admin.ModelAdmin):
    list_display=['name','slug','price','available','created','updated']
    list_filter=['available','created','updated']
    list_editable=['price','available']
    prepopulated_fields={'slug':('name',)}