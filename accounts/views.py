from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from accounts.forms import CustomUserCreationForm, CustomUserChangeForm

class SignUpView(CreateView): 
    form_class = CustomUserCreationForm  
    success_url = reverse_lazy('login') 
    template_name = 'accounts/signup.html'