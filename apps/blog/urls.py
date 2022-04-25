from django.urls import path
from apps.blog import views
from apps.blog.views import ListBlogView
urlpatterns = [
    
    path('', ListBlogView.as_view(), name='blog'),

    
]