from PyQt5.Qt import *
from resource.UI.record import Ui_Form

import requests
import json

class RecordPlatform(QWidget,Ui_Form):
    return_to_user_platform_signal = pyqtSignal()
    get_data_signal = pyqtSignal()
    def __init__(self,parent = None,*args,**kwargs):
        super().__init__(parent,*args,**kwargs)
        self.setAttribute(Qt.WA_StyledBackground,True)
        self.setupUi(self)

    def return_to_user_platform(self):
        self.return_to_user_platform_signal.emit()

    def get_data(self):
        self.get_data_signal.emit()


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = RecordPlatform()

    def paihang():  # 查看排行榜，返回值为json数组
        url = 'http://api.revth.com/rank'
        response = requests.get(url=url)
        # print(response.text)
        r = response.json()
        print(r)
        return r

    x = paihang()
    l = len(x)
    window.tableWidget.setRowCount(l)
    for i in range(0, l):
        y = x[i]
        #print(y)
        idItem = QTableWidgetItem(str(y["player_id"]))
        window.tableWidget.setItem(i, 0, idItem)
        nameItem = QTableWidgetItem(y["name"])
        window.tableWidget.setItem(i, 1, nameItem)
        scoreItem = QTableWidgetItem(str(y["score"]))
        window.tableWidget.setItem(i, 2, scoreItem)

    window.show()

    sys.exit(app.exec_())