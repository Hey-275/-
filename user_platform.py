from PyQt5.Qt import *
from resource.UI.user import Ui_Form

class UserPlatform(QWidget,Ui_Form):
    start_game_signal = pyqtSignal()
    go_to_rank_signal = pyqtSignal()
    go_to_list_signal = pyqtSignal()
    go_to_detail_signal = pyqtSignal()
    return_to_login_platform_signal = pyqtSignal()
    def __init__(self,parent = None,*args,**kwargs):
        super().__init__(parent,*args,**kwargs)
        self.setAttribute(Qt.WA_StyledBackground,True)
        self.setupUi(self)

    def start_game(self):
        self.start_game_signal.emit()

    def go_to_rank(self):
        self.go_to_rank_signal.emit()

    def go_to_list(self):
        self.go_to_list_signal.emit()

    def go_to_detail(self):
        self.go_to_detail_signal.emit()

    def return_to_login_platform(self):
        self.return_to_login_platform_signal.emit()



if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = UserPlatform()

    window.show()

    sys.exit(app.exec_())