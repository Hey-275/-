# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'record.ui'
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
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(501, 702, 100, 50))
        self.label_9.setMinimumSize(QtCore.QSize(100, 50))
        self.label_9.setObjectName("label_9")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(590, 0, 191, 71))
        self.label.setMinimumSize(QtCore.QSize(0, 50))
        self.label.setStyleSheet("font: 36pt \"华文琥珀\";")
        self.label.setObjectName("label")
        self.back_button = QtWidgets.QPushButton(Form)
        self.back_button.setGeometry(QtCore.QRect(10, 20, 93, 28))
        self.back_button.setObjectName("back_button")
        self.refresh = QtWidgets.QPushButton(Form)
        self.refresh.setGeometry(QtCore.QRect(130, 550, 93, 28))
        self.refresh.setObjectName("refresh")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(330, 90, 750, 550))
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 2, item)

        self.retranslateUi(Form)
        self.back_button.clicked.connect(Form.return_to_user_platform)
        self.refresh.clicked.connect(Form.get_data)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_9.setText(_translate("Form", "TextLabel"))
        self.label.setText(_translate("Form", "排行榜"))
        self.back_button.setText(_translate("Form", "返回"))
        self.refresh.setText(_translate("Form", "刷新"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setHorizontalHeaderLabels(['玩家ID','玩家名','分数'])
        self.tableWidget.setColumnWidth(0,200)
        self.tableWidget.setColumnWidth(1, 200)
        self.tableWidget.setColumnWidth(2, 250)
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
