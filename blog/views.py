from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from rest_framework.generics import ListAPIView

from .models import BlogPost, Employee
from .serializers import EmployeeSerializer


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


class EmplayeeDataView(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]
