# -*- coding: utf-8 -*-

from django.conf import settings
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.shortcuts import render_to_response


class IndexView(TemplateView):
	''' Index view.'''

	template_name = 'index.html'
