# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'history_game_list.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1200, 675)
        Form.setMinimumSize(QtCore.QSize(1200, 675))
        Form.setMaximumSize(QtCore.QSize(1200, 675))
        self.history_game_list = QtWidgets.QTableWidget(Form)
        self.history_game_list.setGeometry(QtCore.QRect(330, 90, 750, 550))
        self.history_game_list.setObjectName("history_game_list")
        self.history_game_list.setColumnCount(4)
        self.history_game_list.setRowCount(5)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(520, 0, 371, 71))
        self.label.setStyleSheet("font: 36pt \"华文琥珀\";")
        self.label.setObjectName("label")
        self.input_column = QtWidgets.QLineEdit(Form)
        self.input_column.setGeometry(QtCore.QRect(80, 420, 113, 21))
        self.input_column.setObjectName("input_column")
        self.get_data_button = QtWidgets.QPushButton(Form)
        self.get_data_button.setGeometry(QtCore.QRect(90, 470, 93, 28))
        self.get_data_button.setObjectName("get_data_button")
        self.return_to_user_platform = QtWidgets.QPushButton(Form)
        self.return_to_user_platform.setGeometry(QtCore.QRect(10, 20, 93, 28))
        self.return_to_user_platform.setObjectName("return_to_user_platform")

        self.retranslateUi(Form)
        self.return_to_user_platform.clicked.connect(Form.return_to_user)
        self.get_data_button.clicked.connect(Form.get_data)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "历史战局列表"))
        self.get_data_button.setText(_translate("Form", "刷新数据"))
        self.return_to_user_platform.setText(_translate("Form", "返回"))
        self.history_game_list.setHorizontalHeaderLabels(['战局ID', '出牌情况', '分数变化','结算时间'])
        self.history_game_list.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.history_game_list.setColumnWidth(0,100)
        self.history_game_list.setColumnWidth(1, 350)
        self.history_game_list.setColumnWidth(2, 100)
        self.history_game_list.setColumnWidth(3, 120)
