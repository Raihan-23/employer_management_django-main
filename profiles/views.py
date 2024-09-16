from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Profiles
from .forms import ProfileForm

# Create your views here.

def home(request):
    # return HttpResponse("Welcome to the Home Page!")
    return HttpResponse(
        "Hello, this is the home page of our Employee Management System!"
    )


def create_profile(request):
    if request.method =="POST":
        add_form = ProfileForm(request.POST)
        if add_form.is_valid():
            add_form.save()
            return redirect("home")
        else:
            # return HttpResponse("Form is not valid!")
            context = {
                "add_form": add_form,
            }
            return render(request, "profiles/create_profile.html", context=context)
    else:
        # return HttpResponse("This is not a POST request!")
        add_form = ProfileForm()
        context = {
            "add_form": add_form,
        }
        return render(request, "profiles/create_profile.html", context=context)