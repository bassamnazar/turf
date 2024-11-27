from django.urls import path 
from core.views import *

urlpatterns = [
    path('',home_view,name='home_view'),
    path('signup',signup_view,name='signup_view'),
    path('login',login_view,name='login_view'),
    path('logout',logout_view,name='logout_view'),
    path('book_page/', book_page, name='book_page'),
    path('my_appointments/', my_appointments, name='my_appointments'),
    path('create_appointment/', create_appointment, name='create_appointment'),
    path('delete_appointment/<int:appointment_id>', delete_appointment, name='delete_appointment'),  

]