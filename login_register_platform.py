from PyQt5.Qt import *
from resource.UI.login_register import Ui_Form

class LoginRegisterPlatform(QWidget,Ui_Form):
    register_signal = pyqtSignal()
    login_signal = pyqtSignal()
    account_password_signal = pyqtSignal(str,str)
    def __init__(self,parent = None,*args,**kwargs):
        super().__init__(parent,*args,**kwargs)
        self.setAttribute(Qt.WA_StyledBackground,True)
        self.setupUi(self)

    def check_login(self):
        #print("登入")
        login_text = self.login_column.text()
        register_text = self.register_column.text()

        self.login_signal.emit()
        self.account_password_signal.emit(login_text,register_text)             #发射登入信号和登入是输入的账号密码
    def check_register(self):
        #print("注册")
        self.register_signal.emit()




if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = LoginRegisterPlatform()
    window.setObjectName("From")
    window.setStyleSheet("#From{border-image: url(resource/image/login.png);}")
    window.login_signal.connect(lambda : print("退出"))
    window.register_signal.connect(lambda: print("退出"))
    window.account_password_signal.connect(lambda a,p:print(a,p))
    window.show()

    sys.exit(app.exec_())