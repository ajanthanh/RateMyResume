from django.shortcuts import render
from .forms import ResumeForm


def upload(request):
    #     title = "My Title %s" % (request.user)
    form = ResumeForm(request.POST or None, request.FILES or None)

    context = {
        "form": form,
    }

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        context = {
            "title": "Thank you",
        }

    if request.user.is_authenticated():
        context.update({"user": request.user})

    return render(request, "resume_upload.html", context)
