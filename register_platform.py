from PyQt5.Qt import *
from resource.UI.register import Ui_Form

class RegisterPlatform(QWidget,Ui_Form):
    return_to_login_signal = pyqtSignal()
    register_sinal = pyqtSignal(str,str,str,str)
    def __init__(self,parent = None,*args,**kwargs):
        super().__init__(parent,*args,**kwargs)
        self.setAttribute(Qt.WA_StyledBackground,True)
        self.setupUi(self)

    def return_to_login (self):
        self.return_to_login_signal.emit


    def register (self):
        UserName = self.user_name.text()
        PassWord = self.pass_word.text()
        StudentId = self.student_id.text()
        JwcPassWord = self.jwc_pass_word.text()
        #QMessageBox.about(self,"注册结果","注册按钮被点击了")
        self.register_sinal.emit(UserName,PassWord,StudentId,JwcPassWord)



if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = RegisterPlatform()

    window.register_sinal.connect(lambda a,b,c,d:print(a,b,c,d))

    window.show()

    sys.exit(app.exec_())