# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////
from gui.widgets.py_table_widget.py_table_widget import PyTableWidget
from . functions_main_window import *
import sys
import os

# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from qt_core import *

# IMPORT SETTINGS
# ///////////////////////////////////////////////////////////////
from gui.core.json_settings import Settings

# IMPORT THEME COLORS
# ///////////////////////////////////////////////////////////////
from gui.core.json_themes import Themes

# IMPORT PY ONE DARK WIDGETS
# ///////////////////////////////////////////////////////////////
from gui.widgets import *

# LOAD UI MAIN
# ///////////////////////////////////////////////////////////////
from . ui_main import *

# MAIN FUNCTIONS 
# ///////////////////////////////////////////////////////////////
from . functions_main_window import *

# PY WINDOW
# ///////////////////////////////////////////////////////////////
class SetupMainWindow:
    def __init__(self):
        super().__init__()
        # SETUP MAIN WINDOw
        # Load widgets from "gui\uis\main_window\ui_main.py"
        # ///////////////////////////////////////////////////////////////
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)

    # ADD LEFT MENUS
    # ///////////////////////////////////////////////////////////////
    add_left_menus = [
        {
            "btn_icon" : "icon_home.svg",
            "btn_id" : "home_btn",
            "btn_text" : "Home",
            "btn_tooltip" : "Home page",
            "show_top" : True,
            "is_active" : True
        },
        {
            "btn_icon": "android.svg",
            "btn_id": "phone_btn",
            "btn_text": "Phone Sales",
            "btn_tooltip": "Phone Sales tab",
            "show_top": True,
            "is_active": False
        },

        {
            "btn_icon": "Accessories2.svg",
            "btn_id": "accessories_btn",
            "btn_text": "Phone Accessories",
            "btn_tooltip": "Phone Accessories",
            "show_top": True,
            "is_active": False
        },

        {
            "btn_icon" : "repairs.svg",
            "btn_id" : "service_btn",
            "btn_text" : "Phone Repairs",
            "btn_tooltip" : "Phone Repairs",
            "show_top" : True,
            "is_active" : False
        },


        {
            "btn_icon": "icon_file.svg",
            "btn_id": "report_btn",
            "btn_text": "Reports",
            "btn_tooltip": "Reports",
            "show_top": True,
            "is_active": False
        },
        {
            "btn_icon": "icon_info.svg",
            "btn_id": "btn_info",
            "btn_text": "App Info",
            "btn_tooltip": "application info",
            "show_top": False,
            "is_active": False
        }



    ]

     # ADD TITLE BAR MENUS
    # ///////////////////////////////////////////////////////////////
    add_title_bar_menus = [
        {
            "btn_icon": "icon_add_user.svg",
            "btn_id": "btn_search",
            "btn_tooltip": "notification",
            "is_active": False
        },
        {
            "btn_icon" : "icon_add_user.svg",
            "btn_id" : "btn_search",
            "btn_tooltip" : "Search",
            "is_active" : False
        },
        {
            "btn_icon" : "icon_settings.svg",
            "btn_id" : "btn_top_settings",
            "btn_tooltip" : "Top settings",
            "is_active" : False
        }
    ]

    # SETUP CUSTOM BTNs OF CUSTOM WIDGETS
    # Get sender() function when btn is clicked
    # ///////////////////////////////////////////////////////////////
    def setup_btns(self):
        if self.ui.title_bar.sender() != None:
            return self.ui.title_bar.sender()
        elif self.ui.left_menu.sender() != None:
            return self.ui.left_menu.sender()
        elif self.ui.left_column.sender() != None:
            return self.ui.left_column.sender()

    # SETUP MAIN WINDOW WITH CUSTOM PARAMETERS
    # ///////////////////////////////////////////////////////////////
    def setup_gui(self):
        # APP TITLE
        # ///////////////////////////////////////////////////////////////
        self.setWindowTitle(self.settings["app_name"])
        
        # REMOVE TITLE BAR
        # ///////////////////////////////////////////////////////////////
        if self.settings["custom_title_bar"]:
            self.setWindowFlag(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)

        # ADD GRIPS
        # ///////////////////////////////////////////////////////////////
        if self.settings["custom_title_bar"]:
            self.left_grip = PyGrips(self, "left", self.hide_grips)
            self.right_grip = PyGrips(self, "right", self.hide_grips)
            self.top_grip = PyGrips(self, "top", self.hide_grips)
            self.bottom_grip = PyGrips(self, "bottom", self.hide_grips)
            self.top_left_grip = PyGrips(self, "top_left", self.hide_grips)
            self.top_right_grip = PyGrips(self, "top_right", self.hide_grips)
            self.bottom_left_grip = PyGrips(self, "bottom_left", self.hide_grips)
            self.bottom_right_grip = PyGrips(self, "bottom_right", self.hide_grips)

        # LEFT MENUS / GET SIGNALS WHEN LEFT MENU BTN IS CLICKED / RELEASED
        # ///////////////////////////////////////////////////////////////
        # ADD MENUS
        self.ui.left_menu.add_menus(SetupMainWindow.add_left_menus)

        # SET SIGNALS
        self.ui.left_menu.clicked.connect(self.btn_clicked)
        self.ui.left_menu.released.connect(self.btn_released)

        # TITLE BAR / ADD EXTRA BUTTONS
        # ///////////////////////////////////////////////////////////////
        # ADD MENUS
        self.ui.title_bar.add_menus(SetupMainWindow.add_title_bar_menus)

        # SET SIGNALS
        self.ui.title_bar.clicked.connect(self.btn_clicked)
        self.ui.title_bar.released.connect(self.btn_released)

        # ADD Title
        if self.settings["custom_title_bar"]:
            self.ui.title_bar.set_title(self.settings["app_name"])
        else:
            self.ui.title_bar.set_title("Laky Phone POS")

        # LEFT COLUMN SET SIGNALS
        # ///////////////////////////////////////////////////////////////
        self.ui.left_column.clicked.connect(self.btn_clicked)
        self.ui.left_column.released.connect(self.btn_released)

        # SET INITIAL PAGE / SET LEFT AND RIGHT COLUMN MENUS
        # ///////////////////////////////////////////////////////////////
        MainFunctions.set_page(self, self.ui.load_pages.home_page)
        MainFunctions.set_left_column_menu(
            self,
            menu = self.ui.left_column.menus.menu_1,
            title = "Settings Left Column",
            icon_path = Functions.set_svg_icon("icon_settings.svg")
        )
        MainFunctions.set_right_column_menu(self, self.ui.right_column.menu_1)

        # ///////////////////////////////////////////////////////////////
        # EXAMPLE CUSTOM WIDGETS
        # Here are added the custom widgets to pages and columns that
        # were created using Qt Designer.
        # This is just an example and should be deleted when creating
        # your application.
        #
        # OBJECTS FOR LOAD PAGES, LEFT AND RIGHT COLUMNS
        # You can access objects inside Qt Designer projects using
        # the objects below:
        #
        # <OBJECTS>
        # LEFT COLUMN: self.ui.left_column.menus
        # RIGHT COLUMN: self.ui.right_column
        # LOAD PAGES: self.ui.load_pages
        # </OBJECTS>
        # ///////////////////////////////////////////////////////////////

        # LOAD SETTINGS
        # ///////////////////////////////////////////////////////////////
        settings = Settings()
        self.settings = settings.items

        # LOAD THEME COLOR
        # ///////////////////////////////////////////////////////////////
        themes = Themes()
        self.themes = themes.items



        # ////////////////////////////////////////////////////////////////
        # ADD CUSTOM WIDGET TO MAIN PAGE
        # ///////////////////////////////////////////////////////////////
        # custom py_line_edit
        self.customerName = PyLineEdit(
            place_holder_text = "customer name",
            context_color = self.themes["app_color"]["context_color"],
            color = self.themes["app_color"]["text_active"],
            bg_color = self.themes["app_color"]["bg_three"],

            )
        # add to phone
        self.customerName.height = 40
        self.ui.load_pages.customer_name_edit.addWidget(self.customerName)


        self.contactName = PyLineEdit(
            place_holder_text="customer name",
            context_color=self.themes["app_color"]["context_color"],
            color=self.themes["app_color"]["text_active"],
            bg_color=self.themes["app_color"]["bg_three"],

        )

        self.ui.load_pages.customer_contact_edit.addWidget(self.contactName)

        self.curt_id = PyLineEdit(
            context_color=self.themes["app_color"]["context_color"],
            color=self.themes["app_color"]["text_active"],
            bg_color=self.themes["app_color"]["bg_three"],

        )

        self.ui.load_pages.cutomer_cart_id_edit.addWidget(self.curt_id)

        # phone section

        self.phone_imei = PyLineEdit(
            context_color=self.themes["app_color"]["context_color"],
            color=self.themes["app_color"]["text_active"],
            bg_color=self.themes["app_color"]["bg_three"],

        )

        self.ui.load_pages.phone_imei_edit.addWidget(self.phone_imei)




        self.phone_sn = PyLineEdit(
            context_color=self.themes["app_color"]["context_color"],
            color=self.themes["app_color"]["text_active"],
            bg_color=self.themes["app_color"]["bg_three"],

        )

        self.ui.load_pages.phone_sn_edit.addWidget(self.phone_sn)


        # price section

        self.phone_price = PyLineEdit(
            context_color=self.themes["app_color"]["context_color"],
            color=self.themes["app_color"]["text_active"],
            bg_color=self.themes["app_color"]["bg_three"],

        )

        self.ui.load_pages.phone_price_edit.addWidget(self.phone_price)

        self.phone_discount = PyLineEdit(
            context_color=self.themes["app_color"]["context_color"],
            color=self.themes["app_color"]["text_active"],
            bg_color=self.themes["app_color"]["bg_three"],

        )

        self.ui.load_pages.phone_discount_edit.addWidget(self.phone_discount)


        self.phone_tax = PyLineEdit(
            context_color=self.themes["app_color"]["context_color"],
            color=self.themes["app_color"]["text_active"],
            bg_color=self.themes["app_color"]["bg_three"],

        )

        self.ui.load_pages.phone_tax_edit.addWidget(self.phone_tax)


        # buttons section
        self.add_to_cart = PyIconButton(
          width = 400,
            height = 40
        )

        self.ui.load_pages.phone_addToCart_btn.addWidget(self.add_to_cart)







        # ///////////////////////////////////////////////////////////////
        # END - EXAMPLE CUSTOM WIDGETS
        # ///////////////////////////////////////////////////////////////

    # RESIZE GRIPS AND CHANGE POSITION
    # Resize or change position when window is resized
    # ///////////////////////////////////////////////////////////////
    def resize_grips(self):
        if self.settings["custom_title_bar"]:
            self.left_grip.setGeometry(5, 10, 10, self.height())
            self.right_grip.setGeometry(self.width() - 15, 10, 10, self.height())
            self.top_grip.setGeometry(5, 5, self.width() - 10, 10)
            self.bottom_grip.setGeometry(5, self.height() - 15, self.width() - 10, 10)
            self.top_right_grip.setGeometry(self.width() - 20, 5, 15, 15)
            self.bottom_left_grip.setGeometry(5, self.height() - 20, 15, 15)
            self.bottom_right_grip.setGeometry(self.width() - 20, self.height() - 20, 15, 15)