from django.db import models
from django.utils import timezone


class User(models.Model):

    class Meta:
        db_table = 'user'

    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20)
    useremail = models.CharField(max_length=100)
    userpassword = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now())
    lastlogin = models.DateTimeField(blank=True, null=True)
    lastlogout = models.DateTimeField(blank=True, null=True)
    logintoken = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return "User [ " + self.username + " ] last logged in to your system at [ " + self.lastlogin + " ]."

    def if_recently_logged_in(self):
        return timezone.now() - self.lastlogin < 1
