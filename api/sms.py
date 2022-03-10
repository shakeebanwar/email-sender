import requests
import json
from decouple import config

def sendsms(clientFirstName,clientNumber,compaignStatus = False,messageContent=""):
    smsurl = "https://api.directsms.com.au/s3/rest/sms/send"

    if not compaignStatus:
        messageContent = f'''
        Hi {clientFirstName},
        It’s been great working with you to get your health back on track!
        Do you know anyone else that would benefit from our services?
        Refer a friend to Evolution Medical Care & earn a $50 credit towards your next session!
        Click https://pycare.co NOW
        '''


    else:


        payload = json.dumps({
                            "messageType": "2-way",
                            "messageId": "ID112",
                            "senderId": "0417303105",
                            "messageText": messageContent,
                            "to": clientNumber,
        })

        headers = {
                'Content-Type': 'application/json',
                'Accept': 'application/json',
                'Username': config('smsUsername'),
                'Password': config('smsPassword')
        }


        
        response = requests.request("POST", smsurl, headers=headers, data=payload).json()
        if len(response) == 1:
            return f"sms send successful to {clientNumber}"
        
            
        else:
            return False