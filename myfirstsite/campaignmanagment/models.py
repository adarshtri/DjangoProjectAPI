from django.db import models
from django.utils import timezone


# Create your models here.
class Campaign(models.Model):

    class Meta:
        db_table = 'campaign'

    campaign_id = models.AutoField(primary_key=True)
    campaign_name = models.CharField(max_length=25)
    description = models.CharField(max_length=250, blank=True, null=True)
    start_at = models.DateTimeField(null=False)
    end_at = models.DateTimeField(null=False)
    created_by = models.IntegerField(null=False, blank=False)
    created_at = models.DateTimeField(null=False, blank=True, default=timezone.now())
    updated_at = models.DateTimeField(null=False, blank=True, default=timezone.now())

    def __str__(self):
        print("[" + self.campaign_name + "]" + " created at" + "[" + self.created_at + "].")
