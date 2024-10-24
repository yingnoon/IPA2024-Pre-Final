#######################################################################################
# Yourname: Kwannate Theethuan
# Your student ID: 65070027
# Your GitHub Repo: https://github.com/yingnoon/IPA2024-Pre-Final.git

#######################################################################################
# 1. Import libraries for API requests, JSON formatting, time, and (restconf_final or netconf_final).

import requests
import json
import time
from restconf_final import create, delete, enable, disable, status, delete_interface

#######################################################################################
# 2. Assign the Webex access token to the variable ACCESS_TOKEN using environment variables.
import os

# Assign the Webex access token to the variable ACCESS_TOKEN
ACCESS_TOKEN = os.environ.get('WEBEX_ACCESS_TOKEN')  # ใช้ os.environ.get() เพื่อดึงค่า
# หรือ
# ACCESS_TOKEN = os.environ['WEBEX_ACCESS_TOKEN']  # หรือใช้ os.environ[] แต่หากไม่มีค่าอาจจะเกิดข้อผิดพลาด

# ตรวจสอบว่า ACCESS_TOKEN ได้ค่ามาหรือไม่
if ACCESS_TOKEN:
    print("Webex Access Token: Retrieved successfully!")
else:
    print("Webex Access Token: Not found, please set it in the environment variables.")

#######################################################################################
# 3. Prepare parameters get the latest message for messages API.

# Defines a variable that will hold the roomId
roomIdToGetMessages = (
    "Y2lzY29zcGFyazovL3VzL1JPT00vNTFmNTJiMjAtNWQwYi0xMWVmLWE5YTAtNzlkNTQ0ZjRkNGZi"
)

while True:
    # always add 1 second of delay to the loop to not go over a rate limit of API calls
    time.sleep(1)

    # the Webex Teams GET parameters
    #  "roomId" is the ID of the selected room
    #  "max": 1  limits to get only the very last message in the room
    getParameters = {"roomId": roomIdToGetMessages, "max": 1}

    # the Webex Teams HTTP header, including the Authoriztion
    getHTTPHeader = {"Authorization": ACCESS_TOKEN}

# 4. Provide the URL to the Webex Teams messages API, and extract location from the received message.
    
    # Send a GET request to the Webex Teams messages API.
    # - Use the GetParameters to get only the latest message.
    # - Store the message in the "r" variable.
    r = requests.get(
        "https://webexapis.com/v1/messages",
        params=getParameters,
        headers=getHTTPHeader,
    )
    # verify if the retuned HTTP status code is 200/OK
    if not r.status_code == 200:
        raise Exception(
            "Incorrect reply from Webex Teams API. Status code: {}".format(r.status_code)
        )

    # get the JSON formatted returned data
    json_data = r.json()

    # check if there are any messages in the "items" array
    if len(json_data["items"]) == 0:
        raise Exception("There are no messages in the room.")

    # store the array of messages
    messages = json_data["items"]
    
    # store the text of the first message in the array
    message = messages[0]["text"]
    print("Received message: " + message)

    # check if the text of the message starts with the magic character "/" followed by your studentID and a space and followed by a command name
    #  e.g.  "/66070123 create"
    if message.find("/65070027") == 0:

        # extract the command
        command = message.split(" ")[1]
        print(command)

# 5. Complete the logic for each command

        if command == "create":
            responseMessage = create()     
        elif command == "delete":
            responseMessage = delete()
        elif command == "enable":
            responseMessage = enable()
        elif command == "disable":
            responseMessage = disable()
        elif command == "status":
            responseMessage = status()
        # elif command == "desc":
        #     responseMessage = desc()
        # elif command == "ipv6":
        #     responseMessage = ipv6()
        else:
            responseMessage = "Error: No command or unknown command"
        
# 6. Complete the code to post the message to the Webex Teams room.
        
        # the Webex Teams HTTP headers, including the Authoriztion and Content-Type
        postHTTPHeaders = HTTPHeaders = {"Authorization": ACCESS_TOKEN, "Content-Type": "application/json"}

        # The Webex Teams POST JSON data
        # - "roomId" is is ID of the selected room
        # - "text": is the responseMessage assembled above
        postData = {"roomId": roomIdToGetMessages, "text": responseMessage}

        # Post the call to the Webex Teams message API.
        r = requests.post(
            "https://webexapis.com/v1/messages",
            data=json.dumps(postData),
            headers=postHTTPHeaders,
        )
        if not r.status_code == 200:
            raise Exception(
                "Incorrect reply from Webex Teams API. Status code: {}".format(r.status_code)
            )
        print("Message posted to the Webex Teams room.")

