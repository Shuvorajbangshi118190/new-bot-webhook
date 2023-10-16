import json
from AppApi.Services.SSLBotServices import SSLBotServices

class RouteMobileService:
    def process_webhook_data(self, data):
        try:

            if data["messages"][0]["type"] == 'text':
                message_data = self.process_callback_text(data)

            elif data["messages"][0]["type"] == 'image':
                message_data = self.process_callback_image(data)

            elif data["messages"][0]["type"] == 'interactive':
                message_data = self.process_callback_interactive(data)

            elif data["messages"][0]["interactive"]["type"] == "button_reply":
                message_data = self.process_callback_button_reply(data)

            if message_data["message_type"] is not None:
               #print(message_data)
               return message_data
        except Exception as e:
            print("Error:", e)
            return None

    def process_callback_text(self, data):
        message = data["messages"][0]
        sender = message["from"]
        main_text = message["text"]["body"]
        user_name = data["contacts"][0]["profile"]["name"]
        app_name = data["request_id"]
        message_type = "text"
        return {
            "sender": sender,
            "app_name": app_name,
            "main_text": main_text,
            "user_name": user_name, 
            "message_type": message_type,
            
        }

    def process_callback_image(self, data):
        message = data["messages"][0]
        sender = message["from"]
        main_text = message["image"]["file"] + message["image"]["media_url"]
        user_name = "none"
        app_name = data["request_id"]
        message_type = "image"
        return {
            "sender": sender,
            "app_name": app_name,
            "main_text": main_text,
            "user_name": user_name, 
            "message_type": message_type,
            
        }

    def process_callback_interactive(self, data):
        sender = data["messages"][0]["from"]
        user_name = data["contacts"][0]["profile"]["name"]
        app_name = data["request_id"]
        main_text = data["messages"][0]["interactive"]["list_reply"]["title"]
        message_type = "interactive"
        return {
            "sender": sender,
            "app_name": app_name,
            "main_text": main_text,
            "user_name": user_name, 
            "message_type": message_type,
            
        }

    def process_callback_button_reply(self, data):
        message = data["messages"][0]
        sender = message["from"]
        user_name = data["contacts"][0]["profile"]["name"]
        main_text = message["interactive"]["button_reply"]["title"]
        app_name = data["messages"][0]["id"]
        message_type = "interactive"
        return {
            "sender": sender,
            "app_name": app_name,
            "main_text": main_text,
            "user_name": user_name, 
            "message_type": message_type,
            
        }




