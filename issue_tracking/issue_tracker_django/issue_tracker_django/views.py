
from django.contrib.auth import login
from django.contrib.auth.models import User
from project.serializers import UserSerializer
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.response import Response
from project.serializers import UserSerializer
from .permissions import contribAuthPermissions

class LoginView(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginView, self).post(request, format=None)

@api_view(['GET'])
def fetchUserInfo(request):
    permission_classes=[IsAuthenticated]
    return Response(UserSerializer(request.user).data)

@api_view(['GET'])
def fetchUserList(request):
    permission_classes = [contribAuthPermissions]
    user_list = User.objects.all()
    serializer = UserSerializer(user_list,many =True)
    return Response(serializer.data)