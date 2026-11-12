from django.contrib import admin
from .models import PricingPlan, Review, QuoteRequest

@admin.register(PricingPlan)
class PricingPlanAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'is_popular', 'order']
    list_editable = ['order', 'is_popular']

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['client_name', 'company', 'rating', 'created_at']
    list_filter = ['rating']

@admin.register(QuoteRequest)
class QuoteRequestAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'service_needed', 'submitted_at', 'is_reviewed']
    list_filter = ['is_reviewed', 'submitted_at']
    readonly_fields = ['submitted_at']