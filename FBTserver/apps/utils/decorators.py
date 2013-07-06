# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.utils import simplejson
from functools import wraps

from FBTserver.apps.utils.views import AjaxResponseCode

        
def ajax_login_required(func):
    ''' Verify the user when ajax request wheather he is login.'''

    @wraps(func)
    def verify_login(request, *args, **kwargs):
        if request.user.is_authenticated():
            return func(request, *args, **kwargs)
        else:
            to_return = {
                'status': AjaxResponseCode.error,
                'msg': u'账号没有登陆'
            }
            serialized = simplejson.dumps(to_return)
            return HttpResponse(serialized, mimetype='application/json')
    return verify_login
