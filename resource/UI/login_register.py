# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_register.ui'
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
        #Form.setStyleSheet("QWidget#Form{\n"
#"    border-image: url(:/login_picture/image/login.png);\n"
#"}")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(370, 310, 491, 242))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setVerticalSpacing(20)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setMinimumSize(QtCore.QSize(0, 45))
        self.label.setStyleSheet("font: 20pt \"华文琥珀\";")
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.login_column = QtWidgets.QLineEdit(self.layoutWidget)
        self.login_column.setMinimumSize(QtCore.QSize(0, 45))
        self.login_column.setStyleSheet("background-color: transparent;\n"
"font: 16pt \"华文琥珀\";")
        self.login_column.setObjectName("login_column")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.login_column)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setMinimumSize(QtCore.QSize(0, 45))
        self.label_2.setStyleSheet("font: 20pt \"华文琥珀\";")
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.register_column = QtWidgets.QLineEdit(self.layoutWidget)
        self.register_column.setMinimumSize(QtCore.QSize(0, 45))
        self.register_column.setStyleSheet("background-color: transparent;\n"
"font: 16pt \"华文琥珀\";")
        self.register_column.setObjectName("register_column")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.register_column)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 45))
        self.pushButton.setStyleSheet("QPushButton{\n"
"    font: 20pt \"华文琥珀\";\n"
"}\n"
"QPushButton{\n"
"    background-color: rgb(235, 0, 0);\n"
"}\n"
"QPushButoon:hover{\n"
"    \n"
"    background-color: rgb(255, 255, 0);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(208, 0, 0)\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 45))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"    font: 20pt \"华文琥珀\";\n"
"}\n"
"QPushButton{\n"
"    background-color: rgb(235, 0, 0);\n"
"}\n"
"QPushButoon:hover{\n"
"    \n"
"    background-color: rgb(255, 255, 0);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(208, 0, 0)\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.pushButton_2)

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(Form.check_login)
        self.pushButton_2.clicked.connect(Form.check_register)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", " 账 号："))
        self.label_2.setText(_translate("Form", " 密 码："))
        self.pushButton.setText(_translate("Form", "登入"))
        self.pushButton_2.setText(_translate("Form", "注册"))
#import login_manager_rc
