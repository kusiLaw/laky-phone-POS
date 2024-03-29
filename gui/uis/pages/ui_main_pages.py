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
        MainPages.resize(1193, 770)
        MainPages.setStyleSheet(u"font-family:\"Segoe UI\"")
        self.verticalLayout_41 = QVBoxLayout(MainPages)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.pages = QStackedWidget(MainPages)
        self.pages.setObjectName(u"pages")
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
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
        self.login_content.setFont(font)
        self.login_content.setStyleSheet(u"/**background:rgb(73, 255, 204);**/")
        self.login_content.setFrameShape(QFrame.NoFrame)
        self.login_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.login_content)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 0, 0, 0)
        self.frame_4 = QFrame(self.login_content)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFont(font)
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
        self.frame_2.setFont(font)
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_2)
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(-1, 0, 0, 0)
        self.groupBox = QGroupBox(self.frame_2)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet(u"font-size: 24px;\n"
"")
        self.verticalLayout_29 = QVBoxLayout(self.groupBox)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(11, -1, -1, -1)
        self.content = QFrame(self.groupBox)
        self.content.setObjectName(u"content")
        self.content.setMaximumSize(QSize(490, 16777215))
        self.content.setFont(font)
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
        self.login_form.setFont(font)
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
        self.frame_3.setFont(font)
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
        self.label_31.setFont(font)
        self.label_31.setStyleSheet(u"font-size: 18px;")
        self.label_31.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.label_31, 0, 0, 1, 1)

        self.label_40 = QLabel(self.login_form)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setMaximumSize(QSize(120, 16777215))
        self.label_40.setFont(font)
        self.label_40.setStyleSheet(u"font-size: 18px;")
        self.label_40.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.label_40, 1, 0, 1, 1)

        self.frame_33 = QFrame(self.login_form)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setMaximumSize(QSize(400, 16777215))
        self.frame_33.setFont(font)
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
        self.buttons.setFont(font)
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
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setItalic(True)
        self.login_form_info.setFont(font1)
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
        self.dasboard.setFont(font)
        self.dasboard.setStyleSheet(u"font-family:\"Segoe UI\"")
        self.verticalLayout_31 = QVBoxLayout(self.dasboard)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.frame = QFrame(self.dasboard)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 170))
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.frame_55 = QFrame(self.frame)
        self.frame_55.setObjectName(u"frame_55")
        self.frame_55.setMinimumSize(QSize(300, 0))
        self.frame_55.setFrameShape(QFrame.NoFrame)
        self.frame_55.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frame_55)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_55)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color:#8a95aa;\n"
