from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Message
from .serializers import MessageSerializer
import random
from rest_framework.decorators import action
from rest_framework.response import Response

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    @action(detail=True, methods=['put'])
    def simulate_send(self, request, pk=None):
        message = self.get_object()
        message.status = random.choice(['sent', 'failed'])
        message.save()
        return Response({'status': message.status})
    
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')