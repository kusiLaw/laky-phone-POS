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
        MainPages.resize(1169, 770)
        self.main_pages_layout = QVBoxLayout(MainPages)
        self.main_pages_layout.setSpacing(0)
        self.main_pages_layout.setObjectName(u"main_pages_layout")
        self.main_pages_layout.setContentsMargins(0, 0, 5, 5)
        self.pages = QStackedWidget(MainPages)
        self.pages.setObjectName(u"pages")
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        font = QFont()
        font.setPointSize(20)
        self.home_page.setFont(font)
        self.home_page.setStyleSheet(u"/**font-size: 14pt; background: white; ")
        self.page_1_layout = QVBoxLayout(self.home_page)
        self.page_1_layout.setSpacing(5)
        self.page_1_layout.setObjectName(u"page_1_layout")
        self.page_1_layout.setContentsMargins(5, 5, 5, 5)
        self.header = QFrame(self.home_page)
        self.header.setObjectName(u"header")
        self.header.setStyleSheet(u"/**background:rgb(255, 71, 160)")
        self.header.setFrameShape(QFrame.NoFrame)
        self.header.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.header)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.label_41 = QLabel(self.header)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setStyleSheet(u"  font-size: 30px;\n"
"    text-transform: uppercase;\n"
"    font-weight: 700;\n"
"font-style:italic;\n"
"margin-bottom:20px;\n"
"")
        self.label_41.setFrameShape(QFrame.NoFrame)
        self.label_41.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.verticalLayout_32.addWidget(self.label_41)


        self.page_1_layout.addWidget(self.header)

        self.login_content = QFrame(self.home_page)
        self.login_content.setObjectName(u"login_content")
        self.login_content.setMinimumSize(QSize(500, 0))
        font1 = QFont()
        font1.setPointSize(16)
        self.login_content.setFont(font1)
        self.login_content.setStyleSheet(u"/**background:rgb(73, 255, 204);**/")
        self.login_content.setFrameShape(QFrame.NoFrame)
        self.login_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.login_content)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 0, 0, 0)
        self.frame_4 = QFrame(self.login_content)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFont(font1)
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.mleft = QFrame(self.frame_4)
        self.mleft.setObjectName(u"mleft")
        self.mleft.setMinimumSize(QSize(250, 0))
        self.mleft.setFrameShape(QFrame.StyledPanel)
        self.mleft.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_7.addWidget(self.mleft)

        self.frame_2 = QFrame(self.frame_4)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(500, 16777215))
        self.frame_2.setFont(font1)
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_2)
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(-1, 0, 0, 0)
        self.groupBox = QGroupBox(self.frame_2)
        self.groupBox.setObjectName(u"groupBox")
        font2 = QFont()
        self.groupBox.setFont(font2)
        self.groupBox.setStyleSheet(u"font-size: 24px;\n"
"")
        self.verticalLayout_29 = QVBoxLayout(self.groupBox)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(11, -1, -1, -1)
        self.content = QFrame(self.groupBox)
        self.content.setObjectName(u"content")
        self.content.setMaximumSize(QSize(490, 16777215))
        self.content.setFont(font2)
        self.content.setStyleSheet(u"/**background:red**/")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.content)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.login_form = QFrame(self.content)
        self.login_form.setObjectName(u"login_form")
        self.login_form.setMaximumSize(QSize(16777215, 120))
        self.login_form.setFont(font2)
        self.login_form.setStyleSheet(u"/**background:green**/")
        self.login_form.setFrameShape(QFrame.StyledPanel)
        self.login_form.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.login_form)
        self.gridLayout_6.setSpacing(5)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 5)
        self.frame_3 = QFrame(self.login_form)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(400, 16777215))
        self.frame_3.setFont(font2)
        self.frame_3.setStyleSheet(u"/**background:white")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.login_username_frame = QVBoxLayout(self.frame_3)
        self.login_username_frame.setSpacing(0)
        self.login_username_frame.setObjectName(u"login_username_frame")
        self.login_username_frame.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_6.addWidget(self.frame_3, 0, 1, 1, 1)

        self.label_31 = QLabel(self.login_form)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setMaximumSize(QSize(120, 16777215))
        self.label_31.setFont(font2)
        self.label_31.setStyleSheet(u"font-size: 18px;")
        self.label_31.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.label_31, 0, 0, 1, 1)

        self.label_40 = QLabel(self.login_form)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setMaximumSize(QSize(120, 16777215))
        self.label_40.setFont(font2)
        self.label_40.setStyleSheet(u"font-size: 18px;")
        self.label_40.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.label_40, 1, 0, 1, 1)

        self.frame_33 = QFrame(self.login_form)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setMaximumSize(QSize(400, 16777215))
        self.frame_33.setFont(font2)
        self.frame_33.setStyleSheet(u"/**background:white")
        self.frame_33.setFrameShape(QFrame.NoFrame)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.login_password_frame = QVBoxLayout(self.frame_33)
        self.login_password_frame.setSpacing(0)
        self.login_password_frame.setObjectName(u"login_password_frame")
        self.login_password_frame.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_6.addWidget(self.frame_33, 1, 1, 1, 1)


        self.verticalLayout_15.addWidget(self.login_form)

        self.buttons = QFrame(self.content)
        self.buttons.setObjectName(u"buttons")
        self.buttons.setMaximumSize(QSize(16777215, 45))
        self.buttons.setFont(font2)
        self.buttons.setFrameShape(QFrame.NoFrame)
        self.buttons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.buttons)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_34 = QFrame(self.buttons)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setFrameShape(QFrame.NoFrame)
        self.frame_34.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_9.addWidget(self.frame_34)

        self.frame_50 = QFrame(self.buttons)
        self.frame_50.setObjectName(u"frame_50")
        self.frame_50.setMaximumSize(QSize(500, 16777215))
        self.frame_50.setStyleSheet(u"/**background:white")
        self.frame_50.setFrameShape(QFrame.NoFrame)
        self.frame_50.setFrameShadow(QFrame.Raised)
        self.login_button_fame = QVBoxLayout(self.frame_50)
        self.login_button_fame.setSpacing(0)
        self.login_button_fame.setObjectName(u"login_button_fame")
        self.login_button_fame.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_9.addWidget(self.frame_50)


        self.verticalLayout_15.addWidget(self.buttons)


        self.verticalLayout_29.addWidget(self.content)


        self.verticalLayout_28.addWidget(self.groupBox)


        self.horizontalLayout_7.addWidget(self.frame_2)

        self.mright = QFrame(self.frame_4)
        self.mright.setObjectName(u"mright")
        self.mright.setMinimumSize(QSize(250, 0))
        self.mright.setFrameShape(QFrame.StyledPanel)
        self.mright.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_7.addWidget(self.mright)


        self.verticalLayout.addWidget(self.frame_4)


        self.page_1_layout.addWidget(self.login_content)

        self.footer = QFrame(self.home_page)
        self.footer.setObjectName(u"footer")
        self.footer.setFrameShape(QFrame.StyledPanel)
        self.footer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.footer)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.login_form_info = QLabel(self.footer)
        self.login_form_info.setObjectName(u"login_form_info")
        font3 = QFont()
        font3.setItalic(True)
        self.login_form_info.setFont(font3)
        self.login_form_info.setStyleSheet(u"color:red;\n"
"  font-size: 18px;\n"
" \n"
"font-style:italic;\n"
"")
        self.login_form_info.setScaledContents(True)
        self.login_form_info.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.login_form_info.setWordWrap(True)

        self.verticalLayout_33.addWidget(self.login_form_info)


        self.page_1_layout.addWidget(self.footer)

        self.pages.addWidget(self.home_page)
        self.dasboard = QWidget()
        self.dasboard.setObjectName(u"dasboard")
        font4 = QFont()
        font4.setPointSize(14)
        self.dasboard.setFont(font4)
        self.verticalLayout_31 = QVBoxLayout(self.dasboard)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.frame = QFrame(self.dasboard)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frame)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"\n"
