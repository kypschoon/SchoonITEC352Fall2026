from django.db import models

class PricingPlan(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    features = models.TextField(help_text="One feature per line")
    is_popular = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'price']

    def __str__(self):
        return f"{self.name} – ${self.price}"

    def get_features_list(self):
        return [f.strip() for f in self.features.splitlines() if f.strip()]


class Review(models.Model):
    client_name = models.CharField(max_length=100)
    company = models.CharField(max_length=100, blank=True)
    text = models.TextField()
    rating = models.PositiveIntegerField(default=5, choices=[(i, i) for i in range(1, 6)])
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.client_name} – {self.rating}★"


class QuoteRequest(models.Model):
    full_name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    service_needed = models.CharField(max_length=100)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    is_reviewed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.full_name} – {self.service_needed}"