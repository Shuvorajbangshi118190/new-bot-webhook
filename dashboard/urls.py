from django.urls import path
from . import views

urlpatterns = [
   path('dashboard/', views.dashboard, name='dashboard'),
   path('dashboard/providers/', views.provider_table, name='provider_table'),
   path('dashboard/customers/', views.customer_table, name='customer_table'),
   path('dashboard/create_customer/', views.create_customer, name='create_customer'),
   path('dashboard/create_provider/', views.create_provider, name='create_provider'),
   path('dashboard/edit_provider/<int:provider_id>/', views.edit_provider, name='edit_provider'),
   path('dashboard/edit_customer/<int:customer_id>/', views.edit_customer, name='edit_customer'),
]
