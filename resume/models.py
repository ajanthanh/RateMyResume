from django.db import models
from django.contrib.auth.models import User

from time import time


def get_upload_file_name(instance, filename):
    return "uploaded_files/%s" % (filename)


class Resume(models.Model):
    # file_name = models.CharField(max_length=120, blank=False, null=True)
    thumbnail = models.FileField(upload_to=get_upload_file_name, blank=True, null=True)
    # timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)


def __str__(self):
    return 'test'
