from PyQt5.Qt import *
from resource.UI.history_game_list import Ui_Form
import requests
import json

class ListPlatform(QWidget,Ui_Form):
    get_data_signal = pyqtSignal(int)
    return_to_user_signal = pyqtSignal()

    def __init__(self,parent = None,*args,**kwargs):
        super().__init__(parent,*args,**kwargs)
        self.setAttribute(Qt.WA_StyledBackground,True)
        self.setupUi(self)

    def return_to_user(self):
        self.return_to_user_signal.emit()
    
    def get_data(self):
        player_id = int(self.input_column.text())
        self.get_data_signal.emit(player_id)
        #print(player_id)



if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = ListPlatform()

    def see(token,player_id):  # 查看历史记录，返回为json数组
        url = 'http://api.revth.com/history'
        data = {
            "player_id": player_id,
            "limit": 20,
            "page": 20
        }
        headers = {
            "X-Auth-Token": token
        }
        response = requests.get(url=url, headers=headers, data=data)
        #print(response.text)
        return response.json()

    token = "58f38d29-2589-44a9-badc-1ff79463ecab"
    window.input_column.setText("24")
    player_id = int(window.input_column.text())
    response = see(token,player_id)
    data = response["data"]
    lenth = len(data)
    window.history_game_list.setRowCount(lenth)
    for i in range(0, lenth):
        now_data = data[i]
        card_list = "".join(now_data["card"])
        id_Item = QTableWidgetItem(str(now_data["id"]))
        window.history_game_list.setItem(i, 0, id_Item)
        card_Item = QTableWidgetItem(card_list)
        window.history_game_list.setItem(i, 1, card_Item)
        score_Item = QTableWidgetItem(str(now_data["score"]))
        window.history_game_list.setItem(i, 2, score_Item)
        timestamp_Item = QTableWidgetItem(str(now_data["timestamp"]))
        window.history_game_list.setItem(i, 3, timestamp_Item)

    window.show()

    sys.exit(app.exec_())