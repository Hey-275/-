import requests
import json
def regiseterAndBind(account,jwc):
    url='http://www.revth.com:12300/auth/register2'
    form_data={
        "username": account["username"],
        "password": account["password"],
        "student_number":jwc["student_number"],
        "student_password":jwc["student_password"]
    }
    headers={
        "Content-Type":'application/json',
    }
    response=requests.post(url=url,headers=headers,data=json.dumps(form_data),verify=False);
    print(response.text)
    r = response.json()
    d = r["status"]
    return d
account={"username":"crj",'password':"1222crj+"}
jwc={"student_number":"031702320","student_password":"1222crj+"}
x = regiseterAndBind(account,jwc)
print(x)