#responsive json_data for route mobile end point
    def process_json_data(self, json_data, user_name):
        data = json_data
        print(data)
        sender = data["sender"]
        app_name = data["recipient"]
        user_name= user_name


        def text_post(data, sender):
            texts = data
            delivered_data = {
                "phone": sender,
                "text": texts,
                "enable_acculync": True,
                "extra": "{your value}"
            }
            payload_delivered_json = json.dumps(delivered_data)
            print(payload_delivered_json)

                # Send the payload to the other API here using the appropriate URL
                # api_url = 'https://apis.rmlconnect.net/wba/v1/messages'
                # response = requests.post(api_url, json=payload_delivered_json)
                # print(response.json())
            return payload_delivered_json
        data = json_data
        
        
        for item in data["data"]:
            try:
                text_data = item["text"]["text"][0]
                payload_delivered_json = text_post(text_data, sender)

            except :
                pass
    
        
        def image_post(data, sender,image_url):
            image_url = image_url
            file_name = image_url.split("/")[-1]
            caption = "Sample text"

            delivered_data = {
                "phone": sender,
                "enable_acculync": True,
                "media": {
                    "type": "image",
                    "url": image_url,
                    "file": file_name,
                    "caption": caption
                },
                "extra": "{your value}"
            }
            payload_delivered_json = json.dumps(delivered_data)
            
            return payload_delivered_json
        data=json_data
        for item in data["data"]:
        
            try:
                    image_url= item["payload"]["web"]["image_url"]
                    payload_delivered_json = image_post(item, sender,image_url)
                    print(payload_delivered_json)

                    # Send the payload to the other API here using the appropriate URL
                    # api_url = 'https://apis.rmlconnect.net/wba/v1/messages'
                    # response = requests.post(api_url, json=payload_delivered_json)
                    # print(response.json())

            except:
        
                    pass
        
        def get_buttons_info(data):
            buttons_info = []
            for item in data:
                if "payload" in item:
                    payload = item["payload"]
                    if "web" in payload:
                        web_payload = payload["web"]
                        if "attachment" in web_payload and "payload" in web_payload["attachment"]:
                            buttons = web_payload["attachment"]["payload"]["buttons"]
                            for button in buttons:
                                button_info = {
                                    "payload": button.get("payload", ""),
                                    "title": button.get("title", ""),
                                    "type": button.get("type", "")
                                }
                                buttons_info.append(button_info)
            return buttons_info

        def convert_buttons_to_desired_format(buttons_info):
            converted_buttons = []
            section_title_count = None

            for button_info in buttons_info:
                section_title = button_info["payload"]
                title = button_info["title"]
                description = button_info["type"]

                if section_title_count is None:
                    section_title_count = 1
                else:
                    section_title_count += 1

                id_value = str(section_title_count)
                
                button = {
                    "section_title": section_title,
                    "row": [
                        {
                            "id": id_value,
                            "title": title,
                            "description": description
                        }
                    ]
                }

                converted_buttons.append(button)

            return converted_buttons

        # Your original JSON data here
        json_data = json_data

        # Get the buttons_info from the original JSON data
        buttons_info = get_buttons_info(json_data["data"])

        # Convert buttons_info to the desired format
        converted_buttons = convert_buttons_to_desired_format(buttons_info)

        # Create the final JSON with the desired format
        final_json = {
            "phone": sender,
            "extra": "{your value}",
            "enable_acculync": True,
            "media": {
                "type": "interactive_list",
                "header": {
                    "text": text_data
                },
                "body": "Hello" +" "+user_name+ "."+" "+"Please select from the list below",
                "footer_text": "Menu",
                "button_text": "Select",
                "button": converted_buttons
            }
        }

        payload_delivered_json = json.dumps(final_json)
        print(payload_delivered_json)
        
        # Send the payload to the other API here using the appropriate URL
        # api_url = 'https://apis.rmlconnect.net/wba/v1/messages'
        # response = requests.post(api_url, json=final_json)
        # print(response.json())
        
        def get_quick_reply_info(data):
            quick_reply_info = data["data"][-1]["payload"]["web"]["quick_reply"]
            buttons = quick_reply_info["buttons"]
            quick_reply_title = quick_reply_info["title"]

            quick_reply_buttons = []
            for i, button_name in enumerate(buttons, start=1):
                button_id = str(i)
                quick_reply_buttons.append({"id": button_id, "title": button_name})

            return quick_reply_title, quick_reply_buttons

        # Get the quick reply information from the JSON data
        quick_reply_title, quick_reply_buttons = get_quick_reply_info(json_data)

        # Create the final JSON with the desired format
        final_json = {
            "phone": sender,
            "extra": "your_value",
            "enable_acculync": True,
            "media": {
                "type": "interactive_reply",
                "header": {
                    "text": quick_reply_title
                },
                "body": "Hello" +" "+user_name+ "."+" "+"please select an option below",
                "footer_text": "c@2021",
                "button": quick_reply_buttons
            }
        }

        payload_delivered_json = json.dumps(final_json)
        print(payload_delivered_json)
        # Send the payload to the other API here using the appropriate URL
        # api_url = 'https://apis.rmlconnect.net/wba/v1/messages'
        # response = requests.post(api_url, json=final_json)
        # print(response.json())
        return 0