from django.views.generic import FormView
from .forms import UserRegistration


class SignupView(FormView):
    template_name = "users/signup.html"
    form_class = UserRegistration
    success_url = "home"
