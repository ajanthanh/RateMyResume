from django.shortcuts import render
from .forms import SignUpForm


# Create your views here.

def home(request):
    return render(request, "home.html")


def profile(request):
    #     title = "My Title %s" % (request.user)
    form = SignUpForm(request.POST or None, request.FILES or None)
    title = "SignUp"
    context = {
        #"title": title,
        "form": form,
    }

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        print(instance)
        context = {
            "title": "Thank you",
        }

    if request.user.is_authenticated():
        context.update({"user": request.user})

    return render(request, "signup.html", context)
