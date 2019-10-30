from login_register_platform import LoginRegisterPlatform
from user_platform import UserPlatform
from record_platform import RecordPlatform
from game_platform import GamePlatform
from register_platform import RegisterPlatform
from list_platform import ListPlatform
from detail_platform import DetailPlatform
#以上是导入UI模块

from connector.sign_up import regiseterAndBind          #导入注册接口
from connector.Login import entry           #导入登入接口
from connector.asd import start             #导入开始游戏接口
from connector.lishizhanji import paihang   #导入排行榜接口
from connector.lishizhanji import see       #导入历史列表接口
from connector.lishizhanji import zhanju    #导入战局详情接口

from PyQt5.Qt import *

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    token = "a_random_string"

    window_login = LoginRegisterPlatform()              #创建登入界面
    window_login.setObjectName("Login")
    window_login.setStyleSheet("#Login{border-image: url(resource/image/login.png);}")


    window_register = RegisterPlatform()            #创建注册界面
    window_register.setObjectName("Register")
    window_register.setStyleSheet("#Register{border-image: url(resource/image/login.png);}")


    window_user = UserPlatform()            #创建用户界面
    window_user.setObjectName("User")
    window_user.setStyleSheet("#User{border-image: url(resource/image/user_background.jpg);}")
    window_user.head.setStyleSheet("border-image: url(resource/image/user_head.jpg)")


    window_game = GamePlatform()            #创建游戏界面
    window_game.setObjectName("Game")
    window_game.setStyleSheet("#Game{border-image: url(resource/image/record_background.jpg);}")
    window_game.head.setStyleSheet("border-image: url(resource/image/user_head.jpg)")


    window_record = RecordPlatform()            #创建排行榜界面
    window_record.setObjectName("Record")
    window_record.setStyleSheet("#Record{border-image: url(resource/image/record_background.jpg);}")

    window_list = ListPlatform()                #创建历史战局列表界面
    window_list.setObjectName("List")
    window_list.setStyleSheet("#List{border-image: url(resource/image/record_background.jpg);}")

    window_detail = DetailPlatform()                #创建历史战局详情界面
    window_detail.setObjectName("Detail")
    window_detail.setStyleSheet("#Detail{border-image: url(resource/image/record_background.jpg);}")




    def show_user_platform(login_text,register_text):           #由登入界面跳转到用户界面的函数
        account = {"username": login_text, "password": register_text}
        r = entry(account)
        flag = r["status"]
        print(flag)
        if (flag == 0):
            global token
            data = r["data"]
            token = data["token"]
            QMessageBox.about(window_login, "登入结果", "登入成功")
            window_user.show()
            window_login.hide()
        else:
            QMessageBox.about(window_login, "登入结果", "登入失败,账号或密码错误")

    #def show_login_platform_f_r():
        #print("回到登入界面")
        #window_login.show()
        #window_register.hide()

    def show_register_platform():
        print("展示注册界面")
        window_register.show()
        window_login.hide()

    def show_login_platform_f_u():
        print("展示登入平台")
        window_login.show()
        window_user.hide()

    def show_game_platform():  #由用户界面跳转到游戏界面的函数
        global token
        #print(token)
        r = start(token)
        flag = r["status"]
        data = r["data"]
        id = str(data["id"])
        #print(flag,data,id)
        if (flag == 0):
            window_user.hide()
            window_game.show()
            window_game.game_id.setText(id)
        else:
            QMessageBox.about(window_user, "开始游戏结果", "开始游戏失败，错误状态码："+flag)

    def show_record_platform():           #由用户界面跳转到排行榜界面的函数
        print("展示排行榜平台")
        window_record.show()
        window_user.hide()

    def show_list_platform():
        print("展示历史战局列表平台")
        window_list.show()
        window_user.hide()

    def show_detail_platform():
        print("展示历史战局详情平台")
        window_detail.show()
        window_user.hide()

    def show_user_platform_f_g():  # 由游戏界面跳转到用户界面的函数
        print("展示用户平台")
        window_user.show()
        window_game.hide()

    def show_user_platform_f_r():           #由排行榜界面跳转到用户界面的函数
        print("展示用户平台")
        window_user.show()
        window_record.hide()

    def show_user_platform_f_l():
        print("展示用户平台")
        window_user.show()
        window_list.hide()

    def show_user_platform_f_d():
        print("展示用户平台")
        window_user.show()
        window_detail.hide()

    def register(UserName,PassWord,StudentId,JwcPassWord):         #注册函数
        account = {"username": UserName, 'password': PassWord}
        jwc = {"student_number": StudentId, "student_password": JwcPassWord}
        flag = regiseterAndBind(account,jwc)
        if (flag == 0):
            QMessageBox.about(window_register, "注册结果", "注册成功")
            window_login.show()
            window_register.hide()
        elif (flag == 1002):
            QMessageBox.about(window_register, "注册结果", "学号已绑定")
            window_login.show()
            window_register.hide()
        elif (flag == 1003):
            QMessageBox.about(window_register, "注册结果", "教务处认证失败")
        else :
            QMessageBox.about(window_register, "注册结果", "注册失败")

    def record_get_data():          #获取排行榜
        r = paihang()
        x = len(r)
        window_record.tableWidget.setRowCount(x)
        for i in range(0,x):
            y = r[i]
            idItem = QTableWidgetItem(str(y["player_id"]))
            window_record.tableWidget.setItem(i,0,idItem)
            nameItem = QTableWidgetItem(y["name"])
            window_record.tableWidget.setItem(i, 1, nameItem)
            scoreItem = QTableWidgetItem(str(y["score"]))
            window_record.tableWidget.setItem(i, 2, scoreItem)
        #newItem = QTableWidgetItem('张三')
        #TableWidget.setItem(0, 0, newItem)

    def list_get_data(player_id):
        global token
        print(player_id)
        response = see(token,player_id)

        data = response["data"]
        lenth = len(data)
        window_list.history_game_list.setRowCount(lenth)
        for i in range(0,lenth):
            now_data = data[i]
            card_list = "".join(now_data["card"])
            id_Item = QTableWidgetItem(str(now_data["id"]))
            window_list.history_game_list.setItem(i, 0, id_Item)
            card_Item = QTableWidgetItem(card_list)
            window_list.history_game_list.setItem(i, 1, card_Item)
            score_Item = QTableWidgetItem(str(now_data["score"]))
            window_list.history_game_list.setItem(i, 2, score_Item)
            timestamp_Item = QTableWidgetItem(str(now_data["timestamp"]))
            window_list.history_game_list.setItem(i, 3, timestamp_Item)

    def detail_get_data(game_id):
        global token
        response = zhanju(token,game_id)
        data = response["data"]
        detail = data["detail"]
        lenth = len(detail)
        window_detail.history_game_detail.setRowCount(lenth)
        for i in range(0,lenth):
            now_detail = detail[i]
            card_list = "".join(now_detail["card"])
            game_id_Item = QTableWidgetItem(str(data["id"]))
            window_detail.history_game_detail.setItem(i,0,game_id_Item)
            player_id_Item = QTableWidgetItem(str(now_detail["player_id"]))
            window_detail.history_game_detail.setItem(i, 1, player_id_Item)
            name_Item = QTableWidgetItem(now_detail["name"])
            window_detail.history_game_detail.setItem(i, 2, name_Item)
            card_Item = QTableWidgetItem(card_list)
            window_detail.history_game_detail.setItem(i, 3, card_Item)
            score_Item = QTableWidgetItem(str(now_detail["score"]))
            window_detail.history_game_detail.setItem(i, 4, score_Item)

    window_login.account_password_signal.connect(show_user_platform)                           #登入界面中连接跳转到用户界面的函数
    window_login.register_signal.connect(show_register_platform)                    #登入界面到注册界面的连接
    #window_register.return_to_login_signal.connect(show_login_platform_f_r)        #注册界面回到登入界面
    window_user.return_to_login_platform_signal.connect(show_login_platform_f_u)     #自己看函数名
    window_user.start_game_signal.connect(show_game_platform)                       #用户界面中连接跳转到游戏界面的函数
    window_user.go_to_rank_signal.connect(show_record_platform)                     #用户界面中连接跳转到排行榜界面的函数
    window_user.go_to_list_signal.connect(show_list_platform)
    window_user.go_to_detail_signal.connect(show_detail_platform)
    window_game.return_to_user_platform_signal.connect(show_user_platform_f_g)       #游戏界面中连接跳转到用户界面的函数
    window_record.return_to_user_platform_signal.connect(show_user_platform_f_r)     #排行榜界面中连接跳转到用户界面的函数
    window_list.return_to_user_signal.connect(show_user_platform_f_l)
    window_detail.return_to_user_signal.connect(show_user_platform_f_d)
    window_register.register_sinal.connect(register)                                  #连接向服务器发送注册信息的函数
    window_record.get_data_signal.connect(record_get_data)             #更新排行榜数据
    window_list.get_data_signal.connect(list_get_data)                 #更新历史列表数据
    window_detail.get_data_signal.connect(detail_get_data)             #更新战局详情列表


    window_login.show()


    sys.exit(app.exec_())