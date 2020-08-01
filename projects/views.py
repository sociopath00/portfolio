from django.shortcuts import render
from projects.models import Projects


# Create your views here.
def project_index(request):
	projects = Projects.objects.all()
	context = {"projects": projects}
	return render(request, "projects/project_index.html", context)


def project_details(request, pk):
	# primary key of the project that is being clicked (or to fetch info)
	project = Projects.objects.get(pk=pk)
	context = {"project": project}
	return render(request, "projects/project_details.html", context)