"font-size: 40px;\n"
"text-transform: uppercase;\n"
"font-weight: 700;\n"
"text-align: center;\n"
"text-shadow: 0 15px 40px rgba(0,0,0, 0.6);")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_30.addWidget(self.label)


        self.verticalLayout_31.addWidget(self.frame)

        self.pages.addWidget(self.dasboard)
        self.phone_page = QWidget()
        self.phone_page.setObjectName(u"phone_page")
        self.phone_page.setStyleSheet(u"font-size: 14pt; background : #2c313c; ")
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
        self.contents.setGeometry(QRect(0, 0, 934, 608))
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
        self.phone_form_section.setMinimumSize(QSize(934, 226))
        self.phone_form_section.setMaximumSize(QSize(16777215, 16777215))
        self.phone_form_section.setStyleSheet(u"")
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
        self.phoneform_customer_section.setMinimumSize(QSize(284, 0))
        self.phoneform_customer_section.setMaximumSize(QSize(600, 16777215))
        self.phoneform_customer_section.setStyleSheet(u"")
        self.phoneform_customer_section.setFrameShape(QFrame.NoFrame)
        self.phoneform_customer_section.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.phoneform_customer_section)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(10, 0, 10, 0)
        self.customer_group = QGroupBox(self.phoneform_customer_section)
        self.customer_group.setObjectName(u"customer_group")
        self.formLayout = QFormLayout(self.customer_group)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setVerticalSpacing(12)
        self.formLayout.setContentsMargins(15, 5, 20, 5)
        self.label_3 = QLabel(self.customer_group)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.customer_name = QFrame(self.customer_group)
        self.customer_name.setObjectName(u"customer_name")
        self.customer_name.setStyleSheet(u"")
        self.customer_name.setFrameShape(QFrame.NoFrame)
        self.customer_name.setFrameShadow(QFrame.Raised)
        self.customer_name_edit = QVBoxLayout(self.customer_name)
        self.customer_name_edit.setSpacing(0)
        self.customer_name_edit.setObjectName(u"customer_name_edit")
        self.customer_name_edit.setContentsMargins(0, 0, 0, 0)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.customer_name)

        self.label_2 = QLabel(self.customer_group)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_2)

        self.customer_contact = QFrame(self.customer_group)
        self.customer_contact.setObjectName(u"customer_contact")
        self.customer_contact.setStyleSheet(u"")
        self.customer_contact.setFrameShape(QFrame.NoFrame)
        self.customer_contact.setFrameShadow(QFrame.Raised)
        self.customer_contact_edit = QVBoxLayout(self.customer_contact)
        self.customer_contact_edit.setSpacing(0)
        self.customer_contact_edit.setObjectName(u"customer_contact_edit")
        self.customer_contact_edit.setContentsMargins(0, 0, 0, 0)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.customer_contact)

        self.frame_8 = QFrame(self.customer_group)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setEnabled(False)
        self.frame_8.setMinimumSize(QSize(50, 50))
        self.frame_8.setMaximumSize(QSize(16777215, 100))
        self.frame_8.setStyleSheet(u"")
        self.frame_8.setFrameShape(QFrame.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_8)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 5, 0)
        self.cart_id = QFrame(self.frame_8)
        self.cart_id.setObjectName(u"cart_id")
        self.cart_id.setStyleSheet(u"")
        self.cart_id.setFrameShape(QFrame.NoFrame)
        self.cart_id.setFrameShadow(QFrame.Raised)
        self.cutomer_cart_id_edit = QVBoxLayout(self.cart_id)
        self.cutomer_cart_id_edit.setSpacing(0)
        self.cutomer_cart_id_edit.setObjectName(u"cutomer_cart_id_edit")
        self.cutomer_cart_id_edit.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_4.addWidget(self.cart_id, 1, 1, 1, 1)

        self.frame_14 = QFrame(self.frame_8)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.NoFrame)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.phone_cart_total_edit = QVBoxLayout(self.frame_14)
        self.phone_cart_total_edit.setSpacing(0)
        self.phone_cart_total_edit.setObjectName(u"phone_cart_total_edit")
        self.phone_cart_total_edit.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_4.addWidget(self.frame_14, 2, 1, 1, 1)

        self.label_4 = QLabel(self.frame_8)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"")

        self.gridLayout_4.addWidget(self.label_4, 1, 0, 1, 1)

        self.label_25 = QLabel(self.frame_8)
        self.label_25.setObjectName(u"label_25")

        self.gridLayout_4.addWidget(self.label_25, 2, 0, 1, 1)

        self.line = QFrame(self.frame_8)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_4.addWidget(self.line, 0, 0, 1, 2)


        self.formLayout.setWidget(3, QFormLayout.SpanningRole, self.frame_8)


        self.verticalLayout_6.addWidget(self.customer_group)


        self.horizontalLayout.addWidget(self.phoneform_customer_section)

        self.phoneform_phone_section = QFrame(self.phone_form_section)
        self.phoneform_phone_section.setObjectName(u"phoneform_phone_section")
        self.phoneform_phone_section.setMinimumSize(QSize(396, 0))
        self.phoneform_phone_section.setMaximumSize(QSize(600, 16777215))
        self.phoneform_phone_section.setStyleSheet(u"")
        self.phoneform_phone_section.setFrameShape(QFrame.StyledPanel)
        self.phoneform_phone_section.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.phoneform_phone_section)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(5, 0, 5, 0)
        self.phone_group = QGroupBox(self.phoneform_phone_section)
        self.phone_group.setObjectName(u"phone_group")
        self.gridLayout_2 = QGridLayout(self.phone_group)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(0)
        self.gridLayout_2.setVerticalSpacing(12)
        self.gridLayout_2.setContentsMargins(10, 5, 5, 10)
        self.frame_22 = QFrame(self.phone_group)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setMinimumSize(QSize(100, 0))
        self.frame_22.setStyleSheet(u"")
        self.frame_22.setFrameShape(QFrame.NoFrame)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.phone_type_edit = QVBoxLayout(self.frame_22)
        self.phone_type_edit.setSpacing(0)
        self.phone_type_edit.setObjectName(u"phone_type_edit")
        self.phone_type_edit.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_2.addWidget(self.frame_22, 0, 1, 1, 1)

        self.label_7 = QLabel(self.phone_group)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_2.addWidget(self.label_7, 2, 0, 1, 1)

        self.label_6 = QLabel(self.phone_group)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(60, 0))
        self.label_6.setMaximumSize(QSize(60, 16777215))

        self.gridLayout_2.addWidget(self.label_6, 0, 2, 1, 1)

        self.label_5 = QLabel(self.phone_group)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(60, 0))
        self.label_5.setMaximumSize(QSize(60, 16777215))

        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)

        self.frame_9 = QFrame(self.phone_group)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.phone_imei_edit = QVBoxLayout(self.frame_9)
        self.phone_imei_edit.setSpacing(0)
        self.phone_imei_edit.setObjectName(u"phone_imei_edit")
        self.phone_imei_edit.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_2.addWidget(self.frame_9, 2, 1, 1, 3)

        self.frame_24 = QFrame(self.phone_group)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setMinimumSize(QSize(100, 0))
        self.frame_24.setMaximumSize(QSize(16777215, 16777215))
        self.frame_24.setFrameShape(QFrame.NoFrame)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.phone_model_edit = QVBoxLayout(self.frame_24)
        self.phone_model_edit.setSpacing(0)
        self.phone_model_edit.setObjectName(u"phone_model_edit")
        self.phone_model_edit.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_2.addWidget(self.frame_24, 0, 3, 1, 1)

        self.label_8 = QLabel(self.phone_group)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.label_8, 3, 0, 1, 1)

        self.frame_10 = QFrame(self.phone_group)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setStyleSheet(u"")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.phone_sn_edit = QVBoxLayout(self.frame_10)
        self.phone_sn_edit.setSpacing(0)
        self.phone_sn_edit.setObjectName(u"phone_sn_edit")
        self.phone_sn_edit.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_2.addWidget(self.frame_10, 3, 1, 1, 1)

        self.label_18 = QLabel(self.phone_group)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_2.addWidget(self.label_18, 3, 2, 1, 1)

        self.label_16 = QLabel(self.phone_group)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.label_16, 5, 0, 1, 1)

        self.frame_21 = QFrame(self.phone_group)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setStyleSheet(u"")
        self.frame_21.setFrameShape(QFrame.NoFrame)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.phone_qr = QVBoxLayout(self.frame_21)
        self.phone_qr.setSpacing(0)
        self.phone_qr.setObjectName(u"phone_qr")
        self.phone_qr.setContentsMargins(10, 0, 0, 0)

        self.gridLayout_2.addWidget(self.frame_21, 5, 1, 1, 1)

        self.frame_23 = QFrame(self.phone_group)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_23)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 7)
        self.label_17 = QLabel(self.frame_23)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setStyleSheet(u"")
        self.label_17.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_13.addWidget(self.label_17)


        self.gridLayout_2.addWidget(self.frame_23, 5, 2, 1, 2)


        self.verticalLayout_7.addWidget(self.phone_group)


        self.horizontalLayout.addWidget(self.phoneform_phone_section)

        self.phoneform_cost_section = QFrame(self.phone_form_section)
        self.phoneform_cost_section.setObjectName(u"phoneform_cost_section")
        self.phoneform_cost_section.setMinimumSize(QSize(284, 0))
        self.phoneform_cost_section.setMaximumSize(QSize(600, 16777215))
        self.phoneform_cost_section.setStyleSheet(u"")
        self.phoneform_cost_section.setFrameShape(QFrame.StyledPanel)
        self.phoneform_cost_section.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.phoneform_cost_section)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(10, 0, 10, 0)
        self.cost_group = QGroupBox(self.phoneform_cost_section)
        self.cost_group.setObjectName(u"cost_group")
        self.formLayout_3 = QFormLayout(self.cost_group)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setHorizontalSpacing(7)
        self.formLayout_3.setVerticalSpacing(12)
        self.formLayout_3.setContentsMargins(15, 5, 20, 0)
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
        self.frame_26.setStyleSheet(u"\\")
        self.frame_26.setFrameShape(QFrame.NoFrame)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.phone_price_edit = QVBoxLayout(self.frame_26)
        self.phone_price_edit.setObjectName(u"phone_price_edit")
        self.phone_price_edit.setContentsMargins(0, 0, 0, 0)

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.frame_26)

        self.frame_27 = QFrame(self.cost_group)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setStyleSheet(u"\\")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.phone_discount_edit = QVBoxLayout(self.frame_27)
        self.phone_discount_edit.setObjectName(u"phone_discount_edit")
        self.phone_discount_edit.setContentsMargins(0, 0, 0, 0)

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.frame_27)

        self.frame_28 = QFrame(self.cost_group)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setStyleSheet(u"\\")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.phone_tax_edit = QVBoxLayout(self.frame_28)
        self.phone_tax_edit.setObjectName(u"phone_tax_edit")
        self.phone_tax_edit.setContentsMargins(0, 0, 0, 0)

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.frame_28)

        self.payment = QFrame(self.cost_group)
        self.payment.setObjectName(u"payment")
        self.payment.setStyleSheet(u"\\")
        self.payment.setFrameShape(QFrame.NoFrame)
        self.payment.setFrameShadow(QFrame.Raised)
        self.phone_payment_edit = QVBoxLayout(self.payment)
        self.phone_payment_edit.setObjectName(u"phone_payment_edit")
        self.phone_payment_edit.setContentsMargins(0, 0, 0, 0)

        self.formLayout_3.setWidget(3, QFormLayout.FieldRole, self.payment)


        self.verticalLayout_8.addWidget(self.cost_group)


        self.horizontalLayout.addWidget(self.phoneform_cost_section)


        self.verticalLayout_5.addWidget(self.phone_form_section)

        self.phone_cart_button_section = QFrame(self.phone_bg_layout)
        self.phone_cart_button_section.setObjectName(u"phone_cart_button_section")
        self.phone_cart_button_section.setMinimumSize(QSize(934, 156))
        self.phone_cart_button_section.setMaximumSize(QSize(16777215, 180))
        self.phone_cart_button_section.setStyleSheet(u"")
        self.phone_cart_button_section.setFrameShape(QFrame.NoFrame)
        self.phone_cart_button_section.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.phone_cart_button_section)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, -1, 0, -1)
        self.phone_cart_section = QFrame(self.phone_cart_button_section)
        self.phone_cart_section.setObjectName(u"phone_cart_section")
        self.phone_cart_section.setMaximumSize(QSize(600, 16777215))
        self.phone_cart_section.setStyleSheet(u"")
        self.phone_cart_section.setFrameShape(QFrame.NoFrame)
        self.phone_cart_section.setFrameShadow(QFrame.Raised)
        self.phone_cart_layout = QVBoxLayout(self.phone_cart_section)
        self.phone_cart_layout.setSpacing(0)
        self.phone_cart_layout.setObjectName(u"phone_cart_layout")
        self.phone_cart_layout.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_2.addWidget(self.phone_cart_section)

        self.phone_button_section = QFrame(self.phone_cart_button_section)
        self.phone_button_section.setObjectName(u"phone_button_section")
        self.phone_button_section.setMinimumSize(QSize(484, 0))
        self.phone_button_section.setStyleSheet(u"")
        self.phone_button_section.setFrameShape(QFrame.NoFrame)
        self.phone_button_section.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.phone_button_section)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(10)
        self.gridLayout.setContentsMargins(10, 10, 10, 0)
        self.frame_13 = QFrame(self.phone_button_section)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMinimumSize(QSize(150, 30))
        self.frame_13.setStyleSheet(u"")
        self.frame_13.setFrameShape(QFrame.NoFrame)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_13)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)

        self.gridLayout.addWidget(self.frame_13, 2, 2, 1, 1)

        self.phone_clear = QFrame(self.phone_button_section)
        self.phone_clear.setObjectName(u"phone_clear")
        self.phone_clear.setMinimumSize(QSize(150, 30))
        self.phone_clear.setStyleSheet(u"")
        self.phone_clear.setFrameShape(QFrame.StyledPanel)
        self.phone_clear.setFrameShadow(QFrame.Raised)
        self.phone_clear_layout = QVBoxLayout(self.phone_clear)
        self.phone_clear_layout.setSpacing(0)
        self.phone_clear_layout.setObjectName(u"phone_clear_layout")
        self.phone_clear_layout.setContentsMargins(0, 0, 0, 0)

        self.gridLayout.addWidget(self.phone_clear, 1, 1, 1, 1)

        self.phone_buyme = QFrame(self.phone_button_section)
        self.phone_buyme.setObjectName(u"phone_buyme")
        self.phone_buyme.setMinimumSize(QSize(150, 30))
        self.phone_buyme.setStyleSheet(u"")
        self.phone_buyme.setFrameShape(QFrame.NoFrame)
        self.phone_buyme.setFrameShadow(QFrame.Raised)
        self.phone_buyme_layout = QVBoxLayout(self.phone_buyme)
        self.phone_buyme_layout.setSpacing(0)
        self.phone_buyme_layout.setObjectName(u"phone_buyme_layout")
        self.phone_buyme_layout.setContentsMargins(0, 0, 0, 0)

        self.gridLayout.addWidget(self.phone_buyme, 0, 1, 1, 1)

        self.phone_print = QFrame(self.phone_button_section)
        self.phone_print.setObjectName(u"phone_print")
        self.phone_print.setMinimumSize(QSize(150, 30))
        self.phone_print.setStyleSheet(u"")
        self.phone_print.setFrameShape(QFrame.NoFrame)
        self.phone_print.setFrameShadow(QFrame.Raised)
        self.phone_print_layout = QVBoxLayout(self.phone_print)
        self.phone_print_layout.setSpacing(0)
        self.phone_print_layout.setObjectName(u"phone_print_layout")
        self.phone_print_layout.setContentsMargins(0, 0, 0, 0)

        self.gridLayout.addWidget(self.phone_print, 0, 2, 1, 1)

        self.remov_from_cart = QFrame(self.phone_button_section)
        self.remov_from_cart.setObjectName(u"remov_from_cart")
        self.remov_from_cart.setMinimumSize(QSize(150, 30))
        self.remov_from_cart.setStyleSheet(u"")
        self.remov_from_cart.setFrameShape(QFrame.NoFrame)
        self.remov_from_cart.setFrameShadow(QFrame.Raised)
        self.remov_from_cart_layout = QVBoxLayout(self.remov_from_cart)
        self.remov_from_cart_layout.setSpacing(0)
        self.remov_from_cart_layout.setObjectName(u"remov_from_cart_layout")
        self.remov_from_cart_layout.setContentsMargins(0, 0, 0, 0)

        self.gridLayout.addWidget(self.remov_from_cart, 1, 0, 1, 1)

        self.add_to_cart = QFrame(self.phone_button_section)
        self.add_to_cart.setObjectName(u"add_to_cart")
        self.add_to_cart.setMinimumSize(QSize(150, 30))
        self.add_to_cart.setStyleSheet(u"")
        self.add_to_cart.setFrameShape(QFrame.NoFrame)
        self.add_to_cart.setFrameShadow(QFrame.Raised)
        self.phone_add_to_cart_layout = QVBoxLayout(self.add_to_cart)
        self.phone_add_to_cart_layout.setSpacing(0)
        self.phone_add_to_cart_layout.setObjectName(u"phone_add_to_cart_layout")
        self.phone_add_to_cart_layout.setContentsMargins(0, 0, 0, 0)

        self.gridLayout.addWidget(self.add_to_cart, 0, 0, 1, 1)

        self.phone_delete = QFrame(self.phone_button_section)
        self.phone_delete.setObjectName(u"phone_delete")
        self.phone_delete.setMinimumSize(QSize(150, 30))
        self.phone_delete.setStyleSheet(u"")
        self.phone_delete.setFrameShape(QFrame.StyledPanel)
        self.phone_delete.setFrameShadow(QFrame.Raised)
        self.phone_delete_layout = QVBoxLayout(self.phone_delete)
        self.phone_delete_layout.setSpacing(0)
        self.phone_delete_layout.setObjectName(u"phone_delete_layout")
        self.phone_delete_layout.setContentsMargins(0, 0, 0, 0)

        self.gridLayout.addWidget(self.phone_delete, 2, 1, 1, 1)

        self.phone_all_in_one = QFrame(self.phone_button_section)
        self.phone_all_in_one.setObjectName(u"phone_all_in_one")
        self.phone_all_in_one.setMinimumSize(QSize(150, 30))
        self.phone_all_in_one.setStyleSheet(u"")
        self.phone_all_in_one.setFrameShape(QFrame.NoFrame)
        self.phone_all_in_one.setFrameShadow(QFrame.Raised)
        self.phone_all_in_one_layout = QVBoxLayout(self.phone_all_in_one)
        self.phone_all_in_one_layout.setSpacing(0)
        self.phone_all_in_one_layout.setObjectName(u"phone_all_in_one_layout")
        self.phone_all_in_one_layout.setContentsMargins(0, 0, 0, 0)

        self.gridLayout.addWidget(self.phone_all_in_one, 1, 2, 1, 1)

        self.phone_clear_cart = QFrame(self.phone_button_section)
        self.phone_clear_cart.setObjectName(u"phone_clear_cart")
        self.phone_clear_cart.setMinimumSize(QSize(150, 30))
        self.phone_clear_cart.setStyleSheet(u"")
        self.phone_clear_cart.setFrameShape(QFrame.NoFrame)
        self.phone_clear_cart.setFrameShadow(QFrame.Raised)
        self.phone_clear_cart_layout = QVBoxLayout(self.phone_clear_cart)
        self.phone_clear_cart_layout.setSpacing(0)
        self.phone_clear_cart_layout.setObjectName(u"phone_clear_cart_layout")
        self.phone_clear_cart_layout.setContentsMargins(0, 0, 0, 0)

        self.gridLayout.addWidget(self.phone_clear_cart, 2, 0, 1, 1)

        self.frame_12 = QFrame(self.phone_button_section)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(0, 30))
        self.frame_12.setStyleSheet(u"")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.formLayout_2 = QFormLayout(self.frame_12)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setHorizontalSpacing(0)
        self.formLayout_2.setVerticalSpacing(0)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_23 = QLabel(self.frame_12)
        self.label_23.setObjectName(u"label_23")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_23)

        self.frame_15 = QFrame(self.frame_12)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.NoFrame)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.phone_search_key_edit = QVBoxLayout(self.frame_15)
        self.phone_search_key_edit.setSpacing(0)
        self.phone_search_key_edit.setObjectName(u"phone_search_key_edit")
        self.phone_search_key_edit.setContentsMargins(-1, 0, 0, 0)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.frame_15)


        self.gridLayout.addWidget(self.frame_12, 3, 0, 1, 1)

        self.phone_search = QFrame(self.phone_button_section)
        self.phone_search.setObjectName(u"phone_search")
        self.phone_search.setMinimumSize(QSize(307, 30))
        self.phone_search.setFrameShape(QFrame.NoFrame)
        self.phone_search.setFrameShadow(QFrame.Raised)
        self.phone_search_layout = QVBoxLayout(self.phone_search)
        self.phone_search_layout.setSpacing(0)
        self.phone_search_layout.setObjectName(u"phone_search_layout")
        self.phone_search_layout.setContentsMargins(0, 0, 0, 0)

        self.gridLayout.addWidget(self.phone_search, 3, 1, 1, 2)


        self.horizontalLayout_2.addWidget(self.phone_button_section)


        self.verticalLayout_5.addWidget(self.phone_cart_button_section)

        self.phone_table_section = QFrame(self.phone_bg_layout)
        self.phone_table_section.setObjectName(u"phone_table_section")
        sizePolicy.setHeightForWidth(self.phone_table_section.sizePolicy().hasHeightForWidth())
        self.phone_table_section.setSizePolicy(sizePolicy)
        self.phone_table_section.setMinimumSize(QSize(934, 226))
        self.phone_table_section.setMaximumSize(QSize(16777215, 16777215))
        self.phone_table_section.setStyleSheet(u"")
        self.phone_table_section.setFrameShape(QFrame.NoFrame)
        self.phone_table_section.setFrameShadow(QFrame.Raised)
        self.phone_table = QHBoxLayout(self.phone_table_section)
        self.phone_table.setObjectName(u"phone_table")
        self.phone_table.setContentsMargins(0, -1, 0, 0)

        self.verticalLayout_5.addWidget(self.phone_table_section)


        self.verticalLayout_4.addWidget(self.phone_bg_layout)

        self.scrollArea.setWidget(self.contents)

        self.verticalLayout_3.addWidget(self.scrollArea)

        self.pages.addWidget(self.phone_page)
        self.service_page = QWidget()
        self.service_page.setObjectName(u"service_page")
        self.service_page.setFont(font4)
        self.service_page.setStyleSheet(u"font-size: 14pt; background: lightblue; ")
        self.page_2_layout = QVBoxLayout(self.service_page)
        self.page_2_layout.setSpacing(0)
        self.page_2_layout.setObjectName(u"page_2_layout")
        self.page_2_layout.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_2 = QScrollArea(self.service_page)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setFrameShape(QFrame.NoFrame)
        self.scrollArea_2.setWidgetResizable(True)
        self.Contents = QWidget()
        self.Contents.setObjectName(u"Contents")
        self.Contents.setGeometry(QRect(0, 0, 530, 606))
        self.verticalLayout_2 = QVBoxLayout(self.Contents)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.service_bg = QFrame(self.Contents)
        self.service_bg.setObjectName(u"service_bg")
        self.service_bg.setFrameShape(QFrame.NoFrame)
        self.service_bg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.service_bg)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.service_forms_section = QFrame(self.service_bg)
        self.service_forms_section.setObjectName(u"service_forms_section")
        self.service_forms_section.setMinimumSize(QSize(0, 202))
        self.service_forms_section.setMaximumSize(QSize(16777215, 600))
        self.service_forms_section.setStyleSheet(u"background :rgb(255, 188, 19)")
        self.service_forms_section.setFrameShape(QFrame.NoFrame)
        self.service_forms_section.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.service_forms_section)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.service_customer_section = QFrame(self.service_forms_section)
        self.service_customer_section.setObjectName(u"service_customer_section")
        self.service_customer_section.setMaximumSize(QSize(280, 16777215))
        self.service_customer_section.setStyleSheet(u"background :rgb(0, 255, 127)")
        self.service_customer_section.setFrameShape(QFrame.NoFrame)
        self.service_customer_section.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.service_customer_section)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.service_customer_group = QGroupBox(self.service_customer_section)
        self.service_customer_group.setObjectName(u"service_customer_group")
        self.formLayout_4 = QFormLayout(self.service_customer_group)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.formLayout_4.setHorizontalSpacing(7)
        self.formLayout_4.setVerticalSpacing(7)
        self.formLayout_4.setContentsMargins(10, 0, 10, 0)
        self.label_13 = QLabel(self.service_customer_group)
        self.label_13.setObjectName(u"label_13")

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.label_13)

        self.frame_11 = QFrame(self.service_customer_group)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setStyleSheet(u"background: rgb(255, 255, 255)")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.frame_11)

        self.label_14 = QLabel(self.service_customer_group)
        self.label_14.setObjectName(u"label_14")

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.label_14)

        self.frame_18 = QFrame(self.service_customer_group)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setStyleSheet(u"background: rgb(255, 255, 255)")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.frame_18)

        self.label_15 = QLabel(self.service_customer_group)
        self.label_15.setObjectName(u"label_15")

        self.formLayout_4.setWidget(2, QFormLayout.LabelRole, self.label_15)

        self.label_30 = QLabel(self.service_customer_group)
        self.label_30.setObjectName(u"label_30")

        self.formLayout_4.setWidget(3, QFormLayout.LabelRole, self.label_30)


        self.verticalLayout_20.addWidget(self.service_customer_group)


        self.horizontalLayout_4.addWidget(self.service_customer_section)

        self.service_phone_section = QFrame(self.service_forms_section)
        self.service_phone_section.setObjectName(u"service_phone_section")
        self.service_phone_section.setMaximumSize(QSize(400, 16777215))
        self.service_phone_section.setStyleSheet(u"background :rgb(170, 170, 127)")
        self.service_phone_section.setFrameShape(QFrame.NoFrame)
        self.service_phone_section.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.service_phone_section)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.service_phon_group = QGroupBox(self.service_phone_section)
        self.service_phon_group.setObjectName(u"service_phon_group")
        self.gridLayout_3 = QGridLayout(self.service_phon_group)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_19 = QLabel(self.service_phon_group)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_3.addWidget(self.label_19, 0, 0, 1, 1)

        self.label_22 = QLabel(self.service_phon_group)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout_3.addWidget(self.label_22, 0, 3, 1, 1)

        self.label_20 = QLabel(self.service_phon_group)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_3.addWidget(self.label_20, 2, 0, 1, 1)

        self.label_27 = QLabel(self.service_phon_group)
        self.label_27.setObjectName(u"label_27")

        self.gridLayout_3.addWidget(self.label_27, 1, 3, 1, 1)

        self.label_26 = QLabel(self.service_phon_group)
        self.label_26.setObjectName(u"label_26")

        self.gridLayout_3.addWidget(self.label_26, 2, 3, 1, 1)

        self.label_21 = QLabel(self.service_phon_group)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_3.addWidget(self.label_21, 1, 0, 1, 1)

        self.frame_25 = QFrame(self.service_phon_group)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)

        self.gridLayout_3.addWidget(self.frame_25, 0, 2, 1, 1)

        self.frame_30 = QFrame(self.service_phon_group)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)

        self.gridLayout_3.addWidget(self.frame_30, 0, 5, 1, 1)

        self.label_28 = QLabel(self.service_phon_group)
        self.label_28.setObjectName(u"label_28")

        self.gridLayout_3.addWidget(self.label_28, 3, 0, 1, 1)

        self.frame_17 = QFrame(self.service_phon_group)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)

        self.gridLayout_3.addWidget(self.frame_17, 0, 4, 1, 1)

        self.frame_19 = QFrame(self.service_phon_group)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)

        self.gridLayout_3.addWidget(self.frame_19, 0, 1, 1, 1)


        self.verticalLayout_22.addWidget(self.service_phon_group)


        self.horizontalLayout_4.addWidget(self.service_phone_section)

        self.service_cost_section = QFrame(self.service_forms_section)
        self.service_cost_section.setObjectName(u"service_cost_section")
        self.service_cost_section.setMaximumSize(QSize(400, 16777215))
        self.service_cost_section.setStyleSheet(u"background :rgb(85, 255, 0)")
        self.service_cost_section.setFrameShape(QFrame.NoFrame)
        self.service_cost_section.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.service_cost_section)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.service_cost_group = QGroupBox(self.service_cost_section)
        self.service_cost_group.setObjectName(u"service_cost_group")

        self.verticalLayout_19.addWidget(self.service_cost_group)


        self.horizontalLayout_4.addWidget(self.service_cost_section)

        self.frame_16 = QFrame(self.service_forms_section)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_4.addWidget(self.frame_16)


        self.verticalLayout_18.addWidget(self.service_forms_section)

        self.service_cart_buttons_section = QFrame(self.service_bg)
        self.service_cart_buttons_section.setObjectName(u"service_cart_buttons_section")
        self.service_cart_buttons_section.setMinimumSize(QSize(0, 202))
        self.service_cart_buttons_section.setMaximumSize(QSize(16777215, 600))
        self.service_cart_buttons_section.setStyleSheet(u"background :rgb(24, 8, 255)")
        self.service_cart_buttons_section.setFrameShape(QFrame.StyledPanel)
        self.service_cart_buttons_section.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.service_cart_buttons_section)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.service_cart_buttons_section)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"background: rgb(122, 18, 42)")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.service_cart_buttons_section)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"background: rgb(170, 170, 0)")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_6)


        self.verticalLayout_18.addWidget(self.service_cart_buttons_section)

        self.service_table_section = QFrame(self.service_bg)
        self.service_table_section.setObjectName(u"service_table_section")
        self.service_table_section.setMinimumSize(QSize(0, 202))
        self.service_table_section.setMaximumSize(QSize(16777215, 600))
        self.service_table_section.setStyleSheet(u"background : rgb(255, 43, 199)")
        self.service_table_section.setFrameShape(QFrame.StyledPanel)
        self.service_table_section.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.service_table_section)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.frame_7 = QFrame(self.service_table_section)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)

        self.verticalLayout_23.addWidget(self.frame_7)


        self.verticalLayout_18.addWidget(self.service_table_section)


        self.verticalLayout_2.addWidget(self.service_bg)

        self.scrollArea_2.setWidget(self.Contents)

        self.page_2_layout.addWidget(self.scrollArea_2)

        self.pages.addWidget(self.service_page)
        self.stock = QWidget()
        self.stock.setObjectName(u"stock")
        self.stock.setFont(font4)
        self.stock.setStyleSheet(u"font-size: 14pt; background : #2c313c; \n"
"")
        self.page_3_layout = QVBoxLayout(self.stock)
        self.page_3_layout.setSpacing(0)
        self.page_3_layout.setObjectName(u"page_3_layout")
        self.page_3_layout.setContentsMargins(0, 0, 5, 0)
        self.scrollArea_3 = QScrollArea(self.stock)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setFrameShape(QFrame.NoFrame)
        self.scrollArea_3.setWidgetResizable(True)
        self.stockContents = QWidget()
        self.stockContents.setObjectName(u"stockContents")
        self.stockContents.setGeometry(QRect(0, 0, 1113, 603))
        self.stockContents.setFont(font4)
        self.stockContents.setStyleSheet(u"")
        self.verticalLayout_9 = QVBoxLayout(self.stockContents)
        self.verticalLayout_9.setSpacing(7)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 5, 5, 5)
        self.label_24 = QLabel(self.stockContents)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMaximumSize(QSize(16777215, 232))
        self.label_24.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_9.addWidget(self.label_24)

        self.frame_29 = QFrame(self.stockContents)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setMinimumSize(QSize(0, 50))
        self.frame_29.setMaximumSize(QSize(16777215, 84))
        self.frame_29.setFont(font4)
        self.frame_29.setFrameShape(QFrame.NoFrame)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_29)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(5, 0, 5, 0)
        self.label_29 = QLabel(self.frame_29)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMaximumSize(QSize(16777215, 232))
        self.label_29.setFont(font4)
        self.label_29.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.label_29.setWordWrap(True)

        self.verticalLayout_12.addWidget(self.label_29)


        self.verticalLayout_9.addWidget(self.frame_29)

        self.stock_tab_frame = QFrame(self.stockContents)
        self.stock_tab_frame.setObjectName(u"stock_tab_frame")
        self.stock_tab_frame.setFrameShape(QFrame.StyledPanel)
        self.stock_tab_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.stock_tab_frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.stock_parent_tab = QTabWidget(self.stock_tab_frame)
        self.stock_parent_tab.setObjectName(u"stock_parent_tab")
        self.stock_parent_tab.setStyleSheet(u"QTabWidget::pane { /* The tab widget frame */\n"
"    border-top: 1px solid #C2C7CB;\n"
"	color: white;\n"
"	\n"
"	\n"
"	font: 12pt \"Segoe UI\";\n"
"}\n"
"QTabWidget::tab-bar {\n"
"    left: 5px; /* move to the right by 5px */\n"
"}\n"
"QTabBar::tab:selected, QTabBar::tab:hover {\n"
"    background: #1b1e23;\n"
"		font-size: 18px;\n"
"	\n"
"}\n"
"\n"
"")
        self.stock_parent_tab.setTabShape(QTabWidget.Triangular)
        self.phone_tab = QWidget()
        self.phone_tab.setObjectName(u"phone_tab")
        self.horizontalLayout_6 = QHBoxLayout(self.phone_tab)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(5, 0, 5, 5)
        self.frame_20 = QFrame(self.phone_tab)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_20)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.stock_form = QFrame(self.frame_20)
        self.stock_form.setObjectName(u"stock_form")
        self.stock_form.setMinimumSize(QSize(0, 180))
        self.stock_form.setStyleSheet(u"")
        self.stock_form.setFrameShape(QFrame.StyledPanel)
        self.stock_form.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.stock_form)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.sdp_form_layout_4 = QFrame(self.stock_form)
        self.sdp_form_layout_4.setObjectName(u"sdp_form_layout_4")
        self.sdp_form_layout_4.setMinimumSize(QSize(400, 0))
        self.sdp_form_layout_4.setMaximumSize(QSize(16777215, 16777215))
        self.sdp_form_layout_4.setFrameShape(QFrame.StyledPanel)
        self.sdp_form_layout_4.setFrameShadow(QFrame.Raised)
        self.formLayout_8 = QFormLayout(self.sdp_form_layout_4)
        self.formLayout_8.setObjectName(u"formLayout_8")
        self.label_48 = QLabel(self.sdp_form_layout_4)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setStyleSheet(u"color:#d0d0d0")

        self.formLayout_8.setWidget(0, QFormLayout.LabelRole, self.label_48)

        self.frame_77 = QFrame(self.sdp_form_layout_4)
        self.frame_77.setObjectName(u"frame_77")
        self.frame_77.setMinimumSize(QSize(0, 0))
        self.frame_77.setStyleSheet(u"\\")
        self.frame_77.setFrameShape(QFrame.NoFrame)
        self.frame_77.setFrameShadow(QFrame.Raised)
        self.stock_ph_type_layout = QVBoxLayout(self.frame_77)
        self.stock_ph_type_layout.setSpacing(0)
        self.stock_ph_type_layout.setObjectName(u"stock_ph_type_layout")
        self.stock_ph_type_layout.setContentsMargins(0, 0, 0, 0)

        self.formLayout_8.setWidget(0, QFormLayout.FieldRole, self.frame_77)

        self.label_60 = QLabel(self.sdp_form_layout_4)
        self.label_60.setObjectName(u"label_60")

        self.formLayout_8.setWidget(1, QFormLayout.LabelRole, self.label_60)

        self.frame_78 = QFrame(self.sdp_form_layout_4)
        self.frame_78.setObjectName(u"frame_78")
        self.frame_78.setStyleSheet(u"")
        self.frame_78.setFrameShape(QFrame.NoFrame)
        self.frame_78.setFrameShadow(QFrame.Raised)
        self.stock_ph_model_layout = QVBoxLayout(self.frame_78)
        self.stock_ph_model_layout.setSpacing(0)
        self.stock_ph_model_layout.setObjectName(u"stock_ph_model_layout")
        self.stock_ph_model_layout.setContentsMargins(0, 0, 0, 0)

        self.formLayout_8.setWidget(1, QFormLayout.FieldRole, self.frame_78)

        self.frame_79 = QFrame(self.sdp_form_layout_4)
        self.frame_79.setObjectName(u"frame_79")
        self.frame_79.setStyleSheet(u"")
        self.frame_79.setFrameShape(QFrame.NoFrame)
        self.frame_79.setFrameShadow(QFrame.Raised)
        self.stock_ph_pdt_layout = QVBoxLayout(self.frame_79)
        self.stock_ph_pdt_layout.setSpacing(0)
        self.stock_ph_pdt_layout.setObjectName(u"stock_ph_pdt_layout")
        self.stock_ph_pdt_layout.setContentsMargins(0, 0, 0, 0)

        self.formLayout_8.setWidget(2, QFormLayout.FieldRole, self.frame_79)

        self.label_61 = QLabel(self.sdp_form_layout_4)
        self.label_61.setObjectName(u"label_61")

        self.formLayout_8.setWidget(2, QFormLayout.LabelRole, self.label_61)

        self.label_33 = QLabel(self.sdp_form_layout_4)
        self.label_33.setObjectName(u"label_33")

        self.formLayout_8.setWidget(3, QFormLayout.LabelRole, self.label_33)

        self.widget = QWidget(self.sdp_form_layout_4)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"")
        self.toInsrt = QVBoxLayout(self.widget)
        self.toInsrt.setSpacing(0)
        self.toInsrt.setObjectName(u"toInsrt")
        self.toInsrt.setContentsMargins(0, 0, 0, 0)
        self.dateTimeEdit = QDateTimeEdit(self.widget)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")

        self.toInsrt.addWidget(self.dateTimeEdit)


        self.formLayout_8.setWidget(3, QFormLayout.FieldRole, self.widget)


        self.horizontalLayout_14.addWidget(self.sdp_form_layout_4)

        self.sdp_sn_layout_4 = QFrame(self.stock_form)
        self.sdp_sn_layout_4.setObjectName(u"sdp_sn_layout_4")
        self.sdp_sn_layout_4.setMinimumSize(QSize(400, 0))
        self.sdp_sn_layout_4.setMaximumSize(QSize(750, 16777215))
        self.sdp_sn_layout_4.setFrameShape(QFrame.NoFrame)
        self.sdp_sn_layout_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_11 = QGridLayout(self.sdp_sn_layout_4)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.frame_38 = QFrame(self.sdp_sn_layout_4)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setFrameShape(QFrame.NoFrame)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_38)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.label_37 = QLabel(self.frame_38)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_24.addWidget(self.label_37)


        self.gridLayout_11.addWidget(self.frame_38, 2, 2, 1, 1)

        self.frame_37 = QFrame(self.sdp_sn_layout_4)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setFrameShape(QFrame.NoFrame)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_37)
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.label_35 = QLabel(self.frame_37)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_35.setWordWrap(True)

        self.verticalLayout_27.addWidget(self.label_35)


        self.gridLayout_11.addWidget(self.frame_37, 1, 2, 1, 1)

        self.frame_82 = QFrame(self.sdp_sn_layout_4)
        self.frame_82.setObjectName(u"frame_82")
        self.frame_82.setStyleSheet(u"")
        self.frame_82.setFrameShape(QFrame.NoFrame)
        self.frame_82.setFrameShadow(QFrame.Raised)
        self.stock_sp_layout = QVBoxLayout(self.frame_82)
        self.stock_sp_layout.setSpacing(0)
        self.stock_sp_layout.setObjectName(u"stock_sp_layout")
        self.stock_sp_layout.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_11.addWidget(self.frame_82, 1, 1, 1, 1)

        self.frame_81 = QFrame(self.sdp_sn_layout_4)
        self.frame_81.setObjectName(u"frame_81")
        self.frame_81.setStyleSheet(u"")
        self.frame_81.setFrameShape(QFrame.NoFrame)
        self.frame_81.setFrameShadow(QFrame.Raised)
        self.stock_cp_layout = QVBoxLayout(self.frame_81)
        self.stock_cp_layout.setSpacing(0)
        self.stock_cp_layout.setObjectName(u"stock_cp_layout")
        self.stock_cp_layout.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_11.addWidget(self.frame_81, 0, 1, 1, 1)

        self.frame_80 = QFrame(self.sdp_sn_layout_4)
        self.frame_80.setObjectName(u"frame_80")
        self.frame_80.setStyleSheet(u"")
        self.frame_80.setFrameShape(QFrame.NoFrame)
        self.frame_80.setFrameShadow(QFrame.Raised)
        self.stock_qantity_layout = QVBoxLayout(self.frame_80)
        self.stock_qantity_layout.setSpacing(0)
        self.stock_qantity_layout.setObjectName(u"stock_qantity_layout")
        self.stock_qantity_layout.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_11.addWidget(self.frame_80, 2, 1, 1, 1)

        self.frame_39 = QFrame(self.sdp_sn_layout_4)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setStyleSheet(u"")
        self.frame_39.setFrameShape(QFrame.NoFrame)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.stock_suplier_layout = QVBoxLayout(self.frame_39)
        self.stock_suplier_layout.setSpacing(0)
        self.stock_suplier_layout.setObjectName(u"stock_suplier_layout")
        self.stock_suplier_layout.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_11.addWidget(self.frame_39, 0, 3, 1, 1)

        self.frame_40 = QFrame(self.sdp_sn_layout_4)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setFrameShape(QFrame.NoFrame)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.suplier_contact_layout = QVBoxLayout(self.frame_40)
        self.suplier_contact_layout.setSpacing(0)
        self.suplier_contact_layout.setObjectName(u"suplier_contact_layout")
        self.suplier_contact_layout.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_11.addWidget(self.frame_40, 1, 3, 1, 1)

        self.frame_36 = QFrame(self.sdp_sn_layout_4)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setMinimumSize(QSize(108, 0))
        self.frame_36.setFrameShape(QFrame.NoFrame)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_36)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.label_34 = QLabel(self.frame_36)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setMinimumSize(QSize(102, 0))
        self.label_34.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_26.addWidget(self.label_34)


        self.gridLayout_11.addWidget(self.frame_36, 0, 2, 1, 1)

        self.label_62 = QLabel(self.sdp_sn_layout_4)
        self.label_62.setObjectName(u"label_62")

        self.gridLayout_11.addWidget(self.label_62, 1, 0, 1, 1)

        self.label_63 = QLabel(self.sdp_sn_layout_4)
        self.label_63.setObjectName(u"label_63")

        self.gridLayout_11.addWidget(self.label_63, 0, 0, 1, 1)

        self.label_32 = QLabel(self.sdp_sn_layout_4)
        self.label_32.setObjectName(u"label_32")

        self.gridLayout_11.addWidget(self.label_32, 2, 0, 1, 1)

        self.label_36 = QLabel(self.sdp_sn_layout_4)
        self.label_36.setObjectName(u"label_36")

        self.gridLayout_11.addWidget(self.label_36, 3, 0, 1, 1)

        self.frame_32 = QFrame(self.sdp_sn_layout_4)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setStyleSheet(u"")
        self.frame_32.setFrameShape(QFrame.NoFrame)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.stock_qr_layout = QVBoxLayout(self.frame_32)
        self.stock_qr_layout.setSpacing(0)
        self.stock_qr_layout.setObjectName(u"stock_qr_layout")
        self.stock_qr_layout.setContentsMargins(10, 0, 0, 0)

        self.gridLayout_11.addWidget(self.frame_32, 3, 3, 1, 1)

        self.frame_31 = QFrame(self.sdp_sn_layout_4)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setStyleSheet(u"")
        self.frame_31.setFrameShape(QFrame.NoFrame)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.stock_tax_layout = QVBoxLayout(self.frame_31)
        self.stock_tax_layout.setObjectName(u"stock_tax_layout")
        self.stock_tax_layout.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_11.addWidget(self.frame_31, 3, 1, 1, 1)

        self.frame_51 = QFrame(self.sdp_sn_layout_4)
        self.frame_51.setObjectName(u"frame_51")
        self.frame_51.setFrameShape(QFrame.NoFrame)
        self.frame_51.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_51)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.label_38 = QLabel(self.frame_51)
        self.label_38.setObjectName(u"label_38")

        self.verticalLayout_16.addWidget(self.label_38)


        self.gridLayout_11.addWidget(self.frame_51, 3, 2, 1, 1)

        self.frame_35 = QFrame(self.sdp_sn_layout_4)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setFrameShape(QFrame.NoFrame)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.stock_unique_code_layout = QVBoxLayout(self.frame_35)
        self.stock_unique_code_layout.setSpacing(70)
        self.stock_unique_code_layout.setObjectName(u"stock_unique_code_layout")
        self.stock_unique_code_layout.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_11.addWidget(self.frame_35, 2, 3, 1, 1)


        self.horizontalLayout_14.addWidget(self.sdp_sn_layout_4)

        self.frame_84 = QFrame(self.stock_form)
        self.frame_84.setObjectName(u"frame_84")
        self.frame_84.setMinimumSize(QSize(250, 0))
        self.frame_84.setMaximumSize(QSize(16777215, 16777215))
        self.frame_84.setStyleSheet(u"")
        self.frame_84.setFrameShape(QFrame.NoFrame)
        self.frame_84.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_84)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.frame_85 = QFrame(self.frame_84)
        self.frame_85.setObjectName(u"frame_85")
        self.frame_85.setStyleSheet(u"background: #282a36")
        self.frame_85.setFrameShape(QFrame.StyledPanel)
        self.frame_85.setFrameShadow(QFrame.Raised)
        self.cart_imei_list_layout = QHBoxLayout(self.frame_85)
        self.cart_imei_list_layout.setObjectName(u"cart_imei_list_layout")
        self.cart_imei_list_layout.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_14.addWidget(self.frame_85)


        self.horizontalLayout_14.addWidget(self.frame_84)


        self.verticalLayout_11.addWidget(self.stock_form)

        self.stock_buttom = QFrame(self.frame_20)
        self.stock_buttom.setObjectName(u"stock_buttom")
        self.stock_buttom.setMinimumSize(QSize(0, 100))
        self.stock_buttom.setStyleSheet(u"")
        self.stock_buttom.setFrameShape(QFrame.StyledPanel)
        self.stock_buttom.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.stock_buttom)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.frame_42 = QFrame(self.stock_buttom)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setMinimumSize(QSize(400, 0))
        self.frame_42.setMaximumSize(QSize(400, 16777215))
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_8.addWidget(self.frame_42)

        self.frame_41 = QFrame(self.stock_buttom)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setStyleSheet(u"")
        self.frame_41.setFrameShape(QFrame.NoFrame)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_41)
        self.gridLayout_5.setSpacing(7)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_45 = QFrame(self.frame_41)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setStyleSheet(u"")
        self.frame_45.setFrameShape(QFrame.NoFrame)
        self.frame_45.setFrameShadow(QFrame.Raised)
        self.stock_update_layout = QVBoxLayout(self.frame_45)
        self.stock_update_layout.setSpacing(0)
        self.stock_update_layout.setObjectName(u"stock_update_layout")
        self.stock_update_layout.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_5.addWidget(self.frame_45, 0, 2, 1, 1)

        self.frame_46 = QFrame(self.frame_41)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setStyleSheet(u"")
        self.frame_46.setFrameShape(QFrame.NoFrame)
        self.frame_46.setFrameShadow(QFrame.Raised)
        self.stock_delete_layout = QVBoxLayout(self.frame_46)
        self.stock_delete_layout.setSpacing(0)
        self.stock_delete_layout.setObjectName(u"stock_delete_layout")
        self.stock_delete_layout.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_5.addWidget(self.frame_46, 0, 3, 1, 1)

        self.frame_44 = QFrame(self.frame_41)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setStyleSheet(u"")
        self.frame_44.setFrameShape(QFrame.NoFrame)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.stock_clear_layout = QVBoxLayout(self.frame_44)
        self.stock_clear_layout.setSpacing(0)
        self.stock_clear_layout.setObjectName(u"stock_clear_layout")
        self.stock_clear_layout.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_5.addWidget(self.frame_44, 0, 1, 1, 1)

        self.frame_43 = QFrame(self.frame_41)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setStyleSheet(u"")
        self.frame_43.setFrameShape(QFrame.NoFrame)
        self.frame_43.setFrameShadow(QFrame.Raised)
        self.stock_save_layout = QVBoxLayout(self.frame_43)
        self.stock_save_layout.setSpacing(0)
        self.stock_save_layout.setObjectName(u"stock_save_layout")
        self.stock_save_layout.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_5.addWidget(self.frame_43, 0, 0, 1, 1)

        self.frame_47 = QFrame(self.frame_41)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setStyleSheet(u"")
        self.frame_47.setFrameShape(QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_47)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.label_39 = QLabel(self.frame_47)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_25.addWidget(self.label_39)


        self.gridLayout_5.addWidget(self.frame_47, 1, 0, 1, 1)

        self.frame_48 = QFrame(self.frame_41)
        self.frame_48.setObjectName(u"frame_48")
        self.frame_48.setStyleSheet(u"")
        self.frame_48.setFrameShape(QFrame.NoFrame)
        self.frame_48.setFrameShadow(QFrame.Raised)
        self.stock_search_key_layout = QVBoxLayout(self.frame_48)
        self.stock_search_key_layout.setSpacing(0)
        self.stock_search_key_layout.setObjectName(u"stock_search_key_layout")
        self.stock_search_key_layout.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_5.addWidget(self.frame_48, 1, 1, 1, 1)

        self.frame_49 = QFrame(self.frame_41)
        self.frame_49.setObjectName(u"frame_49")
        self.frame_49.setStyleSheet(u"")
        self.frame_49.setFrameShape(QFrame.NoFrame)
        self.frame_49.setFrameShadow(QFrame.Raised)
        self.stock_search_layout = QVBoxLayout(self.frame_49)
        self.stock_search_layout.setSpacing(0)
        self.stock_search_layout.setObjectName(u"stock_search_layout")
        self.stock_search_layout.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_5.addWidget(self.frame_49, 1, 2, 1, 2)


        self.horizontalLayout_8.addWidget(self.frame_41)


        self.verticalLayout_11.addWidget(self.stock_buttom)

        self.stock_table = QFrame(self.frame_20)
        self.stock_table.setObjectName(u"stock_table")
        self.stock_table.setMinimumSize(QSize(0, 157))
        self.stock_table.setStyleSheet(u"background:rgb(0, 26, 0)")
        self.stock_table.setFrameShape(QFrame.NoFrame)
        self.stock_table.setFrameShadow(QFrame.Raised)
        self.stock_table_frame = QHBoxLayout(self.stock_table)
        self.stock_table_frame.setSpacing(0)
        self.stock_table_frame.setObjectName(u"stock_table_frame")
        self.stock_table_frame.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_11.addWidget(self.stock_table)


        self.horizontalLayout_6.addWidget(self.frame_20)

        self.stock_parent_tab.addTab(self.phone_tab, "")
        self.accessories_tab = QWidget()
        self.accessories_tab.setObjectName(u"accessories_tab")
        self.horizontalLayout_11 = QHBoxLayout(self.accessories_tab)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_58 = QFrame(self.accessories_tab)
        self.frame_58.setObjectName(u"frame_58")
        self.frame_58.setFrameShape(QFrame.StyledPanel)
        self.frame_58.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_58)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.frame_59 = QFrame(self.frame_58)
        self.frame_59.setObjectName(u"frame_59")
        self.frame_59.setMinimumSize(QSize(0, 156))
        self.frame_59.setStyleSheet(u"")
        self.frame_59.setFrameShape(QFrame.StyledPanel)
        self.frame_59.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_59)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.sdp_form_layout_3 = QFrame(self.frame_59)
        self.sdp_form_layout_3.setObjectName(u"sdp_form_layout_3")
        self.sdp_form_layout_3.setFrameShape(QFrame.StyledPanel)
        self.sdp_form_layout_3.setFrameShadow(QFrame.Raised)
        self.formLayout_7 = QFormLayout(self.sdp_form_layout_3)
        self.formLayout_7.setObjectName(u"formLayout_7")
        self.label_47 = QLabel(self.sdp_form_layout_3)
        self.label_47.setObjectName(u"label_47")

        self.formLayout_7.setWidget(0, QFormLayout.LabelRole, self.label_47)

        self.frame_63 = QFrame(self.sdp_form_layout_3)
        self.frame_63.setObjectName(u"frame_63")
        self.frame_63.setStyleSheet(u"background: rgb(255, 255, 255)")
        self.frame_63.setFrameShape(QFrame.StyledPanel)
        self.frame_63.setFrameShadow(QFrame.Raised)

        self.formLayout_7.setWidget(0, QFormLayout.FieldRole, self.frame_63)

        self.label_51 = QLabel(self.sdp_form_layout_3)
        self.label_51.setObjectName(u"label_51")

        self.formLayout_7.setWidget(1, QFormLayout.LabelRole, self.label_51)

        self.frame_64 = QFrame(self.sdp_form_layout_3)
        self.frame_64.setObjectName(u"frame_64")
        self.frame_64.setStyleSheet(u"background: rgb(255, 255, 255)")
        self.frame_64.setFrameShape(QFrame.StyledPanel)
        self.frame_64.setFrameShadow(QFrame.Raised)

        self.formLayout_7.setWidget(1, QFormLayout.FieldRole, self.frame_64)

        self.label_52 = QLabel(self.sdp_form_layout_3)
        self.label_52.setObjectName(u"label_52")

        self.formLayout_7.setWidget(2, QFormLayout.LabelRole, self.label_52)

        self.frame_65 = QFrame(self.sdp_form_layout_3)
        self.frame_65.setObjectName(u"frame_65")
        self.frame_65.setStyleSheet(u"background: rgb(255, 255, 255)")
        self.frame_65.setFrameShape(QFrame.StyledPanel)
        self.frame_65.setFrameShadow(QFrame.Raised)

        self.formLayout_7.setWidget(2, QFormLayout.FieldRole, self.frame_65)


        self.horizontalLayout_12.addWidget(self.sdp_form_layout_3)

        self.sdp_sn_layout_3 = QFrame(self.frame_59)
        self.sdp_sn_layout_3.setObjectName(u"sdp_sn_layout_3")
        self.sdp_sn_layout_3.setMinimumSize(QSize(333, 0))
        self.sdp_sn_layout_3.setFrameShape(QFrame.StyledPanel)
        self.sdp_sn_layout_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.sdp_sn_layout_3)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.label_53 = QLabel(self.sdp_sn_layout_3)
        self.label_53.setObjectName(u"label_53")

        self.gridLayout_9.addWidget(self.label_53, 1, 0, 1, 1)

        self.frame_66 = QFrame(self.sdp_sn_layout_3)
        self.frame_66.setObjectName(u"frame_66")
        self.frame_66.setFrameShape(QFrame.StyledPanel)
        self.frame_66.setFrameShadow(QFrame.Raised)

        self.gridLayout_9.addWidget(self.frame_66, 3, 1, 1, 1)

        self.frame_67 = QFrame(self.sdp_sn_layout_3)
        self.frame_67.setObjectName(u"frame_67")
        self.frame_67.setFrameShape(QFrame.StyledPanel)
        self.frame_67.setFrameShadow(QFrame.Raised)

        self.gridLayout_9.addWidget(self.frame_67, 0, 1, 1, 1)

        self.label_54 = QLabel(self.sdp_sn_layout_3)
        self.label_54.setObjectName(u"label_54")

        self.gridLayout_9.addWidget(self.label_54, 0, 0, 1, 1)

        self.label_55 = QLabel(self.sdp_sn_layout_3)
        self.label_55.setObjectName(u"label_55")

        self.gridLayout_9.addWidget(self.label_55, 2, 0, 1, 1)

        self.frame_68 = QFrame(self.sdp_sn_layout_3)
        self.frame_68.setObjectName(u"frame_68")
        self.frame_68.setStyleSheet(u"background: rgb(255, 255, 255)")
        self.frame_68.setFrameShape(QFrame.StyledPanel)
        self.frame_68.setFrameShadow(QFrame.Raised)

        self.gridLayout_9.addWidget(self.frame_68, 1, 1, 1, 1)

        self.frame_69 = QFrame(self.sdp_sn_layout_3)
        self.frame_69.setObjectName(u"frame_69")
        self.frame_69.setStyleSheet(u"background: rgb(255, 255, 255)")
        self.frame_69.setFrameShape(QFrame.StyledPanel)
        self.frame_69.setFrameShadow(QFrame.Raised)

        self.gridLayout_9.addWidget(self.frame_69, 2, 1, 1, 1)


        self.horizontalLayout_12.addWidget(self.sdp_sn_layout_3)

        self.frame_70 = QFrame(self.frame_59)
        self.frame_70.setObjectName(u"frame_70")
        self.frame_70.setFrameShape(QFrame.StyledPanel)
        self.frame_70.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_70)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_56 = QLabel(self.frame_70)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setMinimumSize(QSize(0, 20))
        self.label_56.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_17.addWidget(self.label_56)

        self.frame_71 = QFrame(self.frame_70)
        self.frame_71.setObjectName(u"frame_71")
        self.frame_71.setStyleSheet(u"background: rgb(255, 255, 255)")
        self.frame_71.setFrameShape(QFrame.StyledPanel)
        self.frame_71.setFrameShadow(QFrame.Raised)

        self.verticalLayout_17.addWidget(self.frame_71)


        self.horizontalLayout_12.addWidget(self.frame_70)

        self.sdp_cost_layout_3 = QFrame(self.frame_59)
        self.sdp_cost_layout_3.setObjectName(u"sdp_cost_layout_3")
        self.sdp_cost_layout_3.setMinimumSize(QSize(300, 0))
        self.sdp_cost_layout_3.setFrameShape(QFrame.StyledPanel)
        self.sdp_cost_layout_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_10 = QGridLayout(self.sdp_cost_layout_3)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.label_57 = QLabel(self.sdp_cost_layout_3)
        self.label_57.setObjectName(u"label_57")

        self.gridLayout_10.addWidget(self.label_57, 0, 0, 1, 1)

        self.label_58 = QLabel(self.sdp_cost_layout_3)
        self.label_58.setObjectName(u"label_58")

        self.gridLayout_10.addWidget(self.label_58, 1, 0, 1, 1)

        self.label_59 = QLabel(self.sdp_cost_layout_3)
        self.label_59.setObjectName(u"label_59")

        self.gridLayout_10.addWidget(self.label_59, 2, 0, 1, 1)

        self.frame_72 = QFrame(self.sdp_cost_layout_3)
        self.frame_72.setObjectName(u"frame_72")
        self.frame_72.setStyleSheet(u"background: rgb(255, 255, 255)")
        self.frame_72.setFrameShape(QFrame.StyledPanel)
        self.frame_72.setFrameShadow(QFrame.Raised)

        self.gridLayout_10.addWidget(self.frame_72, 0, 1, 1, 1)

        self.frame_73 = QFrame(self.sdp_cost_layout_3)
        self.frame_73.setObjectName(u"frame_73")
        self.frame_73.setStyleSheet(u"background: rgb(255, 255, 255)")
        self.frame_73.setFrameShape(QFrame.StyledPanel)
        self.frame_73.setFrameShadow(QFrame.Raised)

        self.gridLayout_10.addWidget(self.frame_73, 1, 1, 1, 1)

        self.frame_74 = QFrame(self.sdp_cost_layout_3)
        self.frame_74.setObjectName(u"frame_74")
        self.frame_74.setStyleSheet(u"background: rgb(255, 255, 255)")
        self.frame_74.setFrameShape(QFrame.StyledPanel)
        self.frame_74.setFrameShadow(QFrame.Raised)

        self.gridLayout_10.addWidget(self.frame_74, 2, 1, 1, 1)


        self.horizontalLayout_12.addWidget(self.sdp_cost_layout_3)


        self.verticalLayout_21.addWidget(self.frame_59)

        self.frame_75 = QFrame(self.frame_58)
        self.frame_75.setObjectName(u"frame_75")
        self.frame_75.setMinimumSize(QSize(0, 80))
        self.frame_75.setStyleSheet(u"background:rgb(64, 255, 84)")
        self.frame_75.setFrameShape(QFrame.StyledPanel)
        self.frame_75.setFrameShadow(QFrame.Raised)

        self.verticalLayout_21.addWidget(self.frame_75)

        self.frame_76 = QFrame(self.frame_58)
        self.frame_76.setObjectName(u"frame_76")
        self.frame_76.setMinimumSize(QSize(0, 157))
        self.frame_76.setStyleSheet(u"background:rgb(0, 26, 0)")
        self.frame_76.setFrameShape(QFrame.StyledPanel)
        self.frame_76.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_76)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.tableView_3 = QTableView(self.frame_76)
        self.tableView_3.setObjectName(u"tableView_3")

        self.horizontalLayout_13.addWidget(self.tableView_3)


        self.verticalLayout_21.addWidget(self.frame_76)


        self.horizontalLayout_11.addWidget(self.frame_58)

        self.stock_parent_tab.addTab(self.accessories_tab, "")

        self.horizontalLayout_3.addWidget(self.stock_parent_tab)


        self.verticalLayout_9.addWidget(self.stock_tab_frame)

        self.scrollArea_3.setWidget(self.stockContents)

        self.page_3_layout.addWidget(self.scrollArea_3)

        self.pages.addWidget(self.stock)

        self.main_pages_layout.addWidget(self.pages)


        self.retranslateUi(MainPages)

        self.pages.setCurrentIndex(0)
        self.stock_parent_tab.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainPages)
    # setupUi

    def retranslateUi(self, MainPages):
        MainPages.setWindowTitle(QCoreApplication.translate("MainPages", u"Form", None))
        self.label_41.setText(QCoreApplication.translate("MainPages", u"welcome to Laky phone shop p.o.s", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainPages", u"Login", None))
        self.label_31.setText(QCoreApplication.translate("MainPages", u"User name :", None))
        self.label_40.setText(QCoreApplication.translate("MainPages", u"Password:", None))
        self.login_form_info.setText("")
        self.label.setText(QCoreApplication.translate("MainPages", u"Dashboard", None))
        self.customer_group.setTitle(QCoreApplication.translate("MainPages", u"Customer | Cart", None))
        self.label_3.setText(QCoreApplication.translate("MainPages", u"Name :", None))
        self.label_2.setText(QCoreApplication.translate("MainPages", u"Contact :", None))
        self.label_4.setText(QCoreApplication.translate("MainPages", u"Cart id", None))
        self.label_25.setText(QCoreApplication.translate("MainPages", u"total Cart", None))
        self.phone_group.setTitle(QCoreApplication.translate("MainPages", u"Phone", None))
        self.label_7.setText(QCoreApplication.translate("MainPages", u"Imei / meid :", None))
        self.label_6.setText(QCoreApplication.translate("MainPages", u"Model :", None))
        self.label_5.setText(QCoreApplication.translate("MainPages", u"Type :", None))
        self.label_8.setText(QCoreApplication.translate("MainPages", u"SN :", None))
        self.label_18.setText(QCoreApplication.translate("MainPages", u"Qty", None))
        self.label_16.setText(QCoreApplication.translate("MainPages", u"Bar/QR reader :", None))
        self.label_17.setText(QCoreApplication.translate("MainPages", u".....................................", None))
        self.cost_group.setTitle(QCoreApplication.translate("MainPages", u"Cost", None))
        self.label_9.setText(QCoreApplication.translate("MainPages", u"Price :", None))
        self.label_10.setText(QCoreApplication.translate("MainPages", u"discount :", None))
        self.label_11.setText(QCoreApplication.translate("MainPages", u"tax :", None))
        self.label_12.setText(QCoreApplication.translate("MainPages", u"paymant :", None))
        self.label_23.setText(QCoreApplication.translate("MainPages", u"Search :", None))
        self.service_customer_group.setTitle(QCoreApplication.translate("MainPages", u"Customer", None))
        self.label_13.setText(QCoreApplication.translate("MainPages", u"Name : ", None))
        self.label_14.setText(QCoreApplication.translate("MainPages", u"contact :", None))
        self.label_15.setText(QCoreApplication.translate("MainPages", u"Email", None))
        self.label_30.setText(QCoreApplication.translate("MainPages", u"Next of kin", None))
        self.service_phon_group.setTitle(QCoreApplication.translate("MainPages", u"GroupBox", None))
        self.label_19.setText(QCoreApplication.translate("MainPages", u"Type:", None))
        self.label_22.setText(QCoreApplication.translate("MainPages", u"Model:", None))
        self.label_20.setText(QCoreApplication.translate("MainPages", u"imei/meid", None))
        self.label_27.setText(QCoreApplication.translate("MainPages", u"repairer", None))
        self.label_26.setText(QCoreApplication.translate("MainPages", u"SN", None))
        self.label_21.setText(QCoreApplication.translate("MainPages", u"Fault ", None))
        self.label_28.setText(QCoreApplication.translate("MainPages", u"state", None))
        self.service_cost_group.setTitle(QCoreApplication.translate("MainPages", u"GroupBox", None))
        self.label_24.setText(QCoreApplication.translate("MainPages", u"IMPORTANT NOTICES", None))
        self.label_29.setText(QCoreApplication.translate("MainPages", u"It it recommende to read individual item or . For more details please to the documentation ", None))
        self.label_48.setText(QCoreApplication.translate("MainPages", u"Type :", None))
        self.label_60.setText(QCoreApplication.translate("MainPages", u"Model :", None))
        self.label_61.setText(QCoreApplication.translate("MainPages", u"product code:", None))
        self.label_33.setText(QCoreApplication.translate("MainPages", u"Date:", None))
        self.label_37.setText(QCoreApplication.translate("MainPages", u"Prefer code :", None))
        self.label_35.setText(QCoreApplication.translate("MainPages", u"Contact:", None))
        self.label_34.setText(QCoreApplication.translate("MainPages", u"Suplier:", None))
        self.label_62.setText(QCoreApplication.translate("MainPages", u"SP/Unit", None))
        self.label_63.setText(QCoreApplication.translate("MainPages", u"CP/Unit:", None))
        self.label_32.setText(QCoreApplication.translate("MainPages", u"Quantity:", None))
        self.label_36.setText(QCoreApplication.translate("MainPages", u"Tax \"%\" :", None))
        self.label_38.setText(QCoreApplication.translate("MainPages", u"QR/Bar code reader :", None))
        self.label_39.setText(QCoreApplication.translate("MainPages", u"Search Key :", None))
        self.stock_parent_tab.setTabText(self.stock_parent_tab.indexOf(self.phone_tab), QCoreApplication.translate("MainPages", u"Phone", None))
        self.label_47.setText(QCoreApplication.translate("MainPages", u"Type :", None))
        self.label_51.setText(QCoreApplication.translate("MainPages", u"Model :", None))
        self.label_52.setText(QCoreApplication.translate("MainPages", u"Suplier :", None))
        self.label_53.setText(QCoreApplication.translate("MainPages", u"QR/ Bar Code :", None))
        self.label_54.setText(QCoreApplication.translate("MainPages", u"Select type :", None))
        self.label_55.setText(QCoreApplication.translate("MainPages", u"Quantity", None))
        self.label_56.setText(QCoreApplication.translate("MainPages", u"Imei/SN/Meid list", None))
        self.label_57.setText(QCoreApplication.translate("MainPages", u"Cost Price", None))
        self.label_58.setText(QCoreApplication.translate("MainPages", u"Selling Price", None))
        self.label_59.setText(QCoreApplication.translate("MainPages", u"TextLabel", None))
        self.stock_parent_tab.setTabText(self.stock_parent_tab.indexOf(self.accessories_tab), QCoreApplication.translate("MainPages", u"Accessories", None))
    # retranslateUi

