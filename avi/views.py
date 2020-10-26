from django.shortcuts import render
from django .http import HttpResponse
from.models import post
from .forms import NewProjectForm

# Create your views here.


def home(request):
    context={
        'posts':post.objects.all()
        }
    return render(request, 'avi/home.html',context)

def about(request):
     return render(request, 'avi/about.html',)

def new_project(request):


@login_required(login_url='/accounts/login/')
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
    return render(request, 'new_project.html', {"form": form})