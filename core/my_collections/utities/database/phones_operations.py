import sys
from mysql.connector import errorcode, errors
from collections import namedtuple
sys.path.append("..")
sys.path.append("../../")

from database.my_db import My_db
from security.discriptor import CharField, IntegerField, Decimalfield, Boolean, EmailField
from security.auth import Encryption


class Active_User:
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

        self.con = My_db()

        # self.login()

    def login(self):  # worked

        statement = "SELECT users.idUsers, users.User_Name, users.User_Password, User_Email, users.Fname," \
                    " users.Lname, privilages.roles, privilages.can_manage_users,privilages.can_view_chart, " \
                    "privilages.can_manage_stock,privilages.can_view_privacy, privilages.managing_role FROM " \
                    "lakydb.users inner join lakydb.privilages on users.idUsers = privilages.User_idUsers where" \
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

        self.role_check()

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
                     " `lakydb`.`privilages` ( `User_idUsers`,`roles`,`can_manage_users`," \
                     "`can_view_chart`, `can_view_privacy`,`can_manage_stock`, `managing_role`) " \
                     "VALUES (%s,%s,%s,%s,%s,%s,%s)"

        con = self.con.connect()
        cur = con.cursor()
        cur2 = con.cursor()
        try:
            cur.execute(statement1,
                        (self.new_user_user_name, Encryption.passcrypt(self.new_user_password), self.new_user_email,
                         self.new_user_fname, self.new_user_lname))
            # print(cur.lastrowid)
            cur2.execute(statement2,
                         (cur.lastrowid, self.new_user_role, self.new_user_manage_user, self.new_user_view_chart,
                            self.new_user_view_privacy, self.new_user_manage_stock, self.new_user_managing_control))
            con.commit()
            print('user added')
        except   errors.Error as err:
            if err.errno == errorcode.ER_DUP_ENTRY:
                print("record already exist")
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

class Phone:
    # caches = {}

    user_id = IntegerField(_min=0)
    ph_type = CharField(_min=2, _max=24)
    ph_model = CharField(_min=2, _max=24)
    ime = CharField(_min=2, _max=24)
    sn = CharField(_min=2, _max=24)
    price = Decimalfield(_min=2)

    def __init__(self):
        self.caches = {}
        self.con = My_db()

    def add_to_cart(self, user_id, ph_type, ph_model, ime, sn, price,
                 cust_name="unknown", cust_num="unknown",
                 payment="Cash", tax=0, discount=0):
        self.user_id = user_id
        self.ph_type = ph_type
        self.ph_model = ph_model
        self.ime = ime
        self.sn =sn
        self.price = price

        self.caches[self.ime] = {
                    "user_id": self.user_id,
                    "ph_type": self.ph_type,
                    "ph_model": self.ph_model,
                    "ime": self.ime,
                    "sn": self.sn,
                    "price": self.price,
                }
        # print(vars(self))
        # self.caches[self.ime]=(vars(self))

    def remove(self, ime):
        del self.caches[str(ime)]

    def clear_all(self):
        self.caches = {}

    def __len__(self):
        return len(self.caches)

#
# class Phone_operatiions(Phone):
#     def __init__(self):
#         self.con = My_db,
#         # pass

    def buyphone(self):

        if not len(self.caches):
            print("Nothing in cart to buy")
            return

        print("reading preparing to save" , "\n", self.caches)
        cn = self.con.connect()
        cur = cn.cursor()
        com = "INSERT INTO" \
              " `lakydb`.`sale_phone` ( `Sale_phone_id`,`type`,`model`, `phone_code`,`Customer_customer_contact`) " \
              "VALUES (%s,%s,%s,%s,%s)"
        cu = 1
        for _, val  in self.caches.items():
            # cur.execute("INSERT INTO `lakydb`.`customer` (`customer_name`,`customer_contact`)"
            #             "VALUE ('lawrence', '0243689393')"
            #             )

            cur.execute(com, (cu,val['ph_type'],val['ph_model'],val['ime'],'243689393'))
            cu +=1
        cn.commit()
        cn.close()

    def search(self, search_key, item):
        pass

    def printout(self):
        pass

class Stock:
    pass

if __name__ == "__main__":
    # d = Phone_operatiions()
    # p = Phone()
    #
    # p.add_to_cart(1,'samsung', 'p500', '123564789','sn-sjdnn',21.05)
    # p.add_to_cart(2, 'samsung', 'j00', '123564759', 'sn-sjdnn', 21.568)
    # p.add_to_cart(3, 'samsung', 'k500', '123564719', 'sn-sjdnn', 21.50)
    # p.buyphone()
    # # print(d.caches)

    #testing user
    u = Active_User("laky", "LAKY68")
    u.login()
    # a = u.reset_password('laky689393', 'LAKY68', "LAKY68")
    # print(a)
    # u.remove_user(25)
    # u.create_user("lawrence", 'secretry', 'sec2','laky689393', 'lawrence@txt.com', "sec",
    #              False, False, False, False, False)
    u.update_user('23',"perter", 'Lara', "lawrencetxt@gmai.com", "user", True,True, False, False, True)
    # u.remove_user(19)


