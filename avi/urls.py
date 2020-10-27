from . import views
from avi import views as user_views
from django.urls import path


urlpatterns = [
    path('', views.home, name='avi-home'),
    path('about/', views.about, name='avi-about'), 
    path('new_project/',views.new_project,name='add-project')
]





