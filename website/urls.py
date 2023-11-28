from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    #path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('cliente/<int:pk>', views.customer_cliente, name='cliente'),
    path('delete_cliente/<int:pk>', views.delete_cliente, name='delete_cliente'),
    path('add_cliente/', views.add_cliente, name='add_cliente'),
    path('update_cliente/<int:pk>', views.update_cliente, name='update_cliente'),
    
]
