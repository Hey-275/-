import requests
import json
import numpy as np
def chupai(account,s):#出牌接口，分完牌后出牌
    url='http://api.revth.com/game/submit'
    t=np.array(s)
    form_data={
      "id": account["id"],
      "card": s[0:3]
    }
    headers={
        "X-Auth-Token":account["token"],
        "Content-Type":"application/json"
    }
    response=requests.post(url=url,headers=headers,data=json.dumps(form_data),verify=False);
    print(response.text)
    return response

# def postcards(cards):  # 出牌
#     global token, id
#     url = "http://api.revth.com/game/submit"
#     headers = {'content-type': "application/json"}
#     headers['X-Auth-Token'] = token
#     data = {'id': id}
#     print('出牌牌型:')
#     best_match = special_cards_type(cards)
#     if best_match[0]:
#         data['card'] = best_match[1]
#     else:
#         data['card'] = best_cards_type(cards)
#
#     res = requests.post(url, data=json.dumps(data), headers=headers)
#     info = res.json()
#     if info['status'] == 0:
#         print("出牌成功!")
#     else:
#         print(info)
#account={"username":"crj",'password':"1222crj+"}
#jwc={"student_number":"031702320","student_password":"1222crj+"}
#regiseterAndBind(account,jwc)

