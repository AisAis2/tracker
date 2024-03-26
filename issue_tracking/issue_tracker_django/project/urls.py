from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('two_projects/',views.twosProjects.as_view()),
    path('project/<int:id>/',views.projectView.as_view()),
    path('project/create/',views.projectView.as_view()),
    path('project/<int:id>/delete',views.projectView.as_view()),
    path('project/<int:id>/edit',views.projectView.as_view()),
    path('group/add/',views.addNewUserToGroup),
    path('group/perms/',views.getPermFrontEnd)

]