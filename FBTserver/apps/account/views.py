# -*- coding: utf-8 -*-

from django.contrib.auth.models import User

from apps.utils.views import AjaxResponseCode
from apps.utils.views import AjaxResponseMixin
from apps.utils.decorators import ajax_login_required


__all__ = [
	'RegisterView',
	'LoginView',
	'LogoutView',
]

class RegisterView(AjaxResponseMixin):
	''' User register.'''

	def post(self, request, *args, **kwargs):
		pass


class LoginView(AjaxResponseMixin):
	''' User login.'''

	def post(self, request, *args, **kwargs):
		pass

class LogoutView(AjaxResponseMixin):
	''' User logout.'''

	def get(self, request, *args, **kwargs):
		pass