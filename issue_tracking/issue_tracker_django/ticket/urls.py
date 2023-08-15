from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('project/<int:id>/tickets/',views.ticketsList.as_view()),
    path('ticket/<int:id>/',views.ticketView.as_view()),
    path('ticket/create/',views.ticketView.as_view()),
    path('ticket/all/',views.ticketsList.as_view()),
    path('ticket/<int:id>/update',views.ticketView.as_view()),
    path('ticket/<int:id>/delete',views.ticketView.as_view())

]