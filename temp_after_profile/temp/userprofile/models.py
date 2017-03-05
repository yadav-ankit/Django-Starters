from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import  User

class UserProfile(models.Model):
    user=models.OneToOneField(User)
    college=models.CharField(max_length=50)
    branch=models.CharField(max_length=50)
    skills=models.CharField(max_length=50)

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])