from django.shortcuts import render
from django.shortcuts import render_to_response
from .forms import ResumeForm
from .models import Resume


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

def resumes(request):
    return render_to_response('resumes.html',
        {'resumes': Resume.objects.all()})
def resume(request, resume_id=1):
    return render_to_response('resume.html',
        {'resume': Resume.objects.get(id=resume_id)})