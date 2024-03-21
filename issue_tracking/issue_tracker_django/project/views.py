from django.http import Http404
from django.contrib.auth.models import User, Group
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.http import HttpResponse
from rest_framework.response import Response

from .models import Project
from .serializers import ProjectSerializer
from .forms import createProject
from .permissions import ProjectPermissions

class twosProjects(APIView):
    def get(self,request, format = None):#overwrite get functionality
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many = True)
        return Response(serializer.data)
class projectView(APIView):
    permission_classes = [ProjectPermissions]
    def get_object(self,id):#get the obeject, we still need to override get()
        try:
            return Project.objects.get(id=id)
        except Project.DoesNotExist:
            raise Http404
    def get(self, request, id, format=None):
        project = self.get_object(id)
        serializer = ProjectSerializer(project)
        return Response(serializer.data)

    def post(self,request):
        serializer = ProjectSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Succesfully created new project','status':'HTTP_200_OK'})
        return Response({'message':'Error when creating projects','status':'HTTP_400_BAD_REQUEST'})
    def put(self,request,id,formate=None):
        project = self.get_object(id)
        serializer = ProjectSerializer(project,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'message':'Error when creating projects','status':'HTTP_400_BAD_REQUEST'})
    def delete(self,request,id=None):
        project = Project.objects.filter(id=id)
        project.delete()
        return Response({"status":"HTTP_204_NO_CONTENT"})

@api_view(['POST'])#This decorator was required for function based V
def addNewUserToGroup(request):
    print('Adding the '+request.data['username']+'to cuser Group')
    if request.method =='POST':
        try:
            u = User.objects.get(username = request.data['username'])
        except User.DoesNotExist:
            raise Http404
        g = Group.objects.get(name = 'cuser')
        g.user_set.add(u)
        return HttpResponse('User Succesfull added to a group')
    return Http404

    
