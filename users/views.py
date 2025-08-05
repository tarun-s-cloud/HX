from django.shortcuts import render
from rest_framework import status , permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login, logout
from .serializers import UserRegisterSerializer, UserLoginSerializer
# Create your views here.
from .models import Users

class RegisterView(APIView):
  def post(self, request):
    serializer = UserRegisterSerializer(data=request.data)
    if serializer.is_valid():
      user = serializer.save()
      return Response({"message": "user register succesfully", "user": serializer.data}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
class LoginView(APIView):
  def post(self, request):
    serializer = UserLoginSerializer(data=request.data)
    if serializer.is_valid():
      user = serializer.validated_data['user']
      login(request, user)
      return Response({"message":"login successful", "user": {
        "email": user.email,
        "username": user.username,
        "name": user.name
      }})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        logout(request)  # ✅ session destroyed
        return Response({'message': 'Logout successful'})

class DeleteAccountView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request):
        request.user.delete()
        return Response({'message': 'Account deleted successfully'})