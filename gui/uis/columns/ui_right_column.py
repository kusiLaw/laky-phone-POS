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
        RightColumn.resize(261, 764)
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
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_2 = QScrollArea(self.setting_page)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scroll_content_area = QWidget()
        self.scroll_content_area.setObjectName(u"scroll_content_area")
        self.scroll_content_area.setGeometry(QRect(0, 0, 249, 752))
        self.horizontalLayout = QHBoxLayout(self.scroll_content_area)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frameContent = QFrame(self.scroll_content_area)
        self.frameContent.setObjectName(u"frameContent")
        self.frameContent.setFrameShape(QFrame.StyledPanel)
        self.frameContent.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frameContent)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.pic_frame_2 = QFrame(self.frameContent)
        self.pic_frame_2.setObjectName(u"pic_frame_2")
        self.pic_frame_2.setMinimumSize(QSize(0, 100))
        self.pic_frame_2.setMaximumSize(QSize(249, 180))
        self.pic_frame_2.setStyleSheet(u"background: green")
        self.pic_frame_2.setFrameShape(QFrame.NoFrame)
        self.pic_frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.pic_frame_2)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 15, 0, 0)
        self.pic_frame_inner_2 = QFrame(self.pic_frame_2)
        self.pic_frame_inner_2.setObjectName(u"pic_frame_inner_2")
        self.pic_frame_inner_2.setMaximumSize(QSize(238, 180))
        self.pic_frame_inner_2.setLayoutDirection(Qt.LeftToRight)
        self.pic_frame_inner_2.setAutoFillBackground(False)
        self.pic_frame_inner_2.setFrameShape(QFrame.NoFrame)
        self.pic_frame_inner_2.setFrameShadow(QFrame.Raised)
        self.pro_pic_frame_2 = QVBoxLayout(self.pic_frame_inner_2)
        self.pro_pic_frame_2.setSpacing(0)
        self.pro_pic_frame_2.setObjectName(u"pro_pic_frame_2")
        self.pro_pic_frame_2.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_9.addWidget(self.pic_frame_inner_2)


        self.verticalLayout_13.addWidget(self.pic_frame_2)


        self.horizontalLayout.addWidget(self.frameContent)

        self.scrollArea_2.setWidget(self.scroll_content_area)

        self.verticalLayout.addWidget(self.scrollArea_2)

        self.menus.addWidget(self.setting_page)
        self.profile_page = QWidget()
        self.profile_page.setObjectName(u"profile_page")
        self.profile_page.setStyleSheet(u"background: #2c313c")
        self.verticalLayout_8 = QVBoxLayout(self.profile_page)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.profile_page)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 251, 754))
        self.horizontalLayout_2 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(5, 0, 0, 0)
        self.frame = QFrame(self.scrollAreaWidgetContents)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(16777215, 600))
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 11, 0, 20)
        self.groupBox = QGroupBox(self.frame_5)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_5 = QVBoxLayout(self.groupBox)
        self.verticalLayout_5.setSpacing(15)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, 20, -1, 20)
        self.frame_11 = QFrame(self.groupBox)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMaximumSize(QSize(16777215, 20))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)

        self.verticalLayout_5.addWidget(self.frame_11)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_5.addWidget(self.label_7)

        self.frame_8 = QFrame(self.groupBox)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMaximumSize(QSize(16777215, 40))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.current_password_frame = QVBoxLayout(self.frame_8)
        self.current_password_frame.setSpacing(0)
        self.current_password_frame.setObjectName(u"current_password_frame")
        self.current_password_frame.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_5.addWidget(self.frame_8)

        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_5.addWidget(self.label_8)

        self.frame_9 = QFrame(self.groupBox)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMaximumSize(QSize(16777215, 40))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.new_password_frame = QVBoxLayout(self.frame_9)
        self.new_password_frame.setSpacing(0)
        self.new_password_frame.setObjectName(u"new_password_frame")
        self.new_password_frame.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_5.addWidget(self.frame_9)

        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_5.addWidget(self.label_9)

        self.frame_10 = QFrame(self.groupBox)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMaximumSize(QSize(16777215, 40))
        self.frame_10.setFrameShape(QFrame.NoFrame)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.confirm_password_frame = QVBoxLayout(self.frame_10)
        self.confirm_password_frame.setSpacing(0)
        self.confirm_password_frame.setObjectName(u"confirm_password_frame")
        self.confirm_password_frame.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_5.addWidget(self.frame_10)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)

        self.frame_12 = QFrame(self.groupBox)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMaximumSize(QSize(16777215, 40))
        self.frame_12.setFrameShape(QFrame.NoFrame)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.reset_password_frame = QVBoxLayout(self.frame_12)
        self.reset_password_frame.setSpacing(0)
        self.reset_password_frame.setObjectName(u"reset_password_frame")
        self.reset_password_frame.setContentsMargins(0, 2, 0, 0)

        self.verticalLayout_5.addWidget(self.frame_12)


        self.horizontalLayout_3.addWidget(self.groupBox)


        self.verticalLayout_2.addWidget(self.frame_5)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(16777215, 16777215))
        self.frame_4.setStyleSheet(u"")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setSpacing(5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 70, 0, 0)
        self.frame_6 = QFrame(self.frame_4)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(16777215, 40))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.sing_out_frame = QVBoxLayout(self.frame_6)
        self.sing_out_frame.setSpacing(0)
        self.sing_out_frame.setObjectName(u"sing_out_frame")
        self.sing_out_frame.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_4.addWidget(self.frame_6)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.frame_7 = QFrame(self.frame_4)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMaximumSize(QSize(16777215, 40))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.add_user_frame = QVBoxLayout(self.frame_7)
        self.add_user_frame.setSpacing(0)
        self.add_user_frame.setObjectName(u"add_user_frame")
        self.add_user_frame.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_4.addWidget(self.frame_7)


        self.verticalLayout_2.addWidget(self.frame_4)


        self.horizontalLayout_2.addWidget(self.frame)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_8.addWidget(self.scrollArea)

        self.menus.addWidget(self.profile_page)

        self.main_pages_layout.addWidget(self.menus)


        self.retranslateUi(RightColumn)

        self.menus.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(RightColumn)
    # setupUi

    def retranslateUi(self, RightColumn):
        RightColumn.setWindowTitle(QCoreApplication.translate("RightColumn", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("RightColumn", u"Reset password", None))
        self.label_7.setText(QCoreApplication.translate("RightColumn", u"Password:", None))
        self.label_8.setText(QCoreApplication.translate("RightColumn", u"New password:", None))
        self.label_9.setText(QCoreApplication.translate("RightColumn", u"Confirm Password :", None))
    # retranslateUi