"font-size: 40px;\n"
"text-transform: uppercase;\n"
"font-weight: 700;\n"
"text-align: center;\n"
"text-shadow: 0 15px 40px rgba(0,0,0, 0.6);")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_30.addWidget(self.label)


        self.horizontalLayout_10.addWidget(self.frame_55)

        self.frame_60 = QFrame(self.frame)
        self.frame_60.setObjectName(u"frame_60")
        self.frame_60.setMinimumSize(QSize(0, 0))
        self.frame_60.setMaximumSize(QSize(500, 16777215))
        self.frame_60.setStyleSheet(u"")
        self.frame_60.setFrameShape(QFrame.NoFrame)
        self.frame_60.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_60)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(426, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer)

        self.frame_54 = QFrame(self.frame_60)
        self.frame_54.setObjectName(u"frame_54")
        self.frame_54.setMaximumSize(QSize(500, 16777215))
        self.frame_54.setStyleSheet(u"font-size: 20px;\n"
"color:#8a95aa;\n"
"\n"
"font-weight: 700;")
        self.frame_54.setFrameShape(QFrame.StyledPanel)
        self.frame_54.setFrameShadow(QFrame.Raised)
        self.formLayout_3 = QFormLayout(self.frame_54)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setHorizontalSpacing(10)
        self.formLayout_3.setVerticalSpacing(10)
        self.formLayout_3.setContentsMargins(150, 15, 0, -1)
        self.label_44 = QLabel(self.frame_54)
        self.label_44.setObjectName(u"label_44")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_44)

        self.dash_user_name = QLabel(self.frame_54)
        self.dash_user_name.setObjectName(u"dash_user_name")
        self.dash_user_name.setStyleSheet(u"text-style: italic")
        self.dash_user_name.setWordWrap(True)

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.dash_user_name)

        self.label_45 = QLabel(self.frame_54)
        self.label_45.setObjectName(u"label_45")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_45)

        self.dash_role = QLabel(self.frame_54)
        self.dash_role.setObjectName(u"dash_role")
        self.dash_role.setWordWrap(True)

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.dash_role)

        self.label_50 = QLabel(self.frame_54)
        self.label_50.setObjectName(u"label_50")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.label_50)

        self.dash_email = QLabel(self.frame_54)
        self.dash_email.setObjectName(u"dash_email")
        self.dash_email.setWordWrap(True)

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.dash_email)

        self.label_64 = QLabel(self.frame_54)
        self.label_64.setObjectName(u"label_64")

        self.formLayout_3.setWidget(3, QFormLayout.LabelRole, self.label_64)

        self.dash_last_seen = QLabel(self.frame_54)
        self.dash_last_seen.setObjectName(u"dash_last_seen")
        self.dash_last_seen.setWordWrap(True)

        self.formLayout_3.setWidget(3, QFormLayout.FieldRole, self.dash_last_seen)


        self.horizontalLayout_15.addWidget(self.frame_54)


        self.horizontalLayout_10.addWidget(self.frame_60)


        self.verticalLayout_31.addWidget(self.frame)

        self.frame_24 = QFrame(self.dasboard)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setMaximumSize(QSize(16777215, 16777215))
        self.frame_24.setStyleSheet(u"background:transparent")
        self.frame_24.setFrameShape(QFrame.NoFrame)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.frame_24)
        self.verticalLayout_34.setSpacing(0)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_4 = QScrollArea(self.frame_24)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        self.scrollArea_4.setFrameShape(QFrame.NoFrame)
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1149, 549))
        self.verticalLayout_35 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_35.setSpacing(0)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.frame_86 = QFrame(self.scrollAreaWidgetContents)
        self.frame_86.setObjectName(u"frame_86")
        self.frame_86.setStyleSheet(u"")
        self.frame_86.setFrameShape(QFrame.NoFrame)
        self.frame_86.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_86)
        self.horizontalLayout_16.setSpacing(20)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.chart_stock_sales = QFrame(self.frame_86)
        self.chart_stock_sales.setObjectName(u"chart_stock_sales")
        self.chart_stock_sales.setStyleSheet(u"background:#1e2229;")
        self.chart_stock_sales.setFrameShape(QFrame.NoFrame)
        self.chart_stock_sales.setFrameShadow(QFrame.Raised)
        self.verticalLayout_37 = QVBoxLayout(self.chart_stock_sales)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.frame_88 = QFrame(self.chart_stock_sales)
        self.frame_88.setObjectName(u"frame_88")
        self.frame_88.setLayoutDirection(Qt.LeftToRight)
        self.frame_88.setAutoFillBackground(False)
        self.frame_88.setStyleSheet(u"padding: 0% 50%;\n"
"")
        self.frame_88.setFrameShape(QFrame.NoFrame)
        self.frame_88.setFrameShadow(QFrame.Raised)
        self.stock_per_chart_frame = QVBoxLayout(self.frame_88)
        self.stock_per_chart_frame.setObjectName(u"stock_per_chart_frame")
        self.stock_per_chart_frame.setContentsMargins(20, 15, 20, 10)

        self.verticalLayout_37.addWidget(self.frame_88)

        self.frame_89 = QFrame(self.chart_stock_sales)
        self.frame_89.setObjectName(u"frame_89")
        self.frame_89.setStyleSheet(u"font-size: 20px;\n"
"color:#8a95aa;\n"
"\n"
"font-weight: 700;")
        self.frame_89.setFrameShape(QFrame.StyledPanel)
        self.frame_89.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.frame_89)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.label_43 = QLabel(self.frame_89)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setMaximumSize(QSize(16777215, 40))
        self.label_43.setStyleSheet(u"color:#568af2;\n"
"font-size:24px;")
        self.label_43.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.label_43, 0, 0, 1, 2)

        self.frame_62 = QFrame(self.frame_89)
        self.frame_62.setObjectName(u"frame_62")
        self.frame_62.setFrameShape(QFrame.NoFrame)
        self.frame_62.setFrameShadow(QFrame.Raised)
        self.stock_analysis_frame = QVBoxLayout(self.frame_62)
        self.stock_analysis_frame.setSpacing(0)
        self.stock_analysis_frame.setObjectName(u"stock_analysis_frame")
        self.stock_analysis_frame.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_8.addWidget(self.frame_62, 1, 0, 1, 2)


        self.verticalLayout_37.addWidget(self.frame_89)


        self.horizontalLayout_16.addWidget(self.chart_stock_sales)

        self.chart_average = QFrame(self.frame_86)
        self.chart_average.setObjectName(u"chart_average")
        self.chart_average.setStyleSheet(u"background:#1e2229;")
        self.chart_average.setFrameShape(QFrame.NoFrame)
        self.chart_average.setFrameShadow(QFrame.Raised)
        self.verticalLayout_38 = QVBoxLayout(self.chart_average)
        self.verticalLayout_38.setSpacing(7)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.frame_90 = QFrame(self.chart_average)
        self.frame_90.setObjectName(u"frame_90")
        self.frame_90.setStyleSheet(u"padding: 0% 50%;")
        self.frame_90.setFrameShape(QFrame.NoFrame)
        self.frame_90.setFrameShadow(QFrame.Raised)
        self.daily_sale_avg_frame = QVBoxLayout(self.frame_90)
        self.daily_sale_avg_frame.setObjectName(u"daily_sale_avg_frame")
        self.daily_sale_avg_frame.setContentsMargins(20, 15, 20, 10)

        self.verticalLayout_38.addWidget(self.frame_90)

        self.frame_91 = QFrame(self.chart_average)
        self.frame_91.setObjectName(u"frame_91")
        self.frame_91.setStyleSheet(u"font-size: 20px;\n"
"color:#8a95aa;\n"
"\n"
"font-weight: 700;")
        self.frame_91.setFrameShape(QFrame.NoFrame)
        self.frame_91.setFrameShadow(QFrame.Plain)
        self.gridLayout_13 = QGridLayout(self.frame_91)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setContentsMargins(10, 10, 10, 0)
        self.label_71 = QLabel(self.frame_91)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setMaximumSize(QSize(16777215, 40))
        self.label_71.setStyleSheet(u"color: #568af2;\n"
"font-size:24px;")
        self.label_71.setAlignment(Qt.AlignCenter)

        self.gridLayout_13.addWidget(self.label_71, 0, 0, 1, 2)

        self.frame_87 = QFrame(self.frame_91)
        self.frame_87.setObjectName(u"frame_87")
        self.frame_87.setFrameShape(QFrame.NoFrame)
        self.frame_87.setFrameShadow(QFrame.Raised)
        self.dash_avg_frame = QVBoxLayout(self.frame_87)
        self.dash_avg_frame.setSpacing(0)
        self.dash_avg_frame.setObjectName(u"dash_avg_frame")
        self.dash_avg_frame.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_13.addWidget(self.frame_87, 1, 0, 1, 2)


        self.verticalLayout_38.addWidget(self.frame_91)


        self.horizontalLayout_16.addWidget(self.chart_average)

        self.chart_extra = QFrame(self.frame_86)
        self.chart_extra.setObjectName(u"chart_extra")
        self.chart_extra.setStyleSheet(u"")
        self.chart_extra.setFrameShape(QFrame.StyledPanel)
        self.chart_extra.setFrameShadow(QFrame.Raised)
        self.verticalLayout_36 = QVBoxLayout(self.chart_extra)
        self.verticalLayout_36.setSpacing(20)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.frame_83 = QFrame(self.chart_extra)
        self.frame_83.setObjectName(u"frame_83")
        self.frame_83.setStyleSheet(u"background:#1e2229;")
        self.frame_83.setFrameShape(QFrame.StyledPanel)
        self.frame_83.setFrameShadow(QFrame.Raised)
        self.gridLayout_12 = QGridLayout(self.frame_83)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setHorizontalSpacing(0)
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)
        self.text_collapse2 = QLabel(self.frame_83)
        self.text_collapse2.setObjectName(u"text_collapse2")
        self.text_collapse2.setMaximumSize(QSize(16777215, 0))

        self.gridLayout_12.addWidget(self.text_collapse2, 1, 0, 1, 1)

        self.text_collapse1 = QLabel(self.frame_83)
        self.text_collapse1.setObjectName(u"text_collapse1")
        self.text_collapse1.setMaximumSize(QSize(16777215, 0))

        self.gridLayout_12.addWidget(self.text_collapse1, 1, 1, 1, 1)

        self.todays_sales = QLabel(self.frame_83)
        self.todays_sales.setObjectName(u"todays_sales")
        self.todays_sales.setStyleSheet(u"color:#00ff7f;\n"
"font-size: 55px;\n"
"text-transform: uppercase;\n"
"font-weight: 800;\n"
"text-align: center;\n"
"text-shadow: 0 15px 40px rgba(0,0,0, 0.6)")
        self.todays_sales.setAlignment(Qt.AlignCenter)

        self.gridLayout_12.addWidget(self.todays_sales, 0, 0, 1, 2)


        self.verticalLayout_36.addWidget(self.frame_83)

        self.frame_85 = QFrame(self.chart_extra)
        self.frame_85.setObjectName(u"frame_85")
        self.frame_85.setStyleSheet(u"color:#8a95aa;\n"
"font-size: 20px;\n"
"background:#1e2229;")
        self.frame_85.setFrameShape(QFrame.StyledPanel)
        self.frame_85.setFrameShadow(QFrame.Raised)
        self.verticalLayout_39 = QVBoxLayout(self.frame_85)
        self.verticalLayout_39.setSpacing(0)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(0, -1, 0, 0)
        self.frame_61 = QFrame(self.frame_85)
        self.frame_61.setObjectName(u"frame_61")
        self.frame_61.setStyleSheet(u"")
        self.frame_61.setFrameShape(QFrame.StyledPanel)
        self.frame_61.setFrameShadow(QFrame.Raised)
        self.verticalLayout_40 = QVBoxLayout(self.frame_61)
        self.verticalLayout_40.setSpacing(0)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.label_68 = QLabel(self.frame_61)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setMinimumSize(QSize(0, 60))
        self.label_68.setStyleSheet(u"color:#dce1ec")
        self.label_68.setAlignment(Qt.AlignCenter)

        self.verticalLayout_40.addWidget(self.label_68)


        self.verticalLayout_39.addWidget(self.frame_61)

        self.frame_8 = QFrame(self.frame_85)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setStyleSheet(u"")
        self.frame_8.setFrameShape(QFrame.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.dash_purchase_frame = QVBoxLayout(self.frame_8)
        self.dash_purchase_frame.setSpacing(0)
        self.dash_purchase_frame.setObjectName(u"dash_purchase_frame")
        self.dash_purchase_frame.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_39.addWidget(self.frame_8)


        self.verticalLayout_36.addWidget(self.frame_85)


        self.horizontalLayout_16.addWidget(self.chart_extra)


        self.verticalLayout_35.addWidget(self.frame_86)

        self.chart_reserve_height_collapse = QFrame(self.scrollAreaWidgetContents)
        self.chart_reserve_height_collapse.setObjectName(u"chart_reserve_height_collapse")
        self.chart_reserve_height_collapse.setMaximumSize(QSize(16777215, 0))
        self.chart_reserve_height_collapse.setStyleSheet(u"background:pink")
        self.chart_reserve_height_collapse.setFrameShape(QFrame.StyledPanel)
        self.chart_reserve_height_collapse.setFrameShadow(QFrame.Raised)

        self.verticalLayout_35.addWidget(self.chart_reserve_height_collapse)

        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_34.addWidget(self.scrollArea_4)


        self.verticalLayout_31.addWidget(self.frame_24)

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
        self.contents.setGeometry(QRect(0, 0, 1171, 748))
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
        self.phoneform_customer_section.setMinimumSize(QSize(400, 0))
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
        self.customer_group.setEnabled(True)
        self.customer_group.setMinimumSize(QSize(396, 0))
        self.customer_group.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout_4 = QGridLayout(self.customer_group)
        self.gridLayout_4.setSpacing(7)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(15, 0, 20, 5)
        self.label_25 = QLabel(self.customer_group)
        self.label_25.setObjectName(u"label_25")

        self.gridLayout_4.addWidget(self.label_25, 3, 0, 1, 1)

        self.label_4 = QLabel(self.customer_group)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"")

        self.gridLayout_4.addWidget(self.label_4, 2, 0, 1, 1)

        self.frame_14 = QFrame(self.customer_group)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMinimumSize(QSize(0, 15))
        self.frame_14.setStyleSheet(u"")
        self.frame_14.setFrameShape(QFrame.NoFrame)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.phone_order_id_frame = QVBoxLayout(self.frame_14)
        self.phone_order_id_frame.setSpacing(0)
        self.phone_order_id_frame.setObjectName(u"phone_order_id_frame")
        self.phone_order_id_frame.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_4.addWidget(self.frame_14, 3, 1, 1, 1)

        self.customer_name = QFrame(self.customer_group)
        self.customer_name.setObjectName(u"customer_name")
        self.customer_name.setMaximumSize(QSize(16777215, 60))
        self.customer_name.setStyleSheet(u"")
        self.customer_name.setFrameShape(QFrame.NoFrame)
        self.customer_name.setFrameShadow(QFrame.Raised)
        self.customer_name_edit = QVBoxLayout(self.customer_name)
        self.customer_name_edit.setSpacing(0)
        self.customer_name_edit.setObjectName(u"customer_name_edit")
        self.customer_name_edit.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_4.addWidget(self.customer_name, 0, 1, 1, 1)

        self.customer_contact = QFrame(self.customer_group)
        self.customer_contact.setObjectName(u"customer_contact")
        self.customer_contact.setStyleSheet(u"")
        self.customer_contact.setFrameShape(QFrame.NoFrame)
        self.customer_contact.setFrameShadow(QFrame.Raised)
        self.customer_contact_edit = QVBoxLayout(self.customer_contact)
        self.customer_contact_edit.setSpacing(0)
        self.customer_contact_edit.setObjectName(u"customer_contact_edit")
        self.customer_contact_edit.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_4.addWidget(self.customer_contact, 1, 1, 1, 1)

        self.cart_id = QFrame(self.customer_group)
        self.cart_id.setObjectName(u"cart_id")
        self.cart_id.setMinimumSize(QSize(0, 15))
        self.cart_id.setStyleSheet(u"")
        self.cart_id.setFrameShape(QFrame.NoFrame)
        self.cart_id.setFrameShadow(QFrame.Raised)
        self.phone_date_frame = QVBoxLayout(self.cart_id)
        self.phone_date_frame.setSpacing(0)
        self.phone_date_frame.setObjectName(u"phone_date_frame")
        self.phone_date_frame.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_4.addWidget(self.cart_id, 2, 1, 1, 1)

        self.label_3 = QLabel(self.customer_group)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 0))
        self.label_3.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_4.addWidget(self.label_3, 0, 0, 1, 1)

        self.label_2 = QLabel(self.customer_group)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_4.addWidget(self.label_2, 1, 0, 1, 1)


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
        self.phone_group.setStyleSheet(u"/**background:red**/")
        self.gridLayout_2 = QGridLayout(self.phone_group)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(0)
        self.gridLayout_2.setVerticalSpacing(5)
        self.gridLayout_2.setContentsMargins(10, 5, 10, 10)
        self.label_7 = QLabel(self.phone_group)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_7, 2, 0, 1, 1)

        self.label_5 = QLabel(self.phone_group)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(60, 0))
        self.label_5.setMaximumSize(QSize(60, 16777215))
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)

        self.frame_9 = QFrame(self.phone_group)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setStyleSheet(u"/**background:green**/")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.phone_model_edit = QVBoxLayout(self.frame_9)
        self.phone_model_edit.setSpacing(0)
        self.phone_model_edit.setObjectName(u"phone_model_edit")
        self.phone_model_edit.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_2.addWidget(self.frame_9, 2, 1, 1, 3)

        self.label_8 = QLabel(self.phone_group)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"")
        self.label_8.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_8, 3, 0, 1, 1)

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

        self.frame_22 = QFrame(self.phone_group)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setMinimumSize(QSize(100, 0))
        self.frame_22.setStyleSheet(u"/**background:green**/")
        self.frame_22.setFrameShape(QFrame.NoFrame)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.phone_type_edit = QVBoxLayout(self.frame_22)
        self.phone_type_edit.setSpacing(0)
        self.phone_type_edit.setObjectName(u"phone_type_edit")
        self.phone_type_edit.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_2.addWidget(self.frame_22, 0, 1, 1, 3)

        self.frame_10 = QFrame(self.phone_group)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setStyleSheet(u"")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.phone_sn_edit = QVBoxLayout(self.frame_10)
        self.phone_sn_edit.setSpacing(0)
        self.phone_sn_edit.setObjectName(u"phone_sn_edit")
        self.phone_sn_edit.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_2.addWidget(self.frame_10, 3, 1, 1, 3)


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
        self.cost_group.setStyleSheet(u"")
        self.gridLayout_7 = QGridLayout(self.cost_group)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setHorizontalSpacing(7)
        self.gridLayout_7.setVerticalSpacing(12)
        self.gridLayout_7.setContentsMargins(15, 5, 20, 0)
        self.label_9 = QLabel(self.cost_group)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_7.addWidget(self.label_9, 0, 0, 1, 1)

        self.label_10 = QLabel(self.cost_group)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"")

        self.gridLayout_7.addWidget(self.label_10, 1, 0, 1, 1)

        self.label_12 = QLabel(self.cost_group)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_7.addWidget(self.label_12, 3, 0, 1, 1)

        self.payment = QFrame(self.cost_group)
        self.payment.setObjectName(u"payment")
        self.payment.setStyleSheet(u"\\")
        self.payment.setFrameShape(QFrame.NoFrame)
        self.payment.setFrameShadow(QFrame.Raised)
        self.phone_payment_edit = QVBoxLayout(self.payment)
        self.phone_payment_edit.setObjectName(u"phone_payment_edit")
        self.phone_payment_edit.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_7.addWidget(self.payment, 3, 1, 1, 1)

        self.frame_27 = QFrame(self.cost_group)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setStyleSheet(u"")
        self.frame_27.setFrameShape(QFrame.NoFrame)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.phone_discount_edit = QVBoxLayout(self.frame_27)
        self.phone_discount_edit.setObjectName(u"phone_discount_edit")
        self.phone_discount_edit.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_7.addWidget(self.frame_27, 1, 1, 1, 1)

        self.frame_26 = QFrame(self.cost_group)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setStyleSheet(u"")
        self.frame_26.setFrameShape(QFrame.NoFrame)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.phone_price_edit = QVBoxLayout(self.frame_26)
        self.phone_price_edit.setObjectName(u"phone_price_edit")
        self.phone_price_edit.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_7.addWidget(self.frame_26, 0, 1, 1, 1)

        self.frame_28 = QFrame(self.cost_group)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setStyleSheet(u"\\")
        self.frame_28.setFrameShape(QFrame.NoFrame)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.phone_total_item_frame = QVBoxLayout(self.frame_28)
        self.phone_total_item_frame.setObjectName(u"phone_total_item_frame")
        self.phone_total_item_frame.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_7.addWidget(self.frame_28, 1, 3, 1, 1)

        self.label_6 = QLabel(self.cost_group)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_7.addWidget(self.label_6, 0, 2, 1, 1)

        self.label_46 = QLabel(self.cost_group)
        self.label_46.setObjectName(u"label_46")

        self.gridLayout_7.addWidget(self.label_46, 3, 2, 1, 1)

        self.frame_56 = QFrame(self.cost_group)
        self.frame_56.setObjectName(u"frame_56")
        self.frame_56.setFrameShape(QFrame.NoFrame)
        self.frame_56.setFrameShadow(QFrame.Raised)
        self.phone_tans_code_frame = QVBoxLayout(self.frame_56)
        self.phone_tans_code_frame.setSpacing(0)
        self.phone_tans_code_frame.setObjectName(u"phone_tans_code_frame")
        self.phone_tans_code_frame.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_7.addWidget(self.frame_56, 3, 3, 1, 1)

        self.frame_57 = QFrame(self.cost_group)
        self.frame_57.setObjectName(u"frame_57")
        self.frame_57.setFrameShape(QFrame.NoFrame)
        self.frame_57.setFrameShadow(QFrame.Raised)
        self.phone_total_price_frame = QVBoxLayout(self.frame_57)
        self.phone_total_price_frame.setSpacing(0)
        self.phone_total_price_frame.setObjectName(u"phone_total_price_frame")
        self.phone_total_price_frame.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_7.addWidget(self.frame_57, 0, 3, 1, 1)

        self.label_11 = QLabel(self.cost_group)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_7.addWidget(self.label_11, 1, 2, 1, 1)


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
        self.trrrr = QVBoxLayout(self.frame_13)
        self.trrrr.setSpacing(0)
        self.trrrr.setObjectName(u"trrrr")
        self.trrrr.setContentsMargins(0, 0, 0, 0)

        self.gridLayout.addWidget(self.frame_13, 2, 2, 1, 1)

        self.phone_clear = QFrame(self.phone_button_section)
        self.phone_clear.setObjectName(u"phone_clear")
        self.phone_clear.setMinimumSize(QSize(150, 30))
        self.phone_clear.setStyleSheet(u"")
        self.phone_clear.setFrameShape(QFrame.StyledPanel)
        self.phone_clear.setFrameShadow(QFrame.Raised)
        self.phone_print_layout = QVBoxLayout(self.phone_clear)
        self.phone_print_layout.setSpacing(0)
        self.phone_print_layout.setObjectName(u"phone_print_layout")
        self.phone_print_layout.setContentsMargins(0, 0, 0, 0)

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
        self.phone_clear_layout = QVBoxLayout(self.phone_print)
        self.phone_clear_layout.setSpacing(0)
        self.phone_clear_layout.setObjectName(u"phone_clear_layout")
        self.phone_clear_layout.setContentsMargins(0, 0, 0, 0)

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
        self.phone_all_in_one_layout = QVBoxLayout(self.phone_delete)
        self.phone_all_in_one_layout.setSpacing(0)
        self.phone_all_in_one_layout.setObjectName(u"phone_all_in_one_layout")
        self.phone_all_in_one_layout.setContentsMargins(0, 0, 0, 0)

        self.gridLayout.addWidget(self.phone_delete, 2, 1, 1, 1)

        self.phone_all_in_one = QFrame(self.phone_button_section)
        self.phone_all_in_one.setObjectName(u"phone_all_in_one")
        self.phone_all_in_one.setMinimumSize(QSize(150, 30))
        self.phone_all_in_one.setStyleSheet(u"")
        self.phone_all_in_one.setFrameShape(QFrame.NoFrame)
        self.phone_all_in_one.setFrameShadow(QFrame.Raised)
        self.phone_delete_layout = QVBoxLayout(self.phone_all_in_one)
        self.phone_delete_layout.setSpacing(0)
        self.phone_delete_layout.setObjectName(u"phone_delete_layout")
        self.phone_delete_layout.setContentsMargins(0, 0, 0, 0)

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
        self.database = QWidget()
        self.database.setObjectName(u"database")
        self.database.setStyleSheet(u"font-size: 14pt;")
        self.verticalLayout_42 = QVBoxLayout(self.database)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.frame_92 = QFrame(self.database)
        self.frame_92.setObjectName(u"frame_92")
        self.frame_92.setFrameShape(QFrame.StyledPanel)
        self.frame_92.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_92)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(80, 0, 80, 0)
        self.frame_103 = QFrame(self.frame_92)
        self.frame_103.setObjectName(u"frame_103")
        self.frame_103.setMaximumSize(QSize(16777215, 150))
        self.frame_103.setStyleSheet(u"")
        self.frame_103.setFrameShape(QFrame.NoFrame)
        self.frame_103.setFrameShadow(QFrame.Raised)
        self.verticalLayout_45 = QVBoxLayout(self.frame_103)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.verticalSpacer = QSpacerItem(20, 64, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_45.addItem(self.verticalSpacer)

        self.label_70 = QLabel(self.frame_103)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setStyleSheet(u"color:#8a95aa;\n"
"font-size: 40px;\n"
"\n"
"font-weight: 500;\n"
"text-align: center;\n"
"text-shadow: 0 15px 40px rgba(0,0,0, 0.6);")
        self.label_70.setAlignment(Qt.AlignCenter)

        self.verticalLayout_45.addWidget(self.label_70)


        self.verticalLayout_10.addWidget(self.frame_103)

        self.frame_105 = QFrame(self.frame_92)
        self.frame_105.setObjectName(u"frame_105")
        self.frame_105.setFrameShape(QFrame.NoFrame)
        self.frame_105.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_105)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.frame_107 = QFrame(self.frame_105)
        self.frame_107.setObjectName(u"frame_107")
        self.frame_107.setMinimumSize(QSize(100, 0))
        self.frame_107.setMaximumSize(QSize(100, 16777215))
        self.frame_107.setFrameShape(QFrame.NoFrame)
        self.frame_107.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_17.addWidget(self.frame_107)

        self.frame_94 = QFrame(self.frame_105)
        self.frame_94.setObjectName(u"frame_94")
        self.frame_94.setMaximumSize(QSize(700, 450))
        self.frame_94.setLayoutDirection(Qt.LeftToRight)
        self.frame_94.setStyleSheet(u"")
        self.frame_94.setFrameShape(QFrame.NoFrame)
        self.frame_94.setFrameShadow(QFrame.Raised)
        self.gridLayout_14 = QGridLayout(self.frame_94)
        self.gridLayout_14.setSpacing(15)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setContentsMargins(20, -1, 20, -1)
        self.label_18 = QLabel(self.frame_94)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMaximumSize(QSize(120, 40))

        self.gridLayout_14.addWidget(self.label_18, 1, 0, 1, 1)

        self.label_49 = QLabel(self.frame_94)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_14.addWidget(self.label_49, 2, 0, 1, 1)

        self.line = QFrame(self.frame_94)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_14.addWidget(self.line, 4, 0, 1, 4)

        self.frame_101 = QFrame(self.frame_94)
        self.frame_101.setObjectName(u"frame_101")
        self.frame_101.setMinimumSize(QSize(0, 100))
        self.frame_101.setMaximumSize(QSize(16777215, 100))
        self.frame_101.setStyleSheet(u"")
        self.frame_101.setFrameShape(QFrame.NoFrame)
        self.frame_101.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_101)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(-1, -1, 0, -1)
        self.frame_110 = QFrame(self.frame_101)
        self.frame_110.setObjectName(u"frame_110")
        self.frame_110.setMinimumSize(QSize(313, 0))
        self.frame_110.setMaximumSize(QSize(313, 16777215))
        self.frame_110.setFrameShape(QFrame.NoFrame)
        self.frame_110.setFrameShadow(QFrame.Raised)
        self.verticalLayout_44 = QVBoxLayout(self.frame_110)
        self.verticalLayout_44.setSpacing(0)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.verticalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.error_indicator = QLabel(self.frame_110)
        self.error_indicator.setObjectName(u"error_indicator")
        self.error_indicator.setScaledContents(True)
        self.error_indicator.setWordWrap(True)

        self.verticalLayout_44.addWidget(self.error_indicator)


        self.horizontalLayout_18.addWidget(self.frame_110)

        self.frame_98 = QFrame(self.frame_101)
        self.frame_98.setObjectName(u"frame_98")
        self.frame_98.setFrameShape(QFrame.NoFrame)
        self.frame_98.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.frame_98)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.cont_test_info = QLabel(self.frame_98)
        self.cont_test_info.setObjectName(u"cont_test_info")
        self.cont_test_info.setMinimumSize(QSize(150, 0))
        self.cont_test_info.setScaledContents(True)
        self.cont_test_info.setAlignment(Qt.AlignCenter)
        self.cont_test_info.setWordWrap(True)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.cont_test_info)

        self.frame_112 = QFrame(self.frame_98)
        self.frame_112.setObjectName(u"frame_112")
        self.frame_112.setMinimumSize(QSize(30, 42))
        self.frame_112.setFrameShape(QFrame.NoFrame)
        self.frame_112.setFrameShadow(QFrame.Raised)
        self.test_con_frame = QVBoxLayout(self.frame_112)
        self.test_con_frame.setObjectName(u"test_con_frame")
        self.test_con_frame.setContentsMargins(0, 0, 0, 0)

        self.formLayout.setWidget(1, QFormLayout.SpanningRole, self.frame_112)

        self.indicator_frame = QFrame(self.frame_98)
        self.indicator_frame.setObjectName(u"indicator_frame")
        self.indicator_frame.setMinimumSize(QSize(0, 30))
        self.indicator_frame.setMaximumSize(QSize(200, 30))
        self.indicator_frame.setStyleSheet(u"")
        self.indicator_frame.setFrameShape(QFrame.StyledPanel)
        self.indicator_frame.setFrameShadow(QFrame.Raised)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.indicator_frame)


        self.horizontalLayout_18.addWidget(self.frame_98)


        self.gridLayout_14.addWidget(self.frame_101, 5, 0, 1, 4)

        self.frame_95 = QFrame(self.frame_94)
        self.frame_95.setObjectName(u"frame_95")
        self.frame_95.setMaximumSize(QSize(16777215, 16777203))
        self.frame_95.setStyleSheet(u"")
        self.frame_95.setFrameShape(QFrame.NoFrame)
        self.frame_95.setFrameShadow(QFrame.Raised)
        self.engine_frame = QVBoxLayout(self.frame_95)
        self.engine_frame.setSpacing(0)
        self.engine_frame.setObjectName(u"engine_frame")
        self.engine_frame.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_14.addWidget(self.frame_95, 1, 1, 1, 1)

        self.frame_99 = QFrame(self.frame_94)
        self.frame_99.setObjectName(u"frame_99")
        self.frame_99.setStyleSheet(u"")
        self.frame_99.setFrameShape(QFrame.NoFrame)
        self.frame_99.setFrameShadow(QFrame.Raised)
        self.port_frame = QVBoxLayout(self.frame_99)
        self.port_frame.setSpacing(0)
        self.port_frame.setObjectName(u"port_frame")
        self.port_frame.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_14.addWidget(self.frame_99, 2, 3, 1, 1)

        self.frame_97 = QFrame(self.frame_94)
        self.frame_97.setObjectName(u"frame_97")
        self.frame_97.setMaximumSize(QSize(199, 16777215))
        self.frame_97.setStyleSheet(u"")
        self.frame_97.setFrameShape(QFrame.NoFrame)
        self.frame_97.setFrameShadow(QFrame.Raised)
        self.username_db_frame = QVBoxLayout(self.frame_97)
        self.username_db_frame.setObjectName(u"username_db_frame")
        self.username_db_frame.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_14.addWidget(self.frame_97, 3, 1, 1, 1)

        self.frame_100 = QFrame(self.frame_94)
        self.frame_100.setObjectName(u"frame_100")
        self.frame_100.setMaximumSize(QSize(188, 16777215))
        self.frame_100.setStyleSheet(u"")
        self.frame_100.setFrameShape(QFrame.NoFrame)
        self.frame_100.setFrameShadow(QFrame.Raised)
        self.password_db_frame = QVBoxLayout(self.frame_100)
        self.password_db_frame.setSpacing(0)
        self.password_db_frame.setObjectName(u"password_db_frame")
        self.password_db_frame.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_14.addWidget(self.frame_100, 3, 3, 1, 1)

        self.frame_96 = QFrame(self.frame_94)
        self.frame_96.setObjectName(u"frame_96")
        self.frame_96.setStyleSheet(u"")
        self.frame_96.setFrameShape(QFrame.NoFrame)
        self.frame_96.setFrameShadow(QFrame.Raised)
        self.hostname_frame = QVBoxLayout(self.frame_96)
        self.hostname_frame.setSpacing(0)
        self.hostname_frame.setObjectName(u"hostname_frame")
        self.hostname_frame.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_14.addWidget(self.frame_96, 2, 1, 1, 1)

        self.label_67 = QLabel(self.frame_94)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setMaximumSize(QSize(120, 16777215))

        self.gridLayout_14.addWidget(self.label_67, 2, 2, 1, 1)

        self.label_69 = QLabel(self.frame_94)
        self.label_69.setObjectName(u"label_69")
        self.label_69.setMaximumSize(QSize(120, 16777215))

        self.gridLayout_14.addWidget(self.label_69, 3, 2, 1, 1)

        self.label_66 = QLabel(self.frame_94)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_14.addWidget(self.label_66, 3, 0, 1, 1)

        self.frame_102 = QFrame(self.frame_94)
        self.frame_102.setObjectName(u"frame_102")
        self.frame_102.setStyleSheet(u"")
        self.frame_102.setFrameShape(QFrame.NoFrame)
        self.frame_102.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_102)
        self.horizontalLayout_19.setSpacing(14)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 10, 0, 0)
        self.frame_109 = QFrame(self.frame_102)
        self.frame_109.setObjectName(u"frame_109")
        self.frame_109.setMaximumSize(QSize(140, 16777215))
        self.frame_109.setStyleSheet(u"")
        self.frame_109.setFrameShape(QFrame.StyledPanel)
        self.frame_109.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_19.addWidget(self.frame_109)

        self.frame_113 = QFrame(self.frame_102)
        self.frame_113.setObjectName(u"frame_113")
        self.frame_113.setMaximumSize(QSize(16777215, 16777215))
        self.frame_113.setStyleSheet(u"")
        self.frame_113.setFrameShape(QFrame.NoFrame)
        self.frame_113.setFrameShadow(QFrame.Raised)
        self.db_exit_frame = QVBoxLayout(self.frame_113)
        self.db_exit_frame.setSpacing(0)
        self.db_exit_frame.setObjectName(u"db_exit_frame")
        self.db_exit_frame.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_19.addWidget(self.frame_113)

        self.frame_114 = QFrame(self.frame_102)
        self.frame_114.setObjectName(u"frame_114")
        self.frame_114.setMaximumSize(QSize(16777215, 16777215))
        self.frame_114.setStyleSheet(u"")
        self.frame_114.setFrameShape(QFrame.NoFrame)
        self.frame_114.setFrameShadow(QFrame.Raised)
        self.db_restore_frame = QVBoxLayout(self.frame_114)
        self.db_restore_frame.setSpacing(0)
        self.db_restore_frame.setObjectName(u"db_restore_frame")
        self.db_restore_frame.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_19.addWidget(self.frame_114)

        self.frame_115 = QFrame(self.frame_102)
        self.frame_115.setObjectName(u"frame_115")
        self.frame_115.setMaximumSize(QSize(16777215, 16777215))
        self.frame_115.setStyleSheet(u"")
        self.frame_115.setFrameShape(QFrame.NoFrame)
        self.frame_115.setFrameShadow(QFrame.Raised)
        self.db_save_frame = QVBoxLayout(self.frame_115)
        self.db_save_frame.setObjectName(u"db_save_frame")
        self.db_save_frame.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_19.addWidget(self.frame_115)


        self.gridLayout_14.addWidget(self.frame_102, 6, 0, 1, 4)


        self.horizontalLayout_17.addWidget(self.frame_94)

        self.frame_106 = QFrame(self.frame_105)
        self.frame_106.setObjectName(u"frame_106")
        self.frame_106.setMinimumSize(QSize(100, 0))
        self.frame_106.setMaximumSize(QSize(100, 16777215))
        self.frame_106.setFrameShape(QFrame.NoFrame)
        self.frame_106.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_17.addWidget(self.frame_106)


        self.verticalLayout_10.addWidget(self.frame_105)

        self.frame_104 = QFrame(self.frame_92)
        self.frame_104.setObjectName(u"frame_104")
        self.frame_104.setMinimumSize(QSize(0, 150))
        self.frame_104.setMaximumSize(QSize(16777215, 150))
        self.frame_104.setStyleSheet(u"/**background:green")
        self.frame_104.setFrameShape(QFrame.NoFrame)
        self.frame_104.setFrameShadow(QFrame.Raised)

        self.verticalLayout_10.addWidget(self.frame_104)


        self.verticalLayout_42.addWidget(self.frame_92)

        self.pages.addWidget(self.database)
        self.add_user = QWidget()
        self.add_user.setObjectName(u"add_user")
        self.verticalLayout_43 = QVBoxLayout(self.add_user)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.frame_93 = QFrame(self.add_user)
        self.frame_93.setObjectName(u"frame_93")
        self.frame_93.setFrameShape(QFrame.StyledPanel)
        self.frame_93.setFrameShadow(QFrame.Raised)

        self.verticalLayout_43.addWidget(self.frame_93)

        self.pages.addWidget(self.add_user)
        self.service_page = QWidget()
        self.service_page.setObjectName(u"service_page")
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(14)
        self.service_page.setFont(font2)
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
        self.Contents.setGeometry(QRect(0, 0, 1171, 748))
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
        self.dateEdit = QDateEdit(self.service_cost_group)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setGeometry(QRect(50, 60, 201, 71))

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
        self.stock.setFont(font2)
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
        self.stockContents.setGeometry(QRect(0, 0, 1183, 765))
        self.stockContents.setFont(font2)
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
        self.frame_29.setFont(font2)
        self.frame_29.setFrameShape(QFrame.NoFrame)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_29)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(5, 0, 5, 0)
        self.label_29 = QLabel(self.frame_29)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMaximumSize(QSize(16777215, 232))
        self.label_29.setFont(font2)
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
        self.horizontalLayout_14.setSpacing(10)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.sdp_form_layout_4 = QFrame(self.stock_form)
        self.sdp_form_layout_4.setObjectName(u"sdp_form_layout_4")
        self.sdp_form_layout_4.setMinimumSize(QSize(400, 0))
        self.sdp_form_layout_4.setMaximumSize(QSize(16777215, 16777215))
        self.sdp_form_layout_4.setFrameShape(QFrame.NoFrame)
        self.sdp_form_layout_4.setFrameShadow(QFrame.Raised)
        self.formLayout_8 = QFormLayout(self.sdp_form_layout_4)
        self.formLayout_8.setObjectName(u"formLayout_8")
        self.formLayout_8.setHorizontalSpacing(0)
        self.formLayout_8.setVerticalSpacing(18)
        self.formLayout_8.setContentsMargins(0, 20, 0, 0)
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
        self.label_60.setStyleSheet(u"color:#d0d0d0")

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
        self.stock_datetime_frame = QVBoxLayout(self.widget)
        self.stock_datetime_frame.setSpacing(0)
        self.stock_datetime_frame.setObjectName(u"stock_datetime_frame")
        self.stock_datetime_frame.setContentsMargins(0, 0, 0, 0)

        self.formLayout_8.setWidget(3, QFormLayout.FieldRole, self.widget)


        self.horizontalLayout_14.addWidget(self.sdp_form_layout_4)

        self.sdp_sn_layout_4 = QFrame(self.stock_form)
        self.sdp_sn_layout_4.setObjectName(u"sdp_sn_layout_4")
        self.sdp_sn_layout_4.setMinimumSize(QSize(400, 0))
        self.sdp_sn_layout_4.setMaximumSize(QSize(750, 201))
        self.sdp_sn_layout_4.setFrameShape(QFrame.NoFrame)
        self.sdp_sn_layout_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_11 = QGridLayout(self.sdp_sn_layout_4)
        self.gridLayout_11.setSpacing(0)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_38 = QFrame(self.sdp_sn_layout_4)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setFrameShape(QFrame.NoFrame)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_38)
        self.verticalLayout_24.setSpacing(0)
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
        self.label_62.setStyleSheet(u"color:#d0d0d0")

        self.gridLayout_11.addWidget(self.label_62, 1, 0, 1, 1)

        self.label_63 = QLabel(self.sdp_sn_layout_4)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setStyleSheet(u"color:#d0d0d0")

        self.gridLayout_11.addWidget(self.label_63, 0, 0, 1, 1)

        self.label_32 = QLabel(self.sdp_sn_layout_4)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setStyleSheet(u"color:#d0d0d0")

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
        self.stock_qr_layout.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_11.addWidget(self.frame_32, 3, 3, 1, 1)

        self.frame_31 = QFrame(self.sdp_sn_layout_4)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setStyleSheet(u"")
        self.frame_31.setFrameShape(QFrame.NoFrame)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.stock_tax_layout = QVBoxLayout(self.frame_31)
        self.stock_tax_layout.setSpacing(0)
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
        self.stock_unique_code_layout.setSpacing(0)
        self.stock_unique_code_layout.setObjectName(u"stock_unique_code_layout")
        self.stock_unique_code_layout.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_11.addWidget(self.frame_35, 2, 3, 1, 1)


        self.horizontalLayout_14.addWidget(self.sdp_sn_layout_4)

        self.frame_84 = QFrame(self.stock_form)
        self.frame_84.setObjectName(u"frame_84")
        self.frame_84.setMinimumSize(QSize(0, 0))
        self.frame_84.setMaximumSize(QSize(16777215, 16777215))
        self.frame_84.setStyleSheet(u"")
        self.frame_84.setFrameShape(QFrame.NoFrame)
        self.frame_84.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_84)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 5)
        self.frame_52 = QFrame(self.frame_84)
        self.frame_52.setObjectName(u"frame_52")
        self.frame_52.setMaximumSize(QSize(16777215, 16777215))
        self.frame_52.setStyleSheet(u"")
        self.frame_52.setFrameShape(QFrame.NoFrame)
        self.frame_52.setFrameShadow(QFrame.Raised)
        self.stock_list_frame = QVBoxLayout(self.frame_52)
        self.stock_list_frame.setSpacing(0)
        self.stock_list_frame.setObjectName(u"stock_list_frame")
        self.stock_list_frame.setContentsMargins(0, 10, 0, 0)

        self.verticalLayout_14.addWidget(self.frame_52)

        self.frame_53 = QFrame(self.frame_84)
        self.frame_53.setObjectName(u"frame_53")
        self.frame_53.setMaximumSize(QSize(16777215, 30))
        self.frame_53.setFrameShape(QFrame.NoFrame)
        self.frame_53.setFrameShadow(QFrame.Raised)
        self.fr = QHBoxLayout(self.frame_53)
        self.fr.setSpacing(0)
        self.fr.setObjectName(u"fr")
        self.fr.setContentsMargins(0, 0, 0, 0)
        self.label_42 = QLabel(self.frame_53)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setMaximumSize(QSize(80, 16777215))

        self.fr.addWidget(self.label_42)

        self.stock_sn_total = QLabel(self.frame_53)
        self.stock_sn_total.setObjectName(u"stock_sn_total")

        self.fr.addWidget(self.stock_sn_total)


        self.verticalLayout_14.addWidget(self.frame_53)


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
        self.stock_table.setMinimumSize(QSize(0, 180))
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

        self.verticalLayout_41.addWidget(self.pages)


        self.retranslateUi(MainPages)

        self.pages.setCurrentIndex(3)
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
        self.label.setText(QCoreApplication.translate("MainPages", u"DASHBOARD", None))
        self.label_44.setText(QCoreApplication.translate("MainPages", u"Name :", None))
        self.dash_user_name.setText(QCoreApplication.translate("MainPages", u"unknown", None))
        self.label_45.setText(QCoreApplication.translate("MainPages", u"Role :", None))
        self.dash_role.setText(QCoreApplication.translate("MainPages", u"unknown", None))
        self.label_50.setText(QCoreApplication.translate("MainPages", u"Email :", None))
        self.dash_email.setText(QCoreApplication.translate("MainPages", u"unknown", None))
        self.label_64.setText(QCoreApplication.translate("MainPages", u"Last Seen", None))
        self.dash_last_seen.setText(QCoreApplication.translate("MainPages", u"unknown", None))
        self.label_43.setText(QCoreApplication.translate("MainPages", u"Stock Update", None))
        self.label_71.setText(QCoreApplication.translate("MainPages", u"Average Sales", None))
        self.text_collapse2.setText("")
        self.text_collapse1.setText("")
        self.todays_sales.setText(QCoreApplication.translate("MainPages", u"\u00a20.00", None))
        self.label_68.setText(QCoreApplication.translate("MainPages", u"Highly Purchase items", None))
        self.customer_group.setTitle(QCoreApplication.translate("MainPages", u"Customer | Cart", None))
        self.label_25.setText(QCoreApplication.translate("MainPages", u"Oeder ID:", None))
        self.label_4.setText(QCoreApplication.translate("MainPages", u"Date", None))
        self.label_3.setText(QCoreApplication.translate("MainPages", u"Name :", None))
        self.label_2.setText(QCoreApplication.translate("MainPages", u"Contact :", None))
        self.phone_group.setTitle(QCoreApplication.translate("MainPages", u"Phone", None))
        self.label_7.setText(QCoreApplication.translate("MainPages", u"Model :", None))
        self.label_5.setText(QCoreApplication.translate("MainPages", u"Type :", None))
        self.label_8.setText(QCoreApplication.translate("MainPages", u"SN :", None))
        self.label_16.setText(QCoreApplication.translate("MainPages", u"Bar/QR :", None))
        self.label_17.setText(QCoreApplication.translate("MainPages", u".....................................", None))
        self.cost_group.setTitle(QCoreApplication.translate("MainPages", u"Cost", None))
        self.label_9.setText(QCoreApplication.translate("MainPages", u"Price :", None))
        self.label_10.setText(QCoreApplication.translate("MainPages", u"Quantity :", None))
        self.label_12.setText(QCoreApplication.translate("MainPages", u"Payment :", None))
        self.label_6.setText(QCoreApplication.translate("MainPages", u"Total price:", None))
        self.label_46.setText(QCoreApplication.translate("MainPages", u"Trans code :", None))
        self.label_11.setText(QCoreApplication.translate("MainPages", u"Total items:", None))
        self.label_23.setText(QCoreApplication.translate("MainPages", u"Search :", None))
        self.label_70.setText(QCoreApplication.translate("MainPages", u"Database Settings", None))
        self.label_18.setText(QCoreApplication.translate("MainPages", u"Engine :", None))
        self.label_49.setText(QCoreApplication.translate("MainPages", u"Hostname :", None))
        self.error_indicator.setText("")
        self.cont_test_info.setText("")
        self.label_67.setText(QCoreApplication.translate("MainPages", u"Port :", None))
        self.label_69.setText(QCoreApplication.translate("MainPages", u"Password:", None))
        self.label_66.setText(QCoreApplication.translate("MainPages", u"Username :", None))
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
        self.label_48.setText(QCoreApplication.translate("MainPages", u"Brand :", None))
        self.label_60.setText(QCoreApplication.translate("MainPages", u"Model :", None))
        self.label_61.setText(QCoreApplication.translate("MainPages", u"Order ID:", None))
        self.label_33.setText(QCoreApplication.translate("MainPages", u"Date:", None))
        self.label_37.setText(QCoreApplication.translate("MainPages", u"Prefer code :", None))
        self.label_35.setText(QCoreApplication.translate("MainPages", u"Contact:", None))
        self.label_34.setText(QCoreApplication.translate("MainPages", u"Suplier:", None))
        self.label_62.setText(QCoreApplication.translate("MainPages", u"SP/Unit", None))
        self.label_63.setText(QCoreApplication.translate("MainPages", u"CP/Unit:", None))
        self.label_32.setText(QCoreApplication.translate("MainPages", u"Quantity:", None))
        self.label_36.setText(QCoreApplication.translate("MainPages", u"Tax \"%\" :", None))
        self.label_38.setText(QCoreApplication.translate("MainPages", u"QR/Bar code reader :", None))
        self.label_42.setText(QCoreApplication.translate("MainPages", u"Total :", None))
        self.stock_sn_total.setText(QCoreApplication.translate("MainPages", u"0", None))
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

