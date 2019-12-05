from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from . import forms
from django.views.generic import CreateView
# Create your views here.

class SignUp(CreateView):

    # set the attribute to the class WITHOUT instantiation
    form_class = forms.UserCreateForm

    # reverse_lazy wont redirect the user unless they hit the
    # signup button and are successfully signed up
    success_url = reverse_lazy('login')

    # set the template for this CreateView
    template_name = 'accounts/signup.html'
