from PyQt5.Qt import *
from resource.UI.game import Ui_Form

class GamePlatform(QWidget,Ui_Form):
    return_to_user_platform_signal = pyqtSignal()
    show_poker_signal = pyqtSignal()
    def __init__(self,parent = None,*args,**kwargs):
        super().__init__(parent,*args,**kwargs)
        self.setAttribute(Qt.WA_StyledBackground,True)
        self.setupUi(self)

    def return_to_user_platform(self):
        self.return_to_user_platform_signal.emit()

    def show_poker(self):
        self.show_poker_signal.emit()


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = GamePlatform()

    window.show()

    sys.exit(app.exec_())