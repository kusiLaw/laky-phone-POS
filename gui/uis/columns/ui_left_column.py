# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'left_column.ui'
##
## Created by: Qt User Interface Compiler version 6.1.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_LeftColumn(object):
    def setupUi(self, LeftColumn):
        if not LeftColumn.objectName():
            LeftColumn.setObjectName(u"LeftColumn")
        LeftColumn.resize(252, 600)
        LeftColumn.setStyleSheet(u"")
        self.main_pages_layout = QVBoxLayout(LeftColumn)
        self.main_pages_layout.setSpacing(0)
        self.main_pages_layout.setObjectName(u"main_pages_layout")
        self.main_pages_layout.setContentsMargins(5, 5, 5, 5)
        self.menus = QStackedWidget(LeftColumn)
        self.menus.setObjectName(u"menus")
        self.menu_1 = QWidget()
        self.menu_1.setObjectName(u"menu_1")
        self.menu_1.setStyleSheet(u"font: 12pt \"Microsoft Sans Serif\";")
        self.verticalLayout = QVBoxLayout(self.menu_1)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.scrollArea = QScrollArea(self.menu_1)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.Contents = QWidget()
        self.Contents.setObjectName(u"Contents")
        self.Contents.setGeometry(QRect(0, -369, 217, 1064))
        self.Contents.setStyleSheet(u"color:white")
        self.info_layout_holder = QHBoxLayout(self.Contents)
        self.info_layout_holder.setSpacing(0)
        self.info_layout_holder.setObjectName(u"info_layout_holder")
        self.info_layout_holder.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.Contents)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.info_layout = QVBoxLayout(self.frame)
        self.info_layout.setSpacing(0)
        self.info_layout.setObjectName(u"info_layout")
        self.info_layout.setContentsMargins(0, 7, 0, 0)
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 40))
        self.frame_3.setMaximumSize(QSize(16777215, 80))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.heading = QLabel(self.frame_3)
        self.heading.setObjectName(u"heading")
        self.heading.setMinimumSize(QSize(0, 60))
        self.heading.setMaximumSize(QSize(16777215, 80))
        font = QFont()
        font.setFamilies([u"Microsoft Sans Serif"])
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.heading.setFont(font)
        self.heading.setStyleSheet(u"color:  #568af2;\n"
"text-transform: uppercase;\n"
"text-indent: 50px;\n"
"line-height: 1.8;")
        self.heading.setTextFormat(Qt.AutoText)
        self.heading.setScaledContents(False)
        self.heading.setAlignment(Qt.AlignCenter)
        self.heading.setWordWrap(True)
        self.heading.setIndent(-1)
        self.heading.setOpenExternalLinks(False)

        self.verticalLayout_4.addWidget(self.heading)


        self.info_layout.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 0))
        self.frame_4.setMaximumSize(QSize(16777215, 600))
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_4)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frame_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 0))
        self.label_3.setMaximumSize(QSize(16777215, 16777215))
        self.label_3.setStyleSheet(u"color:white;\n"
"text-align: justify;\n"
"")
        self.label_3.setScaledContents(False)
        self.label_3.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.label_3.setWordWrap(True)
        self.label_3.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)

        self.verticalLayout_5.addWidget(self.label_3)


        self.info_layout.addWidget(self.frame_4)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 10))
        self.label_4.setMaximumSize(QSize(16777215, 20))
        self.label_4.setStyleSheet(u"QLabel {\n"
"	color: #568af2;\n"
"}\n"
"QLabel:hover{\n"
"	color : #ff79c6;\n"
"	text-decoration: underline;\n"
"}")
        self.label_4.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.label_4.setWordWrap(True)

        self.info_layout.addWidget(self.label_4)

        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(0, 30))
        self.label_6.setMaximumSize(QSize(16777215, 30))
        self.label_6.setAlignment(Qt.AlignCenter)
        self.label_6.setWordWrap(True)

        self.info_layout.addWidget(self.label_6)

        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(0, 30))
        self.label_7.setMaximumSize(QSize(16777215, 30))
        self.label_7.setStyleSheet(u"QLabel {\n"
"	color: #568af2;\n"
"}\n"
"QLabel:hover{\n"
"	color : #ff79c6;\n"
"	text-decoration: underline;\n"
"}")
        self.label_7.setAlignment(Qt.AlignCenter)
        self.label_7.setWordWrap(True)

        self.info_layout.addWidget(self.label_7)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.info_layout.addWidget(self.label)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 40))
        self.frame_2.setMaximumSize(QSize(16777215, 40))
        self.frame_2.setStyleSheet(u"border:1px solid  #00ff7f")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_10 = QLabel(self.frame_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"border: none")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_10)


        self.info_layout.addWidget(self.frame_2)

        self.label_11 = QLabel(self.frame)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"QLabel {\n"
