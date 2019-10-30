import requests
import json
def  entry(account):
    url='http://api.revth.com/auth/login'
    data={
        "username": account["username"],
        "password": account["password"]
    }
    headers={
        "Content-Type":"application/json"
    }
    response=requests.post(url=url,headers=headers,data=json.dumps(data),verify=False);
    print(response.text)
    r = response.json()
    return r

def decode_data(response):#解码
    r = response.json()
    d = r["data"]
    print(d)
    return d
account={"username":"wangqin","password":"wq110919."}
x = entry(account)



