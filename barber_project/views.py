from .models import Barber, Comment
from django.db.models.functions import Cast
from rest_framework import generics, permissions
from django.contrib.auth import get_user_model, authenticate, logout, login
from .serializers import BarberSerializer, CommentSerializer, UserSerializer

class CreateUser(generics.CreateAPIView):
  model = get_user_model()
  serializer_class = UserSerializer
  permission_classes = [permissions.AllowAny]

class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.AllowAny]
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class BarberList(generics.ListCreateAPIView):
  serializer_class = BarberSerializer
  queryset = Barber.objects.all()
  permission_classes = [permissions.AllowAny]

class BarberDetail(generics.RetrieveUpdateDestroyAPIView):
  serializer_class = BarberSerializer
  queryset = Barber.objects.all()
  permission_classes = [permissions.AllowAny]

  def put(self, request, *args, **kwargs):
    print(request)
    return self.update(request, *args, **kwargs)

  def delete(self, request, *args, **kwargs):
    return self.destroy(request, *args, **kwargs)
 