from django.urls import path
from apps.core import views
from apps.core.views import IndexView, Destination,DiscountView,AboutView,ContactView,BookingView
urlpatterns = [
    
    path('', IndexView.as_view(), name='home'),
    path('destination/', Destination.as_view(), name='country'),
    path('discount/', DiscountView.as_view(), name='discount'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('booking/', BookingView.as_view(), name='booking'),
    
]