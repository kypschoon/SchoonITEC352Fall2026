from django import forms
from .models import QuoteRequest

class QuoteRequestForm(forms.ModelForm):
    class Meta:
        model = QuoteRequest
        fields = ['full_name', 'email', 'phone', 'service_needed', 'message']
        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder': 'Your full name', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'your@email.com', 'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'placeholder': '(555) 555-5555', 'class': 'form-control'}),
            'service_needed': forms.TextInput(attrs={'placeholder': 'Monthly Bookkeeping, Catch-Up, etc.', 'class': 'form-control'}),
            'message': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Tell us about your business...', 'class': 'form-control'}),
        }