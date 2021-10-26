import sys
from mysql.connector import errorcode, errors
from collections.abc import Sequence
from decimal import Decimal
sys.path.append("..")
sys.path.append("../../")

from my_db import My_db
from security.discriptor import CharField, IntegerField, Decimalfield, Boolean, EmailField
from security.auth import Encryption
from common import OutOfStockException, InvalidSalesPrice

'''
insert into acc_price_list(AccModel,costPrice,selPrice,acc_quantity) value(@accmodel,@acc_cp ,@acc_sp,@accquantity)
on duplicate key update costPrice = @acc_cp, selPrice= @acc_sp , acc_quantity =(acc_quantity  + @accquantity )
'''


class PhoneStock:
    user_id = IntegerField(_min=0)
    st_name = CharField(_min=2, _max=24)
    st_ph_model = CharField(_min=2, _max=24)
    suplier = CharField(_min=2, _max=24)
    sn = CharField(_min=2, _max=24)
    cp = Decimalfield(_min=2)
    sp = Decimalfield()
    qty = IntegerField(_min = 0)
    prod_code = CharField(_min = 0 , _max= 45)
    tax = IntegerField(_min = 0, )
    suplier_number = CharField()
    code_list = None
    # id = None

    def __init__(self):
        self.con = My_db()

    def save_stock(self, user_id, name, model, cp, sp, qty, dat, tax=0, suplier="n/a",suplier_number = "n/a",
                   prod_code='n/a', code_list='n/a' ):
        self.user_id = user_id
        self.st_name = name
        self.st_ph_model = model
        self.suplier = suplier
        self.cp = cp
        self.sp = sp
        self.qty = qty
        self.dat = dat
        self.code_list = code_list
        self.tax = int(tax)
        self.prod_code = prod_code
        self.suplier_number = suplier_number

        con = self.con.connect()
        cur = con.cursor()
        stoct_st = "INSERT INTO lakydb.`stock` ( `phone_name`,`Phonr_type`, `Users_idUsers`) " \
                    "VALUES (%s, %s, %s)"
        price_st = "INSERT INTO  lakydb.`stock_prices` " \
                     "(`Stock_stockId`,`quantity`,`cost_price`,`sale_price`,`tax`,`created_date`,`last_update`)" \
                     "VALUES (%s,%s,%s,%s,%s,%s,%s);"
        suplier_st = "INSERT INTO lakydb.`suplier` (`supliername`,`contact`) VALUES(%s, %s)"
        suply_st = "INSERT INTO lakydb.`Suply` (`suply_code`,`quantity`,`dates`,`Suplier_idsuplier`)" \
                     "VALUES (%s,%s,%s,%s)"
        suply_st2 = "INSERT INTO lakydb.`Suply` (`suply_code`,`quantity`,`dates`)" \
                   "VALUES (%s,%s,%s)"
        info_st = "INSERT INTO lakydb.stock_phone_info(phone_sn,Stock_stockId,Suply_idsuplies)" \
                     "VALUES (%s,%s,%s)"
        info_st2 = "INSERT INTO lakydb.stock_phone_info(phone_sn,Stock_stockId)" \
                  "VALUES (%s,%s)"

        su_lastid = "Null"
        sply_lastid = "Null"
        try:
            cur.execute(stoct_st, (self.st_name, self.st_ph_model, self.user_id))
            st_lastid = cur.lastrowid
            cur.execute(price_st, (st_lastid, self.qty, self.cp, self.sp, self.tax, self.dat, self.dat ))
            if not self.suplier == 'n/a' :
                print("am executing ")
                cur.execute(suplier_st, (self.suplier, self.suplier_number))
                su_lastid = cur.lastrowid

            if not self.prod_code == "n/a":  # prod code was given
                if su_lastid == "Null":  # but suplier was not executed (not given)
                    cur.execute(suply_st2, (self.prod_code, self.qty, self.dat))
                    sply_lastid = cur.lastrowid
                else:
                    cur.execute(suply_st, (self.prod_code, self.qty, self.dat, su_lastid))
                    sply_lastid = cur.lastrowid

            if not self.code_list == 'n/a' and isinstance(self.code_list, Sequence):

                if sply_lastid == "Null": # suply was not executed
                    print('info executing ')
                    for sn in code_list:
                        cur.execute(info_st2, (sn,st_lastid))
                else:
                    print("hi all fine")
                    for sn in code_list:
                        cur.execute(info_st, (sn,st_lastid, sply_lastid))

            con.commit()

        except  errors.Error as err:
            if err.errno == errorcode.ER_DUP_ENTRY:
                print("record already exist")

            print(err)
            con.close()
        except:
            print('error ocurs')
        else:
            print('run ok')
        finally:
            con.close()

    def update_stock(self):
        pass

    def delete_stock(self):
        pass

    def delete_all(self):
        pass


