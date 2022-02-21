import sys
from datetime import datetime
from mysql.connector import errorcode, errors
from collections.abc import Sequence
from decimal import Decimal
sys.path.append("..")
sys.path.append("../../")

from .my_db import My_db
from .discriptor import CharField, IntegerField, Decimalfield, Boolean, EmailField
from .auth import Encryption
from .my_exceptions import OutOfStockException, InvalidSalesPrice,Invalid_Item_Purchase,LakyException
from .trans import Transcode

''' 

insert into acc_price_list(AccModel,costPrice,selPrice,acc_quantity) value(@accmodel,@acc_cp ,@acc_sp,@accquantity)
on duplicate key update costPrice = @acc_cp, selPrice= @acc_sp , acc_quantity =(acc_quantity  + @accquantity )
'''


class PhoneStock:
    user_id = IntegerField(_min=0)
    st_name = CharField(_min=2, _max=24)
    st_ph_model = CharField(_min=2, _max=24)
    suplier = CharField(_min=0, _max=24)
    sn = CharField()
    cp = Decimalfield(_min=1)
    sp = Decimalfield(_min=1)
    qty = IntegerField(_min = 0)
    prod_code = CharField(_min = 0 , _max= 45)
    tax = IntegerField(_min = 0, )
    suplier_number = None
    code_list = None
    # id = None

    def __init__(self):
        self.con = My_db()

    def save_stock(self, user_id, name, model, cp, sp, qty, dat, tax=0, suplier='unknown',suplier_number = '+233',
                   prod_code="n/a", code_list=None ):
        self.user_id = user_id
        self.st_name = name
        self.st_ph_model = model
        self.suplier = suplier
        self.cp =  round(float(cp),2)
        self.sp = round(float(sp),2)
        self.qty = qty
        self.dat = dat
        self.code_list = code_list
        self.tax = int(tax)
        self.prod_code = prod_code
        self.suplier_number = suplier_number

        con = self.con.connect()
        cur = con.cursor()

        su_lastid = None
        sply_lastid = None

        print(self.sp,self.cp )

        try:
            cur.execute("use lakydb;", tuple())
            try: # if duplicate key, get it id

                stoct_st = "INSERT INTO lakydb.`stock` ( `phone_name`,`phone_model`, `Users_idUsers`) " \
                           "VALUES (%s, %s, %s)"
                cur.execute(stoct_st, (self.st_name, self.st_ph_model, self.user_id))
                st_lastid = cur.lastrowid
                # print("stock inserted")
            except  errors.Error as err:
                if err.errno == errorcode.ER_DUP_ENTRY:
                    stoct_st = " SELECT stockId FROM lakydb.`stock` WHERE phone_model = %s "
                    cur.execute(stoct_st, ( self.st_ph_model, ))
                    st_lastid = cur.fetchone()[0] # come as tuple

                    # update stock inself, maybe name was not correctly spelt
                    stoct_st = "UPDATE  lakydb.`stock` SET phone_name = %s WHERE phone_model = %s "
                    cur.execute(stoct_st, (self.st_name,self.st_ph_model))

                    # update price table, there is duplicate
                    price_st = "UPDATE lakydb.`stock_prices` SET quantity = quantity + %s," \
                               "cost_price = %s,sale_price = %s,tax = %s,last_update = %s WHERE Stock_stockId = %s"
                    cur.execute(price_st, (self.qty, self.cp, self.sp, self.tax, self.dat,st_lastid))
                    print("stock updated")
                else:
                    raise LakyException("Unknown error", err)

            else:
                # not duplicate error, is new insertion
                price_st = "INSERT INTO  lakydb.`stock_prices` " \
                           "(`Stock_stockId`,`quantity`,`cost_price`,`sale_price`,`tax`,`created_date`,`last_update`)" \
                           "VALUES (%s,%s,%s,%s,%s,%s,%s);"
                cur.execute(price_st, (st_lastid, self.qty, self.cp, self.sp, self.tax, self.dat, self.dat ))
                print("stock info  inserted")


            # supplier table
            #no need to check as defualt is provided if not given
            try: # if duplicate key, get it id
                suplier_st = "INSERT INTO lakydb.`suplier` (`supliername`,`contact`) VALUES(%s, %s)"
                cur.execute(suplier_st, (self.suplier, self.suplier_number))
                su_lastid = cur.lastrowid

                print("suplier inserted")
            except  errors.Error as err:
                if err.errno == errorcode.ER_DUP_ENTRY:
                    # get id
                    suplier_st = "SELECT idsuplier FROM lakydb.`suplier` WHERE contact = %s"

                    cur.execute(suplier_st, (self.suplier_number,))
                    su_lastid = cur.fetchone()[0] # come as tuple
                    # print(f"printing suplier id from duplicate section{su_lastid}")

                    # update suplier contact maybe erorr
                    suplier_st = "UPDATE lakydb.`suplier` SET contact =%s,supliername =%s WHERE idsuplier = %s"
                    cur.execute(suplier_st, ( self.suplier_number,self.suplier,su_lastid))
                    print("suplier updated")
                else:
                    raise LakyException("Unknown error please check database connection")


            # executing on orders table
            if not self.prod_code == "n/a":  # order id was given
                if su_lastid: # suplier executed

                    try:
                        #insert the code if not in table
                        suply_st = "INSERT INTO lakydb.`Orders` (`order_codes`,`dates`,`Suplier_idsuplier`)" \
                                   "VALUES (%s,%s,%s)"
                        cur.execute(suply_st, (self.prod_code, self.dat, su_lastid))
                        sply_lastid = cur.lastrowid
                        print("order inserted with suplier ref")
                    except  errors.Error as err:
                        if err.errno == errorcode.ER_DUP_ENTRY:
                            # code in table get hold of it

                            suply_st = "SELECT  idorder FROM Lakydb.`Orders` WHERE order_codes = %s "
                            cur.execute(suply_st, (self.prod_code,))
                            sply_lastid = cur.fetchone()[0]

                else:   # but suplier was not executed (not given)
                    try:
                        suply_st2 = "INSERT INTO lakydb.`Orders` (`order_codes`,`dates`)" \
                                    "VALUES (%s,%s)"
                        cur.execute(suply_st2, (self.prod_code,  self.dat))
                        sply_lastid = cur.lastrowid
                        print("order inserted without suplier ref")
                    except  errors.Error as err:
                        if err.errno == errorcode.ER_DUP_ENTRY:
                            # code it table get hold of it
                            suply_st2 = "SELECT  idorder FROM Lakydb.`Orders` WHERE order_codes = %s "
                            cur.execute(suply_st2, (self.prod_code,))
                            sply_lastid = cur.fetchone()[0]


                # inserting on Order_info
                if  sply_lastid: # supply was executed and it code is provided and must be ref
                    try:
                        suply_code_info = "INSERT INTO lakydb.Order_info (Orders_idorder, phone_name, phone_model, quantity, cost_price)" \
                                          "VALUES(%s, %s, %s, %s, %s)"
                        cur.execute(suply_code_info, (sply_lastid, self.st_name, self.st_ph_model, self.qty, self.cp))
                        print("order info inserted with order ref")
                    except  errors.Error as err:
                        if err.errno == errorcode.ER_DUP_ENTRY:
                            #order code there in orders, update information
                            suply_code_info = "UPDATE lakydb.Order_info SET phone_name = %s,phone_model =%s, " \
                                        "quantity =%s, cost_price= %s WHERE Orders_idorder = %s "
                            cur.execute(suply_code_info, (self.st_name, self.st_ph_model, self.qty, self.cp, sply_lastid))
                            print("order info upadted with order ref")

            #checking if serial number is provide and is a seqience type
            if  self.code_list  and isinstance(self.code_list, Sequence):

                if not sply_lastid : # oders was not executed
                    info_st2 = "INSERT INTO lakydb.Order_sn_info(phone_sn,Stock_stockId)" \
                               "VALUES (%s,%s)"
                    for sn in code_list:
                        try:
                            cur.execute(info_st2, (sn,st_lastid))
                        except  errors.Error as err:
                            if err.errno == errorcode.ER_DUP_ENTRY:
                                continue
                    print("sn_list info inserted with stock ref")
                else: # orders was executed add it referernce
                    info_st = "INSERT INTO lakydb.Order_sn_info(phone_sn,Stock_stockId,Orders_idorder)" \
                              "VALUES (%s,%s,%s)"
                    for sn in code_list:
                        try:
                            cur.execute(info_st, (sn,st_lastid, sply_lastid))
                        except  errors.Error as err:
                            if err.errno == errorcode.ER_DUP_ENTRY:
                                continue
                    print("sn_list info inserted and order with stock ref")

        except  errors.Error as err:
            if err.errno == errorcode.ER_DUP_ENTRY:
                print("record already exist")
                return "record already exist"
            else:
                print(err)
        except LakyException as e:
            raise LakyException(e.extra_message)

        except :
            raise LakyException("Unknown errror occured")
        else:
            con.commit()
            self.update_stock_cach()
            print('run ok')
        finally:
            con.close()


    def load_stock(self):
        con = self.con.connect()
        cur = con.cursor()
        statement = 'SELECT stock.stockId as "ID", stock.phone_name as "Type", stock.phone_model as "Model", ' \
                'quantity as "Quantity",cost_price as "Cost Price",sale_price as "Salling Price",tax as "tax %", '\
                'created_date as "Created Date",last_update as "Last Upadte", '\
                'users.User_Name as "User"  FROM lakydb.stock '\
                'inner join	lakydb.users on users.idUsers = stock.Users_idUsers '\
                'inner join lakydb.stock_prices on stock.stockId = stock_prices.Stock_stockId;'
        try:
            cur.execute(statement, tuple())
            result = cur.fetchall()
        except  errors.Error as err:
            print(err.msg)
            return []
        else:
            return result

        finally:
            print("closing")
            con.close()

    def update_stock_cach(self):
        con = self.con.connect()
        cur = con.cursor()
        statement = "insert into  lakydb.stock_caches_table   value (current_date(),  (SELECT sum(stock_prices.quantity) FROM lakydb.stock_prices)) " \
                " on duplicate key update stock_caches_table.quntity_update = (SELECT sum(stock_prices.quantity) FROM lakydb.stock_prices)"
        try:
            cur.execute(statement, tuple())

        except:
            pass
        else:
            con.commit()
        finally:
            con.close()

    def delete_stock(self):
        pass

    def delete_all(self):
        pass

    def feed_type(self):
        con = self.con.connect()
        cur = con.cursor()
        statement = "SELECT distinct  phone_name FROM lakydb.stock;"
        try:
            cur.execute(statement,tuple())
            result = cur.fetchall()
            result = [val[0] for val in result]
        except  errors.Error as err:
            return []
        else:
            return result
        finally:
            con.close()

    def feed_model(self, key):
        statement = 'SELECT phone_model FROM lakydb.stock where phone_name = %s'
        con = self.con.connect()
        cur = con.cursor()

        try:
            cur.execute(statement, (key, ))
            result = cur.fetchall()
            result = [val[0] for val in result]
        except  errors.Error as err:
            return []
        else:
            return result
        finally:
            con.close()

    def model_feed_rest(self, key):
        statement ="SELECT stock_prices.quantity as qty, stock_prices.cost_price as cp, stock_prices.sale_price as sp ," \
        " stock_prices.tax as tax, stock_prices.last_update FROM lakydb.stock  inner join " \
        " lakydb.stock_prices on  stock.stockId = stock_prices.Stock_stockId where stock.phone_model = %s;"

        con = self.con.connect()
        cur = con.cursor()

        try:
            cur.execute(statement, (key, ))
            result = cur.fetchone()
            # h = dict()
            # h = dict()
            if result:
                result = dict(zip(cur.column_names, result))

            # print(result, 'ygghghg')
        except  errors.Error as err:
            return {}
        except :
            return {}
        else:
            return result

        finally:
            con.close()

    def feed_order_id(self,key):
        """
        it pre-suplies the 'order id combobox' with order information from database
        :param key: key
        :return: list
        """

        statement= "SELECT distinct orders.order_codes  FROM lakydb.orders left join lakydb.order_info on  orders.idorder = order_info.Orders_idorder " \
        "where order_info.phone_model = %s"
        con = self.con.connect()
        cur = con.cursor()

        try:
            cur.execute(statement, (key,))
            result = cur.fetchall()
            if result:
                result = [x[0] for x in result]
                # print(result)
            # print(result, 'ygghghg')
        except  errors.Error as err:
            return []
        except:
            return []
        else:
            return result

        finally:
            con.close()

    def order_id_feed_rest(self, key):
        statement = "SELECT suplier.supliername, suplier.contact,orders.dates, Order_sn_info.phone_sn  FROM lakydb.orders " \
                    "left join lakydb.Order_sn_info on  orders.idorder = Order_sn_info.Orders_idorder " \
                    " right join lakydb.suplier on Suplier.idsuplier = orders.Suplier_idsuplier where orders.order_codes = %s order by orders.dates asc;"
        con = self.con.connect()
        cur = con.cursor()

        try:
            cur.execute(statement, (key,))
            result = cur.fetchall()

            h = {'sn': list(), 'suplier': None, 'contact': None,'dates': None}
            if result:
                for tup in result:
                    h['suplier'] = str(tup[0]) # for suplier name
                    h['contact'] = str(tup[1]) # for suplier contact
                    h['dates'] = tup[2]  # for  date
                    h.get('sn').append(tup[3])

                    # for item in tup:
                    #     h[item] = item
                # print(result, 're')
                # print(h)
        except  errors.Error as err:

            return {}
        except:

            return {}
        else:
            return h

        finally:
            con.close()

    def feed_suplier(self):
        statement ="SELECT supliername, contact FROM lakydb.Suplier"
        con = self.con.connect()
        cur = con.cursor()

        try:
            cur.execute(statement)
            result = cur.fetchall()

        except  errors.Error as err:

            return {}
        except:

            return {}
        else:
            return result

        finally:
            con.close()

    def feed_phone_sn(self, model_text, has_bought = False):
        if has_bought is None:
            statement = "select Order_sn_info.phone_sn from lakydb.Order_sn_info " \
                        "right join	lakydb.stock on Order_sn_info.Stock_stockId = stock.stockId " \
                        "where stock.phone_model = %s "
        else:
            statement = "select Order_sn_info.phone_sn from lakydb.Order_sn_info" \
                        " right join	lakydb.stock on Order_sn_info.Stock_stockId = stock.stockId " \
                        "where stock.phone_model = %s and  Order_sn_info.has_bought = %s"
                        #"{0}".format(has_bought)
        con = self.con.connect()
        cur = con.cursor()

        try:
            if   has_bought is None:
                cur.execute(statement, (model_text,))
            else:
                cur.execute(statement,(model_text,has_bought))

            result = cur.fetchall()
            result = [val[0] for val in result]
        except  errors.Error as err:
            print(err)
            return []
        except:

            return []
        else:
            return result

        finally:
            con.close()

    def feed_dasboard_stock_table(self):
        con = self.con.connect()
        cur = con.cursor()
        temp_cache = {}
        st_list = [
            "SELECT cache_date, quntity_update FROM lakydb.stock_caches_table  where  cache_date = (select max(cache_date) FROM lakydb.stock_caches_table);" ,
          "SELECT 'Today', sum(quantity) FROM lakydb.stock_prices ;"
        ]

        try:
            for stat in st_list:
                cur.execute(stat, tuple())
                result = cur.fetchone()
                if result:
                    temp_cache[result[0]] = result[1]
                    # print(temp_cache )
        except:
            pass
        else:
            return temp_cache
        finally:
            con.close()

    def printer_feed(self, transcode):
        con = self.con.connect()
        cur = con.cursor()
        st = "SELECT customer.customer_name, customer.customer_contact, sale_phone.phone_type, sale_phone.model , phone_prices.quantity, phone_prices.sp, phone_prices.tax, phone_prices.dates, phone_transaction.discount, phone_transaction.trans_code " \
            "FROM lakydb.sale_phone right join  lakydb.phone_transaction " \
            "on  sale_phone.phone_transaction_phone_transaction_id = phone_transaction.phone_transaction_id  " \
            "right join  lakydb.customer " \
            "on sale_phone.Customer_customer_id = customer.customer_id " \
            "inner join phone_prices  " \
            "on sale_phone.Sale_phone_id = phone_prices.Sale_phone_Sale_phone_id " \
            "where phone_transaction.trans_code = %s;"

        try:
            cur.execute(st, (transcode,))
            result = cur.fetchall()
            # if result:
            #     print(result)
        except  errors.Error as err:
            if err.errno == errorcode.ER_DUP_ENTRY:
                print("record already exist")
                return "record already exist"
            else:
                print(err)
        except:

            return []
        else:
            return result

        finally:
            con.close()




