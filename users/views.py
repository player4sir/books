from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreateForms


class SignupPageView(generic.CreateView):
    form_class = CustomUserCreateForms
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
