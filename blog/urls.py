from django.urls import path
from .views import HomeView, NewBlogBView

app_name = "blog"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("", NewBlogBView.as_view(), name="home"),
]
