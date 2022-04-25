from django.shortcuts import render
from django.views.generic import TemplateView,ListView
# Create your views here.
class ListBlogView(TemplateView):
    template_name = "blog.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context