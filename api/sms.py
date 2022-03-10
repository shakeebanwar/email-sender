import requests
import json


def sendsms(clientFirstName,clientNumber,compaignStatus = False):
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
        messageContent = '''Hey there,
heads up, I’ve been attending Evolution Medical Care to get my health back on track and they have been making such a big difference!🙌I 

I think that they can help you also! What’s more, they mentioned that if I sent you this invite, you will get a $50 discount off of your first session!👍
https://pycare.co

        ''' 




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
            'Username': 'evomedical',
            'Password': 'Marchon21'
    }

    response = requests.request("POST", smsurl, headers=headers, data=payload).json()
    if len(response) == 1:
        return f"sms send successful to {clientNumber}"
    
        
    else:
        return False