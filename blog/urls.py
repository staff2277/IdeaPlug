from django.urls import path
from .views import HomeView, NewBlogBView, EmplayeeDataView

app_name = "blog"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("blog/new_blog", NewBlogBView.as_view(), name="new_blog"),
    path("data", EmplayeeDataView.as_view()),
]
