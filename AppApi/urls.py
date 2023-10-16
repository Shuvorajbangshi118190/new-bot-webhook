from django.urls import path,include
from .views import AppWebhookView


urlpatterns = [
    path('webhook/', AppWebhookView.as_view(), name='webhook'),
    
]


