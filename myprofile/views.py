from django.shortcuts import render
from .profile_details import MyProfile


# Create your views here.
def profile(request):
	context = {"my_profile": MyProfile}
	return render(request, "myprofile/profile.html", context)