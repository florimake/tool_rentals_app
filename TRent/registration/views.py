from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib import messages


def homepage(request):
    user = [x.username for x in User.objects.all() if x.is_authenticated]
    context = {
		"user":user,
		"anonim":User.normalize_username
	}
    return render ( request , 'home.html', context)

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("../home/")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	print(request)
	form = NewUserForm()
	return render (request=request, template_name="registration/register.html", context={"register_form":form})