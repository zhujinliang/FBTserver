# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.db import models



class UserProfile(models.Model):
	user = models.OneToOneField(User, verbose_name=u'')
	ip = models.GenericIPAddressField(verbose_name=u'')
	friends = models.ManyToManyField(User, related_name='friends+')
	updated_on = models.DateTimeField(auto_now=True)

	class Meta:
		app_label = 'auth'
		db_table = 'fbt_user_profile'

	def get_friends_ip(self):
		pass