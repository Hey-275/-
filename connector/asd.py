import requests
import json
def  start(token):
    url='http://api.revth.com/game/open'
    headers={
        "X-Auth-Token":token
    }
    response=requests.post(url=url,headers=headers,verify=False);
    #print(response.text)
    r = response.json()
    return r

token = "e206bb94-bcb4-4eff-88b5-0adcc7bad3f3"
x = start(token)

