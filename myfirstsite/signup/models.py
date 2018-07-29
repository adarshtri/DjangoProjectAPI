from django.db import models
from datetime import datetime


# Create your models here.
class SiteUser(models.Model):

    username = models.CharField(max_length=20)
    useremail = models.CharField(max_length=100)
    userpassword = models.CharField(max_length=30)
    created_at = models.DateTimeField(default=datetime.now())
    lastlogin = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return "Username: %s\tUserEmail: %s".format_map(self.username, self.useremail)
