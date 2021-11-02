
# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////
from gui.uis.windows.main_window.functions_main_window import *
from gui.uis.splashscreen.splash_screen import *
import sys
import os
from decimal import Decimal
# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from qt_core import *

# IMPORT SETTINGS
# ///////////////////////////////////////////////////////////////
from gui.core.json_settings import Settings
from gui.core.json_themes import Themes
# IMPORT PY ONE DARK WINDOWS
# ///////////////////////////////////////////////////////////////
# MAIN WINDOW
from gui.uis.windows.main_window import *

# IMPORT PY ONE DARK WIDGETS
# ///////////////////////////////////////////////////////////////
from gui.widgets import *
from gui.engine.phones_operations import Active_User

# ADJUST QT FONT DPI FOR HIGHT SCALE AN 4K MONITOR
# ///////////////////////////////////////////////////////////////
os.environ["QT_FONT_DPI"] = "96"
# IF IS 4K MONITOR ENABLE 'os.environ["QT_SCALE_FACTOR"] = "2"'

# set splashscreen Counter
counter = 0
user = Active_User()
user.login("laky1", "laky689393")

# MAIN WINDOW
# ///////////////////////////////////////////////////////////////
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # SETUP MAIN WINDOw
        # Load widgets from "gui\uis\main_window\ui_main.py"
        # ///////////////////////////////////////////////////////////////
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)

        # LOAD SETTINGS
        # ///////////////////////////////////////////////////////////////
        settings = Settings()
        self.settings = settings.items

        # SETUP MAIN WINDOW
        # ///////////////////////////////////////////////////////////////
        self.hide_grips = True # Show/Hide resize grips
        SetupMainWindow.setup_gui(self)

        self.add_to_cart_btn.clicked.connect(lambda: self.dispatch(self.add_to_cart_btn))
        self.remove_from_cart_btn.clicked.connect(lambda: self.dispatch(self.remove_from_cart_btn))
        self.phone_clear_cart_btn.clicked.connect(lambda: self.dispatch(self.phone_clear_cart_btn))
        self.phone_buyme_btn.clicked.connect(lambda : self.dispatch(self.phone_buyme_btn))
        self.phone_print_btn.clicked.connect(lambda: self.dispatch(self.phone_print_btn))

        # stock btn signals
        # stock_table.clicked.connect(lambda: self.dispatch(self.stock_table))



        self.load_sale_tables()
        self.load_stock_tables()

        # SHOW MAIN WINDOW
        # ///////////////////////////////////////////////////////////////
        self.show()

    def dispatch(self, obj):

        if obj.text() == "Print":
            print("print was pressed")

        elif obj.text()  == "Buy / Save":
            print('save was pressde')

        elif obj.text() == "Clear Cart":
            user.caches_retail = {}
            self.load_phone_cart()

        elif obj.text() == "Remove from Cart":
            print('save was pressde')
        elif obj.text() == "Add to Cart":
            user.add_to_cart(ph_type= str(self.phone_type.currentText()),ph_model= str(self.phone_model.currentText()),
                             sn = str(self.phone_sn.text()),ime= str(self.phone_imei.currentText()),price=Decimal(self.phone_price.text()))
            # print(user.caches_retail)
            self.load_phone_cart()


    def load_phone_cart(self):
        while (self.phone_cart.rowCount() > 0):
                self.phone_cart.removeRow(0)

        for _, val in  user.caches_retail.items():
            cart_row_number = self.phone_cart.rowCount()
            self.phone_cart.insertRow(cart_row_number) # Insert row
            self.phone_cart.setItem(cart_row_number, 0, QTableWidgetItem(str(val["ph_type"]))) # Add name
            self.phone_cart.setItem(cart_row_number, 1, QTableWidgetItem(str(val["ph_model"]))) # Add nick
            self.phone_cart.setItem(cart_row_number, 2, QTableWidgetItem(str(val["sn"]))) # Add pass
            self.phone_cart.setItem(cart_row_number, 3, QTableWidgetItem(str(val["ime"]))) # Add pass
            self.phone_cart.setItem(cart_row_number, 4, QTableWidgetItem(str(val["price"]))) # Add pass

            self.phone_cart.setRowHeight(cart_row_number, 20)


    def load_sale_tables(self):
        result = user.load_sale_phone_table()
        while (self.table_widget.rowCount() > 0):
            self.table_widget.removeRow(0)

        for tup in result:
            cart_row_number = self.table_widget.rowCount()
            self.table_widget.insertRow(cart_row_number)  # Insert row
            self.table_widget.setItem(cart_row_number, 0, QTableWidgetItem(str(tup[0])))  # Add name
            self.table_widget.setItem(cart_row_number, 1, QTableWidgetItem(str(tup[1])))  # Add nick
            self.table_widget.setItem(cart_row_number, 2, QTableWidgetItem(str(tup[2])))  # Add pass
            self.table_widget.setItem(cart_row_number, 3, QTableWidgetItem(str(tup[3])))  # Add pass
            self.table_widget.setItem(cart_row_number, 4, QTableWidgetItem(str(tup[4])))  # Add pass
            self.table_widget.setItem(cart_row_number, 5, QTableWidgetItem(str(tup[5])))  # Add pass
            self.table_widget.setItem(cart_row_number, 6, QTableWidgetItem(str(tup[6])))  # Add pass
            self.table_widget.setItem(cart_row_number, 7, QTableWidgetItem(str(tup[7])))  # Add pass
            self.table_widget.setItem(cart_row_number, 8, QTableWidgetItem(str(tup[8])))  # Add pass
            self.table_widget.setItem(cart_row_number, 9, QTableWidgetItem(str(tup[9])))  # Add pass
            self.table_widget.setItem(cart_row_number, 10, QTableWidgetItem(str(tup[10])))  # Add pass


            self.table_widget.setRowHeight(cart_row_number, 20)

    def load_stock_tables(self):
        result = user.load_stock()
        while (self.stock_table.rowCount() > 0):
            self.stock_table.removeRow(0)
        print(result)

        for tup in result:
            cart_row_number = self.stock_table.rowCount()
            self.stock_table.insertRow(cart_row_number)  # Insert row
            self.stock_table.setItem(cart_row_number, 0, QTableWidgetItem(str(tup[0])))  # Add name
            self.stock_table.setItem(cart_row_number, 1, QTableWidgetItem(str(tup[1])))  # Add nick
            self.stock_table.setItem(cart_row_number, 2, QTableWidgetItem(str(tup[2])))  # Add pass
            self.stock_table.setItem(cart_row_number, 3, QTableWidgetItem(str(tup[3])))  # Add pass
            self.stock_table.setItem(cart_row_number, 4, QTableWidgetItem(str(tup[4])))  # Add pass
            self.stock_table.setItem(cart_row_number, 5, QTableWidgetItem(str(tup[5])))  # Add pass
            self.stock_table.setItem(cart_row_number, 6, QTableWidgetItem(str(tup[6])))  # Add pass
            self.stock_table.setItem(cart_row_number, 7, QTableWidgetItem(str(tup[7])))  # Add pass
            self.stock_table.setItem(cart_row_number, 8, QTableWidgetItem(str(tup[8])))  # Add pass
            self.stock_table.setItem(cart_row_number, 9, QTableWidgetItem(str(tup[9])))  # Add pass


            self.stock_table.setRowHeight(cart_row_number, 20)

    # LEFT MENU BTN IS CLICKED
    # Run function when btn is clicked
    # Check funtion by object name / btn_id
    # ///////////////////////////////////////////////////////////////
    def btn_clicked(self):
        # GET BT CLICKED
        btn = SetupMainWindow.setup_btns(self)

        # if btn.objectName == "phone_buyme_btn":
        #     print('buybought')
        # print(btn.objectName)

        # Open Page 1
        if btn.objectName() == "home_btn":
            self.ui.left_menu.select_only_one(btn.objectName())

            # Load page
            MainFunctions.set_page(self, self.ui.load_pages.home_page)

        # Open Page 2
        if btn.objectName() == "phone_btn":
            self.ui.left_menu.select_only_one(btn.objectName())

            # Load page
            MainFunctions.set_page(self, self.ui.load_pages.phone_page)

        # service page
        if btn.objectName() == "service_btn":
            self.ui.left_menu.select_only_one(btn.objectName())

            # Load page
            MainFunctions.set_page(self, self.ui.load_pages.service_page)

        # inventory page
        if btn.objectName() == "stock_btn":
            self.ui.left_menu.select_only_one(btn.objectName())

            # Load page
            MainFunctions.set_page(self, self.ui.load_pages.stock)




        # open menu 2 of left colomn stackwiew

        # get top settings
        top_btn_settings = MainFunctions.get_title_bar_btn(self, "btn_top_settings")
        top_btn_user = MainFunctions.get_title_bar_btn(self, "btn_user")
        if btn.objectName() == "report_btn" or btn.objectName() == "btn_close_left_column":
            # disable to btn active
            top_btn_settings.set_active(False)
            top_btn_user.set_active(False)

            # check if left column is visible
            if not MainFunctions.left_column_is_visible(self):
                # show /hide
                MainFunctions.toggle_left_column(self)
                self.ui.left_menu.select_only_one_tab(self.objectName())
            else:
                if btn.objectName() == "btn_close_left_column":
                    # deselect all
                    self.ui.left_menu.deselect_all_tab()

                    # show/hide
                    MainFunctions.toggle_left_column(self)

                    # select tab
                self.ui.left_menu.select_only_one_tab(btn.objectName())

            # chge to second menu
            if btn.objectName() != "btn_close_left_column":
                MainFunctions.set_left_column_menu(self,
                                                   menu = self.ui.left_column.menus.menu_2,
                                                   title = "Report Tab",
                                                   icon_path= Functions.set_svg_icon("icon_file.svg")
                )


            # Open settings
        if btn.objectName() == "btn_info" or btn.objectName() == "btn_close_left_column":
            # disable to btn active
            top_btn_settings.set_active(False)
            top_btn_user.set_active(False)

            # check if left column is visible
            if not MainFunctions.left_column_is_visible(self):
                # show /hide
                MainFunctions.toggle_left_column(self)
                self.ui.left_menu.select_only_one_tab(self.objectName())
            else:
                if btn.objectName() == "btn_close_left_column" :
                    # deselect all
                    self.ui.left_menu.deselect_all_tab()

                    # show/hide
                    MainFunctions.toggle_left_column(self)

                    #select tab
                self.ui.left_menu.select_only_one_tab(btn.objectName())
            # chge  menu
            if btn.objectName() != "btn_close_left_column":
                MainFunctions.set_left_column_menu(self,
                                                   menu=self.ui.left_column.menus.menu_1,
                                                   title="Info tab",
                                                   icon_path=Functions.set_svg_icon("icon_info.svg")
                                                   )



        # TITLE BAR MENU
        # ///////////////////////////////////////////////////////////////
        # self.right_column_has_open = False


        # SETTINGS TITLE BAR
        if btn.objectName() == "btn_top_settings":
            # check if left column is visible
            if not MainFunctions.right_column_is_visible(self):
                # first toggle will  open, default is close when app start
                # make it active and deactivate other

                btn.set_active(True)
                top_btn_user.set_active(False)

                # Show / Hide
                MainFunctions.toggle_right_column(self)
                # self.right_column_has_open = True

                MainFunctions.set_right_column_menu(self, menu=self.ui.right_column.setting_page)

            else:
                # now right-column  open
                # this indicate button is pressed the second time
                # toggle again will close it, so deselect all
                btn.set_active(False)
                top_btn_user.set_active(False)

                # Show / Hide
                MainFunctions.toggle_right_column(self)
                # self.right_column_has_open = False
                MainFunctions.set_right_column_menu(self, menu=self.ui.right_column.setting_page)


            # # Get Left Menu settings
            # top_settings = MainFunctions.get_left_menu_btn(self, "btn_user")
            # top_settings.set_active_tab(False)

            # # Get Left Menu info
            # top_info = MainFunctions.get_left_menu_btn(self, "btn_info")
            # top_info.set_active_tab(False)

        if btn.objectName() == "btn_user":
            # Toogle Active
            if not MainFunctions.right_column_is_visible(self):
                # first toggle will  open, default is close when app start
                # make it active and deactivate other

                btn.set_active(True)
                top_btn_settings.set_active(False)

                # Show / Hide
                MainFunctions.toggle_right_column(self)

                MainFunctions.set_right_column_menu(self, menu=self.ui.right_column.profile_page)
                # self.right_column_has_open = True


            else:
                # now right-column  open
                # this indicate button is pressed the second time
                # toggle again will close it, so deselect all

                btn.set_active(False)
                top_btn_settings.set_active(False)


                # Show / Hide
                MainFunctions.toggle_right_column(self)
                MainFunctions.set_right_column_menu(self, menu=self.ui.right_column.profile_page)


            # # Get Left Menu settings
            # top_settings = MainFunctions.get_left_menu_btn(self, "btn_top_settings")
            # top_settings.set_active_tab(False)

            # # Get Left Menu info
            # top_info = MainFunctions.get_left_menu_btn(self, "btn_info")
            # top_info.set_active_tab(False)

            # DEBUG
        print(f"Button {btn.objectName()}, clicked!")




    # LEFT MENU BTN IS RELEASED
    # Run function when btn is released
    # Check funtion by object name / btn_id
    # ///////////////////////////////////////////////////////////////
    def btn_released(self):
        # GET BT CLICKED
        btn = SetupMainWindow.setup_btns(self)

        # DEBUG
        print(f"Button {btn.objectName()}, released!")

    # RESIZE EVENT
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        SetupMainWindow.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()



