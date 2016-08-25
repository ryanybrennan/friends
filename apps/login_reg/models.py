from __future__ import unicode_literals
import re
from django.db import models
import bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
from datetime import datetime, timedelta, time, date
from time import strftime
# Create your models here.
class UserManager(models.Manager):
    def register(request, reg_data):
        errors = []
        name = reg_data['name']
        alias = reg_data['alias']
        email = reg_data['email']
        password = reg_data['password']
        confirm_password = reg_data['confirm_password']
        birthday = reg_data['birthday']
        now = strftime("%Y-%m-%d")
        if not len(name)>0:
            errors.append("Please enter a valid name")
        if not alias:
            errors.append("Please enter a valid alias")
        if not EMAIL_REGEX.match(email):
            errors.append("Please enter a valid email")
        if not password:
            errors.append("Please enter a valid password")
        if not password == confirm_password:
            errors.append("Please make sure password and confirm password are matching")
        if birthday == "":
            errors.append("Please enter a date, stupid")
        if birthday > now:
            errors.append("You are not a time traveler")
        if errors:
            return (True, errors)
        else:
            return (False, reg_data)
    def login(self, log_data):
        errors = []
        email = log_data['email']
        user = self.filter(email=email)
        password = log_data['password']
        if (len(user)>0) and bcrypt.hashpw(password.encode(), user[0].password.encode()) == user[0].password:
            return (True, user[0])
        else:
            errors.append("Invalid information, try again")
            return (False, errors)

    pass
class User(models.Model):
    name = models.CharField(max_length = 255)
    alias = models.CharField(max_length= 50)
    email = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)
    birthday = models.DateField()
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now = True)

    UserManager= UserManager()
    objects = models.Manager()
