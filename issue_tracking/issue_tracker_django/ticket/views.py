from django.shortcuts import render
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Ticket
from .serializers import TicketSerializer
from project.models import Project
from project.serializers import ProjectSerializer

class ticketsList(APIView):
    def get(self,request,format = None):
        # print('-----------------')
        # print('-----------------')
        # print('get requst data below')
        # print(request)
        # print('get requst data above')
        tickets = Ticket.objects.all()
        serializer = TicketSerializer(tickets, many =True)
        return Response(serializer.data)

class ticketView(APIView):
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
        print(ticket)
        serializer = TicketSerializer(data = ticket)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Succesfully created new ticket','status':'HTTP_500_OK'})
        print(serializer.errors)
        return Response({'message':'Error when creating ticket','status':'HTTP_500_ERROR'}) 
    def put(self,request,id, formate=None):
        ticket=self.get_object(id)
        serializer = TicketSerializer(ticket, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Succesfully updated the ticket','status':'HTTP_200_OK'})
        
        return Response({'message':'Error when creating ticket','status':'HTTP_500_ERROR'}) 

    def delete(self,request,id):
        ticket = self.get_object(id)
        ticket.delete()
        return Response({'message':'Succesfully deleted the ticket','status':'HTTP_200_OK'})
