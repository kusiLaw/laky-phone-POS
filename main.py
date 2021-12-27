
# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////
from gui.uis.windows.main_window.functions_main_window import *
from gui.uis.splashscreen.splash_screen import *
from gui.uis.login.login import *

import sys
import os
from time import perf_counter
from decimal import Decimal
# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from qt_core import *
from datetime import datetime
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

        self.showcomponents()
        self.login_btn.clicked.connect(lambda: self.login())
        self.sign_out.clicked.connect(lambda: self.logout())
        self.user_name.textChanged.connect(lambda: self.ui.load_pages.login_form_info.setText('') )
        self.user_passsword.textChanged.connect(lambda: self.ui.load_pages.login_form_info.setText(''))

        # phone signals
        self.add_to_cart_btn.clicked.connect(lambda: self.dispatch(self.add_to_cart_btn))
        self.remove_from_cart_btn.clicked.connect(lambda: self.dispatch(self.remove_from_cart_btn))
        self.phone_clear_cart_btn.clicked.connect(lambda: self.dispatch(self.phone_clear_cart_btn))
        self.phone_buyme_btn.clicked.connect(lambda : self.dispatch(self.phone_buyme_btn))
        self.phone_print_btn.clicked.connect(lambda: self.dispatch(self.phone_print_btn))
        self.phone_clear_btn.clicked.connect(lambda : self.clearforms(flag='phone'))
        self.table_widget.currentItemChanged.connect(lambda :self.table_row_Change(self.table_widget, flag='phone'))


        self.phone_type.currentIndexChanged.connect(lambda: self.type_feed_model(self.phone_model,str(self.phone_type.currentText().strip())))
        self.phone_model.currentIndexChanged.connect(lambda:self.model_feed(str(self.phone_model.currentText().strip()), "phone"))

        # stock btn signals
        self.stock_save.clicked.connect(lambda: self.dispatch(self.stock_save))
        self.stock_type.currentIndexChanged.connect(lambda: self.type_feed_model(self.stock_model,str(self.stock_type.currentText().strip())))
        self.stock_model.currentIndexChanged.connect(lambda:self.model_feed(str(self.stock_model.currentText().strip())))
        self.stock_clear.clicked.connect(lambda: self.clearforms())
        self.stock_table.currentItemChanged.connect(lambda :self.table_row_Change( self.stock_table, flag='stock'))

        self.load_sale_tables()
        self.load_stock_tables()

        # SHOW MAIN WINDOW
        # ///////////////////////////////////////////////////////////////
        self.show()

    def login(self):
        if user.login(str(self.user_name.text()), str(self.user_passsword.text())):
            self.showcomponents(True)
            #clear user password in order not to hack
            user.password = ''
            self.user_passsword.clear()

            #load the dashbord
            MainFunctions.set_page(self, self.ui.load_pages.dasboard)

        else:
            self.ui.load_pages.login_form_info.setText('Wrong username or password')




    def logout(self):
        # load the login form
        MainFunctions.set_page(self, self.ui.load_pages.home_page)
        #hide buttons
        self.showcomponents(False)

        if  MainFunctions.left_column_is_visible:
            MainFunctions.toggle_left_column(self)
        if MainFunctions.right_column_is_visible:
            MainFunctions.toggle_right_column(self)


    def table_row_Change(self, table_widget, flag = None):
        index = table_widget.currentIndex() # get hold of row index clicked
        # print(index.row(), index.column())

        data = []
        for col in range(table_widget.columnCount()): # iterate through column count
            # it = table_widget.item(ind.row(), col)
            data.append(table_widget.item(index.row(), col).text())

        # feed data to the form base on index
        print(data)
        if data:
            if flag == 'phone':
                self.customerName.setText(data[0])
                self.contactName.setText(data[1])

                self.phone_type.setCurrentText(data[2])
                self.phone_model.setCurrentText(data[3])
                # self.phone_imei.setText(data[1])

                self.phone_sn.setText(data[4])
                self.phone_price.setText(data[5])
                self.phone_discount.setText(data[6])
                self.phone_tax.setText(data[8])


            elif flag == 'stock':
                self.stock_type.setCurrentText(data[1])
                self.stock_model.setCurrentText(data[2])
                self.stock_qantity.setText(data[3])
                self.stock_cp.setText(data[4])
                self.stock_sp.setText(data[5])
                self.stock_tax.setText(data[6])

                #load rest of the field


    def dispatch(self, obj):

        if obj.text() == "Print":
            print("print was pressed")

        elif obj.text()  == "Buy / Save":
            print('save was pressde')
            print(user.caches_retail)
        elif obj.text() == "Save":
            # stock
            self.save_stock()
            # print(user.caches_retail)

        elif obj.text() == "Clear Cart":
            user.caches_retail = {}
            self.load_phone_cart()

        elif obj.text() == "Remove from Cart":
            print('save was pressde')
        elif obj.text() == "Add to Cart":
            if not self.phone_sn.text() == '':
                user.add_to_cart(ph_type= str(self.phone_type.currentText()),ph_model= str(self.phone_model.currentText()),
                                 sn = str(self.phone_sn.text()),ime= str(self.phone_imei.currentText()),price=Decimal(self.phone_price.text()))
                # print(user.caches_retail)
                self.load_phone_cart()
                self.select_table_row(self.phone_cart)
                return
            QMessageBox.information(None, "Received Key Release EVent", f"Nothing to add to cart, make sure sn is not empty \n Thank you" )

    def clearforms(self, flag = "stock"):
        if flag == 'stock':
            self.stock_cp.setText("")
            self.stock_qantity.setText("")
            self.stock_sp.setText("")
            self.stock_tax.setText("")
            self.stock_type.clearEditText()
            self.stock_model.clearEditText()
            return
        if flag == 'phone':
            self.customerName.setText("")
            self.contactName.setText("")
            self.phone_sn.setText("")
            self.phone_price.setText("")
            self.phone_type.clearEditText()
            self.phone_model.clearEditText()
            self.phone_imei.clearEditText()

            # self.phone_price.setText(str(dic.get('sp', "")))
            # self.phone_tax.setText(str(dic.get('tax', "")))
            # self.phone_discount.setText(str(dic.get('0')))

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

    def save_stock(self):

        user.savestock(user_id=user.id, name=str(self.stock_type.currentText()).strip(),
                       model=str(self.stock_model.currentText()).strip(),
                     cp=Decimal(self.stock_cp.text().strip()),
                       sp=Decimal(self.stock_sp.text().strip()),
                       qty=int(self.stock_qantity.text().strip()),
                        date=datetime.now(),
                       tax= int(self.stock_tax.text().strip()),
                       suplier = str(self.stock_suplier.currentText()).strip(),
                        suplier_number='+233684010',
                       prod_code= str(self.stock_prod_code.currentText()).strip(),
                       code_list=None)

        self.load_stock_tables()

        # LEFT MENU BTN IS CLICKED

    def update_stock(self):
        pass
    def delete_stock(self):
        pass

    def show_required_field(self):
        pass

    def feed_combo(self, Qobj, feed : list= None ):
        items = feed
        # items.append('')
        print(items)
        Qobj.clear()
        Qobj.addItems(items)
        # Qobj.setCurrentText("")

        # calling completer class to autocomplete
        self.completer = QCompleter(items)
        self.completer.setCaseSensitivity(Qt.CaseInsensitive)
        Qobj.setCompleter(self.completer)
        print(user.feed_type())

    def type_feed_model(self,Qpassive ,text):
        if text == "":
            return
        self.feed_combo(Qobj= Qpassive, feed = user.feed_model(text))

    def model_feed(self, model_text, flag = "stock"):
        dic= user.model_feed_rest(model_text)
        if flag == "stock":
            self.stock_cp.setText(str(dic.get('cp', "")))
            self.stock_qantity.setText(str(dic.get('qty', "")))
            self.stock_sp.setText(str(dic.get('sp', "")))
            self.stock_tax.setText(str(dic.get('tax', "")))
            return
        self.phone_price.setText(str(dic.get('sp', "")))
        self.phone_tax.setText(str(dic.get('tax', "")))
        self.phone_discount.setText(str(dic.get('0')))


    def select_table_row(self, table_obj):
        # auto select record if not empty
        if (table_obj.rowCount()):
            table_obj.selectRow(0)
            # print(table_obj.currentRow())

    def showcomponents(self, state =False):

        # self.ui.left_menu.setVisible(False)
        title_comp =["btn_user","btn_top_settings"]
        left_comp = ["btn_info","report_btn","stock_btn","phone_btn","home_btn"]
        for comp in title_comp:
            self.ui.title_bar_frame.findChild(QPushButton, comp).setVisible(state)

        for comp in left_comp:
            self.ui.left_menu.findChild(QPushButton, comp).setVisible(state)


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
            MainFunctions.set_page(self, self.ui.load_pages.dasboard)

        # Open Page 2
        if btn.objectName() == "phone_btn":
            self.ui.left_menu.select_only_one(btn.objectName())

            # Load page
            MainFunctions.set_page(self, self.ui.load_pages.phone_page)


           # feed form with data from db
            self.feed_combo(self.phone_type,user.feed_type())
            self.clearforms(flag='phone')
            self.select_table_row(self.phone_cart)
            self.select_table_row(self.table_widget)
        # service page
        # if btn.objectName() == "service_btn":
        #     self.ui.left_menu.select_only_one(btn.objectName())
        #
        #     # Load page
        #     MainFunctions.set_page(self, self.ui.load_pages.service_page)

        # inventory page
        if btn.objectName() == "stock_btn":
            self.ui.left_menu.select_only_one(btn.objectName())

            # Load page
            MainFunctions.set_page(self, self.ui.load_pages.stock)

           # feed form with data from db
            self.feed_combo(self.stock_type,user.feed_type())
            self.clearforms()
            self.select_table_row(self.stock_table)

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

        if event.key() == Qt.Key_Return :

            if self.user_name.hasFocus() or self.user_passsword.hasFocus():
                # user on login interface
                self.login()
            print(MainFunctions.get_current_stack_page(self))



class LoginWindow(QMainWindow):
    # Load theme
    settings = Themes()
    theme = settings.items

    def __init__(self):
        # QMainWindow.__init__(self)
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # remove the standard tiltle bar
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.show()

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
    # window = LoginWindow()
    # EXEC APP
    # ///////////////////////////////////////////////////////////////
    sys.exit(app.exec())