class SplashScreen(QMainWindow):
    # Load theme
    settings = Themes()
    theme = settings.items

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)


        # remove the standard tiltle bar
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)


        print(self.theme["app_color"]["dark_three"])
        # import circular progress
        self.progress = PyCircularProgress(
            progress_color = self.theme["app_color"]["context_color"],
            text_color = self.theme["app_color"]["context_color"]
        )
        self.progress.width = 250  # 270
        self.progress.height = 250  # 270
        self.progress.value = 0
        self.progress.setFixedSize(self.progress.width, self.progress.height)

        # move definds the distance of widget in relation to parent
        self.progress.move(25,26)  #(15,15)
        self.progress.add_shadow(True)
        self.progress.font_size = 25
        self.progress.bg_color = QColor(68,71,90,140)

        # set to CircularProgress centralwedgit
        self.progress.setParent(self.ui.centralwidget)
        self.progress.show()

        # Drop shadow
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(15)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 120))
        self.setGraphicsEffect(self.shadow)

        # Qtimer
        self.timer = QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(2) # 25

        self.show()


    def update(self):
        global counter

        self.progress.set_value(counter)

        counter += 1

        if counter >= 101:
            self.timer.stop()
            self.main = MainWindow()
            self.main.show()
            self.close()

    # def keyPressEvent(self, event):
    #     if event.key() == Qt.Key_Escape:
    #         QMessageBox.information(None, "Received Key Release EVent", "You Pressed ewewewewewe  ewewewewewewe  we wwew wewe we w: "+ event.text())
    #         self.close()



# SETTINGS WHEN TO START
# Set the initial class and also additional parameters of the "QApplication" class
# ///////////////////////////////////////////////////////////////
if __name__ == "__main__":
    # APPLICATION
    # ///////////////////////////////////////////////////////////////
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    # window = MainWindow()
    window = SplashScreen()
    # EXEC APP
    # ///////////////////////////////////////////////////////////////
    sys.exit(app.exec())