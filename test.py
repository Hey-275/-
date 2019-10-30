import requests
import json
def paihang():#查看排行榜，返回值为json数组
    url='http://api.revth.com/rank'
    response=requests.get(url=url)
    #print(response.text)
    r = response.json()
    print(r)
    return r

def see(token):#查看历史记录，返回为json数组
    url='http://api.revth.com/history'
    data={
        "player_id":24,
        "limit":20,
        "page":20
    }
    headers={
        "X-Auth-Token":token
    }
    response=requests.get(url=url,headers=headers,data=data)
    #print(response.text)
    return response.json()



