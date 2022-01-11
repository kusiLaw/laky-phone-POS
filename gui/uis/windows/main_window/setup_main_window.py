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


# from core import Active_User
# from gui.engine.phones_operations import Active_User


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
            "btn_icon": "repairs.svg",
            "btn_id": "stock_btn",
            "btn_text": "Inventory",
            "btn_tooltip": "Inventory",
            "show_top": True,
            "is_active": False
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

    # {
    #     "btn_icon": "Accessories2.svg",
    #     "btn_id": "accessories_btn",
    #     "btn_text": "Phone Accessories",
    #     "btn_tooltip": "Phone Accessories",
    #     "show_top": True,
    #     "is_active": False
    # },
    #
    # {
    #     "btn_icon": "repairs.svg",
    #     "btn_id": "service_btn",
    #     "btn_text": "Phone Repairs",
    #     "btn_tooltip": "Phone Repairs",
    #     "show_top": True,
    #     "is_active": False
    # },

     # ADD TITLE BAR MENUS
    # ///////////////////////////////////////////////////////////////
    add_title_bar_menus = [

        {
            "btn_icon" : "icon_add_user.svg",
            "btn_id" : "btn_user",
            "btn_tooltip" : "user profile",
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

        # elif self.ui.load_pages.sender() != None:
        #     return self.ui.load_pages.sender()

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
        MainFunctions.set_right_column_menu(self, self.ui.right_column.setting_page)

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

        # RIGHT COLUMN SECTION
        # self.pro_pic = PyPicture()
        # self.ui.right_column.pro_pic_frame.addWidget(self.pro_pic)

        self.sign_out = PyPushButton2(
            text="sign out",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"],
            hover_border_color=self.themes["app_color"]["red"],
            show_boader_color = True
        )
        self.sign_out.setMinimumHeight(30)

        self.ui.right_column.sing_out_frame.addWidget(self.sign_out)

        self.add_user = PyPushButton2(
            text="Add User",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"],
            hover_border_color=self.themes["app_color"]["context_color"]
        )
        self.add_user.setMinimumHeight(30)

        self.ui.right_column.add_user_frame.addWidget(self.add_user)

        self.reset_pass = PyPushButton2(
            text="Reset Password",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"],
            hover_border_color=self.themes["app_color"]["context_color"]
        )
        self.reset_pass.setMinimumHeight(30)

        self.ui.right_column.reset_password_frame.addWidget(self.reset_pass)
        # p = Active_User("Laky3" "laky689393")
        # self.reset_pass.clicked.connect(p.login())

        self.old_pass = PyLineEdit(

            context_color=self.themes["app_color"]["context_color"],
            color=self.themes["app_color"]["text_active"],
            bg_color=self.themes["app_color"]["dark_one"],
            echomode=True
        )

        self.ui.right_column.current_password_frame.addWidget(self.old_pass)

        self.new_pass = PyLineEdit(

            context_color=self.themes["app_color"]["context_color"],
            color=self.themes["app_color"]["text_active"],
            bg_color=self.themes["app_color"]["dark_one"],
            echomode=True
        )

        self.ui.right_column.new_password_frame.addWidget(self.new_pass)

        self.comfirm_pass = PyLineEdit(

            context_color=self.themes["app_color"]["context_color"],
            color=self.themes["app_color"]["text_active"],
            bg_color=self.themes["app_color"]["bg_three"],
            echomode=True
        )

        self.ui.right_column.confirm_password_frame.addWidget(self.comfirm_pass)


#///////////////////////////////////////////////////////////////////////////////////////////////////
        # MAIN PAGE SECTION
#///////////////////////////////////////////////////////////////////////////////////////////////////


        self.user_name = PyLineEdit(

            context_color=self.themes["app_color"]["context_color"],
            color=self.themes["app_color"]["text_active"],
            bg_color=self.themes["app_color"]["bg_three"],
            maxlen=22,
            # validator=QIntValidator()
        )
        # self.user_name.height = 40
        self.user_name.setMinimumHeight(40)
        self.ui.load_pages.login_username_frame.addWidget(self.user_name)


        self.user_passsword = PyLineEdit(

            context_color=self.themes["app_color"]["context_color"],
            color=self.themes["app_color"]["text_active"],
            bg_color=self.themes["app_color"]["bg_three"],
            maxlen=22,
            # validator=QIntValidator()
            echomode = True
        )
        # self.user_passsword.height = 40
        self.user_passsword.setMinimumHeight(40)
        self.ui.load_pages.login_password_frame.addWidget(self.user_passsword)

        self.login_btn = PyPushButton2(
            text="Login",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"],
            hover_border_color=self.themes["app_color"]["context_color"]

        )
        self.login_btn.setMinimumHeight(40)
        self.ui.load_pages.login_button_fame.addWidget(self.login_btn)



        # ///////////////////////

        self.customerName = PyLineEdit(

            context_color = self.themes["app_color"]["context_color"],
            color = self.themes["app_color"]["text_active"],
            bg_color = self.themes["app_color"]["bg_three"],
            maxlen=22,
            # validator=QIntValidator()
            )

        # add to phone
        self.customerName.height = 40
        self.ui.load_pages.customer_name_edit.addWidget(self.customerName)


        self.contactName = PyLineEdit(

            context_color=self.themes["app_color"]["context_color"],
            color=self.themes["app_color"]["text_active"],
            bg_color=self.themes["app_color"]["bg_three"],
            maxlen=15,
            validator=QIntValidator()
        )

        self.ui.load_pages.customer_contact_edit.addWidget(self.contactName)

        # self.curt_id = PyLineEdit(
        #     context_color=self.themes["app_color"]["context_color"],
        #     color=self.themes["app_color"]["text_active"],
        #     bg_color=self.themes["app_color"]["bg_three"],
        #
        # )
        #
        # self.ui.load_pages.cutomer_cart_id_edit.addWidget(self.curt_id)

        # phone section
        self.phone_type = PyComBox(

            color=self.themes["app_color"]["text_active"],
            bg_color=self.themes["app_color"]["dark_one"],
            radius=8,
            bg_color_hover=self.themes["app_color"]["context_color"],
            items=['item 1', 'item 2', 'item 2'],
            editable = False

        )

        self.ui.load_pages.phone_type_edit.addWidget(self.phone_type)

        self.phone_model = PyComBox(

            color=self.themes["app_color"]["text_active"],
            bg_color=self.themes["app_color"]["dark_one"],
            radius=8,
            bg_color_hover=self.themes["app_color"]["context_color"],
            items=['item 1', 'item 2', 'item 2'],
            editable=False

        )

        self.ui.load_pages.phone_model_edit.addWidget(self.phone_model)

        #
        # self.phone_imei = PyComBox(
        #
        #     color=self.themes["app_color"]["text_active"],
        #     bg_color=self.themes["app_color"]["dark_one"],
        #     radius = 8,
        #     bg_color_hover = self.themes["app_color"]["context_color"],
        #     items = ['item 1', 'item 2', 'item 2']
        #
        # )
        #
        # self.ui.load_pages.phone_imei_edit.addWidget(self.phone_imei)

        self.phone_payment = PyComBox(

            color=self.themes["app_color"]["text_active"],
            bg_color=self.themes["app_color"]["dark_one"],
            radius = 8,
            bg_color_hover = self.themes["app_color"]["context_color"],
            items = ['Cash', 'Paypal', 'mtn momo'],
            editable = False
        )

        self.ui.load_pages.phone_payment_edit.addWidget(self.phone_payment)


        self.phone_search_key = PyComBox(

            color=self.themes["app_color"]["text_active"],
            bg_color=self.themes["app_color"]["dark_one"],
            radius=8,
            bg_color_hover=self.themes["app_color"]["context_color"],
            items=['Cash', 'Paypal', 'mtn momo'],
            editable=False
        )

        self.ui.load_pages.phone_search_key_edit.addWidget(self.phone_search_key)


        self.qr_toggle = PyToggle(
            width=70,
            bg_color=self.themes["app_color"]["dark_one"],
            circle_color=self.themes["app_color"]["icon_color"],
            active_color=self.themes["app_color"]["context_color"],
            animation_curve=QEasingCurve.OutCirc


        )
        self.ui.load_pages.phone_qr.addWidget(self.qr_toggle)


        self.phone_sn = PyComBox(
            color=self.themes["app_color"]["text_active"],
            bg_color=self.themes["app_color"]["dark_one"],
            radius=8,
            bg_color_hover=self.themes["app_color"]["context_color"],
            editable=True

        )

        self.ui.load_pages.phone_sn_edit.addWidget(self.phone_sn)


        # price section

        self.phone_price = PyLineEdit(
            context_color=self.themes["app_color"]["context_color"],
            color=self.themes["app_color"]["text_active"],
            bg_color=self.themes["app_color"]["bg_three"],
            maxlen=7,
            validator=QDoubleValidator(0.99,99.99,2)
        )

        self.ui.load_pages.phone_price_edit.addWidget(self.phone_price)


        self.phone_discount = PyLineEdit(
            context_color=self.themes["app_color"]["context_color"],
            color=self.themes["app_color"]["text_active"],
            bg_color=self.themes["app_color"]["bg_three"],
            maxlen = 2,
            read_only=True,
            validator = QIntValidator()
        )

        self.ui.load_pages.phone_discount_edit.addWidget(self.phone_discount)


        self.phone_total_price = PyLineEdit(
            context_color=self.themes["app_color"]["context_color"],
            color=self.themes["app_color"]["text_active"],
            bg_color=self.themes["app_color"]["bg_three"],
            read_only=True,
            validator = QIntValidator()
        )

        self.ui.load_pages.phone_total_price_frame.addWidget(self.phone_total_price)




        self.phone_pay_code = PyLineEdit(
            context_color=self.themes["app_color"]["context_color"],
            color=self.themes["app_color"]["text_active"],
            bg_color=self.themes["app_color"]["bg_three"],
            maxlen= 30,

        )

        self.ui.load_pages.phone_tans_code_frame.addWidget(self.phone_pay_code)

        self.total_item = PyLineEdit(
            context_color=self.themes["app_color"]["context_color"],
            color=self.themes["app_color"]["text_active"],
            bg_color=self.themes["app_color"]["bg_three"],
            maxlen=30,
            read_only=True
        )

        self.ui.load_pages.phone_total_item_frame.addWidget(self.total_item)

        # buttons section

        self.add_to_cart_btn= PyPushButton2(
            text = "Add to Cart",
            radius = 8,
            color = self.themes["app_color"]["text_foreground"],
            bg_color = self.themes["app_color"]["dark_one"],
            bg_color_hover = self.themes["app_color"]["dark_three"],
            bg_color_pressed = self.themes["app_color"]["dark_four"],
            hover_border_color = self.themes["app_color"]["context_color"]
        )
        self.add_to_cart_btn.setMinimumHeight(30)
        self.ui.load_pages.phone_add_to_cart_layout.addWidget(self.add_to_cart_btn)

        # self.add_to_cart_btn.clicked.connect(printInput)




        self.remove_from_cart_btn = PyPushButton2(
            text="Remove from Cart",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"],
            hover_border_color=self.themes["app_color"]["context_color"]

        )

        self.remove_from_cart_btn.setMinimumHeight(30)
        self.ui.load_pages.remov_from_cart_layout.addWidget(self.remove_from_cart_btn)


        self.phone_clear_cart_btn = PyPushButton2(
            text="Clear Cart",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"],
            hover_border_color=self.themes["app_color"]["context_color"]

        )
        self.phone_clear_cart_btn.setMinimumHeight(30)
        self.ui.load_pages.phone_clear_cart_layout.addWidget(self.phone_clear_cart_btn)


        self.phone_buyme_btn = PyPushButton2(
            text="Buy / Save",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"],
            hover_border_color=self.themes["app_color"]["green"],
            show_boader_color = False
        )
        self.phone_buyme_btn.setMinimumHeight(30)
        self.ui.load_pages.phone_buyme_layout.addWidget(self.phone_buyme_btn)


        self.phone_clear_btn = PyPushButton2(
            text="Clear",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"],
            hover_border_color=self.themes["app_color"]["red"]
        )
        self.phone_clear_btn.setMinimumHeight(30)
        self.ui.load_pages.phone_clear_layout.addWidget(self.phone_clear_btn)


        self.phone_delete_btn = PyPushButton2(
            text="Delete",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"],
            hover_border_color=self.themes["app_color"]["red"]

        )
        self.phone_delete_btn.setMinimumHeight(30)
        self.ui.load_pages.phone_delete_layout.addWidget(self.phone_delete_btn)

        self.phone_all_in_one_btn = PyPushButton2(
            text="all-in_one",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"],
            hover_border_color=self.themes["app_color"]["context_color"]

        )
        self.phone_all_in_one_btn.setMinimumHeight(30)
        self.ui.load_pages.phone_all_in_one_layout.addWidget(self.phone_all_in_one_btn)


        self.phone_print_btn = PyPushButton2(
            text="Print",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"],
            hover_border_color=self.themes["app_color"]["context_color"]

        )
        self.phone_print_btn.setMinimumHeight(30)
        self.ui.load_pages.phone_print_layout.addWidget(self.phone_print_btn)

        # def printInput(message = None):
        #     QMessageBox.information(None, "Received Key Release EVent", f"You Pres: " )
        #     print(self.phone_price.text())
        #
        # self.phone_print_btn.clicked.connect(lambda messasage: printInput(messasage))
        # self.phone_print_btn.clicked.connect(printInput(message='hjkhjghjgh'))

        # Search
        self.phone_search_edit = PyLineEdit(

            context_color=self.themes["app_color"]["context_color"],
            color=self.themes["app_color"]["text_active"],
            bg_color=self.themes["app_color"]["dark_three"]

        )

        self.ui.load_pages.phone_search_layout.addWidget(self.phone_search_edit)



        # Phone table section

     # TABLE WIDGETS

        self.table_widget = PyTableWidget(
            radius = 8,
            color = self.themes["app_color"]["text_foreground"],
            selection_color = self.themes["app_color"]["context_color"],
            bg_color = self.themes["app_color"]["bg_two"],
            header_horizontal_color = self.themes["app_color"]["bg_one"],
            header_vertical_color = self.themes["app_color"]["bg_three"],
            bottom_line_color = self.themes["app_color"]["bg_three"],
            grid_line_color = self.themes["app_color"]["bg_one"],
            scroll_bar_bg_color = self.themes["app_color"]["bg_one"],
            scroll_bar_btn_color = self.themes["app_color"]["dark_four"],
            context_color = self.themes["app_color"]["context_color"]
        )
        self.table_widget.setColumnCount(11)
        self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)


        self.table_widget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.table_widget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_widget.setEditTriggers(QAbstractItemView.NoEditTriggers)


        # Columns / Header
        self.column_1 = QTableWidgetItem()
        self.column_1.setTextAlignment(Qt.AlignCenter)
        self.column_1.setText("Customer")

        self.column_2 = QTableWidgetItem()
        self.column_2.setTextAlignment(Qt.AlignCenter)
        self.column_2.setText("Customer Contact")

        self.column_3 = QTableWidgetItem()
        self.column_3.setTextAlignment(Qt.AlignCenter)
        self.column_3.setText("Phone Type")

        self.column_4 = QTableWidgetItem()
        self.column_4.setTextAlignment(Qt.AlignCenter)
        self.column_4.setText("Phone Model")

        self.column_5 = QTableWidgetItem()
        self.column_5.setTextAlignment(Qt.AlignCenter)
        self.column_5.setText("Serial Number")

        self.column_6 = QTableWidgetItem()
        self.column_6.setTextAlignment(Qt.AlignCenter)
        self.column_6.setText("Price")

        self.column_7 = QTableWidgetItem()
        self.column_7.setTextAlignment(Qt.AlignCenter)
        self.column_7.setText("Tax")

        self.column_8 = QTableWidgetItem()
        self.column_8.setTextAlignment(Qt.AlignCenter)
        self.column_8.setText("Transaction Code")

        self.column_9 = QTableWidgetItem()
        self.column_9.setTextAlignment(Qt.AlignCenter)
        self.column_9.setText("Discount")

        self.column_10 = QTableWidgetItem()
        self.column_10.setTextAlignment(Qt.AlignCenter)
        self.column_10.setText("Date")

        self.column_11 = QTableWidgetItem()
        self.column_11.setTextAlignment(Qt.AlignCenter)
        self.column_11.setText("User")



        # Set column
        self.table_widget.setHorizontalHeaderItem(0, self.column_1)
        self.table_widget.setHorizontalHeaderItem(1, self.column_2)
        self.table_widget.setHorizontalHeaderItem(2, self.column_3)
        self.table_widget.setHorizontalHeaderItem(3, self.column_4)
        self.table_widget.setHorizontalHeaderItem(4, self.column_5)
        self.table_widget.setHorizontalHeaderItem(5, self.column_6)
        self.table_widget.setHorizontalHeaderItem(6, self.column_7)
        self.table_widget.setHorizontalHeaderItem(7, self.column_8)
        self.table_widget.setHorizontalHeaderItem(8, self.column_9)
        self.table_widget.setHorizontalHeaderItem(9, self.column_10)
        self.table_widget.setHorizontalHeaderItem(10, self.column_11)

        self.ui.load_pages.phone_table.addWidget(self.table_widget)




        self.phone_cart = PyTableWidget(
            radius = 8,
            color = self.themes["app_color"]["text_foreground"],
            selection_color = self.themes["app_color"]["context_color"],
            bg_color = self.themes["app_color"]["bg_two"],
            header_horizontal_color = self.themes["app_color"]["bg_one"],
            header_vertical_color = self.themes["app_color"]["bg_three"],
            bottom_line_color = self.themes["app_color"]["bg_three"],
            grid_line_color = self.themes["app_color"]["bg_one"],
            scroll_bar_bg_color = self.themes["app_color"]["bg_one"],
            scroll_bar_btn_color = self.themes["app_color"]["dark_four"],
            context_color = self.themes["app_color"]["context_color"]
        )
        self.phone_cart.setColumnCount(4)
        self.phone_cart.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.phone_cart.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.phone_cart.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.phone_cart.setEditTriggers(QAbstractItemView.NoEditTriggers)


        # Columns / Header
        self.cart_column_1 = QTableWidgetItem()
        self.cart_column_1.setTextAlignment(Qt.AlignCenter)
        self.cart_column_1.setText("Type")

        self.cart_column_2 = QTableWidgetItem()
        self.cart_column_2.setTextAlignment(Qt.AlignCenter)
        self.cart_column_2.setText("Model")

        self.cart_column_3 = QTableWidgetItem()
        self.cart_column_3.setTextAlignment(Qt.AlignCenter)
        self.cart_column_3.setText("S/N")

        # self.cart_column_4 = QTableWidgetItem()
        # self.cart_column_4.setTextAlignment(Qt.AlignCenter)
        # self.cart_column_4.setText("Imei")

        self.cart_column_5 = QTableWidgetItem()
        self.cart_column_5.setTextAlignment(Qt.AlignCenter)
        self.cart_column_5.setText("Price")

        # Set column
        self.phone_cart.setHorizontalHeaderItem(0, self.cart_column_1)
        self.phone_cart.setHorizontalHeaderItem(1, self.cart_column_2)
        self.phone_cart.setHorizontalHeaderItem(2, self.cart_column_3)
        # self.phone_cart.setHorizontalHeaderItem(3, self.cart_column_4)
        self.phone_cart.setHorizontalHeaderItem(3, self.cart_column_5)

        self.ui.load_pages.phone_cart_layout.addWidget(self.phone_cart)


# ///////////////////////////////////////////////////////////////////////////////////////////////////
        # STOCK SECTION
# ///////////////////////////////////////////////////////////////////////////////////////////////////

        self.stock_type = PyComBox(

            color=self.themes["app_color"]["text_active"],
            bg_color=self.themes["app_color"]["bg_three"],
            radius=0,
            bg_color_hover=self.themes["app_color"]["context_color"],
            items=[],
            maxlen=20,
            editable=True
        )

        self.ui.load_pages.stock_ph_type_layout.addWidget(self.stock_type)


        self.stock_model = PyComBox(

            color=self.themes["app_color"]["text_active"],
            bg_color=self.themes["app_color"]["bg_three"],
            radius=0,
            bg_color_hover=self.themes["app_color"]["context_color"],
            items=[],
            maxlen=20,
            editable=True
        )

        self.ui.load_pages.stock_ph_model_layout.addWidget(self.stock_model)


        self.stock_prod_code = PyComBox(

            color=self.themes["app_color"]["text_active"],
            bg_color=self.themes["app_color"]["bg_three"],
            radius=8,
            bg_color_hover=self.themes["app_color"]["context_color"],
            items=[],
            maxlen=25,
            editable=True
        )

        self.ui.load_pages.stock_ph_pdt_layout.addWidget(self.stock_prod_code)


        self.stock_suplier = PyComBox(

            color=self.themes["app_color"]["text_active"],
            bg_color=self.themes["app_color"]["bg_three"],
            radius=0,
            bg_color_hover=self.themes["app_color"]["context_color"],
            items=[],
            maxlen=25,
            editable=True
        )

        self.ui.load_pages.stock_suplier_layout.addWidget(self.stock_suplier)

        self.stock_unique_code = PyComBox(

            color=self.themes["app_color"]["text_active"],
            bg_color=self.themes["app_color"]["bg_three"],
            radius=0,
            bg_color_hover=self.themes["app_color"]["context_color"],
            items=['SN Number only'],
            editable=False
        )

        self.ui.load_pages.stock_unique_code_layout.addWidget(self.stock_unique_code)

        self.stock_cp = PyLineEdit(

            context_color=self.themes["app_color"]["context_color"],
            color=self.themes["app_color"]["text_active"],
            bg_color=self.themes["app_color"]["bg_three"],
            maxlen = 9,
            validator = QDoubleValidator(0.99, 9999999.99, 2)
        )

        self.ui.load_pages.stock_cp_layout.addWidget(self.stock_cp)


        self.stock_qantity = PyLineEdit(

            context_color=self.themes["app_color"]["context_color"],
            color=self.themes["app_color"]["text_active"],
            bg_color=self.themes["app_color"]["bg_three"],
            maxlen = 9,
            validator = QDoubleValidator(0.99, 99.99, 0)

        )

        self.ui.load_pages.stock_qantity_layout.addWidget(self.stock_qantity)

        self.stock_sp = PyLineEdit(

            context_color=self.themes["app_color"]["context_color"],
            color=self.themes["app_color"]["text_active"],
            bg_color=self.themes["app_color"]["bg_three"],
            maxlen=9,
            validator=QDoubleValidator(0.99, 9999999.99, 2)

        )

        self.ui.load_pages.stock_sp_layout.addWidget(self.stock_sp)

        self.stock_tax = PyLineEdit(

            context_color=self.themes["app_color"]["context_color"],
            color=self.themes["app_color"]["text_active"],
            bg_color=self.themes["app_color"]["bg_three"],
            maxlen = 3,
            validator=QDoubleValidator(0.99, 99999.99,1)

        )

        self.ui.load_pages.stock_tax_layout.addWidget(self.stock_tax)


        self.stock_suplier_contact = PyLineEdit(

            context_color=self.themes["app_color"]["context_color"],
            color=self.themes["app_color"]["text_active"],
            bg_color=self.themes["app_color"]["bg_three"],
            maxlen=15,
            validator=QDoubleValidator(0.99, 99.99, 2)

        )

        self.ui.load_pages.suplier_contact_layout.addWidget(self.stock_suplier_contact)




        self.stock_qr = PyToggle(
            width=70,
            active_color=self.themes["app_color"]["context_color"],
            circle_color=self.themes["app_color"]["text_active"],
            bg_color=self.themes["app_color"]["bg_three"]

        )

        self.ui.load_pages.stock_qr_layout.addWidget(self.stock_qr)



        self.stock_sn_list = Pylist(
            context_color=self.themes["app_color"]["context_color"],
            color=self.themes["app_color"]["text_active"],
            bg_color=self.themes["app_color"]["bg_three"],

        )

        self.ui.load_pages.stock_list_frame.addWidget(self.stock_sn_list)


        self.stock_datetime = Py_datetime(

            context_color=self.themes["app_color"]["context_color"],
            color=self.themes["app_color"]["text_active"],
            bg_color=self.themes["app_color"]["bg_three"],
        )

        self.ui.load_pages.stock_datetime_frame.addWidget(self.stock_datetime)


        self.stock_save = PyPushButton2(
            text="Save",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"],
            hover_border_color=self.themes["app_color"]["green"]

        )
        # self.phone_delete_btn.setMinimumHeight(30)
        self.ui.load_pages.stock_save_layout.addWidget(self.stock_save)

        self.stock_update = PyPushButton2(
            text="Update",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"],
            hover_border_color=self.themes["app_color"]["context_color"]

        )
        # self.phone_delete_btn.setMinimumHeight(30)
        self.ui.load_pages.stock_update_layout.addWidget(self.stock_update)

        self.stock_delete = PyPushButton2(
            text="Delete",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"],
            hover_border_color=self.themes["app_color"]["red"]

        )
        # self.phone_delete_btn.setMinimumHeight(30)
        self.ui.load_pages.stock_delete_layout.addWidget(self.stock_delete)

        self.stock_clear = PyPushButton2(
             text="Clear",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"],
            hover_border_color=self.themes["app_color"]["context_color"]

        )
        # self.phone_delete_btn.setMinimumHeight(30)
        self.ui.load_pages.stock_clear_layout.addWidget(self.stock_clear)

        self.stock_search_key = PyComBox(

            color=self.themes["app_color"]["text_active"],
            bg_color=self.themes["app_color"]["dark_one"],
            radius=0,
            bg_color_hover=self.themes["app_color"]["context_color"],
            items=['SN Number only', 'Imei Number only', 'Meid Number only'],
            editable=True
        )

        self.ui.load_pages.stock_search_key_layout.addWidget(self.stock_search_key)

        self.stock_search = PyLineEdit(

            context_color=self.themes["app_color"]["context_color"],
            color=self.themes["app_color"]["text_active"],
            bg_color=self.themes["app_color"]["dark_one"]

        )

        self.ui.load_pages.stock_search_layout.addWidget(self.stock_search)

        self.stock_table = PyTableWidget(
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["context_color"],
            bg_color=self.themes["app_color"]["bg_two"],
            header_horizontal_color=self.themes["app_color"]["bg_one"],
            header_vertical_color=self.themes["app_color"]["bg_three"],
            bottom_line_color=self.themes["app_color"]["bg_three"],
            grid_line_color=self.themes["app_color"]["bg_one"],
            scroll_bar_bg_color=self.themes["app_color"]["bg_one"],
            scroll_bar_btn_color=self.themes["app_color"]["dark_four"],
            context_color=self.themes["app_color"]["context_color"]
        )
        self.stock_table.setColumnCount(10)
        self.stock_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.stock_table.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.stock_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.stock_table.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # Columns / Header
        self.cart_column_1 = QTableWidgetItem()
        self.cart_column_1.setTextAlignment(Qt.AlignCenter)
        self.cart_column_1.setText("ID")

        self.cart_column_2 = QTableWidgetItem()
        self.cart_column_2.setTextAlignment(Qt.AlignCenter)
        self.cart_column_2.setText("Type")

        self.cart_column_3 = QTableWidgetItem()
        self.cart_column_3.setTextAlignment(Qt.AlignCenter)
        self.cart_column_3.setText("Model")

        self.cart_column_4 = QTableWidgetItem()
        self.cart_column_4.setTextAlignment(Qt.AlignCenter)
        self.cart_column_4.setText("Quantity")

        self.cart_column_5 = QTableWidgetItem()
        self.cart_column_5.setTextAlignment(Qt.AlignCenter)
        self.cart_column_5.setText("Cost Price")

        self.cart_column_6 = QTableWidgetItem()
        self.cart_column_6.setTextAlignment(Qt.AlignCenter)
        self.cart_column_6.setText("Salling Price")

        self.cart_column_7 = QTableWidgetItem()
        self.cart_column_7.setTextAlignment(Qt.AlignCenter)
        self.cart_column_7.setText("tax %")

        self.cart_column_8 = QTableWidgetItem()
        self.cart_column_8.setTextAlignment(Qt.AlignCenter)
        self.cart_column_8.setText("Created Date")

        self.cart_column_9 = QTableWidgetItem()
        self.cart_column_9.setTextAlignment(Qt.AlignCenter)
        self.cart_column_9.setText("Last Upadte")

        self.cart_column_10 = QTableWidgetItem()
        self.cart_column_10.setTextAlignment(Qt.AlignCenter)
        self.cart_column_10.setText("User")

        # Set column
        self.stock_table.setHorizontalHeaderItem(0, self.cart_column_1)
        self.stock_table.setHorizontalHeaderItem(1, self.cart_column_2)
        self.stock_table.setHorizontalHeaderItem(2, self.cart_column_3)
        self.stock_table.setHorizontalHeaderItem(3, self.cart_column_4)
        self.stock_table.setHorizontalHeaderItem(4, self.cart_column_5)
        self.stock_table.setHorizontalHeaderItem(5, self.cart_column_6)
        self.stock_table.setHorizontalHeaderItem(6, self.cart_column_7)
        self.stock_table.setHorizontalHeaderItem(7, self.cart_column_8)
        self.stock_table.setHorizontalHeaderItem(8, self.cart_column_9)
        self.stock_table.setHorizontalHeaderItem(8, self.cart_column_10)

        self.ui.load_pages.stock_table_frame.addWidget(self.stock_table)

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