"	color: #568af2;\n"
"}\n"
"QLabel:hover{\n"
"	color : #ff79c6;\n"
"	text-decoration: underline;\n"
"}")
        self.label_11.setAlignment(Qt.AlignCenter)
        self.label_11.setWordWrap(True)

        self.info_layout.addWidget(self.label_11)

        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.label_5.setWordWrap(True)

        self.info_layout.addWidget(self.label_5)

        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 100))
        self.frame_5.setMaximumSize(QSize(16777215, 100))
        self.frame_5.setStyleSheet(u"")
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_5)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.frame_5)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignCenter)
        self.label_9.setWordWrap(True)

        self.gridLayout.addWidget(self.label_9, 1, 0, 1, 1)

        self.label_8 = QLabel(self.frame_5)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignCenter)
        self.label_8.setWordWrap(True)

        self.gridLayout.addWidget(self.label_8, 0, 0, 1, 1)


        self.info_layout.addWidget(self.frame_5)


        self.info_layout_holder.addWidget(self.frame)

        self.scrollArea.setWidget(self.Contents)

        self.verticalLayout.addWidget(self.scrollArea)

        self.menus.addWidget(self.menu_1)
        self.menu_2 = QWidget()
        self.menu_2.setObjectName(u"menu_2")
        self.verticalLayout_2 = QVBoxLayout(self.menu_2)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.label_2 = QLabel(self.menu_2)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(16)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"font-size: 16pt")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        self.menus.addWidget(self.menu_2)

        self.main_pages_layout.addWidget(self.menus)


        self.retranslateUi(LeftColumn)

        self.menus.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(LeftColumn)
    # setupUi

    def retranslateUi(self, LeftColumn):
        LeftColumn.setWindowTitle(QCoreApplication.translate("LeftColumn", u"Form", None))
        self.heading.setText(QCoreApplication.translate("LeftColumn", u"Laky Phone Point of Sales ", None))
        self.label_3.setText(QCoreApplication.translate("LeftColumn", u"This software was named after the core develper's initials \"Lawrence Addai Kusi\" and a local name \"Yaw\" ( thursday born in Ashanti Ghana). The earlier version of this software was name  \"Advance POS\" which  with microsoft visuall basic in 2018. It was very powerful but has a little draw back. \n"
"\n"
" As a solution to the draw back, evolved in this more poweful, scalable and mordern application which was release 2021. \n"
"\n"
"For more information and documentation, please visit :", None))
        self.label_4.setText(QCoreApplication.translate("LeftColumn", u"www.ithousegh.com/lakypos/doc", None))
        self.label_6.setText(QCoreApplication.translate("LeftColumn", u"\n"
"Video tutorials, visit :", None))
        self.label_7.setText(QCoreApplication.translate("LeftColumn", u"www.youtube.com", None))
        self.label.setText(QCoreApplication.translate("LeftColumn", u"\n"
"App status:", None))
        self.label_10.setText(QCoreApplication.translate("LeftColumn", u" Activated", None))
        self.label_11.setText(QCoreApplication.translate("LeftColumn", u"\n"
"\n"
" Check For Update\n"
"", None))
        self.label_5.setText(QCoreApplication.translate("LeftColumn", u"Contact Details", None))
        self.label_9.setText(QCoreApplication.translate("LeftColumn", u"Phone:\n"
" +233243689393", None))
        self.label_8.setText(QCoreApplication.translate("LeftColumn", u"email: lawcubegsm@gmail.com", None))
        self.label_2.setText(QCoreApplication.translate("LeftColumn", u"Menu 2 - Left Menu", None))
    # retranslateUi

