from django.shortcuts import render
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Ticket
from .serializers import TicketSerializer
from project.models import Project
from project.serializers import ProjectSerializer
from project.permissions import TicketPermissions

class ticketsProject(APIView):
    def get(self,request,id,format = None):
        p = Project.objects.get(id=id)
        tickets = Ticket.objects.filter(project=p)
        serializer = TicketSerializer(tickets, many =True)
        return Response(serializer.data)
class ticketsList(APIView):
    def get(self,request,format = None):
        ticket_per_page = 10
        if not 'page' in request.GET.keys():
            tickets = Ticket.objects.all()
            serializer = TicketSerializer(tickets, many =True)
            return Response(serializer.data)
        page_number = int(request.GET['page'])-1
        length = len(Ticket.objects.all())
        if page_number*ticket_per_page+ticket_per_page>length:
            end = length
        else:
            end = page_number*ticket_per_page+ticket_per_page
        tickets = Ticket.objects.all()[page_number*ticket_per_page:end]
        serializer = TicketSerializer(tickets, many =True)
        return Response([serializer.data,length])
class ticketView(APIView):
    permission_classes=[TicketPermissions]
    def get_object(self,id):
        try:
            return Ticket.objects.get(id=id)
        except Ticket.DoesNotExist:
            raise Http404
    def get(self,request,id,format=None):
        ticket = self.get_object(id)
        serializer = TicketSerializer(ticket)
        return Response(serializer.data)
    def post(self,request):
        ticket  = request.data
        serializer = TicketSerializer(data = ticket)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Succesfully created new ticket','status':'HTTP_500_OK'})
        return Response({'message':'Error when creating ticket','status':'HTTP_500_ERROR'}) 
    
    def put(self,request,id, formate=None):
        ticket=self.get_object(id)
        serializer = TicketSerializer(ticket, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Succesfully updated the ticket','status':'HTTP_200_OK'})
        return Response({'message':'Error when updating ticket','status':'HTTP_500_ERROR'}) 

    def delete(self,request,id):
        ticket = self.get_object(id)
        ticket.delete()
        return Response({'message':'Succesfully deleted the ticket','status':'HTTP_200_OK'})
