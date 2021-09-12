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
        MainPages.resize(961, 613)
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
        self.phone_page.setStyleSheet(u"font-size: 14pt; background:rgb(255, 110, 243); ")
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
        self.contents.setGeometry(QRect(0, 0, 956, 608))
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
        self.phone_form_section = QFrame(self.phone_bg_layout)
        self.phone_form_section.setObjectName(u"phone_form_section")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.phone_form_section.sizePolicy().hasHeightForWidth())
        self.phone_form_section.setSizePolicy(sizePolicy)
        self.phone_form_section.setMinimumSize(QSize(934, 191))
        self.phone_form_section.setMaximumSize(QSize(16777215, 16777215))
        self.phone_form_section.setStyleSheet(u"background: rgb(29, 59, 0)")
        self.phone_form_section.setFrameShape(QFrame.StyledPanel)
        self.phone_form_section.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.phone_form_section)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.phoneform_customer_section = QFrame(self.phone_form_section)
        self.phoneform_customer_section.setObjectName(u"phoneform_customer_section")
        sizePolicy.setHeightForWidth(self.phoneform_customer_section.sizePolicy().hasHeightForWidth())
        self.phoneform_customer_section.setSizePolicy(sizePolicy)
        self.phoneform_customer_section.setMinimumSize(QSize(280, 0))
        self.phoneform_customer_section.setMaximumSize(QSize(600, 16777215))
        self.phoneform_customer_section.setStyleSheet(u"background: rgb(82, 52, 255)")
        self.phoneform_customer_section.setFrameShape(QFrame.NoFrame)
        self.phoneform_customer_section.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.phoneform_customer_section)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 5, 0)
        self.customer_group = QGroupBox(self.phoneform_customer_section)
        self.customer_group.setObjectName(u"customer_group")
        self.formLayout = QFormLayout(self.customer_group)
        self.formLayout.setObjectName(u"formLayout")
        self.label_3 = QLabel(self.customer_group)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.frame_10 = QFrame(self.customer_group)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setStyleSheet(u"background: rgb(255, 255, 255)")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.frame_10)

        self.label_2 = QLabel(self.customer_group)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_2)

        self.frame_11 = QFrame(self.customer_group)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setStyleSheet(u"background: rgb(255, 255, 255)")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.frame_11)

        self.label_4 = QLabel(self.customer_group)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_4)

        self.frame_8 = QFrame(self.customer_group)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.frame_8)

        self.frame_21 = QFrame(self.customer_group)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setStyleSheet(u"background:rgb(255, 255, 255);")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.frame_21)


        self.verticalLayout_6.addWidget(self.customer_group)


        self.horizontalLayout.addWidget(self.phoneform_customer_section)

        self.phoneform_phone_section = QFrame(self.phone_form_section)
        self.phoneform_phone_section.setObjectName(u"phoneform_phone_section")
        self.phoneform_phone_section.setMinimumSize(QSize(318, 0))
        self.phoneform_phone_section.setMaximumSize(QSize(600, 16777215))
        self.phoneform_phone_section.setStyleSheet(u"background:rgb(30, 188, 255)")
        self.phoneform_phone_section.setFrameShape(QFrame.StyledPanel)
        self.phoneform_phone_section.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.phoneform_phone_section)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(5, 0, 5, 0)
        self.phone_group = QGroupBox(self.phoneform_phone_section)
        self.phone_group.setObjectName(u"phone_group")
        self.formLayout_2 = QFormLayout(self.phone_group)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_5 = QLabel(self.phone_group)
        self.label_5.setObjectName(u"label_5")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_5)

        self.frame_22 = QFrame(self.phone_group)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setStyleSheet(u"background:rgb(255, 255, 255);")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.frame_22)

        self.label_6 = QLabel(self.phone_group)
        self.label_6.setObjectName(u"label_6")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_6)

        self.label_7 = QLabel(self.phone_group)
        self.label_7.setObjectName(u"label_7")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_7)

        self.label_8 = QLabel(self.phone_group)
        self.label_8.setObjectName(u"label_8")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.label_8)

        self.frame_23 = QFrame(self.phone_group)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setStyleSheet(u"background:rgb(255, 255, 255);")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.frame_23)

        self.frame_24 = QFrame(self.phone_group)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setStyleSheet(u"background:rgb(255, 255, 255);")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.frame_24)

        self.frame_25 = QFrame(self.phone_group)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setStyleSheet(u"background:rgb(255, 255, 255);")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.frame_25)


        self.verticalLayout_7.addWidget(self.phone_group)


        self.horizontalLayout.addWidget(self.phoneform_phone_section)

        self.frame_9 = QFrame(self.phone_form_section)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(318, 0))
        self.frame_9.setMaximumSize(QSize(600, 16777215))
        self.frame_9.setStyleSheet(u"background:rgb(17, 255, 84);")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_9)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(5, 0, 5, 0)
        self.cost_group = QGroupBox(self.frame_9)
        self.cost_group.setObjectName(u"cost_group")
        self.formLayout_3 = QFormLayout(self.cost_group)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.label_9 = QLabel(self.cost_group)
        self.label_9.setObjectName(u"label_9")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_9)

        self.label_10 = QLabel(self.cost_group)
        self.label_10.setObjectName(u"label_10")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_10)

        self.label_11 = QLabel(self.cost_group)
        self.label_11.setObjectName(u"label_11")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.label_11)

        self.label_12 = QLabel(self.cost_group)
        self.label_12.setObjectName(u"label_12")

        self.formLayout_3.setWidget(3, QFormLayout.LabelRole, self.label_12)

        self.frame_26 = QFrame(self.cost_group)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setStyleSheet(u"background:rgb(255, 255, 255);")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.frame_26)

        self.frame_27 = QFrame(self.cost_group)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setStyleSheet(u"background:rgb(255, 255, 255);")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.frame_27)

        self.frame_28 = QFrame(self.cost_group)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setStyleSheet(u"background:rgb(255, 255, 255);")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.frame_28)

        self.frame_29 = QFrame(self.cost_group)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setStyleSheet(u"background:rgb(255, 255, 255);")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)

        self.formLayout_3.setWidget(3, QFormLayout.FieldRole, self.frame_29)


        self.verticalLayout_8.addWidget(self.cost_group)


        self.horizontalLayout.addWidget(self.frame_9)


        self.verticalLayout_5.addWidget(self.phone_form_section)

        self.phone_cart_button_section = QFrame(self.phone_bg_layout)
        self.phone_cart_button_section.setObjectName(u"phone_cart_button_section")
        self.phone_cart_button_section.setMinimumSize(QSize(934, 190))
        self.phone_cart_button_section.setMaximumSize(QSize(16777215, 16777215))
        self.phone_cart_button_section.setStyleSheet(u"background: rgb(29, 100, 100)")
        self.phone_cart_button_section.setFrameShape(QFrame.NoFrame)
        self.phone_cart_button_section.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.phone_cart_button_section)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, -1, 0, -1)
        self.phone_cart_section = QFrame(self.phone_cart_button_section)
        self.phone_cart_section.setObjectName(u"phone_cart_section")
        self.phone_cart_section.setStyleSheet(u"background:rgb(255, 161, 28)")
        self.phone_cart_section.setFrameShape(QFrame.StyledPanel)
        self.phone_cart_section.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.phone_cart_section)

        self.phone_button_section = QFrame(self.phone_cart_button_section)
        self.phone_button_section.setObjectName(u"phone_button_section")
        self.phone_button_section.setStyleSheet(u"background:rgb(194, 39, 255)")
        self.phone_button_section.setFrameShape(QFrame.StyledPanel)
        self.phone_button_section.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.phone_button_section)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_13 = QFrame(self.phone_button_section)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setStyleSheet(u"background:rgb(255, 255, 255);")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_13)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.pushButton_9 = QPushButton(self.frame_13)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.verticalLayout_10.addWidget(self.pushButton_9)


        self.gridLayout.addWidget(self.frame_13, 2, 2, 1, 1)

        self.frame_14 = QFrame(self.phone_button_section)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setStyleSheet(u"background:rgb(255, 255, 255);")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_14)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.pushButton_5 = QPushButton(self.frame_14)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.verticalLayout_11.addWidget(self.pushButton_5)


        self.gridLayout.addWidget(self.frame_14, 1, 1, 1, 1)

        self.frame_12 = QFrame(self.phone_button_section)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setStyleSheet(u"background:rgb(255, 255, 255);")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_12)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.pushButton_6 = QPushButton(self.frame_12)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.verticalLayout_9.addWidget(self.pushButton_6)


        self.gridLayout.addWidget(self.frame_12, 1, 2, 1, 1)

        self.frame_15 = QFrame(self.phone_button_section)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setStyleSheet(u"background:rgb(255, 255, 255);")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_15)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.pushButton_8 = QPushButton(self.frame_15)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.verticalLayout_12.addWidget(self.pushButton_8)


        self.gridLayout.addWidget(self.frame_15, 2, 1, 1, 1)

        self.frame_16 = QFrame(self.phone_button_section)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setStyleSheet(u"background:rgb(255, 255, 255);")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_16)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.pushButton_2 = QPushButton(self.frame_16)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout_13.addWidget(self.pushButton_2)


        self.gridLayout.addWidget(self.frame_16, 0, 1, 1, 1)

        self.frame_17 = QFrame(self.phone_button_section)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setStyleSheet(u"background:rgb(255, 255, 255);")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_17)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.pushButton_3 = QPushButton(self.frame_17)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout_14.addWidget(self.pushButton_3)


        self.gridLayout.addWidget(self.frame_17, 0, 2, 1, 1)

        self.frame_18 = QFrame(self.phone_button_section)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setStyleSheet(u"background:rgb(255, 255, 255);")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_18)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.pushButton = QPushButton(self.frame_18)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_15.addWidget(self.pushButton)


        self.gridLayout.addWidget(self.frame_18, 0, 0, 1, 1)

        self.frame_19 = QFrame(self.phone_button_section)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setStyleSheet(u"background:rgb(255, 255, 255);")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_19)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.pushButton_4 = QPushButton(self.frame_19)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.verticalLayout_16.addWidget(self.pushButton_4)


        self.gridLayout.addWidget(self.frame_19, 1, 0, 1, 1)

        self.frame_20 = QFrame(self.phone_button_section)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setStyleSheet(u"background:rgb(255, 255, 255);")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_20)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.pushButton_7 = QPushButton(self.frame_20)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.verticalLayout_17.addWidget(self.pushButton_7)


        self.gridLayout.addWidget(self.frame_20, 2, 0, 1, 1)


        self.horizontalLayout_2.addWidget(self.phone_button_section)


        self.verticalLayout_5.addWidget(self.phone_cart_button_section)

        self.phone_table_section = QFrame(self.phone_bg_layout)
        self.phone_table_section.setObjectName(u"phone_table_section")
        sizePolicy.setHeightForWidth(self.phone_table_section.sizePolicy().hasHeightForWidth())
        self.phone_table_section.setSizePolicy(sizePolicy)
        self.phone_table_section.setMinimumSize(QSize(934, 191))
        self.phone_table_section.setMaximumSize(QSize(16777215, 16777215))
        self.phone_table_section.setStyleSheet(u"background: rgb(29, 59, 255);")
        self.phone_table_section.setFrameShape(QFrame.NoFrame)
        self.phone_table_section.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.phone_table_section)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, -1, 0, 0)
        self.tableWidget = QTableWidget(self.phone_table_section)
        if (self.tableWidget.columnCount() < 8):
            self.tableWidget.setColumnCount(8)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.horizontalLayout_3.addWidget(self.tableWidget)


        self.verticalLayout_5.addWidget(self.phone_table_section)


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
        self.customer_group.setTitle(QCoreApplication.translate("MainPages", u"Customer", None))
        self.label_3.setText(QCoreApplication.translate("MainPages", u"Name :", None))
        self.label_2.setText(QCoreApplication.translate("MainPages", u"Contact :", None))
        self.label_4.setText(QCoreApplication.translate("MainPages", u"Cart id", None))
        self.phone_group.setTitle(QCoreApplication.translate("MainPages", u"Phone", None))
        self.label_5.setText(QCoreApplication.translate("MainPages", u"type", None))
        self.label_6.setText(QCoreApplication.translate("MainPages", u"Model", None))
        self.label_7.setText(QCoreApplication.translate("MainPages", u"Imei", None))
        self.label_8.setText(QCoreApplication.translate("MainPages", u"SN", None))
        self.cost_group.setTitle(QCoreApplication.translate("MainPages", u"Cost", None))
        self.label_9.setText(QCoreApplication.translate("MainPages", u"Price :", None))
        self.label_10.setText(QCoreApplication.translate("MainPages", u"discount :", None))
        self.label_11.setText(QCoreApplication.translate("MainPages", u"tax :", None))
        self.label_12.setText(QCoreApplication.translate("MainPages", u"paymant :", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainPages", u"PushButton", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainPages", u"PushButton", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainPages", u"PushButton", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainPages", u"PushButton", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainPages", u"PushButton", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainPages", u"PushButton", None))
        self.pushButton.setText(QCoreApplication.translate("MainPages", u"PushButton", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainPages", u"PushButton", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainPages", u"PushButton", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainPages", u"id", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainPages", u"name", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainPages", u"col1", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainPages", u"col2", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainPages", u"col3", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainPages", u"col4", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainPages", u"col5", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainPages", u"col6", None));
        self.empty_page_label.setText(QCoreApplication.translate("MainPages", u"Empty Page", None))
    # retranslateUi

