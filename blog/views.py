from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from .models import BlogPost


# Create your views here.
class HomeView(TemplateView):
    template_name = "blog/home.html"


class NewBlogBView(CreateView):
    model = BlogPost
    template_name = "blog/new_blog.html"
    fields = [
        "title",
        "sub_title",
        "bg_image",
    ]
    success_url = reverse_lazy("blog:home")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
