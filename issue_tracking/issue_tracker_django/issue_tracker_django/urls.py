from django.contrib import admin
from django.urls import path, include
from knox import views as knox_views
from .views import LoginView,fetchUserInfo,fetchUserList
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/v1/',include('djoser.urls')),
    # path('api/v1/',include('djoser.urls.authtoken')),
    path('api/v1/', include('project.urls')),
    path('api/v1/', include('ticket.urls')),
    # path('api/v1/',include('knox.urls')),
    path('api/v1/login/',LoginView.as_view(),name='know_login'),
    path('api/v1/logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
    path('api/v1/logoutall/', knox_views.LogoutAllView.as_view(), name='knox_logoutall'),
    path('api/v1/users/me/',fetchUserInfo),
    path('api/v1/users/',fetchUserList)
]
