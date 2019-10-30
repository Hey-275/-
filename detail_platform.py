from PyQt5.Qt import *
from resource.UI.history_game_detail import Ui_Form


class DetailPlatform(QWidget, Ui_Form):
    get_data_signal = pyqtSignal(int)
    return_to_user_signal = pyqtSignal()

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setupUi(self)

    def return_to_user(self):
        self.return_to_user_signal.emit()

    def get_data(self):
        game_id = int(self.input_column.text())
        print(game_id)
        self.get_data_signal.emit(game_id)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    window = DetailPlatform()

    window.show()

    sys.exit(app.exec_())