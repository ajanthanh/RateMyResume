from django.contrib import admin

# Register your models here.
from .forms import SignUpForm
from .models import Account


class SignUpAdmin(admin.ModelAdmin):
    list_display = ["__str__", "timestamp", "update"]
    form = SignUpForm
    # class Meta:
    #     model = SignUp


admin.site.register(Account, SignUpAdmin)
