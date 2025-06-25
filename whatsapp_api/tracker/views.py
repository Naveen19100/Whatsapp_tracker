from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Message
from .serializers import MessageSerializer
import random

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    
    def create(self, request, *args, **kwargs):
       print("📥 Incoming data:", request.data)

       serializer = self.get_serializer(data=request.data)
       if serializer.is_valid():
         print("✅ Validated data:", serializer.validated_data)
         self.perform_create(serializer)
         return Response(serializer.data, status=201)
       else:
         print("❌ Serializer errors:", serializer.errors)
         return Response(serializer.errors, status=400)


    

    @action(detail=True, methods=['put'])
    def simulate_send(self, request, pk=None):
        message = self.get_object()
        message.status = random.choice(['sent', 'failed'])
        message.save()
        return Response({'status': message.status})


def home(request):
    return render(request, 'index.html')