class DemoService:

    def process_callback_text(self, data):
        message = data["messages"][0]
        sender = message["from"]
        main_text = message["text"]["body"]
        user_name = data["contacts"][0]["profile"]["name"]
        app_name = data["request_id"]
        message_type = "text"
        return {
            "message": message,
            "sender": sender,
            "main_text": main_text,
            "user_name": user_name,
            "app_name": app_name,
            "message_type": message_type
        }
    

import json

class RouteMobileService:
    
    def payload_fun(sender, app_name, main_text, user_name, message_type):
        payload = {
            "data": {
                "sender": sender,
                "recipient": app_name,
                "messenger": "whatsapp",
                "payload": {
                    "type": message_type,
                    "text": main_text,
                    "user": {
                        "id": None,
                        "name": user_name,
                        "image": None
                    }
                },
            }
        }
        payload_json = json.dumps(payload)
        return payload_json

    @classmethod
    def process_webhook_data(cls, data):
        try:
            message_type = None

            if data["messages"][0]["type"] == 'text':
                message_data = cls.process_callback_text(data)
                message_type = "text"

            elif data["messages"][0]["type"] == 'image':
                message_data = cls.process_callback_image(data)
                message_type = "image"

            elif data["messages"][0]["type"] == 'interactive':
                message_data = cls.process_callback_interactive(data)
                message_type = "interactive"

            elif data["messages"][0]["interactive"]["type"] == "button_reply":
                message_data = cls.process_callback_button_reply(data)
                message_type = "button_reply"

            if message_type is not None:
                payload_data = cls.payload_fun(**message_data)

        except Exception as e:
            print("Error:", e)

    def process_callback_text(self, data):
        message = data["messages"][0]
        sender = message["from"]
        main_text = message["text"]["body"]
        user_name = data["contacts"][0]["profile"]["name"]
        app_name = data["request_id"]
        message_type = "text"
        return {
           
            "sender": sender,
            "main_text": main_text,
            "user_name": user_name,
            "app_name": app_name,
            "message_type": message_type
        }

    def process_callback_image(self, data):
        message = data["messages"][0]
        sender = message["from"]
        main_text = message["image"]["file"] + message["image"]["media_url"]
        user_name = None
        app_name = data["request_id"]
        message_type = "image"
        return{
            
            "sender": sender,
            "main_text": main_text,
            "user_name": user_name,
            "app_name": app_name,
            "message_type": message_type



        }

    def process_callback_interactive(self, data):
        sender = data["messages"][0]["from"]
        user_name = data["contacts"][0]["profile"]["name"]
        app_name = data["request_id"]
        main_text = data["messages"][0]["interactive"]["list_reply"]["title"]
        message_type = "interactive"
        return{
          
            "sender": sender,
            "main_text": main_text,
            "user_name": user_name,
            "app_name": app_name,
            "message_type": message_type



        }

    def process_callback_button_reply(self, data):
        message = data["messages"][0]
        sender = message["from"]
        user_name = data["contacts"][0]["profile"]["name"]
        main_text = message["interactive"]["button_reply"]["title"]
        app_name = message["id"]
        message_type = "interactive"
        return{
          
            "sender": sender,
            "main_text": main_text,
            "user_name": user_name,
            "app_name": app_name,
            "message_type": message_type



        }