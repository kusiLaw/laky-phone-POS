# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.1.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(434, 341)
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"font-size: 14pt; background : #2c313c; color:white")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header = QFrame(self.frame)
        self.header.setObjectName(u"header")
        self.header.setMaximumSize(QSize(16777215, 45))
        self.header.setStyleSheet(u"background-color:white;")
        self.header.setFrameShape(QFrame.NoFrame)
        self.header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.header)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.header)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_5)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(5, 0, 0, 0)
        self.label = QLabel(self.frame_5)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Segoe Script"])
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setLayoutDirection(Qt.RightToLeft)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet(u"font-size: 20px;\n"
"color :#568af2;\n"
"font-style:italic")
        self.label.setTextFormat(Qt.RichText)
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.label)


        self.horizontalLayout_2.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.header)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.frame_6)


        self.verticalLayout.addWidget(self.header)

        self.login = QFrame(self.frame)
        self.login.setObjectName(u"login")
        self.login.setMaximumSize(QSize(16777215, 45))
        self.login.setStyleSheet(u"/**background-color:#777**/\n"
"")
        self.login.setFrameShape(QFrame.StyledPanel)
        self.login.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.login)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.login)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 45))
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)


        self.verticalLayout.addWidget(self.login)

        self.content = QFrame(self.frame)
        self.content.setObjectName(u"content")
        self.content.setStyleSheet(u"background:red")
        self.content.setFrameShape(QFrame.StyledPanel)
        self.content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.content)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.login_form = QFrame(self.content)
        self.login_form.setObjectName(u"login_form")
        self.login_form.setStyleSheet(u"background:green")
        self.login_form.setFrameShape(QFrame.StyledPanel)
        self.login_form.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.login_form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_2 = QFrame(self.login_form)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background:white")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.frame_2, 0, 1, 1, 1)

        self.label_3 = QLabel(self.login_form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(120, 16777215))

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)

        self.label_4 = QLabel(self.login_form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(120, 16777215))

        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)

        self.frame_3 = QFrame(self.login_form)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"background:white")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.frame_3, 1, 1, 1, 1)


        self.verticalLayout_4.addWidget(self.login_form)

        self.buttons = QFrame(self.content)
        self.buttons.setObjectName(u"buttons")
        self.buttons.setMaximumSize(QSize(16777215, 45))
        self.buttons.setFrameShape(QFrame.NoFrame)
        self.buttons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.buttons)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.buttons)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_3.addWidget(self.frame_7)

        self.frame_4 = QFrame(self.buttons)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(150, 16777215))
        self.frame_4.setStyleSheet(u"background:white")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_3.addWidget(self.frame_4)


        self.verticalLayout_4.addWidget(self.buttons)


        self.verticalLayout.addWidget(self.content)

        self.status = QFrame(self.frame)
        self.status.setObjectName(u"status")
        self.status.setMaximumSize(QSize(16777215, 45))
        self.status.setStyleSheet(u"background-color:rgb(46, 46, 255)")
        self.status.setFrameShape(QFrame.StyledPanel)
        self.status.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.status)


        self.horizontalLayout.addWidget(self.frame)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"LAKY PHONE POS", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Login", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Username :", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Password:", None))
    # retranslateUi

