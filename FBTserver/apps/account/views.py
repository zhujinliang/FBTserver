# -*- coding: utf-8 -*-

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.models import User
from django.views.generic.edit import FormView


from FBTserver.apps.utils.views import AjaxResponseCode
from FBTserver.apps.utils.views import AjaxResponseMixin
from FBTserver.apps.utils.decorators import ajax_login_required


__all__ = [
    'RegisterView',
    'LoginView',
    'LogoutView',
    'SetPasswordView'
]

class BaseFormView(FormView):

    def http_method_not_allowed(self, request, *args, **kwargs):
        allowed_methods = [m for m in self.http_method_names if hasattr(self, m)]
        error_msg = 'Method Not Allowed (%s): %s' % (request.method, request.path)
        self.update_errors(error_msg)
        context = {'allowed_methods': allowed_methods}
        return self.ajax_response(context)


class RegisterView(BaseFormView, AjaxResponseMixin):
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


class LoginView(BaseFormView, AjaxResponseMixin):
    ''' User login view.'''

    http_method_names = ['post']
    form_class = AuthenticationForm

    def form_valid(self, form):
        login(self.request, form.get_user())
        return self.ajax_response()

    def form_invalid(self, form):
        self.update_errors(form.errors)
        return self.ajax_response()


class LogoutView(BaseFormView, AjaxResponseMixin):
    ''' User logout view.'''

    def get(self, request, *args, **kwargs):
        logout(request)
        return self.ajax_response()


class SetPasswordView(BaseFormView, AjaxResponseMixin):
    ''' User set password when user forget the password.'''

    http_method_names = ['post']
    form_class = SetPasswordForm

    def form_valid(self, form):
        form.save()
        return self.ajax_response()

    def form_invalid(self, form):
        self.update_errors(form.errors)
        return self.ajax_response()