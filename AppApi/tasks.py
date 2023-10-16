import requests
from celery import shared_task
import logging
logger = logging.getLogger('django')
import json

@shared_task
def test(data):
    print("Hello from celery")

from celery import shared_task
import json
from AppApi.Services.RoutemobileServices import RouteMobileService
from AppApi.Services.SSLBotServices import SSLBotServices



@shared_task
def process_webhook_data(data):
    #print(data)
    route_mobile_service = RouteMobileService()
    ssl_bot_service = SSLBotServices()
    message_data = route_mobile_service.process_webhook_data(data)

    payload_fun = ssl_bot_service.payload_fun(message_data)
    print(payload_fun)
    json_data = ssl_bot_service.api_hit(payload_fun)
    
    process_json_data=route_mobile_service.process_json_data(json_data, message_data["user_name"])
   
    
    return 0

   
   