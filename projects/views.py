from django.shortcuts import render,redirect
from projects.models import Project,ProjectCategory
from .forms import newProjectForm
from django.contrib.auth.models import User


def project_index(request):
    projects = Project.objects.all()
    context = {"projects": projects}
    return render(request, "project_index.html", context)

def profile_project_index(request):
    projects = Project.objects.filter(user = request.user)
    context = {"projects": projects}
    return render(request, "profile_project_index.html", context)

def user_project_index(request,username):
    user = User.objects.get(username=username)
    projects = Project.objects.filter(user = user)
    context = {
        "projects": projects,
        "user":user
    }
    return render(request, "user_project_index.html", context)

def category_project_index(request,name):
    projectCategory = ProjectCategory.objects.get(name=name)
    projects = Project.objects.filter(projectcategory = projectCategory)
    context = {
        "projects": projects,
        "projectCategory":projectCategory,
    }
    return render(request, "category_project_index.html", context)

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {"project": project}
    return render(request, "project_detail.html", context)

def add_project(request):
    if request.method == "POST":
        form = newProjectForm(request.POST)
        if form.is_valid():
            project_x = Project(user = request.user,
                title = form.cleaned_data['title'],
                description = form.cleaned_data['description'],
                technology = form.cleaned_data['technology'],
                projectcategory = form.cleaned_data['projectcategory'])
            project_x.save()
            return redirect('profile_project_index')
    else:
        form = newProjectForm()
    return render(request, 'add_project.html', {'form': form})


def base_page(request):
    return render(request,"base1.html")

