from __future__ import unicode_literals
from ..login_reg.models import User
from django.db import models

# Create your models here.
class Friendship(models.Model):
    user = models.ForeignKey('login_reg.User', related_name = 'userfriend')
    friend = models.ForeignKey('login_reg.User', related_name = 'friendfriend')
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now = True)
