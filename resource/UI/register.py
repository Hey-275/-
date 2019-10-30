# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register.ui'
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
        self.register_2 = QtWidgets.QPushButton(Form)
        self.register_2.setGeometry(QtCore.QRect(350, 490, 501, 61))
        self.register_2.setStyleSheet("font: 22pt \"华文琥珀\";\n"
"background-color: rgb(255, 0, 0);")
        self.register_2.setObjectName("register_2")
        self.return_button = QtWidgets.QPushButton(Form)
        self.return_button.setGeometry(QtCore.QRect(20, 40, 111, 51))
        self.return_button.setStyleSheet("font: 22pt \"华文琥珀\";\n"
"background-color: rgb(255, 0, 0);")
        self.return_button.setObjectName("return_button")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(330, 200, 531, 242))
        self.widget.setMinimumSize(QtCore.QSize(0, 45))
        self.widget.setObjectName("widget")
        self.formLayout = QtWidgets.QFormLayout(self.widget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setVerticalSpacing(20)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setMinimumSize(QtCore.QSize(0, 45))
        self.label.setStyleSheet("font: 18pt \"华文琥珀\";")
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.user_name = QtWidgets.QLineEdit(self.widget)
        self.user_name.setMinimumSize(QtCore.QSize(0, 45))
        self.user_name.setStyleSheet("font: 22pt \"华文琥珀\";\n"
"background-color : transparent ;")
        self.user_name.setObjectName("user_name")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.user_name)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setMinimumSize(QtCore.QSize(0, 45))
        self.label_2.setStyleSheet("font: 18pt \"华文琥珀\";")
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.pass_word = QtWidgets.QLineEdit(self.widget)
        self.pass_word.setMinimumSize(QtCore.QSize(0, 45))
        self.pass_word.setStyleSheet("font: 22pt \"华文琥珀\";\n"
"background-color : transparent ;")
        self.pass_word.setObjectName("pass_word")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.pass_word)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setMinimumSize(QtCore.QSize(0, 45))
        self.label_3.setStyleSheet("font: 18pt \"华文琥珀\";")
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.student_id = QtWidgets.QLineEdit(self.widget)
        self.student_id.setMinimumSize(QtCore.QSize(0, 45))
        self.student_id.setStyleSheet("font: 22pt \"华文琥珀\";\n"
"background-color : transparent ;")
        self.student_id.setObjectName("student_id")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.student_id)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setMinimumSize(QtCore.QSize(0, 45))
        self.label_4.setStyleSheet("font: 18pt \"华文琥珀\";")
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.jwc_pass_word = QtWidgets.QLineEdit(self.widget)
        self.jwc_pass_word.setMinimumSize(QtCore.QSize(0, 45))
        self.jwc_pass_word.setStyleSheet("font: 22pt \"华文琥珀\";\n"
"background-color : transparent ;")
        self.jwc_pass_word.setObjectName("jwc_pass_word")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.jwc_pass_word)

        self.retranslateUi(Form)
        self.return_button.clicked.connect(Form.return_to_login)
        self.register_2.clicked.connect(Form.register)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.register_2.setText(_translate("Form", "注册"))
        self.return_button.setText(_translate("Form", "返回"))
        self.label.setText(_translate("Form", "账号"))
        self.label_2.setText(_translate("Form", "密码"))
        self.label_3.setText(_translate("Form", "学号"))
        self.label_4.setText(_translate("Form", "教务处密码"))
