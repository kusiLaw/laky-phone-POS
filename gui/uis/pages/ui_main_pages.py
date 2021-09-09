# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_pages.ui'
##
## Created by: Qt User Interface Compiler version 6.1.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_MainPages(object):
    def setupUi(self, MainPages):
        if not MainPages.objectName():
            MainPages.setObjectName(u"MainPages")
        MainPages.resize(860, 601)
        self.main_pages_layout = QVBoxLayout(MainPages)
        self.main_pages_layout.setSpacing(0)
        self.main_pages_layout.setObjectName(u"main_pages_layout")
        self.main_pages_layout.setContentsMargins(0, 0, 5, 5)
        self.pages = QStackedWidget(MainPages)
        self.pages.setObjectName(u"pages")
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        self.home_page.setStyleSheet(u"font-size: 14pt; background: white; ")
        self.page_1_layout = QVBoxLayout(self.home_page)
        self.page_1_layout.setSpacing(5)
        self.page_1_layout.setObjectName(u"page_1_layout")
        self.page_1_layout.setContentsMargins(5, 5, 5, 5)
        self.frame_3 = QFrame(self.home_page)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)

        self.page_1_layout.addWidget(self.frame_3)

        self.frame_2 = QFrame(self.home_page)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.logo_layout = QVBoxLayout(self.frame_4)
        self.logo_layout.setObjectName(u"logo_layout")
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.logo_layout.addWidget(self.label)


        self.verticalLayout.addWidget(self.frame_4)


        self.page_1_layout.addWidget(self.frame_2)

        self.frame = QFrame(self.home_page)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.page_1_layout.addWidget(self.frame)

        self.pages.addWidget(self.home_page)
        self.phone_page = QWidget()
        self.phone_page.setObjectName(u"phone_page")
        self.phone_page.setStyleSheet(u"font-size: 14pt; background: yellow; ")
        self.verticalLayout_3 = QVBoxLayout(self.phone_page)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.phone_page)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.contents = QWidget()
        self.contents.setObjectName(u"contents")
        self.contents.setGeometry(QRect(0, 0, 855, 596))
        self.verticalLayout_4 = QVBoxLayout(self.contents)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.phone_bg_layout = QFrame(self.contents)
        self.phone_bg_layout.setObjectName(u"phone_bg_layout")
        self.phone_bg_layout.setFrameShape(QFrame.NoFrame)
        self.phone_bg_layout.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.phone_bg_layout)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.phone_forms = QFrame(self.phone_bg_layout)
        self.phone_forms.setObjectName(u"phone_forms")
        self.phone_forms.setFrameShape(QFrame.StyledPanel)
        self.phone_forms.setFrameShadow(QFrame.Raised)

        self.verticalLayout_5.addWidget(self.phone_forms)

        self.phone_buttons = QFrame(self.phone_bg_layout)
        self.phone_buttons.setObjectName(u"phone_buttons")
        self.phone_buttons.setFrameShape(QFrame.StyledPanel)
        self.phone_buttons.setFrameShadow(QFrame.Raised)

        self.verticalLayout_5.addWidget(self.phone_buttons)

        self.phone_table = QFrame(self.phone_bg_layout)
        self.phone_table.setObjectName(u"phone_table")
        self.phone_table.setFrameShape(QFrame.StyledPanel)
        self.phone_table.setFrameShadow(QFrame.Raised)

        self.verticalLayout_5.addWidget(self.phone_table)


        self.verticalLayout_4.addWidget(self.phone_bg_layout)

        self.scrollArea.setWidget(self.contents)

        self.verticalLayout_3.addWidget(self.scrollArea)

        self.pages.addWidget(self.phone_page)
        self.service_page = QWidget()
        self.service_page.setObjectName(u"service_page")
        self.service_page.setStyleSheet(u"font-size: 14pt; background: lightblue; ")
        self.page_2_layout = QVBoxLayout(self.service_page)
        self.page_2_layout.setSpacing(5)
        self.page_2_layout.setObjectName(u"page_2_layout")
        self.page_2_layout.setContentsMargins(5, 5, 5, 5)
        self.frame_6 = QFrame(self.service_page)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tableView = QTableView(self.frame_6)
        self.tableView.setObjectName(u"tableView")

        self.verticalLayout_2.addWidget(self.tableView)


        self.page_2_layout.addWidget(self.frame_6)

        self.frame_5 = QFrame(self.service_page)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.table_layout = QVBoxLayout(self.frame_5)
        self.table_layout.setObjectName(u"table_layout")
        self.frame_7 = QFrame(self.frame_5)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Raised)

        self.table_layout.addWidget(self.frame_7)


        self.page_2_layout.addWidget(self.frame_5)

        self.pages.addWidget(self.service_page)
        self.stock = QWidget()
        self.stock.setObjectName(u"stock")
        self.stock.setStyleSheet(u"QFrame {\n"
"	font-size: 16pt; background-color:lightyellow;\n"
"}")
        self.page_3_layout = QVBoxLayout(self.stock)
        self.page_3_layout.setObjectName(u"page_3_layout")
        self.empty_page_label = QLabel(self.stock)
        self.empty_page_label.setObjectName(u"empty_page_label")
        font = QFont()
        font.setPointSize(16)
        self.empty_page_label.setFont(font)
        self.empty_page_label.setAlignment(Qt.AlignCenter)

        self.page_3_layout.addWidget(self.empty_page_label)

        self.pages.addWidget(self.stock)

        self.main_pages_layout.addWidget(self.pages)


        self.retranslateUi(MainPages)

        self.pages.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainPages)
    # setupUi

    def retranslateUi(self, MainPages):
        MainPages.setWindowTitle(QCoreApplication.translate("MainPages", u"Form", None))
        self.label.setText(QCoreApplication.translate("MainPages", u"HOME PAGE", None))
        self.empty_page_label.setText(QCoreApplication.translate("MainPages", u"Empty Page", None))
    # retranslateUi