class Phone:
    caches_whole = {}
    caches_retail = {}

    user_id = IntegerField(_min=0)
    ph_type = CharField(_min=2, _max=24)
    ph_model = CharField(_min=2, _max=24)
    ime = CharField(_min=2, _max=24)
    sn = CharField(_min=2, _max=24)
    price = Decimalfield(_min=2)
    quantity =IntegerField(_min= 1)

    def __init__(self):
        # caches_whole = {}
        # caches_retail = {}
        self.con = My_db()

    def add_to_cart(self, user_id, ph_type, ph_model, ime, sn, price,
                    cust_name="unknown", cust_num="unknown",
                    payment="Cash", tax=0, discount=0):
        self.user_id = user_id
        self.ph_type = ph_type
        self.ph_model = ph_model
        self.ime = ime
        self.sn = sn
        self.price = price


        self.caches_retail[self.sn] = {
            # "user_id": self.user_id,
            "ph_type": self.ph_type,
            "ph_model": self.ph_model,
            "ime": self.ime,
            "sn": self.sn,
            "price": self.price,
        }
        # print(vars(self))
        # self.caches[self.ime]=(vars(self))

    def add_to_cart_whole(self,user_id, ph_type, ph_model, sn, quantity, price):
        self.user_id = user_id
        self.ph_type = ph_type
        self.ph_model = ph_model
        self.sn = sn
        self.price = price
        self.quantity = quantity

        self.caches_whole[self.ph_model] = {
            # "user_id": self.user_id,
            "ph_type": self.ph_type,
            "ph_model": self.ph_model,
            "ime": self.ime,
            "sn": self.sn,
            "quantity": self.quantity,
            "price": self.price,
            "total": self.quantity * price
        }

    def buyphone(self, cache, customer_name, customer_number ):

        if not (cache == "retail" or  cache == "wholesale"):
            print('specified caches not implemented' )
            return
        if cache == 'retail' and not len(self.caches_retail):
            print("Nothing in retail cart to buy")
            return
        if cache == 'wholesale' and not len(self.caches_whole) :
            print("Nothing in wholesale cart to buy")
            return

        com = "INSERT INTO" \
              " lakydb.`sale_phone` ( `Sale_phone_id`,`type`,`model`, `phone_code`,`Customer_customer_contact`) " \
              "VALUES (%s,%s,%s,%s,%s)"

        statment = "SELECT" \
            " stock_prices.quantity ,stock_prices.sale_price,stock.stockId FROM lakydb.stock_prices inner join lakydb.stock on "  \
            "stock_prices.Stock_stockId = stock.stockId  where stock.Phonr_type = %s"

        se = "select quantity  from lakydb.stock_prices where Stock_stockId = %s"
        update_quantity = "UPDATE lakydb.stock_prices SET quantity = %s where Stock_stockId = %s"

        con = self.con.connect()
        cur = con.cursor()
        try:
            for _, val in self.caches_retail.items():
                # go through  cache if item in stock
                # raise error if not is stock and continue otherwise
                cur.execute(statment, (val["ph_model"],))
                # get quantity and price from db for the particular item
                result =  cur.fetchone()
                if result:
                     # if record id not empty, bundled with it column names
                    result = dict(zip(cur.column_names, result))
                    # print(result,result["quantity"])
                    if not result.get('quantity') - 1 < 0 :
                        # stock available process to buy
                        #  check stock price
                        if Decimal(val['price']) > result.get('sale_price'):
                            result['quantity'] =  result.get('quantity') - 1 # substract 1 from total stock
                            # update  stock
                            cur.execute(update_quantity, (result['quantity'], result["stockId"],))
                            # print("updated")
                            # print(result)
                            # save record to record table
                        else:
                            raise InvalidSalesPrice(f"Saling price can not be lesser than the cost price {result.get('sale_price')}")

                    else:
                        raise OutOfStockException(f"{val['ph_type']}-{val['ph_model']} is out of stock")
                else:
                    raise ValueError(f"{val['ph_type']}-{val['ph_model']} not found in stock")
                # print(self.caches_retail[self.sn]["ph_model"])
                # for x in cur:
                #     print(x)

        except  errors.Error as err:
            if err.errno == errorcode.ER_DUP_ENTRY:
                print("record already exist")
            # if err.errno == errorcode.P:
            #     print(err)
            self.p = err
        except IndexError as e:
            print(e)
        except (OutOfStockException, InvalidSalesPrice, ValueError) as ex:
            print(ex)

        else:
            con.commit()
            print('run ok')
        finally:
            con.close()


    def remove(self, ime):
        del self.caches[str(ime)]

    def clear_all(self):
        self.caches = {}

    def __len__(self):
        return len(self.caches)


    def search(self, search_key, item):
        pass

    def printout(self):
        pass

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

    def __init__(self, username =None, password =None):
        PhoneStock.__init__(self)
        self.username = username
        self.password = password
        self.id = None
        self.role = None
        self.lname = None
        self.fname = None
        self.email = None
        self.has_login = False

        self.can_take_stock = False
        self.can_manage_user = False
        self.can_view_privacy = False
        self.can_view_chart = False
        self.managing_control = False

        # self.con = My_db()

        # self.login()

    def login(self):  # worked

        statement = "SELECT users.idUsers, users.User_Name, users.User_Password, User_Email, users.Fname," \
                    " users.Lname, user_privilages.roles, user_privilages.can_manage_users,user_privilages.can_view_chart, " \
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
            # print(result)

            # if the password from the data base is same when compared the access grant
            if Encryption.passcheck(self.password, result['User_Password']):

                print("login access")
                # assign role settings to user from the database
                self.id = result['idUsers']
                self.role = result['roles']
                self.lname = result['Lname']
                self.fname = result['Fname']
                self.email = result['User_Email']

                self.can_take_stock = bool(result['can_manage_stock'])
                self.can_manage_user = bool(result['can_manage_users'])
                self.can_view_privacy = bool(result['can_view_privacy'])
                self.can_view_chart = bool(result['can_view_chart'])
                self.managing_control = bool(result['managing_role'])
                print(f"hi {self.lname} your assign info is \n", vars(self))

                self.has_login = True

                con.close()
                return True
            # print("invalid username or password ")
        print("invalid username or password ")
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

    def reset_password(self,old_password, current_password, confirm_password, user_name = None):

        if not current_password == confirm_password:
            print('password not same')
            return
        if not len(current_password) >= 4:
            print("weak password")
            return

        con = self.con.connect()
        cur = con.cursor()

        statement = "SELECT users.idUsers, users.User_Name, users.User_Password FROM " \
                    "lakydb.users  where" \
                    " users.User_Name =%s"

        if self.has_login:
            cur.execute(statement, (self.username,))
            result = cur.fetchone()
            # print(result)
            if result:
                # if record id not empty, bundled with it column names
                result = dict(zip(cur.column_names, result))
                # print(result)
                if Encryption.passcheck(old_password, result['User_Password']):
                    # verified update password
                    statement = "UPDATE  lakydb.users SET User_Password= %s WHERE users.idUsers =%s"
                    cur.execute(statement, (Encryption.passcrypt(current_password), self.id,))
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
    def savestock(self, user_id, name, model, cp, sp, qty, date,tax=0, suplier = "n/a", suplier_number='n/a',
                  prod_code='n/a', code_list='n/a'):
        # (self, user_id, name, model, cp, sp, qty, dat, suplier=None, prod_code=None,
        # tax=0, prefer_code="sn", code_list=None, suplier_number = None):
        # (user_id=u.id, name="samsung", model="T300", cp=100, sp=200, qty=20,
        # date='2020-12-12', prod_code='1235468', tax= 0,
        # code_list=['sn/1234', 'sn/1235', 'sn/1236', 'sn/1237', 'sn/1238'], suplier_number='0243689564')
        if not self.has_login:
            print("Not authorised, please login first")
            return
        if not self.can_take_stock:
            print("This account is not allow to take stock")
        # self.stock_handler = PhoneStock( )
        # self.stock_handler.save_stock(user_id,name, model, cp, sp, qty, date, tax, suplier,suplier_number, prod_code,
        #                               code_list,)
        PhoneStock.save_stock(self,user_id,name, model, cp, sp, qty, date, tax, suplier,suplier_number, prod_code,
                                      code_list,)

    def buyphone(self, cache = "retail", customer_name ="", customer_number=""):
        if not self.has_login:
            print("Not authorised, please login first")
            return
        Phone.buyphone(self, cache , customer_name, customer_number)


