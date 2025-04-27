from django.urls import reverse_lazy
from django.views.generic import FormView
from .forms import UserRegistration


class SignupView(FormView):
    template_name = "users/signup.html"
    form_class = UserRegistration
    success_url = reverse_lazy("blog:home")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
