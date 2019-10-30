import requests
import json
i=0
def see(token,player_id):#查看历史记录，返回为json数组
    global i
    url='http://api.revth.com/history'
    data={
        "player_id":player_id,
        "limit":20,
        "page":i
    }
    i=i+1
    headers={
        "X-Auth-Token":token
    }
    response=requests.get(url=url,headers=headers,data=data)
    print(response.text)
    return response.json()

def paihang():#查看排行榜，返回值为json数组
    url='http://api.revth.com/rank'
    response=requests.get(url=url)
    r = response.json()
    return r

def zhanju(token,id):#查看历史战局详情，参数为房间号，返回值为json数组，详细见十三水api
    url="http://api.revth.com/history/"+str(id)
    headers = {
        "X-Auth-Token": token
    }
    response = requests.get(url=url,headers=headers)
    return response.json()

# token = "1da4fb48-3d4c-4afd-ac80-6604e1dd5e21"
# id = 60255
# response = zhanju(token,id)
# print(response)
# data = response["data"]
# print(data)
# detail = data["detail"]
# print(detail)
# lenth = len(detail)
# print(lenth)
# now_detail = detail[0]
# print(now_detail)
# card_list = "".join(now_detail["card"])
# print(card_list)
