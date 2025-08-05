from django.db import models
from django.contrib.auth.models import AbstractBaseUser , BaseUserManager , PermissionsMixin
# Create your models here.
class UsersManager(BaseUserManager):
  def create_user(self , email , username, password=None , **extra_fields):
    if not email:
      raise ValueError('Email is required.')
    email = self.normalize_email(email)
    user = self.model(email=email,username=username,**extra_fields)
    user.set_password(password)
    user.save(using=self._db)
    return user
  def create_superuser(self,email, username, password=None , **extra_fields):
    extra_fields.setdefault('is_staff', True)
    extra_fields.setdefault('is_superuser',True)
    return self.create_user(email, username, password, **extra_fields)

class Users(AbstractBaseUser, PermissionsMixin):
   email = models.EmailField(unique=True)
   username = models.CharField( max_length=50,unique=True)
   name = models.CharField(max_length=20)
   bio = models.TextField(blank=True)
   profile_image = models.ImageField(upload_to='profiles/',null=True , blank=True)
   is_active = models.BooleanField(default=True)
   is_staff = models.BooleanField(default=False)

   objects = UsersManager()

   USERNAME_FIELD = 'email'
   REQUIRED_FIELDS = ['username']
  
   def __str__(self):
       return self.email
  