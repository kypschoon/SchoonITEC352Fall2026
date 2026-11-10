from django.contrib import admin
# Import Django's built-in admin module

from .models import Category, Products, Customer, Order
# Import models so they can be registered in the admin interface


# ---------------------------
# Category Admin Configuration
# ---------------------------
@admin.register(Category)
# Registers the Category model with the admin site
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    # Controls which fields are shown in the admin list view

    search_fields = ('name',)
    # Adds a search box that allows searching by category name


# ---------------------------
# Products Admin Configuration
# ---------------------------
@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category')
    # Displays product ID, name, price, and category in admin list

    list_filter = ('category',)
    # Adds a sidebar filter so admin can filter products by category

    search_fields = ('name', 'description')
    # Enables search by product name and description


# ---------------------------
# Customer Admin Configuration
# ---------------------------
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email')
    # Shows customer details in the admin list view

    search_fields = ('first_name', 'last_name', 'email')
    # Allows searching customers by name or email


# ---------------------------
# Order Admin Configuration
# ---------------------------
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'product', 'quantity', 'date', 'status')
    # Displays key order information in admin panel

    list_filter = ('status', 'date')
    # Adds filters to narrow down orders by status or date

    search_fields = ('customer__email', 'product__name')
    # Allows searching orders by:
    # - customer's email (customer__email)
    # - product name (product__name)
    # The double underscore (__) is used to search related model fields