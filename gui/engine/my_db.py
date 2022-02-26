# from PySide6.QtSql import QSqlDatabase, QSqlQuery, QSqlError
import json
import sys
import  mysql.connector
from mysql.connector import errorcode, errors

from mysql.connector import errorcode
import sqlite3
from .auth import Encryption

# sys.path.append("..")
# from  import Custom_json
# print("catching")
# from json_util import custom_deserializer, custom_serializer
from .json_base import custom_deserializer, custom_serializer


# this help to read the file once.
class DB_Meta(type):
    def __new__(cls, name,base, class_dict):
        obj = super().__new__(cls, name, base, class_dict)

        try:
            # we must read json file to populate the  class
            obj.initial_args = dict(custom_deserializer())  # dict obj
            print("everything cool, file exit and is valid, done reading")
        except FileNotFoundError :
            # file not in folder
            # exit()
            raise FileNotFoundError("file not found please activate")
        except json.JSONDecodeError:
            print("Invalid file")

        # except:
        #     print("didnt find it try defaul")
        #     try:
        #         print("reading file from default in init")
        #         self.initial_args = self.restore_default()
        #     except:
        #         print("Error initilising object")
        # else:
        #
        #     # # when everything runs smooth
        #     # pass
        #     # # obj.db = QSqlDatabase.addDatabase(obj.initial_args["Default"])
        #     #
        #

        return obj


# class My_db(metaclass=DB_Meta):