class Phone:
    caches_whole = {}
    caches_retail = {}

    user_id = IntegerField(_min=0)
    ph_type = CharField(_min=2, _max=24)
    ph_model = CharField(_min=2, _max=24)
    ime = CharField(_min=2, _max=24)
    sn = CharField()
    price = Decimalfield(_min=2)
    cost_p = Decimalfield(_min=2)
    quantity =IntegerField(_min= 1)
    discount = IntegerField()

    customer_name= CharField()
    customer_number= CharField()
    def __init__(self):
        # caches_whole = {}
        # caches_retail = {}
        self.con = My_db()

    def add_to_cart(self,  ph_type, ph_model,  sn, price, quantity = 1,  cp = 0, use_retails = False ):
        # self.user_id = user_id
        self.ph_type = ph_type
        self.ph_model = ph_model
        self.quantity = int(quantity)
        self.sn = sn
        self.price = price

        print("inner operation retials = ",use_retails )

        if  use_retails :
            # same phone is seen as individual items
            self.caches_retail[self.sn] = {

                "ph_type": self.ph_type,
                "ph_model": self.ph_model,
                "cost_price": cp,
                "sn": self.sn,
                "quantity": self.quantity,  #is always 1 but security let stills multiply
                "price": Decimal( round(float(self.price) * self.quantity,2) )

            }

            return

        # whole sales sn rules violated same phone is seen as one

        if not self.ph_model in self.caches_retail : #n key not in
            #does not contain cache, key not in
            #print("cache  called", self.caches_retail, self.ph_model in self.caches_retail )
            self.caches_retail[self.ph_model] = {

                "ph_type": self.ph_type,
                "ph_model": self.ph_model,
                "cost_price": cp, #privately hold to compare with price when bougth
                "sn": self.sn,
                "quantity": self.quantity ,
                "sp_per_unit" :self.price,
                "price": Decimal( round(float(self.price) * self.quantity,2) )

            }
        else:
            #update
            print("cache update called", self.caches_retail, self.ph_model in self.caches_retail)
            self.caches_retail[self.ph_model]["ph_type"] = self.ph_type
            self.caches_retail[self.ph_model]["ph_model"] = self.ph_model
            self.caches_retail[self.ph_model]["cost_price"] = cp
            self.caches_retail[self.ph_model]["sn"] = self.sn # overwrite sn
            self.caches_retail[self.ph_model]["sp_per_unit"] = self.price
            self.caches_retail[self.ph_model]["quantity"] = self.caches_retail[self.ph_model]["quantity"] + self.quantity
            self.caches_retail[self.ph_model]["price"]= Decimal(
                round(float(self.caches_retail[self.ph_model]["sp_per_unit"] ) * self.caches_retail[self.ph_model]["quantity"],2))



    def buyphone(self,  customer_name = None, customer_number= '+233' ):

        if  not len(self.caches_retail):
            raise Invalid_Item_Purchase("Nothing in  cart to buy")


        self.customer_number =customer_number
        self.customer_name = customer_name
        tran = Transcode()


        con = self.con.connect()
        cur = con.cursor()
        try:
            statment = "SELECT" \
                       " stock_prices.quantity ,stock_prices.tax, stock_prices.sale_price,stock_prices.cost_price, stock.stockId FROM lakydb.stock_prices inner join lakydb.stock on " \
                       "stock_prices.Stock_stockId = stock.stockId  where stock.phone_model = %s"


            # generate  transaction code first
            #  generate transcode before code execute
            transcode = tran.transact_code()

            cust = "INSERT INTO lakydb.phone_transaction (trans_code,discount )" \
                   "VALUES(%s,%s)"

            # Todo read discount from settings
            self.discount = 0
            try:
                # "on duplicate key update customer_name = %(name)s "
                cur.execute(cust, (transcode, self.discount))
                trans_lastid = cur.lastrowid
            except  errors.Error as err:
                if err.errno == errorcode.ER_DUP_ENTRY:
                    # regenerate code  in dp
                    transcode = tran.transact_code()
                    cur.execute(cust, (transcode, self.discount))
                    trans_lastid = cur.lastrowid
                else:
                    raise LakyException("Transaction Failed")


            for _, val in self.caches_retail.items():
                # go through  cache if item in stock
                # raise error if not is stock and continue otherwise

                cur.execute(statment, (val["ph_model"],))
                # get quantity and price from db for the particular item
                result =  cur.fetchone()


                if result:
                     # if record id not empty, bundled with it column names
                    result = dict(zip(cur.column_names, result))
                    # print(result) #result["quantity"]

                    # quantity_bought =  1 if cache_to_use == "retail" else val.get('quantity', 1)

                    if not int(result.get('quantity')) - int(val['quantity']) < 0 :
                        # stock available process to buy
                        #  check stock price
                        #  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

                        # Decimal(val['price'])  has ben catered in cart , not to recal
                        print(Decimal(val['price']) )

                        if Decimal(val['price']) >=  Decimal(round(float( result.get('cost_price')) * int(val['quantity']),2)) :

                            result['quantity'] =  int(result.get('quantity')) - int(val['quantity']) # substract  from total stock

                            # update  stock
                            update_quantity = "UPDATE lakydb.stock_prices SET quantity = %s where Stock_stockId = %s"
                            cur.execute(update_quantity, (result['quantity'], result["stockId"],))
                            # print("updated")
                            print(result)
                            # save record to record table

                            # insert to customer
                            try:
                                cust= "INSERT INTO lakydb.customer(customer_name,customer_contact)VALUES (%s,%s)"
                                      # "on duplicate key update customer_name = %(name)s "
                                cur.execute(cust, (self.customer_name, self.customer_number))
                                cust_lastid = cur.lastrowid
                            except  errors.Error as err:
                                if err.errno == errorcode.ER_DUP_ENTRY:
                                    cust = "SELECT customer_id FROM lakydb.customer where customer_contact = %s "
                                    cur.execute(cust, (self.customer_number,))
                                    cust_lastid = cur.fetchone()[0]

                                    cust = "UPDATE lakydb.customer SET customer_name = %s where customer_contact = %s "
                                    cur.execute(cust, (self.customer_name, self.customer_number))
                            # print(cust_lastid)
                                else:
                                    raise LakyException("Unknown error occured, Please check database connection")

                            # insert phone sales
                            try:
                                if  not val['sn']:
                                    cust = "INSERT INTO lakydb.sale_phone (phone_type, model,Users_idUsers,Customer_customer_id,phone_transaction_phone_transaction_id ) " \
                                           "VALUES(%s,%s,%s,%s,%s)"
                                    # "on duplicate key update customer_name = %(name)s "
                                    cur.execute(cust, (
                                    val['ph_type'], val['ph_model'],self.id, cust_lastid, trans_lastid))
                                    sales_lastid = cur.lastrowid
                                else:
                                    cust = "INSERT INTO lakydb.sale_phone (phone_type, model, phone_code,Users_idUsers,Customer_customer_id,phone_transaction_phone_transaction_id ) " \
                                           "VALUES(%s,%s,%s,%s,%s,%s)"
                                    # "on duplicate key update customer_name = %(name)s "
                                    cur.execute(cust, (val['ph_type'], val['ph_model'], val['sn'], self.id, cust_lastid, trans_lastid))
                                    sales_lastid = cur.lastrowid
                            except  errors.Error as err:
                                if err.errno == errorcode.ER_DUP_ENTRY:
                                    raise Invalid_Item_Purchase(f"{val['ph_type']}, {val['ph_model']} with this serial {val['sn']} is already bought")
                                else:
                                    print(err.msg)
                                    raise LakyException("Unknown error occured, Please check database connection")


                            # insert phone price
                            try:
                                cust = "INSERT INTO lakydb.Phone_prices (sp,tax, dates, Sale_phone_Sale_phone_id, quantity) " \
                                       "VALUES(%s,%s,%s,%s,%s)"
                                # "on duplicate key update customer_name = %(name)s "
                                cur.execute(cust,
                                            (val['price'], result['tax'], datetime.now(), sales_lastid,  val['quantity']))
                                # sales_lastid = cur.lastrowid
                            except  errors.Error as err:
                                if err.errno == errorcode.ER_DUP_ENTRY:
                                    print("sales duplicate key catch")
                                    raise LakyException("Unknown error occured, Please check database connection")
                                else:
                                    print(err.msg)

                        else:
                            raise InvalidSalesPrice(f"Saling price can not be lesser than the cost price {result.get('sale_price')}")

                    else:
                        raise OutOfStockException(f"{val['ph_type']}-{val['ph_model']} is out of stock \n stock available : {result.get('quantity')} ")
                else:
                    raise ValueError(f"{val['ph_type']}-{val['ph_model']} not found in stock")

        except  errors.Error as err:
            if err.errno == errorcode.ER_DUP_ENTRY:
                print("record already exist")
            else:
                print(err.msg)

        except IndexError as e:
            print(e)
        # except:# (OutOfStockException, InvalidSalesPrice, Invalid_Item_Purchase, ValueError) as ex:
        #     raise LakyException("Unknown error occured, Please check database connection")  #upper level is handling that


        else:
            con.commit()
            print('run ok')
            # patche the cache  to imform the printer
            self.caches_retail['transcode'] = transcode
        finally:
            con.close()


    def undo_buy(self, key):
        # get all items in the transaction, if length is one then delete  by trans_code

        con = self.con.connect()
        cur = con.cursor()
        cur2 = con.cursor()

        statement_code = "SELECT  Sale_phone_id, quantity, model  FROM lakydb.sale_phone inner join  lakydb.phone_transaction  on " \
                         "phone_transaction.phone_transaction_id = sale_phone.phone_transaction_phone_transaction_id " \
                         "inner join lakydb.phone_prices on sale_phone.Sale_phone_id = phone_prices.Sale_phone_Sale_phone_id " \
                         " where phone_transaction.trans_code = %s"

        stock_update = "UPDATE lakydb.stock_prices SET quantity = quantity + %s where Stock_stockId = %s"

        get_stock_id = "SELECT stockId FROM lakydb.stock WHERE phone_model = %s"

        try:

            # deletion by trans_code,
            if isinstance(key, str) and '-' in key:  # every trans_code has '-'
                # Todo: i must use 're' to for more sufficiency
                self.inner_code_delete(key, cur, cur2,statement_code,stock_update,get_stock_id, _conn=con)
                # con.commit()
                # con.close()

            else:
                raise LakyException(f"invalid order id: {key}")
            # Todo: must support this later
            # else:
            #     # deletion by id
            #     try:
            #         int(key)
            #     except ValueError:
            #         print('key error')
            #         return
            #     statement_id = "SELECT  quantity, trans_code, model  FROM lakydb.sale_phone inner join  lakydb.phone_transaction  on " \
            #                    " phone_transaction.phone_transaction_id = sale_phone.phone_transaction_phone_transaction_id " \
            #                    "inner join lakydb.phone_prices on sale_phone.Sale_phone_id = phone_prices.Sale_phone_Sale_phone_id " \
            #                    "where sale_phone.Sale_phone_id =%s"
            #     cur.execute(statement_id, (key,))
            #     result = cur.fetchone()  # only one data, it quantity and trans_code
            #
            #     if result: # has item?, or if found
            #         get_code_by_id = dict(zip(cur.column_names, result))
            #         print('code', get_code_by_id)
            #
            #         # check if this data is the only item left in the trans_code tree,
            #         # we first got hold the "code" and "quantity" and we use the code to check if is the only child left
            #         cur.execute(statement_code, (get_code_by_id['trans_code'],))
            #         get_qty_by_code = cur.fetchall() # may return more than one records
            #         print('id',get_qty_by_code)
            #
            #         if get_qty_by_code and len(get_qty_by_code) < 2:
            #             # delete by trans_code, has just tested to be the only child
            #             print("am the only child letf am calling my parent to delete me")
            #
            #             self.inner_code_delete(get_code_by_id['trans_code'], cur, cur2, statement_code, stock_update, get_stock_id, _conn=con)
            #             # con.commit()
            #             # con.close()
            #         else:
            #            print(f"am delete my self mum has many {len(result)} children ")
            #             # has more than one node, delete only this record
            #            cur2.execute(get_stock_id,(get_code_by_id['model'],))
            #            stock_id = cur2.fetchone()
            #            # print(stock_id)
            #
            #            if stock_id:  # found
            #                # upadte stock and delete record
            #                cur2.execute(stock_update, (get_code_by_id['quantity'],stock_id[0]))
            #
            #                delete_phone = "DELETE FROM lakydb.sale_phone WHERE Sale_phone_id = %s"
            #                cur2.execute(delete_phone, (key,))
            #
            #                con.commit()
            #
            #            else:
            #                print("Record not found in stock")
            #
            #     else:
            #         print('Record not found')

        except  errors.Error as err:
            if err.errno == errorcode.ER_DUP_ENTRY:
                print("record already exist")
            else:
                raise LakyException("unknown error please check database connection")
        except LakyException as e:
            raise LakyException(e.extra_message)
        finally:
            con.close()

    def inner_code_delete(self,key, cur, cur2 = None, statement_code = None, stock_update = None, get_stock_id =None, _conn =None ):

        cur.execute(statement_code, (key,))
        result_code = cur.fetchall()

        if result_code:
            # get_stock_id  = "SELECT stockId FROM lakydb.stock WHERE phone_model = %s"
            delete_code = "DELETE FROM lakydb.phone_transaction WHERE trans_code = %s"

            print("result_code is", result_code)

            for data in result_code: # one transaction may link different records
                data2=dict(zip(cur.column_names, data))

                # go to stock and check if record is there
                cur2.execute(get_stock_id, (data2.get("model",0), ) )
                stock_id = cur.fetchone()
                # print("data fetched is", stock_id, ' model is', data2.get("model",0) )

                if stock_id: # found (in tuple)
                    # update the stock table
                    cur2.execute(stock_update, (data2.get("quantity",0), stock_id[0]) )

                    # delete the record
                    cur2.execute(delete_code, (key,))

                else:
                    LakyException(f"Recode not found in stock {data2.get('model','')}")
            _conn.commit()
            _conn.close()

        else:
            raise LakyException(f'Invalid transaction code: {key}')
            # print("Record not found")



    def load_sale_phone_table(self):
        con = self.con.connect()
        cur = con.cursor()
        statement = "SELECT trans_code as 'Transaction Code',  " \
            "sale_phone.phone_type as 'Phone Type', sale_phone.model as 'Phone Model', sale_phone.phone_code as 'Serial Number', " \
            "phone_prices.quantity as 'quantity',phone_prices.sp as 'Price',phone_prices.tax as 'Tax', discount as 'Discount', dates as 'Date', " \
            "customer.customer_name as 'Customer', customer.customer_contact as 'Customer Contact', users.Lname as 'User' " \
            "FROM lakydb.users " \
            "inner join lakydb.sale_phone on users.idUsers = sale_phone.Users_idUsers " \
            "inner join lakydb.phone_prices on sale_phone.Sale_phone_id =  phone_prices.Sale_phone_Sale_phone_id " \
            "inner join lakydb.phone_transaction on phone_transaction.phone_transaction_id = sale_phone.phone_transaction_phone_transaction_id " \
            "inner join lakydb.customer on customer.customer_id = Sale_phone.Customer_customer_id    where datediff(  now(), phone_prices.dates ) <1  order by sale_phone.Sale_phone_id desc "

        try:
            cur.execute(statement,tuple())
            result = cur.fetchall()
        except  errors.Error as err:
            print(err.msg)
        else:
            return  result

        finally:

            con.close()


    def remove_from_cache(self, sn):
        try:
            del self.caches_retail[str(sn)]
        except KeyError:
            pass

    def clear_all(self):
        self.caches_whole = {}
        self.caches_retail= {}

    def __len__(self):
        return len(self.caches_retail)

    def highly_purchase(self):
        statement = "SELECT Sale_phone.model as 'Model', sum(phone_prices.quantity) as 'Purchases' from " \
               " lakydb.Sale_phone  inner join lakydb.phone_prices on Sale_phone.Sale_phone_id = phone_prices.Sale_phone_Sale_phone_id "\
               " group by  Sale_phone.model order by sum(phone_prices.quantity) desc limit 10  "
        con = self.con.connect()
        cur = con.cursor()
        try:
            cur.execute(statement, tuple())
            result = cur.fetchall()
            # print(result)
            # if result:
            #     result = dict(zip(cur.column_names, result))
            #     # result = [val[0] for val in result]
        except  errors.Error as err:
            return []
        else:
            return result
        finally:
            con.close()

    def feed_dash_avg(self):
        con = self.con.connect()
        cur = con.cursor()

        stat = "SELECT  max( year( date(dates))) as 'yr', sum(quantity) / count( distinct  date(dates))  as 'avg', " \
           " (SELECT sum( quantity ) from  lakydb.phone_prices where  date(phone_prices.dates) =   date(now())) as 'today', " \
           " (SELECT sum(sp) from lakydb.phone_prices where date(phone_prices.dates) = date(now())) as 'today sales' ," \
                "sum(sp) / count(distinct date(dates))  as 'avg money' " \
        " FROM lakydb.phone_prices where	year( date(phone_prices.dates)) >=   year( date(now())) ;"

        try:

            cur.execute(stat, tuple())
            result = cur.fetchone()
            if result:
             result = dict(zip(cur.column_names, result))
        except:
            pass
        else:
            return result
        finally:
            con.close()




