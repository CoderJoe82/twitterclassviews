from django.urls import path
from authentication import views

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='loginpage'),
    path('logout/', views.LogoutView.as_view()),
    path('signup/', views.SignupView.as_view())
]
