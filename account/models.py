from django.db import models
from django.contrib.auth.models import User

#UPLOAD FILE: This is only for following demo purposes and may need to be changed
from time import time
def get_upload_file_name(instance, filename):
	return "uploaded_files/%s" % (filename)
#UPLOAD FILE: This is only for following demo purposes and may need to be changed

# Create your models here.
class Account(models.Model):
    email = models.EmailField()
    first_name = models.CharField(max_length=120, blank=False, null=True)
    last_name = models.CharField(max_length=120, blank=False, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    update = models.DateTimeField(auto_now_add=False, auto_now=True)
    password = models.CharField(max_length=50, blank=False, null=True)
    thumbnail = models.FileField(upload_to=get_upload_file_name, blank=True, null=True)
    # type_of_account = models.CharField(max_length=50)
    # user = models.ForeignKey(User, unique=True)
    # type_of_account = models.CharField(max_lengtth=50)

    def __str__(self):
        return self.email