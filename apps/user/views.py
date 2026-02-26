from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.views.generic import View, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout

from apps.user.models import User
from apps.user.forms import LoginForm


class LoginView(View):

    @staticmethod
    def get(request: HttpRequest) -> HttpResponse:
        return redirect('user:account') if request.user.is_authenticated else render(request, 'auth/login.html')

    @staticmethod
    def post(request: HttpRequest) -> HttpResponse:

        form = LoginForm(request.POST)

        if not form.is_valid():
            messages.error(request, 'Please provide valid credentials.', extra_tags='danger')
            return render(request, 'auth/login.html', status=400)

        credentials = form.cleaned_data

        user = authenticate(request, username=credentials['email'], password=credentials['password'])

        if user is not None:
            login(request, user)
            messages.success(request, 'You have been successfully logged in.')
            return redirect('core:home')

        messages.error(request, 'Invalid email / password provided.', extra_tags='danger')
        return render(request, 'auth/login.html', status=400)


class AccountUpdatePasswordView(LoginRequiredMixin, View):

    @staticmethod
    def post(request: HttpRequest) -> HttpResponse:

        user = request.user

        try:
            new_password = request.POST['new_password']
            current_password = request.POST['current_password']
            confirm_password = request.POST['confirm_password']
        except KeyError:
            messages.error(request, 'Both current and new password is required.', extra_tags='danger')
            return redirect('user:account')

        if not user.check_password(current_password):
            messages.error(request, 'Current password is incorrect.', extra_tags='danger')
            return redirect('user:account')

        if new_password != confirm_password:
            messages.error(request, 'New password and confirm password do not match.', extra_tags='danger')
            return redirect('user:account')

        user.set_password(new_password)
        user.save()

        messages.success(request, 'Your password has been updated successfully.')
        return redirect('user:account')


class AccountView(LoginRequiredMixin, UpdateView):

    model = User
    fields = ['email', 'name']
    context_object_name = 'user'
    template_name = 'auth/account.html'
    success_url = reverse_lazy('user:account')

    def get_object(self, queryset=...):
        return self.request.user


def logout_view(request: HttpRequest) -> HttpResponse:
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('core:home')
