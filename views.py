from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer
    
    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)
        
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
