import json
import requests

class SSLBotServices:

    def __init__(self):
        self.url = "https://ibot.sslwireless.com/api/integration/whatsapp"

    def payload_fun(self, message_data):
        payload = {
            "data": {
                "sender": message_data['sender'],
                "recipient": message_data['app_name'],
                "messenger": "whatsapp",
                "payload": {
                    "type": message_data['message_type'],
                    "text": message_data['main_text'],
                    "user": {
                        "id": None,
                        "name": message_data['user_name'],
                        "image": None
                    }
                },
            }
        }
       
        return payload
    
    def api_hit(self, payload):
         
        

        # Send the data to the other API as JSON
        response = requests.post(self.url, json=payload)  # Change this line
        #print(json_data.json())  # Print the response as JSON
        
        return response.json()

