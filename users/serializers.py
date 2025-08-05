from rest_framework import serializers
from .models import Users
from django.contrib.auth import authenticate , get_user_model

user = get_user_model()

class UserRegisterSerializer(serializers.ModelSerializer):
  password = serializers.CharField(write_only=True)

  class Meta:
    model = Users
    fields = ['email', 'username','name','password']

  def create(self,validate_data):
    user=Users.objects.create_user(
      username=validate_data['username'],
      email=validate_data['email'],
      password=validate_data['password']
    )
    return user
     
  
class UserLoginSerializer(serializers.Serializer):
  email = serializers.EmailField()
  password = serializers.CharField()

  def validate(self, data):
    user = authenticate(email=data['email'],
                        password=data['password'])
    if not user:
      raise serializers.ValidationError("invalide email or password")
    data['user'] = user
    return data
  