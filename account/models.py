from django.db import models


# Create your models here.
class SignUp(models.Model):
    email = models.EmailField()
    first_name = models.CharField(max_length=120, blank=False, null=True)
    last_name = models.CharField(max_length=120, blank=False, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    update = models.DateTimeField(auto_now_add=False, auto_now=True)
    password = models.CharField(max_length=50, blank=False, null=True)
    # type_of_account = models.CharField(max_length=50)

    def __str__(self):
        return self.email
