from pyexpat import model
from django.shortcuts import render
from django.views.generic import TemplateView
from apps.blog.models import Blog
from apps.core.models import About, Service, Testimonial, Slider,Feature,OurTeam
from apps.setting.models import SEO, SocialSettings, Logo, Address, Title
# Create your views here.
class IndexView(TemplateView):
    
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["services"] = Service.objects.all()[:3]
        context["sliders"] = Slider.objects.all()
        context["blogs"] = Blog.objects.filter().order_by('-created_at')[:2]
        context["seo"] = SEO.objects.all().first()
        context["address"] = Address.objects.all().first()
        context["logo"] = Logo.objects.all().first()
        context["title"] = Title.objects.all().first()
        context["reviews"] = Testimonial.objects.all()
        context["features"] = Feature.objects.all()
        context["social"] = SocialSettings.objects.all().first()
        return context

class Destination(TemplateView):
    template_name = "destination.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["seo"] = SEO.objects.all().first()
        context["reviews"] = Testimonial.objects.all()
        context["address"] = Address.objects.all().first()
        context["logo"] = Logo.objects.all().first()
        context["title"] = Title.objects.all().first()
        context["social"] = SocialSettings.objects.all().first()
        return context
        

class DiscountView(TemplateView):
    template_name = "discount.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["seo"] = SEO.objects.all().first()
        context["reviews"] = Testimonial.objects.all()
        context["address"] = Address.objects.all().first()
        context["logo"] = Logo.objects.all().first()
        context["title"] = Title.objects.all().first()
        context["social"] = SocialSettings.objects.all().first()
        return context

class AboutView(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["seo"] = SEO.objects.all().first()
        context["about"] = About.objects.all().first()
        context["reviews"] = Testimonial.objects.all()
        context["teams"] = OurTeam.objects.all()
        context["address"] = Address.objects.all().first()
        context["logo"] = Logo.objects.all().first()
        context["title"] = Title.objects.all().first()
        context["social"] = SocialSettings.objects.all().first()
        return context

class ContactView(TemplateView):
    template_name = "contact.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["seo"] = SEO.objects.all().first()
        context["reviews"] = Testimonial.objects.all()
        context["address"] = Address.objects.all().first()
        context["logo"] = Logo.objects.all().first()
        context["title"] = Title.objects.all().first()
        context["social"] = SocialSettings.objects.all().first()
        return context

class BookingView(TemplateView):
    template_name = "booking.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["seo"] = SEO.objects.all().first()
        context["reviews"] = Testimonial.objects.all()
        context["address"] = Address.objects.all().first()
        context["logo"] = Logo.objects.all().first()
        context["title"] = Title.objects.all().first()
        context["social"] = SocialSettings.objects.all().first()
        return context

class ServiceView(TemplateView):
    template_name = "service.html"
    model = Service
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["services"] = Service.objects.all()
        context["seo"] = SEO.objects.all().first()
        context["reviews"] = Testimonial.objects.all()
        context["address"] = Address.objects.all().first()
        context["logo"] = Logo.objects.all().first()
        context["title"] = Title.objects.all().first()
        context["social"] = SocialSettings.objects.all().first()
        return context
