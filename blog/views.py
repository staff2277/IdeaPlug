from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from .models import BlogPost


# Create your views here.
class HomeView(ListView):
    model = BlogPost
    template_name = "blog/home.html"
    context_object_name = "blogPosts"


class NewBlogBView(CreateView):
    model = BlogPost
    template_name = "blog/new_blog.html"
    fields = [
        "title",
        "sub_title",
        "bg_image",
        "main_content",
    ]
    success_url = reverse_lazy("blog:home")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
