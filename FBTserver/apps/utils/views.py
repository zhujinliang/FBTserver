# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.utils import simplejson


__all__ = [
    'AjaxResponseCode',
    'AjaxResponseMixin',        
]


class AjaxResponseCode:

    success = 0
    error = 1


class AjaxResponseMixin(object):

    errors = None
    status_code = AjaxResponseCode.success

    def update_errors(self, msg, errors=None):
        '''
        msg: an error message
        errors: a dictionary of errors, e.g., form.errors
        '''
        self.status_code = AjaxResponseCode.error
        if errors is not None:
            self.errors = errors
        else:
            self.errors = msg

    def render_to_json(self, data):
        context = {
            'status': self.status_code,
            'msg': self.errors,
            'data': data
        }
        return HttpResponse(simplejson.dumps(context),
                            content_type='application/json')

    def ajax_response(self, context=None, **kwargs):
        if context is None:
            context = {}
        context.update(kwargs)
        return self.render_to_json(context)


