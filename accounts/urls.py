from django.urls import path
from .views import SignupView, custom_login

urlpatterns = [
   path('', custom_login, name='login'),   
   path('signup/', SignupView, name='signup'),
]