class My_db():
    def __init__(self):
        try:

            self.initial_args = dict(custom_deserializer())  # dict obj
            # print('as new instan reding file')
        except FileNotFoundError:
            raise FileNotFoundError('File not found. You need to retore')

    def connect(self):
        # if self.initial_args["Default"] == "sqlite":
        #     self.con = sqlite3.connect(self.initial_args["mysql"]["dbname"] + ".sqlite")
        #     print("sqlite success")
        #     return self.con.cursor()

        if self.initial_args["Default"] == "mysql":

            try:
                self.con = mysql.connector.connect(
                    host= self.initial_args["mysql"]["hostname"],
                    user=self.initial_args["mysql"]['user'],
                    password=self.initial_args["mysql"]['password'],
                    database=self.initial_args["mysql"]["dbname"]
                )
                # connection was sucessful and return connetion to caller
                # print('db aready on server')

            except mysql.connector.Error as err:
                # print(err)
                if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                    raise mysql.connector.errors.ProgrammingError('Access denied,Please check username or password')
                if err.errno == 2003:
                    raise mysql.connector.errors.ProgrammingError("Can't connect to MySQL server ")

                elif err.errno == errorcode.ER_BAD_DB_ERROR:
                    # print("Database does not exist")
                    #to avoid long delay starting program creating database is seperated
                    raise mysql.connector.errors.ProgrammingError("LakyPOS database not found.  Please press 'create db', wait for some minutes and test connection again")
                return
            except:
                raise mysql.connector.errors.ProgrammingError('Unknown database error occured.\nGuidelines:\n step 1: Check server, username or password if correct. \n step 2:Press "create db", wait for some minutes and test connection again. \n If problem exist, please contact customer care')


            else:
                return self.con


            # # TODO: password should be well handled

        else:
            raise ValueError("Sorry database engine not supported")
            # raise NotImplemented("Database specified currently not supported")

    def create_table(self):
        if self.initial_args["Default"] == "mysql":

            try:
                self.con = mysql.connector.connect(
                    host=self.initial_args["mysql"]["hostname"],
                    user=self.initial_args["mysql"]['user'],
                    password=self.initial_args["mysql"]['password'],

                )
                a = self.con.cursor()
                for result in a.execute(self.create_tables(), multi=True):
                    print("Number of rows affected by statement '{}': {}".format(
                        result.statement, result.rowcount))

            except mysql.connector.Error as err:
                # print(err)
                if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                    raise mysql.connector.errors.ProgrammingError('Access denied,Please check username or password')
                if err.errno == 2003:
                    raise mysql.connector.errors.ProgrammingError("Can't connect to MySQL server ")

            except:
                raise mysql.connector.errors.ProgrammingError('unknown database error occured')

            else:
                #init defualt user for login
                try:
                    self.create_user(
                     fname = "laky", lname = "Pos", username = "lakypos", password = "12345", email = 'lakypos@gmail.com', role = "Admin",
                    can_take_stock = True, can_manage_user= True, can_view_privacy= True, managing_control= True, can_view_chart= True, inner_call = True
                    )
                    print("cretin")
                except:
                    raise
                else:
                    return True


    def create_user(self, fname, lname, username, password, email, role,
                    can_take_stock, can_manage_user, can_view_privacy, managing_control, can_view_chart,
                    inner_call=False):  # Worked

        statement1 = "INSERT INTO" \
                     " `lakydb`.`users` ( `User_Name`,`User_Password`,`User_Email`, `Fname`,`Lname`) " \
                     "VALUES (%s,%s,%s,%s,%s)"

        statement2 = "INSERT INTO" \
                     " `lakydb`.`user_privilages` ( `Users_idUsers`,`roles`,`can_manage_users`," \
                     "`can_view_chart`, `can_view_privacy`,`can_manage_stock`, `managing_role`) " \
                     "VALUES (%s,%s,%s,%s,%s,%s,%s)"


        con = self.connect() #self caller from main createdb
        cur = con.cursor()
        cur2 = con.cursor()
        try:

            cur.execute(statement1,
                        (username, Encryption.passcrypt(password), email,
                         fname, lname))
            lastid = cur.lastrowid
            print(cur.lastrowid)
            # con.commit()
            cur2.execute(statement2,
                         (lastid, role, can_manage_user, can_view_chart,
                          can_view_privacy, can_take_stock, managing_control))
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


    # @classmethod
    def save_changes(cls, host,user,password,port= 3306,dbname= "lakydb", default_engin ="mysql"):

        # change the class parameter and save change to use be used the next type
        # if  default_engin == "sqlite":
        #     cls.initial_args["Default"] = default_engin
        #     cls.initial_args["sqlite"]["dbname"] = dbname
        #
        #     custom_serializer(cls.initial_args)
        #     return
        if default_engin == "mysql":
            cls.initial_args["Default"] = default_engin

            cls.initial_args["mysql"]["dbname"] = dbname
            cls.initial_args["mysql"]["hostname"] = host
            cls.initial_args["mysql"]['user'] = user
            cls.initial_args["mysql"]['port'] = port
            # Todo : get proper way to handle password
            cls.initial_args["mysql"]['password'] =password

            custom_serializer(cls.initial_args)
            return
        else:
            raise ValueError("Database specified currently not supported")

    @classmethod
    def restore_to_default(cls):
        # TODO: authenticate if the software is activated
        custom_serializer({
            "Default": "mysql",
            "sqlite": {
                "dbname": "lakydb"
                },
            "mysql": {
                "hostname": "localhost",
                "user": "root",
                "dbname": "lakydb",
                "password": "Laky@689393",
                "port": 3306,
                "cert":"activation key here"
              }
        })
        # pass

    def create_tables(self):

        exec_str = """
   CREATE SCHEMA IF NOT EXISTS `lakydb` DEFAULT CHARACTER SET utf8 ;
USE `lakydb` ;

CREATE TABLE IF NOT EXISTS `lakydb`.`Users` (
  `idUsers` INT NOT NULL AUTO_INCREMENT,
  `User_Name` VARCHAR(25) NOT NULL,
  `User_Password` VARCHAR(255) NOT NULL,
  `User_Email` VARCHAR(45) NULL,
  `Fname` VARCHAR(45) NULL DEFAULT NULL,
  `Lname` VARCHAR(45) NULL DEFAULT NULL,
  `last_seen` DATETIME NULL,
  PRIMARY KEY (`idUsers`),
  UNIQUE INDEX `idUsers_UNIQUE` (`idUsers` ASC) VISIBLE,
  UNIQUE INDEX `User_Name_UNIQUE` (`User_Name` ASC) VISIBLE)
ENGINE = InnoDB;



CREATE TABLE IF NOT EXISTS `lakydb`.`Customer` (
  `customer_id` INT NOT NULL AUTO_INCREMENT,
  `customer_contact` VARCHAR(20) NULL DEFAULT 'n/a',
  `customer_name` VARCHAR(30) NULL DEFAULT '\"Customer\"',
  PRIMARY KEY (`customer_id`),
  UNIQUE INDEX `customer_contact_UNIQUE` (`customer_contact` ASC) VISIBLE)
ENGINE = InnoDB;


CREATE TABLE IF NOT EXISTS `lakydb`.`Stock` (
  `stockId` INT NOT NULL AUTO_INCREMENT,
  `phone_name` VARCHAR(20) NOT NULL,
  `phone_model` VARCHAR(20) NOT NULL,
  `Users_idUsers` INT NOT NULL,
  PRIMARY KEY (`stockId`),
  INDEX `fk_Stock_Users1_idx` (`Users_idUsers` ASC) VISIBLE,
  UNIQUE INDEX `Phonr_type_UNIQUE` (`phone_model` ASC) VISIBLE,
  CONSTRAINT `fk_Stock_Users1`
    FOREIGN KEY (`Users_idUsers`)
    REFERENCES `lakydb`.`Users` (`idUsers`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;



CREATE TABLE IF NOT EXISTS `lakydb`.`Suplier` (
  `idsuplier` INT NOT NULL AUTO_INCREMENT,
  `supliername` VARCHAR(20) NULL,
  `contact` VARCHAR(20) NULL,
  PRIMARY KEY (`idsuplier`),
  UNIQUE INDEX `contact_UNIQUE` (`contact` ASC) VISIBLE,
  UNIQUE INDEX `supliername_UNIQUE` (`supliername` ASC) VISIBLE)
ENGINE = InnoDB;


CREATE TABLE IF NOT EXISTS `lakydb`.`Orders` (
  `idorder` INT NOT NULL AUTO_INCREMENT,
  `order_codes` VARCHAR(45) NOT NULL,
  `dates` DATETIME NULL,
  `Suplier_idsuplier` INT NULL DEFAULT NULL,
  PRIMARY KEY (`idorder`),
  INDEX `fk_Suply_Suplier1_idx` (`Suplier_idsuplier` ASC) VISIBLE,
  UNIQUE INDEX `suply_code_UNIQUE` (`order_codes` ASC) VISIBLE,
  CONSTRAINT `fk_Suply_Suplier1`
    FOREIGN KEY (`Suplier_idsuplier`)
    REFERENCES `lakydb`.`Suplier` (`idsuplier`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;



CREATE TABLE IF NOT EXISTS `lakydb`.`Order_sn_info` (
  `info_id` INT NOT NULL AUTO_INCREMENT,
  `phone_sn` VARCHAR(45) NULL,
  `Stock_stockId` INT NOT NULL,
  `Orders_idorder` INT NOT NULL,
  `has_bought` TINYINT NULL,
  INDEX `fk_phone_info_Stock1_idx` (`Stock_stockId` ASC) VISIBLE,
  PRIMARY KEY (`info_id`),
  UNIQUE INDEX `phone_sn_UNIQUE` (`phone_sn` ASC) VISIBLE,
  INDEX `fk_Order_sn_info_Orders1_idx` (`Orders_idorder` ASC) VISIBLE,
  CONSTRAINT `fk_phone_info_Stock1`
    FOREIGN KEY (`Stock_stockId`)
    REFERENCES `lakydb`.`Stock` (`stockId`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Order_sn_info_Orders1`
    FOREIGN KEY (`Orders_idorder`)
    REFERENCES `lakydb`.`Orders` (`idorder`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


CREATE TABLE IF NOT EXISTS `lakydb`.`Stock_prices` (
  `Stock_stockId` INT NOT NULL,
  `quantity` INT UNSIGNED NOT NULL,
  `cost_price` DECIMAL(12) NOT NULL,
  `sale_price` DECIMAL(12) NOT NULL,
  `tax` INT NULL DEFAULT 0,
  `created_date` DATETIME NULL,
  `last_update` DATETIME NULL,
  PRIMARY KEY (`Stock_stockId`),
  INDEX `fk_Stock_prices_Stock1_idx` (`Stock_stockId` ASC) VISIBLE,
  CONSTRAINT `fk_Stock_prices_Stock1`
    FOREIGN KEY (`Stock_stockId`)
    REFERENCES `lakydb`.`Stock` (`stockId`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;



CREATE TABLE IF NOT EXISTS `lakydb`.`phone_transaction` (
  `phone_transaction_id` INT NOT NULL AUTO_INCREMENT,
  `trans_code` VARCHAR(45) NOT NULL,
  `discount` INT NULL,
  PRIMARY KEY (`phone_transaction_id`),
  UNIQUE INDEX `trans_code_UNIQUE` (`trans_code` ASC) VISIBLE)
ENGINE = InnoDB;



CREATE TABLE IF NOT EXISTS `lakydb`.`Sale_phone` (
  `Sale_phone_id` INT NOT NULL AUTO_INCREMENT,
  `phone_type` VARCHAR(45) NULL,
  `model` VARCHAR(45) NULL,
  `phone_code` VARCHAR(45) NULL,
  `Users_idUsers` INT NOT NULL,
  `Customer_customer_id` INT NOT NULL,
  `phone_transaction_phone_transaction_id` INT NOT NULL,
  PRIMARY KEY (`Sale_phone_id`),
  INDEX `fk_Sale_phone_Users1_idx` (`Users_idUsers` ASC) VISIBLE,
  INDEX `fk_Sale_phone_Customer1_idx` (`Customer_customer_id` ASC) VISIBLE,
  UNIQUE INDEX `phone_code_UNIQUE` (`phone_code` ASC) VISIBLE,
  INDEX `fk_Sale_phone_phone_transaction1_idx` (`phone_transaction_phone_transaction_id` ASC) VISIBLE,
  CONSTRAINT `fk_Sale_phone_Users1`
    FOREIGN KEY (`Users_idUsers`)
    REFERENCES `lakydb`.`Users` (`idUsers`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Sale_phone_Customer1`
    FOREIGN KEY (`Customer_customer_id`)
    REFERENCES `lakydb`.`Customer` (`customer_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Sale_phone_phone_transaction1`
    FOREIGN KEY (`phone_transaction_phone_transaction_id`)
    REFERENCES `lakydb`.`phone_transaction` (`phone_transaction_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;



CREATE TABLE IF NOT EXISTS `lakydb`.`Phone_prices` (
  `sp` DECIMAL(12) NULL,
  `tax` VARCHAR(45) NULL,
  `dates` DATETIME NULL,
  `Sale_phone_Sale_phone_id` INT NOT NULL,
  `quantity` INT NOT NULL,
  PRIMARY KEY (`Sale_phone_Sale_phone_id`),
  INDEX `fk_Phone_prices_Sale_phone1_idx` (`Sale_phone_Sale_phone_id` ASC) VISIBLE,
  CONSTRAINT `fk_Phone_prices_Sale_phone1`
    FOREIGN KEY (`Sale_phone_Sale_phone_id`)
    REFERENCES `lakydb`.`Sale_phone` (`Sale_phone_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;



CREATE TABLE IF NOT EXISTS `lakydb`.`User_privilages` (
  `Users_idUsers` INT NOT NULL,
  `roles` VARCHAR(25) NOT NULL,
  `can_manage_users` TINYINT NULL DEFAULT 0,
  `can_view_chart` TINYINT NULL DEFAULT NULL,
  `can_view_privacy` TINYINT NULL DEFAULT 0,
  `can_manage_stock` TINYINT NULL DEFAULT 0,
  `managing_role` TINYINT NULL DEFAULT 0,
  PRIMARY KEY (`Users_idUsers`),
  CONSTRAINT `fk_table1_Users1`
    FOREIGN KEY (`Users_idUsers`)
    REFERENCES `lakydb`.`Users` (`idUsers`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


CREATE TABLE IF NOT EXISTS `lakydb`.`Order_info` (
  `phone_name` VARCHAR(20) NOT NULL,
  `phone_model` VARCHAR(20) NOT NULL,
  `quantity` INT NOT NULL,
  `cost_price` DECIMAL(12) NOT NULL,
  `Orders_idorder` INT NOT NULL,
  PRIMARY KEY (`Orders_idorder`),
  CONSTRAINT `fk_Order_info_Orders1`
    FOREIGN KEY (`Orders_idorder`)
    REFERENCES `lakydb`.`Orders` (`idorder`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


CREATE TABLE IF NOT EXISTS `lakydb`.`discount_settings` (
  `dis_min` DECIMAL(12) NULL,
  `dos_max` DECIMAL(12) NULL,
  `id_discount_settings` INT NOT NULL,
  PRIMARY KEY (`id_discount_settings`))
ENGINE = InnoDB;


CREATE TABLE IF NOT EXISTS `lakydb`.`stock_caches_table` (
  `cache_date` DATE NOT NULL,
  `quntity_update` DOUBLE NOT NULL,
  UNIQUE INDEX `cache_date_UNIQUE` (`cache_date` ASC))
ENGINE = InnoDB;


        """
        return exec_str