class Active_User(PhoneStock, Phone):
    new_user_fname = CharField(_min=2, _max=25)
    new_user_lname = CharField(_min=2, _max=25)
    new_user_user_name = CharField(_min=2, _max=25)
    new_user_role = CharField(_min=2, _max=25)
    new_user_password = CharField(_min=4, _max=25)
    new_user_email = EmailField()
    new_user_manage_stock = Boolean()
    new_user_manage_user = Boolean()
    new_user_view_chart = Boolean()
    new_user_view_privacy = Boolean()
    new_user_managing_control  = Boolean()

    def __init__(self):
        PhoneStock.__init__(self)
        # self.username = username
        # self.password = password
        self.id = None
        self.role = None
        self.lname = None
        self.fname = None
        self.email = None
        self.last_seen = None
        self.has_login = False
        self.username = None

        self.can_take_stock = False
        self.can_manage_user = False
        self.can_view_privacy = False
        self.can_view_chart = False
        self.managing_control = False

        # self.con = My_db()

        # self.login()

    def login(self, username =None, password =None):  # worked
        self.username = username
        self.password = password

        statement = "SELECT users.idUsers, users.User_Name, users.User_Password, User_Email, users.Fname," \
                    " users.Lname,users.last_seen, user_privilages.roles, user_privilages.can_manage_users,user_privilages.can_view_chart, " \
                    "user_privilages.can_manage_stock,user_privilages.can_view_privacy, user_privilages.managing_role FROM " \
                    "lakydb.users inner join lakydb.user_privilages on users.idUsers = user_privilages.Users_idUsers where" \
                    " users.User_Name =%s"

        con = self.con.connect()
        cur = con.cursor()
        cur.execute(statement, (self.username,))

        result = cur.fetchone()
        # print(result)
        if result:
            # if record id not empty, bundled with it column names
            result = dict(zip(cur.column_names, result))
            print(result)

            # if the password from the data base is same when compared the access grant
            if Encryption.passcheck(self.password, result['User_Password']):

                print("login access")
                # assign role settings to user from the database
                self.id = result['idUsers']
                self.role = result['roles']
                self.lname = result['Lname']
                self.fname = result['Fname']
                self.email = result['User_Email']
                self.last_seen = result["last_seen"] or datetime.now()
                self.username = result["User_Name"]

                self.can_take_stock = bool(result['can_manage_stock'])
                self.can_manage_user = bool(result['can_manage_users'])
                self.can_view_privacy = bool(result['can_view_privacy'])
                self.can_view_chart = bool(result['can_view_chart'])
                self.managing_control = bool(result['managing_role'])
                # print(f"hi {self.lname} your assign info is \n", vars(self))

                self.has_login = True

                con.close()
                return True
            # print("invalid username or password ")
        # print("invalid username or password ")
        con.close()

    def create_user(self,fname, lname, username, password, email, role,
                   can_take_stock,can_manage_user, can_view_privacy, managing_control, can_view_chart):  # Worked

        # self.role_check()

        self.new_user_fname = fname
        self.new_user_lname = lname
        self.new_user_user_name = username
        self.new_user_email = email
        self.new_user_password = password
        self.new_user_role = role
        self.new_user_manage_stock = can_take_stock
        self.new_user_view_chart = can_view_chart
        self.new_user_manage_user = can_manage_user
        self.new_user_view_privacy = can_view_privacy
        self.new_user_managing_control = managing_control

        statement1 = "INSERT INTO" \
                     " `lakydb`.`users` ( `User_Name`,`User_Password`,`User_Email`, `Fname`,`Lname`) " \
                     "VALUES (%s,%s,%s,%s,%s)"

        statement2 = "INSERT INTO" \
                     " `lakydb`.`user_privilages` ( `Users_idUsers`,`roles`,`can_manage_users`," \
                     "`can_view_chart`, `can_view_privacy`,`can_manage_stock`, `managing_role`) " \
                     "VALUES (%s,%s,%s,%s,%s,%s,%s)"

        con = self.con.connect()
        cur = con.cursor()
        cur2 = con.cursor()
        try:

            cur.execute(statement1,
                        (self.new_user_user_name, Encryption.passcrypt(self.new_user_password), self.new_user_email,
                         self.new_user_fname, self.new_user_lname))
            lastid = cur.lastrowid
            print(cur.lastrowid)
            # con.commit()
            cur2.execute(statement2,
                         (lastid, self.new_user_role, self.new_user_manage_user, self.new_user_view_chart, self.new_user_view_privacy, self.new_user_manage_stock, self.new_user_managing_control))
            print(cur2.lastrowid)
            con.commit()
            print('user added')
        except  errors.Error as err:
            if err.errno == errorcode.ER_DUP_ENTRY:
                print("record already exist")

            print(err)
        except:
            print('error ocurs')
        else:
            print('run ok')
        finally:
            con.close()

    def reset_password(self,old_password, new_password, confirm_password= None, user_name = None, user_id = None):

        # if not current_password == confirm_password:
        #     print('password not same')
        #     return
        # if not len(current_password) >= 4:
        #     print("weak password")
        #     return

        con = self.con.connect()
        cur = con.cursor()

        statement = "SELECT users.idUsers, users.User_Name, users.User_Password FROM " \
                    "lakydb.users  where" \
                    " users.User_Name =%s"

        if self.has_login:
            cur.execute(statement, (user_name,))
            result = cur.fetchone()
            # print(result)
            if result:
                # if record id not empty, bundled with it column names
                result = dict(zip(cur.column_names, result))
                # print(result)
                if Encryption.passcheck(old_password, result['User_Password']):
                    # verified update password
                    statement = "UPDATE  lakydb.users SET User_Password= %s WHERE users.idUsers =%s"
                    cur.execute(statement, (Encryption.passcrypt(new_password), user_id,))
                    print("reset success")
                    con.commit()
                    con.close()
                    return True
            return False
        else :
            # cur.execute(statement, (self.username,))
            # # print(cur.with_rows)
            # result = cur.fetchone()
            # # print(result)
            # if result:
            #     # if record id not empty, bundled with it column names
            #     result = dict(zip(cur.column_names, result))
            #     print(result)
            #     if Encryption.passcheck(old_password, result['User_Password']):
            #         # verified update password
            #         cur.execute(statement2, (current_password, self.id,))
            #         con.commit()
            #         con.close()
            #         return True
            return False

    def remove_user(self,user_id):
        if not self.has_login:
            print("Not authorised, please login first")
            return
        if not self.can_manage_user:
            print("This account is not authorised to delete user, Please contact administrator")
            return
        if isinstance(user_id, int):
            statement = "DELETE FROM lakydb.users WHERE idUsers =%s "
            con = self.con.connect()
            cur = con.cursor()
            try:
                cur.execute(statement, (int(user_id),))
                con.commit()
            except errors.Error as err:
                print(err)
            finally:
                con.close()

        else:
            return NotImplemented

    def update_user(self, id, fname, lname, email, role,
                   can_take_stock, can_manage_user, can_view_privacy, managing_control, can_view_chart):
        self.role_check()
        self.new_user_fname = fname
        self.new_user_lname = lname
        self.new_user_email = email
        self.new_user_role = role
        self.new_user_manage_stock = can_take_stock
        self.new_user_view_chart = can_view_chart
        self.new_user_manage_user = can_manage_user
        self.new_user_view_privacy = can_view_privacy
        self.new_user_managing_control = managing_control

        con = self.con.connect()
        cur = con.cursor()
        cur2 = con.cursor()
        statement1 = "update lakydb.users set User_Email = %s, Fname = %s, Lname =%s where idUsers = %s"

        statement2 = "update lakydb.privilages set roles =%s, can_manage_users = %s, can_view_chart =%s," \
                     "can_view_privacy =%s ,can_manage_stock =%s ,managing_role =%s where User_idUsers = %s"
        try:
            cur.execute(statement1, (self.new_user_email,self.new_user_fname, self.new_user_lname, int(id)))
            # print(cur.lastrowid)
            cur2.execute(statement2,
                         (self.new_user_role, self.new_user_manage_user, self.new_user_view_chart,
                            self.new_user_view_privacy, self.new_user_manage_stock, self.new_user_managing_control,int(id)))
            con.commit()
            print('user added')
        except errors.Error as err:
            if err.errno == errorcode.ER_DUP_ENTRY:
                print("record already exist")
        finally:
            con.close()

    def role_check(self):
        if not self.has_login:
            print("Not authorised, please login first")
            return

        if not self.can_manage_user:
            print("This account is not authorised to create user, Please contact administrator")
            return

    #PhoneDb Operation
    def savestock(self, **kwargs):
                  # user_id, name, model, cp, sp, qty, date,tax=0, suplier = "n/a", suplier_number='n/a',
                  # prod_code='n/a', code_list='n/a'):

        if not self.has_login:
            print("Not authorised, please login first")
            return
        if not self.can_take_stock:
            print("This account is not allow to take stock")
        # self.stock_handler = PhoneStock( )
        # self.stock_handler.save_stock(user_id,name, model, cp, sp, qty, date, tax, suplier,suplier_number, prod_code,
        #                               code_list,)
        PhoneStock.save_stock(self,**kwargs)
                              # user_id,name, model, cp, sp, qty, date, tax, suplier,suplier_number, prod_code,
                              #         code_list,)

    # cache = "retail",
    def buyphone(self,  customer_name ="customer", customer_number="n/a"):
        if not self.has_login:
            print("Not authorised, please login first")
            return
        Phone.buyphone(self , customer_name, customer_number)


