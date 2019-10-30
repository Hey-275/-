# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'user.ui'
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
        Form.setStyleSheet("")
        self.head = QtWidgets.QPushButton(Form)
        self.head.setGeometry(QtCore.QRect(520, 140, 141, 141))
        self.head.setStyleSheet("")
        self.head.setText("")
        self.head.setObjectName("head")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(430, 330, 364, 225))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(320, 50))
        self.pushButton_2.setMaximumSize(QtCore.QSize(90, 50))
        self.pushButton_2.setStyleSheet("font: 22pt \"华文琥珀\";\n"
"background-color: rgb(255, 255, 0);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_3.setMinimumSize(QtCore.QSize(320, 50))
        self.pushButton_3.setMaximumSize(QtCore.QSize(90, 50))
        self.pushButton_3.setStyleSheet("font: 22pt \"华文琥珀\";\n"
"background-color: rgb(255, 255, 0);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.pushButton_4 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_4.setMinimumSize(QtCore.QSize(320, 50))
        self.pushButton_4.setMaximumSize(QtCore.QSize(90, 50))
        self.pushButton_4.setStyleSheet("font: 22pt \"华文琥珀\";\n"
"background-color: rgb(255, 255, 0);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_2.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_5.setMinimumSize(QtCore.QSize(320, 50))
        self.pushButton_5.setMaximumSize(QtCore.QSize(90, 50))
        self.pushButton_5.setStyleSheet("font: 22pt \"华文琥珀\";\n"
"background-color: rgb(255, 255, 0);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_2.addWidget(self.pushButton_5)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(40, 30, 93, 40))
        self.pushButton.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton.setMaximumSize(QtCore.QSize(16777215, 40))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        self.pushButton_2.clicked.connect(Form.start_game)
        self.pushButton_3.clicked.connect(Form.go_to_rank)
        self.pushButton_4.clicked.connect(Form.go_to_list)
        self.pushButton_5.clicked.connect(Form.go_to_detail)
        self.pushButton.clicked.connect(Form.return_to_login_platform)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_2.setText(_translate("Form", "开始游戏"))
        self.pushButton_3.setText(_translate("Form", "排行榜"))
        self.pushButton_4.setText(_translate("Form", "历史战局列表"))
        self.pushButton_5.setText(_translate("Form", "历史战局详情"))
        self.pushButton.setText(_translate("Form", "退出登入"))