__all__ = ['Active_User']

if __name__ == "__main__":
    # TEST PHONE

    # p = Phone()
    #
    # p.add_to_cart(1,'samsung', 'P300', '123564789','sn-123',210.05)
    # p.add_to_cart(2, 'samsung', 'T300', '123564759', 'sn-321', 210.568)
    # p.add_to_cart(3, 'samsung', 'F300', '123564719', 'sn-213', 210.50)
    # # print(p.caches_whole)
    # # print(p.caches_retail)
    # p.buyphone(cache= 'retail')
    # print(d.caches)

    #testing user
    u = Active_User("laky1", "laky689393")
    u.login()
    #USER TEST BUY PHONE
    u.add_to_cart(1,'samsung', 'P300', '123564789','sn-123',210.05)
    u.add_to_cart(2, 'samsung', 'T300', '123564759', 'sn-321', 210.568)
    u.add_to_cart(3, 'samsung', 'F770', '123564719', 'sn-213', 210.50)
    # print(u.caches_whole)
    # print(u.caches_retail)
    u.buyphone()

    # USER RESET PASSWORD
    # a = u.reset_password('laky689393', 'LAKY68', "LAKY68")
    # print(a)
    # u.remove_user(25)
    # u.create_user("lawrence", 'secretry', 'laky1','laky689393', 'lawrence@txt.com', "sec",
    #              True, True, True, True, True, )
    # u.update_user('23',"perter", 'Lara', "lawrencetxt@gmai.com", "user", True,True, False, False, True)
    # u.remove_user(19)

    #Testing Stock
    # u.savestock(user_id=u.id,name="samsung",model="P300", cp=100,sp=200, qty=20,
    #             date='2020-12-12',tax= 0,suplier="law2",prod_code='1235464',
    #             code_list=('sn2234','sn2235','sn2236','sn2237','sn2238'))

