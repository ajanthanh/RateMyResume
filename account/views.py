from django.shortcuts import render
from .forms import SignUpForm


# Create your views here.

def home(request):
    return render(request, "home.html")


def signup(request):
    title = "Sign Up"
    body_content = "In just a few moments we can get you signed up, and you can upload, view and critque resumes from the community"

    #     title = "My Title %s" % (request.user)
    form = SignUpForm(request.POST or None)

    context = {
        "title": title,
        "form": form,
        "body_content": body_content,
    }

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        print(instance)
        context = {
            "title": "Thank you",
            "body_content": "You will be recieving an email confirmation shortly"
        }

    if request.user.is_authenticated():
        context.update({"user": request.user})

    return render(request, "signup.html", context)
