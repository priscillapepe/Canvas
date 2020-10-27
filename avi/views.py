from django.shortcuts import render,redirect
from django .http import HttpResponse
from.models import Project
from .forms import NewProjectForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    
    return render(request, 'avi/home.html')

def about(request):
     return render(request, 'avi/about.html',)




# @login_required(login_url='/accounts/login/')
def new_project(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.editor = current_user
            project.save()
        return redirect('avi-home')

    else:
        form = NewProjectForm()
    return render(request, 'avi/new_project.html', {"form": form})