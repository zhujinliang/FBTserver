# -*- coding: utf-8 -*-

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.models import User
from django.views.generic.edit import FormView


from apps.utils.views import AjaxResponseCode
from apps.utils.views import AjaxResponseMixin
from apps.utils.decorators import ajax_login_required


__all__ = [
    'RegisterView',
    'LoginView',
    'LogoutView',
]

class RegisterView(FormView, AjaxResponseMixin):
    ''' User register view.'''

    http_method_names = ['post']
    form_class = UserCreationForm

    def form_valid(self, form):
        form.save()
        user = authenticate(username=f.cleaned_data['email'], password=f.cleaned_data['password1'])
        if user is not None and user.is_active:
            login(self.request, user)
        return self.ajax_response()

    def form_invalid(self, form):
        self.update_errors(form.errors)
        return self.ajax_response()


class LoginView(FormView, AjaxResponseMixin):
    ''' User login view.'''

    http_method_names = ['post']
    form_class = AuthenticationForm

    def form_valid(self, form):
        login(self.request, form.get_user())
        return self.ajax_response()

    def form_invalid(self, form):
        self.update_errors(form.errors)
        return self.ajax_response()


class LogoutView(FormView, AjaxResponseMixin):
    ''' User logout view.'''

    def get(self, request, *args, **kwargs):
        logout(request)
        return self.ajax_response()

class SetPasswordView(FormView, AjaxResponseMixin):
    ''' User set password when user forget the password.'''

    http_method_names = ['post']
    form_class = SetPasswordForm

    def form_valid(self, form):
        form.save()
        return self.ajax_response()

    def form_invalid(self, form):
        self.update_errors(form.errors)
        return self.ajax_response()