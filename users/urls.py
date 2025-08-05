from django.urls import path
from .views import RegisterView, LoginView, LogoutView, DeleteAccountView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('delete/', DeleteAccountView.as_view()),
]
