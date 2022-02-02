
# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////
from gui.uis.windows.main_window.functions_main_window import *
from gui.uis.splashscreen.splash_screen import *
from gui.uis.login.login import *
from gui.engine.my_exceptions import InvalidSalesPrice, OutOfStockException,Invalid_Item_Purchase,LakyException


import sys
import os
from time import perf_counter
from datetime import datetime
from decimal import Decimal, InvalidOperation
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
from mysql.connector import errorcode, errors

# IMPORT PY ONE DARK WIDGETS
# ///////////////////////////////////////////////////////////////
from gui.widgets import *
from gui.engine.phones_operations import Active_User
from gui.engine.discriptor import *

# ADJUST QT FONT DPI FOR HIGHT SCALE AN 4K MONITOR
# ///////////////////////////////////////////////////////////////
os.environ["QT_FONT_DPI"] = "96"
# IF IS 4K MONITOR ENABLE 'os.environ["QT_SCALE_FACTOR"] = "2"'

# set splashscreen Counter
counter = 0

user = Active_User()

# user.create_user("lawrence", 'secretry', 'laky', 'laky', 'lawrence@txt.com', "sec",
#               True, True, True, True, True, )



# MAIN WINDOW
# ///////////////////////////////////////////////////////////////
class MainWindow(QMainWindow):
    name = CharField(_min=2, _max=24)
    model = CharField(_min=2, _max=24)
    suplier = CharField(_min=0, _max=24)
    number = CharField(_min=0, _max=24)
    sn = CharField()
    cp = Decimalfield(_min=1)
    sp = Decimalfield(_min=1)
    qty = IntegerField(_min=0)
    order_id = CharField(_min=0, _max=45)
    tax = IntegerField(_min=0, )
    suplier_cached = {}

    sales_oporation_mapper = {
        "Retial" : False,
        "Retail (Strict)" : True  ,
        "Wholesale" : False
    }



    def __init__(self):
        super().__init__()

        # SETUP MAIN WINDOw
        # Load widgets from "gui\uis\main_window\ui_main.py"
        # ///////////////////////////////////////////////////////////////l
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

        # print(datetime.now().strftime('%Y/%m/%d %H:%M'))

        # self.messageBox  = MessageBox()



        self.use_retail_oporation_flag = self.sales_oporation_mapper.get(self.sale_opperation_mode.currentText(), False)

        self.showcomponents()
        self.login_btn.clicked.connect(lambda: self.login())
        self.sign_out.clicked.connect(lambda: self.logout())
        self.reset_pass.clicked.connect(lambda : self.reset_passwrd())
        self.user_name.textChanged.connect(lambda: self.ui.load_pages.login_form_info.setText('') )
        self.user_passsword.textChanged.connect(lambda: self.ui.load_pages.login_form_info.setText(''))

        #settings signals

        self.sale_opperation_mode.currentTextChanged.connect(lambda : self.write_settings() )



        # phone signals
        self.add_to_cart_btn.clicked.connect(lambda: self.add_to_cart(use_retail = self.use_retail_oporation_flag )) #use_retail mustread from settins

        self.remove_from_cart_btn.clicked.connect(lambda: self.remove_from_cart(self.phone_cart, use_retail = self.use_retail_oporation_flag))
        self.phone_cart.itemDoubleClicked.connect(lambda: self.remove_from_cart(self.phone_cart,use_retail = self.use_retail_oporation_flag))

        self.phone_clear_cart_btn.clicked.connect(lambda: self.clear_cart())
        self.phone_buyme_btn.clicked.connect(lambda : self.buy_phone())
        self.phone_delete_btn.clicked.connect(lambda : self.delete_buy())
        self.phone_print_btn.clicked.connect(lambda: self.dispatch(self.phone_print_btn))
        self.phone_clear_btn.clicked.connect(lambda : self.clearforms(flag='phone'))
        self.phone_all_in_one_btn.clicked.connect(lambda : self.all_in_one_buy())
        self.table_widget.currentItemChanged.connect(lambda :self.table_row_Change(self.table_widget, flag='phone'))
        # self.phone_cart.itemClicked.connect(lambda :self.remove_from_cart(self.phone_cart))



        self.phone_type.currentIndexChanged.connect(lambda: self.type_feed_model(self.phone_model,str(self.phone_type.currentText().strip())))
        self.phone_model.currentIndexChanged.connect(lambda:self.model_feed(str(self.phone_model.currentText().strip()), "phone"))
        self.phone_search_edit.textChanged.connect( lambda: self.find_name(self.phone_search_edit,self.table_widget , self.phone_search_key.currentText(), flag='phone'))



        # stock btn signals
        self.stock_save.clicked.connect(lambda: self.save_stock())

        self.stock_type.currentIndexChanged.connect(lambda: self.type_feed_model(self.stock_model,str(self.stock_type.currentText().strip())))
        self.stock_model.currentIndexChanged.connect(lambda:self.model_feed(str(self.stock_model.currentText().strip())))
        self.stock_prod_code.currentIndexChanged.connect(lambda:self.order_id_feed_rest())
        self.stock_suplier.currentIndexChanged.connect(lambda:self.feed_suplier(internal_op=False))

        self.stock_clear.clicked.connect(lambda: self.clearforms())
        self.stock_table.currentItemChanged.connect(lambda :self.table_row_Change( self.stock_table, flag='stock'))

        self.stock_cp.editingFinished.connect(lambda: self.stock_cp.setText(self.decimal_Input(self.stock_cp.text())))
        self.stock_sp.editingFinished.connect(lambda: self.stock_sp.setText(self.decimal_Input(self.stock_sp.text())))
        self.stock_tax.editingFinished.connect(lambda: self.stock_tax.setText(self.tax_Input(self.stock_tax.text())))
        self.stock_sn_list.itemDoubleClicked.connect(lambda : self.stock_sn_list.takeItem(self.stock_sn_list.currentRow()))
        self.stock_sn_list.itemClicked.connect(lambda:self.count_sn())
        self.stock_search.textChanged.connect(lambda:self.find_name(self.stock_search, self.stock_table, self.stock_search_key.currentText() ))

        # SHOW MAIN WINDOW
        # ///////////////////////////////////////////////////////////////
        self.show()



        self.user_name.setText('laky')
        self.user_passsword.setText('11111')
    def login(self):
        if user.login(str(self.user_name.text()), str(self.user_passsword.text())):
            self.showcomponents(True)
            #clear user password in order not to hack
            user.password = ''
            self.user_passsword.clear()
            user.has_login = True
            #load the dashbord
            self.ui.load_pages.dash_user_name.setText(" ".join([user.fname, user.lname]))
            self.ui.load_pages.dash_role.setText(user.role)
            self.ui.load_pages.dash_email.setText(user.email)
            self.ui.load_pages.dash_last_seen.setText(str(user.last_seen))
            self.load_high_purchase()

            self.dash_board_stock_table()
            self.dash_board_avg()

            MainFunctions.set_page(self, self.ui.load_pages.dasboard)

            # try:
            #     for x in ("T", "F", "G", "F"):
            #         user.savestock(user_id=user.id, name="Infinix", model=f"{x}20r", cp=125.90, sp=401.32, qty=8,
            #                        date='2020-12-26', tax=0, suplier='Adams bee', suplier_number='+23302152222', prod_code='ADMB-157',
            #                        code_list=(f'sn-232456-1', f'sn-232456-4', f'sn-232456-5', f'sn-232456-41', f'sn-232456-50'))
            #
            #
            # except  errors.Error as err:
            #     if err.errno == errorcode.ER_DUP_ENTRY:
            #         return "record already exist"
            #     else:
            #         print(err)
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

    def reset_passwrd(self):

        if not self.comfirm_pass.text() == self.new_pass.text():
            MessageBox( "password not same", title ="password")
            #
            return
        if not self.old_pass.text() or not len(self.comfirm_pass.text()) > 4 or not len(self.new_pass.text()) >= 4:
            MessageBox("password lenght must be more than 4 digit", title = "weak password")
            return
        if user.reset_password( old_password= self.old_pass.text(),
                                new_password= self.new_pass.text(),
                                user_name= user.username ,
                                user_id= user.id):
            MessageBox(  "Password reset ok", title ="Reset Password")
            self.old_pass.setText('')
            self.new_pass.setText('')
            self.comfirm_pass.setText('')
            self.logout()
        else:
            MessageBox("Wrong password", title ="Reset Password")

    def buy_phone(self):
        print(user.caches_retail)
        try:
            # 'retail',
            user.buyphone( customer_name = self.customerName.text() or 'Customer', customer_number=self.contactName.text() or '+233')
        except (ValueError, InvalidSalesPrice, OutOfStockException,Invalid_Item_Purchase, LakyException) as ex:

            MessageBox( f"{ex}", title ="Item")
        # except:print('save unknown error')
        else:
            #successfull save,  patch the cache with trans code, set to form
            self.load_sale_tables()
            self.phone_order_id.setText(user.caches_retail.get('transcode' , ''))
            self.clear_cart()
            self.select_table_row(self.table_widget)

    def delete_buy(self):
        if self.phone_order_id.text():
            try:
                user.undo_buy(self.phone_order_id.text())
            except LakyException as e:
                MessageBox( f"{e}", title =  "Delete")

            self.load_sale_tables()

        else:
            # QMessageBox.information(self, "Delete", f"Transaction ID is empty")
            MessageBox(f"this Transaction ID is empty", title =  "Delete")

            # self.messageBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

    def all_in_one_buy(self):
        self.add_to_cart(use_retail=self.use_retail_oporation_flag)
        self.buy_phone()

    def save_stock(self):
        # supplier table
        # if none given used unknown and interface should be '' for both
        # if number only given used number and name as 'suplier'
        # if name only given unmber  +233 and interface should be ''

        try:
            # descriptor take care of it assignment
            self.name = self.remove_white_spaces(self.stock_type.currentText())
            self.model = self.remove_white_spaces(self.stock_model.currentText()).upper()
            self.number =self.remove_white_spaces(self.stock_suplier_contact.text(), space='') or "+233"
            self.qty = int(self.stock_qantity.text().strip()) or 0


            if self.number == "+233" : #num not given
                self.suplier =  "unknown"
                # print('number not given' , self.name, self.number)
            else:
                #num given, so suplier name or name "suplier" is used
                self.suplier = self.remove_white_spaces(self.stock_suplier.currentText()) or "Suplier"
                # print('number given', self.name, self.number)


            try:
                self.cp = Decimal(self.stock_cp.text().strip())
                self.sp = Decimal(self.stock_sp.text().strip())
            except:
                raise ValueError("invalid value for cp/unit or sp/unit")


            self.order_id = self.remove_white_spaces(self.stock_prod_code.currentText(), space='') or "n/a"
            self.tax = int(self.stock_tax.text().strip()) or 0

            #todo: delete this
            self.stock_sn_list.clear()
            # for sn in ['t-32344523i2e', 't-32344523i2i', 't-32344523i2a', 't-32344523i2f']:
            #     self.stock_sn_list.insertItem(0, sn)

            sn_list = [self.stock_sn_list.item(x).text() for x in range(self.stock_sn_list.count())]

            # print("exceptions pass")

        except (ValueError )as ex:
            MessageBox(str(ex), title = "Value Error")

        else:

            # print(self.name, self.model,
            #       self.number,self.suplier,
            #       self.cp,self.sp, self.stock_datetime.text(),
            #       self.qty,self.order_id,self.tax,sn_list,
            #       self.stock_datetime.text().split("-"),
            #       self.stock_datetime.toPydate()
            #       )
            #     #sn
            try:
                user.savestock(user_id=user.id, name=self.name, model=self.model, cp=self.cp,
                               sp= self.sp ,qty=self.qty,
                               dat=self.stock_datetime.toPydate(),
                               tax= self.tax, suplier = self.suplier,suplier_number=self.number,
                               prod_code= self.order_id,
                               code_list=sn_list)
            except LakyException as e:
                MessageBox(str(e), title="Unknown Error")


            self.load_stock_tables()
            self.select_table_row(self.stock_table, flag='stock')

    def find_name(self, line_edit , table, col_to_sch, flag= 'stock'):
        '''
        :param line_edit: QLineEdit obj
        :param table:
        :param col_to_sch:
        :param flag:
        :return: none
        '''
        col = {

           "stock": {
               'Model': 2,
               'Type/Brand': 1
           },

            "phone":{
                'Transaction code': 0,
                'Model': 2,
                'Contact': 1,
                'Date': 9,
            }
        }

        ind = col[flag][col_to_sch]
        if ind:
            name = line_edit.text().lower()
            for row in range(table.rowCount()):
                item = table.item(row, ind)
                # if the search is *not* in the item's text *do not hide* the row
                table.setRowHidden(row, name not in item.text().lower())

    def table_row_Change(self, table_widget, flag = None):
        index = table_widget.currentIndex() # get hold of row index clicked
        print("row and colunm index",index.row(), index.column())

        data = []
        print("row count",table_widget.rowCount(),"col count", table_widget.columnCount())
        # if not table_widget.rowCount() < 1:
        #go through the columns to get data
        for col in range(table_widget.columnCount()): # iterate through column count
            # print(index.row())
            if not index.row() < 0: #select row at lest 0
                # if not table_widget.item(index.row(), col):
                data.append(table_widget.item(index.row(), col).text())

        # feed data to the form base on index
        print(data)
        if data:
            if flag == 'phone':
                self.customerName.setText(data[9])
                self.contactName.setText(data[10])

                self.phone_type.setCurrentText(data[1])
                self.phone_model.setCurrentText(data[2])
                # self.phone_imei.setText(data[1])
                if data[3] == 'None':
                    # print(data[3], 'not')
                    self.phone_sn.setCurrentText( "")
                else:
                    self.phone_sn.setCurrentText(data[3])
                self.phone_price.setText(data[5])
                self.quantity.setText(data[4])
                self.phone_order_id.setText(data[0])
                # self.phone_tax.setText(data[8])


            elif flag == 'stock':
                self.stock_type.setCurrentText(data[1])
                self.stock_model.setCurrentText(data[2])
                self.stock_qantity.setText(data[3] )
                self.stock_cp.setText(self.decimal_Input(data[4]))
                self.stock_sp.setText(self.decimal_Input(data[5]))
                self.stock_tax.setText( self.tax_Input(data[6]) )

                #load rest of the field
                self.order_id_feed(self.stock_model.currentText())

    def add_to_cart(self, use_retail: bool ):
        if  use_retail and (not self.phone_sn.currentText() or self.phone_sn.currentText().strip()== "")   :
            MessageBox( f'If "Retails (Strict)" is selected, SN number must not be empty. '
                         f'Please change "Sales Operation Mode" in settings to Retail or Wholesale', title=" Add To Cart",)
            return
        if not self.phone_price.text().strip():# or isinstance(self.phone_price.text().strip(),Decimal):

            MessageBox(f"Price should not be empty", title="Price")
            return
        if not self.quantity.text().strip():
            MessageBox( f"Quantity should not be empty",title = "Quantity",)
            return

        #Todo: self.cost_price must multiply the qty and compare to sum of price
        try:
            if not Decimal(round(float(self.phone_price.text().strip())  * int(self.quantity.text().strip()),2)) < Decimal(round(float(self.cost_price) * int(self.quantity.text().strip()),2)) :# to compare before save, at model feed
                print('not lesser', self.cost_price)
                user.add_to_cart(ph_type=str(self.phone_type.currentText()), ph_model=str(self.phone_model.currentText()),
                                 sn=str(self.phone_sn.currentText().strip()), price=Decimal(self.phone_price.text()),cp=Decimal(self.cost_price),
                                 quantity = self.quantity.text() , use_retails= use_retail)


                self.store_sp = Decimal(0)  # to sum the tatol saling perice in the cart(dict)
                self.store_cp = Decimal(0)  # to sum the tatol cost perice in the cart(dict) , to show on interface
                self.store_qty = 0
                # sum the total price in the dict

                for _, item in user.caches_retail.items(): # to prevent recall for setting each btn
                    self.store_sp += item['price']
                    self.store_cp += item['cost_price']
                    self.store_qty += item['quantity']
                print(self.store_cp)
            else :
                MessageBox(f"Saling price can not be lesser than Price of {round(float(self.cost_price) * int(self.quantity.text().strip()),2)} \n Thank you", title= "Invalid Saling Price",)
                return

        except InvalidOperation :
            MessageBox(f"Invalid price input " ,title= "Price")


        else:

            self.phone_total_price.setText(str(self.store_sp))
            self.total_item.setText(str(self.store_qty) ) # str(int(sum([val['quantity'] for  _,val in user.caches_retail.items()])))

            self.load_phone_cart()
            self.select_table_row(self.phone_cart)

    def remove_from_cart(self,table_widget, use_retail = True):
        index = table_widget.currentIndex()
        if use_retail:
            item = table_widget.item(index.row(), 2) # 2 for s/n according to the table
        else:
            item = table_widget.item(index.row(), 1)
        # print('dfsdfsdfdsfsf')
        #del from cache
        try:
            del user.caches_retail[item.text()]
        except:
            # print('dfsdfsdfdsfsf')
            return


        self.store_sp = Decimal(0)  # to sum the tatol saling perice in the cart(dict)
        self.store_cp = Decimal(0)  # to sum the tatol cost perice in the cart(dict) , to show on interface
        self.store_qty = 0
        # sum the total price in the dict

        for _, item in user.caches_retail.items():  # to prevent recall for setting each btn
            self.store_sp += item['price']
            self.store_cp += item['cost_price']
            self.store_qty += item['quantity']


        self.load_phone_cart()


        self.total_item.setText(str(self.store_qty ))
        self.phone_total_price.setText(str(self.store_sp))
        self.select_table_row(self.phone_cart)

    def clear_cart(self):
        user.caches_retail = {}
        self.load_phone_cart()
        self.phone_total_price.setText("0")
        self.total_item.setText("0")

    def clearforms(self, flag = "stock"):
        if flag == 'stock':
            print('clearing')
            self.stock_cp.setText("")
            self.stock_qantity.setText("")
            self.stock_sp.setText("")
            self.stock_tax.setText("")
            self.stock_suplier_contact.setText("")
            self.stock_type.clearEditText()
            self.stock_model.clearEditText()
            self.stock_suplier.clearEditText()
            self.stock_prod_code.clearEditText()
            self.stock_datetime.setDate(datetime.now())
            self.stock_sn_list.clear()


            return
        if flag == 'phone':
            # print('clearing....')
            self.customerName.setText("")
            self.contactName.setText("")
            self.phone_sn.setCurrentText("")
            self.phone_price.setText("")
            # self.phone_type.setCurrentText("")
            self.phone_model.setCurrentText("5555")

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
            self.phone_cart.setItem(cart_row_number, 3, QTableWidgetItem(str(val["quantity"]))) # Add pass
            self.phone_cart.setItem(cart_row_number, 4, QTableWidgetItem(str(val["price"]))) # Add pass

            self.phone_cart.setRowHeight(cart_row_number, 20)

    def load_sale_tables(self):

        result = user.load_sale_phone_table()
        while (self.table_widget.rowCount() > 0):
            self.table_widget.removeRow(0)
        print(result)
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
            self.table_widget.setItem(cart_row_number, 11, QTableWidgetItem(str(tup[11])))  # Add pass

            self.table_widget.setRowHeight(cart_row_number, 20)

    def load_stock_tables(self):
        result = user.load_stock()

        while (self.stock_table.rowCount() > 0):
            self.stock_table.removeRow(0)
        # print(result)

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

    def load_high_purchase(self):
        result = user.highly_purchase()
        print(result)
        while (self.dash_table.rowCount() > 0):
            self.dash_table.removeRow(0)

        for tup in result:
            cart_row_number = self.dash_table.rowCount()
            self.dash_table.insertRow(cart_row_number)  # Insert row
            self.dash_table.setItem(cart_row_number, 0, QTableWidgetItem(str(tup[0])))  # Add name
            self.dash_table.setItem(cart_row_number, 1, QTableWidgetItem(str(tup[1])))  # Add nick

            self.table_widget.setRowHeight(cart_row_number, 20)

    def dash_board_stock_table(self):
        result = user.feed_dasboard_stock_table()

        while (self.dash_stock_analysis.rowCount() > 0):
            self.dash_stock_analysis.removeRow(0)
        if result:
            for tup in result.items():

                cart_row_number = self.dash_stock_analysis.rowCount()
                self.dash_stock_analysis.insertRow(cart_row_number)  # Insert row
                self.dash_stock_analysis.setItem(cart_row_number, 0, QTableWidgetItem(str(tup[0])))  # Add name
                self.dash_stock_analysis.setItem(cart_row_number, 1, QTableWidgetItem(str(int(tup[1]))))  # Add nick


                self.dash_stock_analysis.setRowHeight(cart_row_number, 20)

            #repaint acrc
            print("redy", result.values(), '--------', result)
            # cur_total/ prev_total * 100
            try:
                val=tuple(result.values())
                result =round(int(val[1]) / int(val[0]) * 100, 1)

            except:
                self.stock_sale_progress.progress_color = self.themes["app_color"]["red"]
                self.stock_sale_progress.text_color = self.themes["app_color"]["red"]
                self.stock_sale_progress.set_value(0)

            # result =100.5855
            if result >= 100:
                result = 100
                self.stock_sale_progress.progress_color = self.themes["app_color"]["green"]
                self.stock_sale_progress.text_color = self.themes["app_color"]["green"]
                self.stock_sale_progress.set_value(result)

            elif result < 25:

                self.stock_sale_progress.progress_color = self.themes["app_color"]["red"]
                self.stock_sale_progress.text_color = self.themes["app_color"]["red"]
                self.stock_sale_progress.set_value(result)
            else:
                self.stock_sale_progress.progress_color = self.themes["app_color"]["context_color"]
                self.stock_sale_progress.text_color = self.themes["app_color"]["context_color"]
                self.stock_sale_progress.set_value(result)

        else:
            self.stock_sale_progress.progress_color = self.themes["app_color"]["red"]
            self.stock_sale_progress.text_color = self.themes["app_color"]["red"]
            self.stock_sale_progress.set_value(0)

    def dash_board_avg(self):
        result = user.feed_dash_avg()

        while (self.dash_avg_analysis.rowCount() > 0):
            self.dash_avg_analysis.removeRow(0)
        print(result)

        if result:
            cart_row_number = self.dash_avg_analysis.rowCount()
            self.dash_avg_analysis.insertRow(cart_row_number)  # Insert row
            self.dash_avg_analysis.setItem(cart_row_number, 0, QTableWidgetItem(str( result.get('yr', str(datetime.today().year))))) # Add name
            self.dash_avg_analysis.setItem(cart_row_number, 1, QTableWidgetItem(str(int(result.get('avg', "0")))))  # Add nick

            cart_row_number = self.dash_avg_analysis.rowCount()
            self.dash_avg_analysis.insertRow(cart_row_number)
            self.dash_avg_analysis.setItem(cart_row_number, 0, QTableWidgetItem(str("Today")))  # Add name
            self.dash_avg_analysis.setItem(cart_row_number, 1, QTableWidgetItem(str(int(result.get("today", "0")or 0))))  # Add nick

            self.dash_avg_analysis.setRowHeight(cart_row_number, 20)

            self.ui.load_pages.todays_sales.setText(str(f'¢ {Decimal(result.get("today sales",  0) or 0.0) }'))
            quater_sale_color_temp= round(float(result.get('avg money', 1 )) /4)


            if quater_sale_color_temp > Decimal(result.get('today sales', 0 ) or 0) :
                # print(quater_sale_color_temp)  #below quater
                self.ui.load_pages.todays_sales.setStyleSheet(f'color: { self.themes["app_color"]["red"] };'
                                                          f'font-size: 55px;'
                                                          f'font-weight: 800;'
                                                          f'text-align: center;'
                                                          f'text-transform: uppercase;')

            elif   quater_sale_color_temp < Decimal(result.get('today sales', 0 )) and Decimal(result.get('today sales', 0 )) < result.get('avg money', 1 ) :
                # below quater
                self.ui.load_pages.todays_sales.setStyleSheet(f'color: {self.themes["app_color"]["context_color"]};'
                                                              f'font-size: 55px;'
                                                              f'font-weight: 800;'
                                                              f'text-align: center;'
                                                              f'text-transform: uppercase;')

            elif  Decimal(result.get('today sales', 0 )) > result.get('avg money', 1 ) :
                #above avg
                self.ui.load_pages.todays_sales.setStyleSheet(f'color: {self.themes["app_color"]["green"]};'
                                                              f'font-size: 55px;'
                                                              f'font-weight: 800;'
                                                              f'text-align: center;'
                                                              f'text-transform: uppercase;')

            else:
                self.ui.load_pages.todays_sales.setStyleSheet(f'color: {self.themes["app_color"]["red"]};'
                                                              f'font-size: 55px;'
                                                              f'font-weight: 800;'
                                                              f'text-align: center;'
                                                              f'text-transform: uppercase;')

            #repaint acrc

            # cur_avg/ avg * 100
            try:
                result = round( result['today'] / result['avg']* 100, 1)

            except:
                self.daily_sale_avg_progress.progress_color = self.themes["app_color"]["red"]
                self.daily_sale_avg_progress.text_color = self.themes["app_color"]["red"]
                self.daily_sale_avg_progress.set_value(0)

                self.ui.load_pages.todays_sales.setStyleSheet(f'color: {self.themes["app_color"]["red"]};'
                                                              f'font-size: 55px;'
                                                              f'font-weight: 800;'
                                                              f'text-align: center;'
                                                              f'text-transform: uppercase;')
                return
            # result = 1312

            if result >= 100:
                result = 100
                self.daily_sale_avg_progress.progress_color = self.themes["app_color"]["green"]
                self.daily_sale_avg_progress.text_color = self.themes["app_color"]["green"]
                self.daily_sale_avg_progress.set_value(result)

            elif result <  25:

                self.daily_sale_avg_progress.progress_color = self.themes["app_color"]["red"]
                self.daily_sale_avg_progress.text_color = self.themes["app_color"]["red"]
                self.daily_sale_avg_progress.set_value(result)
            else:
                self.daily_sale_avg_progress.progress_color = self.themes["app_color"]["context_color"]
                self.daily_sale_avg_progress.text_color = self.themes["app_color"]["context_color"]
                self.daily_sale_avg_progress.set_value(result)
        else:
            self.daily_sale_avg_progress.progress_color = self.themes["app_color"]["red"]
            self.daily_sale_avg_progress.text_color = self.themes["app_color"]["red"]
            self.daily_sale_avg_progress.set_value(0)

            self.ui.load_pages.todays_sales.setText('¢ 0.0')

    def decimal_Input(self, val):
        return f"{Decimal(str(val)):.2f}"

    def tax_Input(self, val):
        if int(val) > 100:
            return "100"
        return val

    def update_stock(self):
        pass
    def delete_stock(self):
        pass

    def show_required_field(self):
        pass

    def feed_combo(self, Qobj, feed : list= None ):
        items = feed
        # items.append('')
        # print(items)
        Qobj.clear()
        Qobj.addItems(items)
        # Qobj.setCurrentText("")

        # calling completer class to autocomplete
        self.completer = QCompleter(items)
        self.completer.setCaseSensitivity(Qt.CaseInsensitive)
        Qobj.setCompleter(self.completer)
        # print(user.feed_type())

    def type_feed_model(self,Qpassive ,text):
        if text == "":
            return
        self.feed_combo(Qobj= Qpassive, feed = user.feed_model(text))

    def model_feed(self, model_text, flag = "stock"):
        dic= user.model_feed_rest(model_text)
        # print(dic, "model_feed")
        if dic:
            if flag == "stock":
                self.stock_cp.setText(str(dic.get('cp', "")))
                self.stock_qantity.setText(str(dic.get('qty', "")))
                self.stock_sp.setText(str(dic.get('sp', "")))
                self.stock_tax.setText(str(dic.get('tax', "")))
                self.order_id_feed(model_text)#self.stock_model.currentText())
                return
            tax = dic.get('sp', 1)
            if not tax or tax == 0:
                tax = 1
            self.phone_price.setText(str( dic.get('sp', "")) )
            self.cost_price = dic.get('cp', 0) # to compare before save, a change in combobox update with current data
            self.quantity.setText(str('1'))

            # self.order_id_feed(model_text, tab_call= flag)
            self.model_feed_phone_sn(model_text)

    def order_id_feed(self, model_text , tab_call = None):
        result = user.feed_order_id(str(model_text)) #list self.stock_model.currentText()
        # if  tab_call == 'phone':
        #     self.feed_combo(self.phone_sn, result)
        #     return
        self.feed_combo(self.stock_prod_code, result)

    def order_id_feed_rest(self):
        result = user.order_id_feed_rest(str(self.stock_prod_code.currentText())) #dic
        print(result, "oder_id_feed")
        self.stock_suplier.setCurrentText(result.get('suplier', ''))
        self.stock_suplier_contact.setText(result.get('contact', ''))
        self.stock_datetime.setDate(result.get('dates', datetime.now()))
        self.stock_sn_list.clear()
        for sn in result['sn']:
            self.stock_sn_list.insertItem(0,sn)

        #count total item in sn
        self.count_sn()

    def feed_suplier(self, internal_op = True):
        """
        feed suplier combo
        :arg internal_op set to true if function was called internal or external by signal
        :param internal_op:
        :return:
        """


        if not internal_op: #exteernal call, and before currentindex change call with inter_op=false there must be items in combo
            self.stock_suplier_contact.setText(self.suplier_cached.get(self.stock_suplier.currentText(), ""))
            print("external call",self.suplier_cached)
        else:
            result = user.feed_suplier()

            if result:
                # cache it
                # print(result)
                for li in result:
                    self.suplier_cached[li[0]] = li[1]  #name as key, contact as value

                # fetch from caache.
                # print(self.suplier_cached)
                self.feed_combo(self.stock_suplier, list(self.suplier_cached.keys()))

                print("internal call", self.suplier_cached)

    def model_feed_phone_sn(self, model_text,has_bought=False ):

        result = user.feed_phone_sn(model_text,has_bought )
        # print('I am about to feed sn using ', model_text)

        if result:
            self.feed_combo(self.phone_sn, result)
            return

        #empty clear sn
        self.phone_sn.clear()
        # print(' sn empty using',  model_text)

    def select_table_row(self, table_obj, flag = None):
        # auto select record if not empty
        if table_obj.rowCount():
            table_obj.selectRow(0)
            # print(table_obj.currentRow())

            #if table has only one row, currentItemChanged never call to feed form so
            if table_obj.currentIndex() == 0: #only one record in take
                self.table_row_Change(table_obj, flag) #call this fn to feed more

    def showcomponents(self, state =False):

        # self.ui.left_menu.setVisible(False)
        title_comp =["btn_user","btn_top_settings"]
        left_comp = ["btn_info","report_btn","stock_btn","phone_btn","home_btn"]
        for comp in title_comp:
            self.ui.title_bar_frame.findChild(QPushButton, comp).setVisible(state)

        for comp in left_comp:
            self.ui.left_menu.findChild(QPushButton, comp).setVisible(state)

    def count_sn(self):
        self.ui.load_pages.stock_sn_total.setText(str(self.stock_sn_list.count()))

    def remove_white_spaces(self,text , space = ' '):
        if isinstance(text, str):
            return space.join(text.strip().split()).title()

    def write_settings(self):
        self.use_retail_oporation_flag = self.sales_oporation_mapper.get(self.sale_opperation_mode.currentText(), False)
        print(self.use_retail_oporation_flag)


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


            #dashboard
            self.load_high_purchase()
            self.dash_board_stock_table()
            self.dash_board_avg()
            # Load page
            MainFunctions.set_page(self, self.ui.load_pages.dasboard)

        # Open Page 2
        if btn.objectName() == "phone_btn":
            self.ui.left_menu.select_only_one(btn.objectName())

            # Load page
            MainFunctions.set_page(self, self.ui.load_pages.phone_page)


           # feed form with data from db
            self.load_sale_tables()
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
            self.load_stock_tables()
            self.feed_combo(self.stock_type,user.feed_type())
            self.feed_suplier()
            self.clearforms()
            self.select_table_row(self.stock_table,flag="stock")
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
        # print(f"Button {btn.objectName()}, clicked!")




    # LEFT MENU BTN IS RELEASED
    # Run function when btn is released
    # Check funtion by object name / btn_id
    # ///////////////////////////////////////////////////////////////
    def btn_released(self):
        # GET BT CLICKED
        btn = SetupMainWindow.setup_btns(self)

        # DEBUG
        # print(f"Button {btn.objectName()}, released!")

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
            text_color = self.theme["app_color"]["context_color"],
            progress_width=8,
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
        self.timer.start(15) # 25

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