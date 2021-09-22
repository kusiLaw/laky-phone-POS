# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'right_column.ui'
##
## Created by: Qt User Interface Compiler version 6.1.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_RightColumn(object):
    def setupUi(self, RightColumn):
        if not RightColumn.objectName():
            RightColumn.setObjectName(u"RightColumn")
        RightColumn.resize(269, 600)
        RightColumn.setMaximumSize(QSize(269, 16777215))
        self.main_pages_layout = QVBoxLayout(RightColumn)
        self.main_pages_layout.setSpacing(0)
        self.main_pages_layout.setObjectName(u"main_pages_layout")
        self.main_pages_layout.setContentsMargins(5, 5, 5, 5)
        self.menus = QStackedWidget(RightColumn)
        self.menus.setObjectName(u"menus")
        self.menus.setStyleSheet(u"font: 14pt \"Microsoft Sans Serif\";")
        self.setting_page = QWidget()
        self.setting_page.setObjectName(u"setting_page")
        self.verticalLayout = QVBoxLayout(self.setting_page)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.label_1 = QLabel(self.setting_page)
        self.label_1.setObjectName(u"label_1")
        font = QFont()
        font.setFamilies([u"Microsoft Sans Serif"])
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        self.label_1.setFont(font)
        self.label_1.setStyleSheet(u"font-size: 16pt")
        self.label_1.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_1)

        self.menus.addWidget(self.setting_page)
        self.profile_page = QWidget()
        self.profile_page.setObjectName(u"profile_page")
        self.verticalLayout_2 = QVBoxLayout(self.profile_page)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 0, 5, 5)
        self.pic_frame = QFrame(self.profile_page)
        self.pic_frame.setObjectName(u"pic_frame")
        self.pic_frame.setMinimumSize(QSize(0, 100))
        self.pic_frame.setMaximumSize(QSize(249, 180))
        self.pic_frame.setStyleSheet(u"")
        self.pic_frame.setFrameShape(QFrame.NoFrame)
        self.pic_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.pic_frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 15, 0, 0)
        self.pic_frame_inner = QFrame(self.pic_frame)
        self.pic_frame_inner.setObjectName(u"pic_frame_inner")
        self.pic_frame_inner.setMaximumSize(QSize(238, 180))
        self.pic_frame_inner.setLayoutDirection(Qt.LeftToRight)
        self.pic_frame_inner.setAutoFillBackground(False)
        self.pic_frame_inner.setFrameShape(QFrame.NoFrame)
        self.pic_frame_inner.setFrameShadow(QFrame.Raised)
        self.pro_pic_frame = QVBoxLayout(self.pic_frame_inner)
        self.pro_pic_frame.setSpacing(0)
        self.pro_pic_frame.setObjectName(u"pro_pic_frame")
        self.pro_pic_frame.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_3.addWidget(self.pic_frame_inner)


        self.verticalLayout_2.addWidget(self.pic_frame)

        self.user_content_frame = QFrame(self.profile_page)
        self.user_content_frame.setObjectName(u"user_content_frame")
        self.user_content_frame.setFrameShape(QFrame.StyledPanel)
        self.user_content_frame.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.user_content_frame)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.user_content_frame)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.label_2 = QLabel(self.user_content_frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setWordWrap(True)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.label_3 = QLabel(self.user_content_frame)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.label_4 = QLabel(self.user_content_frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setScaledContents(False)
        self.label_4.setWordWrap(True)

        self.formLayout.setWidget(4, QFormLayout.SpanningRole, self.label_4)

        self.label_5 = QLabel(self.user_content_frame)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_5)

        self.label_6 = QLabel(self.user_content_frame)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_6)


        self.verticalLayout_2.addWidget(self.user_content_frame)

        self.change_password_frame = QFrame(self.profile_page)
        self.change_password_frame.setObjectName(u"change_password_frame")
        self.change_password_frame.setMinimumSize(QSize(0, 200))
        self.change_password_frame.setFrameShape(QFrame.StyledPanel)
        self.change_password_frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.change_password_frame)

        self.menus.addWidget(self.profile_page)

        self.main_pages_layout.addWidget(self.menus)


        self.retranslateUi(RightColumn)

        self.menus.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(RightColumn)
    # setupUi

    def retranslateUi(self, RightColumn):
        RightColumn.setWindowTitle(QCoreApplication.translate("RightColumn", u"Form", None))
        self.label_1.setText(QCoreApplication.translate("RightColumn", u"Menu 1 - Right Menu", None))
        self.label.setText(QCoreApplication.translate("RightColumn", u"Name :", None))
        self.label_2.setText(QCoreApplication.translate("RightColumn", u"Lawrence Addai kusi", None))
        self.label_3.setText(QCoreApplication.translate("RightColumn", u"Email : ", None))
        self.label_4.setText(QCoreApplication.translate("RightColumn", u"lawcubegsm@gmail.com", None))
        self.label_5.setText(QCoreApplication.translate("RightColumn", u"Last seen :", None))
        self.label_6.setText(QCoreApplication.translate("RightColumn", u"27th oct 2021", None))
    # retranslateUi

