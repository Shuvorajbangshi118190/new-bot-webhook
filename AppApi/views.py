import logging, json


from rest_framework.response import Response
import json
import xmltodict
import urllib.parse


from django.http import JsonResponse
from rest_framework.views import APIView
from .tasks import process_webhook_data,test
logger = logging.getLogger('django')

class AppWebhookView(APIView):
    def post(self, request, *args, **kwargs):
        #headers = request.META
        #content_type = headers.get('Content-Type', '')
        #content_type = request.META.get('CONTENT_TYPE', '').lower()
        #print(content_type)
        data = request.data

        '''
        # Check if the incoming data is in XML format
        if "xml" in content_type:
            try:
                data = xmltodict.parse(data)
            except Exception as e:
                return Response({"error": "Invalid XML format"}, status=400)

        # Check if the incoming data is in x-www-form-urlencoded format
        elif "x-www-form-urlencoded" in content_type:
            try:
                data = urllib.parse.parse_qs(data)
            except Exception as e:
                return Response({"error": "Invalid x-www-form-urlencoded format"}, status=400)

        # Otherwise, assume it is in JSON format
        elif "json" in content_type:
            try:
                data = json.loads(data)
            except Exception as e:
                return Response({"error": "Invalid JSON format"}, status=400)

        # Handle other formats or raise an error if the format is not recognized
        else:
            return Response({"error": "Unsupported content type"}, status=415)
'''
        
        #print(data)

        
        #print(data.dict())
        
        try:
            if data["messages"][0]["type"] == 'text' or data["messages"][0]["type"] == 'image'or data["messages"][0]["type"] == 'interactive':
              process_webhook_data.delay(data)  
            elif data['type'] == 'message-event':
                print('msg event')
                pass
        except Exception as e:
            print("Error in views:", e)

        return JsonResponse({'status': 'success'})
       