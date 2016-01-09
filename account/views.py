from django.shortcuts import render
from .forms import SignUpForm


# Create your views here.
def home(request):
    title = "Welcome"
    # if request.user.is_authenticated():
    #     title = "My Title %s" % (request.user)
    form = SignUpForm(request.POST or None)

    context = {
        "title": title,
        "form": form
    }

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        print(instance)
        context ={
            "title": "Thank you"
        }

    return render(request, "home.html", context)
