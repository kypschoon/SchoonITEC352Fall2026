from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .models import PricingPlan, Review
from .forms import QuoteRequestForm

def home(request):
    return render(request, 'core/home.html')

def about(request):
    return render(request, 'core/about.html')

def pricing(request):
    plans = PricingPlan.objects.all()
    return render(request, 'core/pricing.html', {'plans': plans})

def reviews(request):
    reviews = Review.objects.all()
    return render(request, 'core/reviews.html', {'reviews': reviews})

def quote(request):
    if request.method == 'POST':
        form = QuoteRequestForm(request.POST)
        if form.is_valid():
            quote = form.save()
            subject = f"New Quote Request from {quote.full_name}"
            message = (
                f"Name: {quote.full_name}\n"
                f"Email: {quote.email}\n"
                f"Phone: {quote.phone}\n"
                f"Service: {quote.service_needed}\n\n"
                f"Message:\n{quote.message}"
            )
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                ['bookkeeping@allthingsequal.net'],
                fail_silently=False,
            )
            return render(request, 'core/quote.html', {'form': QuoteRequestForm(), 'success': True})
    else:
        form = QuoteRequestForm()
    return render(request, 'core/quote.html', {'form': form})