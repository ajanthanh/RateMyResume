from django.contrib import admin

from .forms import ResumeForm
from .models import Resume


class ResumeAdmin(admin.ModelAdmin):
    list_display = ["id", "file_name"]
    form = ResumeForm

    class Meta:
        model = Resume


admin.site.register(Resume, ResumeAdmin)