# INSERT INTO `lakydb`.`users` (`User_Name`, `User_Password`, `User_Email`, `Fname`, `Lname`) VALUES ('lakypos', '12345', '', 'laky', 'Pos');
# INSERT INTO `lakydb`.`user_privilages` ( `Users_idUsers`,`roles`, `can_manage_users`, `can_view_chart`, `can_view_privacy`, `can_manage_stock`, `managing_role`) VALUES ((select idUsers from lakydb.users where User_Name = 'lakypos' ),'Admin', '1', '1', '1', '1', '1');

__all__ = ["My_db"]

if __name__ == "__main__":
    dic = My_db()
    a =dic.connect()
    b = a.cursor()
    b.execute("INSERT INTO `lakydb`.`users` ( `User_Name`,`User_Password`, `User_Email`)"
                     " VALUES ( 'law2','law2' ,'law@me') on duplicate key  update ('User_name = lawe')")
    a.commit()
    a.close()
    # for x in data:
    #     print(x)
    print(a)




    # My_db.restore_to_default()
    # print("first user start")
    # dic = My_db()
    # print("second user start")
    # dic2 = My_db()
    #
    # print("both dict instance dict")
    # print(dic.__dict__, dic2.__dict__)
    #
    # print("both class dict")
    # print(type(dic).initial_args,"\n", type(dic2).initial_args)
    #
    # print("both connect")
    # a =dic.connect()
    # print("dic connection was ", a)
    # b = dic2.connect()
    # print("dic connection was ", b)
    #
    # print(dic.__dict__, dic2.__dict__)
    #
    #
    # print("dic tries to make change")
    # dic.save_changes("127.0.0.1", 'root', 'Laky@689393',
    #                    default_engin="mysql"
    #                  )
    #
    # print("both class dict")
    # print(type(dic).initial_args,"\n", type(dic2).initial_args)
    #
    # print("dif person also  connect")
    # dic3 = My_db()
    # e = dic3.connect()
    # print("dic3 connection was ", e)
    # print(dic3.__dict__)
    #
    #
    # print("both connect")
    # c = dic.connect()
    # print("dic connection was ", c)
    # d = dic2.connect()
    # print("dic connection was ", d)

