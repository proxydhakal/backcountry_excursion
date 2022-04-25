from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
class IndexView(TemplateView):
    
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class Destination(TemplateView):
    template_name = "destination.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
        

class DiscountView(TemplateView):
    template_name = "discount.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class AboutView(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class ContactView(TemplateView):
    template_name = "contact.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class BookingView(TemplateView):
    template_name = "booking.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
