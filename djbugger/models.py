from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ExceptionsHistory(models.Model):
    exception = models.CharField(max_length=2048, null=True,blank=True, verbose_name="Exception Name")
    detail = models.TextField(null=True, blank=True, verbose_name="Exception detail")
    file_name = models.CharField(max_length=2048, null=True,blank=True, verbose_name="File Name")
    line_number = models.IntegerField(default=0, verbose_name="Error Line Number")
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, related_name="user_detail",verbose_name="User Created Error")
    created = models.DateTimeField(editable=False, auto_now_add=True, verbose_name="Error Created")
    updated = models.DateTimeField(editable=False, null=True, blank=True, verbose_name="Error Updated")
    resolved = models.DateTimeField(editable=False, null=True, blank=True, verbose_name="Error Resolved")
    is_resolved = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    exception_id = models.CharField(max_length=2048, null=True,blank=True, verbose_name="File Name")
    status = models.CharField(max_length=2048, null=True,blank=True, verbose_name="Exception Status")
    request_url = models.CharField(max_length=2048, null=True,blank=True, verbose_name="Request URL")
    request_method = models.CharField(max_length=2048, null=True,blank=True, verbose_name="Request Method")
    url_path = models.CharField(max_length=2048, null=True,blank=True, verbose_name="Request URL PAth")
    bug_type = models.BooleanField(default=True, help_text="False for manually added issues")