__all__ = ['Active_User']

if __name__ == "__main__":
    # TEST PHONE

    p = Phone()
    print(p.load_sale_phone_table())
    # p.add_to_cart(1,'samsung', 'P300', '123564789','sn-123',210.05)
    # p.add_to_cart(2, 'samsung', 'T300', '123564759', 'sn-321', 210.568)
    # p.add_to_cart(3, 'samsung', 'F300', '123564719', 'sn-213', 210.50)
    # # print(p.caches_whole)
    # # print(p.caches_retail)
    # p.buyphone(cache= 'retail')
    # print(d.caches)

    #testing user
    u = Active_User()
    # u.login("laky1", "laky689393")

    # # # #USER TEST BUY PHONE
    # # self, ph_type, ph_model, sn, quantity, price):
    # u.add_to_cart('samsung', 'G770', '123564789','',210.05)
    # u.add_to_cart( 'samsung', 'T770', '123564759', 'sn-333', 210.568)
    # u.add_to_cart( 'samsung', 'F770', '123564719', 'sn-234', 210.50)
    #     # # # # print(u.caches_whole)
    # # # # print(u.caches_retail)
    # u.buyphone( customer_number='0246689724')
    #
    # u.undo_buy('31') #\



    # u.remove_from_cache('sn')
    # print(u.caches_retail)
    # USER RESET PASSWORD
    # a = u.reset_password('laky689393', 'LAKY68', "LAKY68")
    # print(a)
    # u.remove_user(25)
    u.create_user("lawrence", 'secretry', 'laky1','laky689393', 'lawrence@txt.com', "sec",
                 True, True, True, True, True, )
    # u.update_user('23',"perter", 'Lara', "lawrencetxt@gmai.com", "user", True,True, False, False, True)
    # u.remove_user(19)

    #Testing Stock
    # for x in ("T", "F", "G","F"):
    #     u.savestock(user_id=u.id,name="samsung",model=f"{x}770", cp=123,sp=350, qty=30,
    #                 date='2020-12-26',tax= 0,suplier_number='+233684010',prod_code='pet-Q17',
    #                 code_list=(f'sn-{x}234',f'sn-{x}235',f'sn-{x}236',f'sn-{x}237',f'sn-{x}238'))

