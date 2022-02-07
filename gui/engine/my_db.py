# from PySide6.QtSql import QSqlDatabase, QSqlQuery, QSqlError
import json
import sys
import  mysql.connector
from mysql.connector import errorcode
import sqlite3

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
                    raise mysql.connector.errors.ProgrammingError(err.msg)
                if err.errno == 2003:
                    raise mysql.connector.errors.ProgrammingError("Can't connect to MySQL server" )

                elif err.errno == errorcode.ER_BAD_DB_ERROR:
                    # print("Database does not exist")
                    self.con = mysql.connector.connect(
                        host=self.initial_args["mysql"]["hostname"],
                        user=self.initial_args["mysql"]['user'],
                        password=self.initial_args["mysql"]['password'],

                    )
                    a = self.con.cursor()
                    for result in a.execute(self.create_tables(), multi=True):
                        print("Number of rows affected by statement '{}': {}".format(
                            result.statement, result.rowcount))

                        # if result.with_rows:
                    # a.executemany(self.create_tables())
                    # print(a)
                    # a.close()
            except:
                raise mysql.connector.errors.ProgrammingError('unknown database error occured')


            else:
                return self.con


            # # TODO: password should be well handled

        else:
            raise ValueError("Sorry databese engine not supported")
            # raise NotImplemented("Database specified currently not supported")


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
  `User_Password` BINARY(20) NOT NULL,
  `User_Email` VARCHAR(45) NULL,
  PRIMARY KEY (`idUsers`),
  UNIQUE INDEX `idUsers_UNIQUE` (`idUsers` ASC) VISIBLE,
  UNIQUE INDEX `User_Name_UNIQUE` (`User_Name` ASC) VISIBLE)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `lakydb`.`Customer` (
  `customer_contact` INT NOT NULL,
  `customer_name` VARCHAR(25) NULL DEFAULT '\"Customer\"',
  `users_idUsers` INT NOT NULL,
  PRIMARY KEY (`customer_contact`),
  INDEX `fk_Customer_Users_idx` (`users_idUsers` ASC) VISIBLE,
  CONSTRAINT `fk_Customer_Users`
    FOREIGN KEY (`users_idUsers`)
    REFERENCES `lakydb`.`Users` (`idUsers`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `lakydb`.`Service_Phone` (
  `Phone_ID` INT NOT NULL AUTO_INCREMENT,
  `Phone_Type` VARCHAR(45) NOT NULL,
  `Phone_Model` VARCHAR(45) NOT NULL,
  `Phone_Fault` VARCHAR(45) NOT NULL,
  `Phone_Imei` INT NULL,
  `Comments` VARCHAR(45) NULL,
  `Phone_Status` VARCHAR(45) NULL DEFAULT 'Faulty',
  `Receive Status` VARCHAR(45) NULL DEFAULT 'No',
  `Customer_Customer_Contact` INT NOT NULL,
  PRIMARY KEY (`Phone_ID`),
  INDEX `fk_Service_Phone_Customer1_idx` (`Customer_Customer_Contact` ASC) VISIBLE,
  CONSTRAINT `fk_Service_Phone_Customer1`
    FOREIGN KEY (`Customer_Customer_Contact`)
    REFERENCES `lakydb`.`Customer` (`customer_contact`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `lakydb`.`Price` (
  `Amount` DOUBLE NOT NULL,
  `Deposite` DOUBLE NULL,
  `Balance` DOUBLE NULL,
  `Pricecol1` DOUBLE NULL,
  `Service_Phone_Phone_ID` INT NOT NULL,
  INDEX `fk_Price_Service_Phone1_idx` (`Service_Phone_Phone_ID` ASC) VISIBLE,
  CONSTRAINT `fk_Price_Service_Phone1`
    FOREIGN KEY (`Service_Phone_Phone_ID`)
    REFERENCES `lakydb`.`Service_Phone` (`Phone_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `lakydb`.`Stock` (
  `stockId` INT NOT NULL,
  `phone_name` VARCHAR(20) NOT NULL,
  `Phonr_type` VARCHAR(20) NOT NULL,
  `phone_imei` INT NULL,
  `Users_idUsers` INT NOT NULL,
  PRIMARY KEY (`stockId`),
  UNIQUE INDEX `phone_imei_UNIQUE` (`phone_imei` ASC) VISIBLE,
  INDEX `fk_Stock_Users1_idx` (`Users_idUsers` ASC) VISIBLE,
  CONSTRAINT `fk_Stock_Users1`
    FOREIGN KEY (`Users_idUsers`)
    REFERENCES `lakydb`.`Users` (`idUsers`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `lakydb`.`Suplier` (
  `idsuplier` INT NOT NULL AUTO_INCREMENT,
  `supliername` VARCHAR(20) NOT NULL,
  `number` VARCHAR(45) NULL,
  PRIMARY KEY (`idsuplier`))
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `lakydb`.`Suply` (
  `idsuplies` INT NOT NULL,
  `suply_code` VARCHAR(45) NOT NULL,
  `quantity` VARCHAR(45) NULL,
  `date` VARCHAR(45) NULL,
  `Suplier_idsuplier` INT NOT NULL,
  PRIMARY KEY (`idsuplies`),
  INDEX `fk_Suply_Suplier1_idx` (`Suplier_idsuplier` ASC) VISIBLE,
  CONSTRAINT `fk_Suply_Suplier1`
    FOREIGN KEY (`Suplier_idsuplier`)
    REFERENCES `lakydb`.`Suplier` (`idsuplier`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `lakydb`.`Stock_phone_info` (
  `info_id` INT NOT NULL AUTO_INCREMENT,
  `phone_sn` VARCHAR(45) NULL,
  `phone_imei` INT NULL,
  `phone_meid` VARCHAR(45) NULL,
  `Stock_stockId` INT NOT NULL,
  `suplier_idsuplier` INT NOT NULL,
  `Suply_idsuplies` INT NOT NULL,
  INDEX `fk_phone_info_Stock1_idx` (`Stock_stockId` ASC) VISIBLE,
  PRIMARY KEY (`info_id`),
  INDEX `fk_phone_info_suplier1_idx` (`suplier_idsuplier` ASC) VISIBLE,
  INDEX `fk_Phone_info_Suply1_idx` (`Suply_idsuplies` ASC) VISIBLE,
  CONSTRAINT `fk_phone_info_Stock1`
    FOREIGN KEY (`Stock_stockId`)
    REFERENCES `lakydb`.`Stock` (`stockId`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_phone_info_suplier1`
    FOREIGN KEY (`suplier_idsuplier`)
    REFERENCES `lakydb`.`Suplier` (`idsuplier`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Phone_info_Suply1`
    FOREIGN KEY (`Suply_idsuplies`)
    REFERENCES `lakydb`.`Suply` (`idsuplies`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `lakydb`.`Stock_prices` (
  `Stock_stockId` INT NOT NULL,
  `quantity` INT NOT NULL,
  `cost_pricel` DECIMAL(12) NOT NULL,
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

CREATE TABLE IF NOT EXISTS `lakydb`.`Sale_phone` (
  `Sale_phone_id` INT NOT NULL,
  `type` VARCHAR(45) NULL,
  `model` VARCHAR(45) NULL,
  `phone_code` VARCHAR(45) NULL,
  `Customer_customer_contact` INT NOT NULL,
  PRIMARY KEY (`Sale_phone_id`),
  INDEX `fk_Sale_phone_Customer1_idx` (`Customer_customer_contact` ASC) VISIBLE,
  CONSTRAINT `fk_Sale_phone_Customer1`
    FOREIGN KEY (`Customer_customer_contact`)
    REFERENCES `lakydb`.`Customer` (`customer_contact`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `lakydb`.`phone_transaction` (
  `phone_transaction_id` INT NOT NULL,
  `trans_code` VARCHAR(45) NOT NULL,
  `discount` INT NULL,
  PRIMARY KEY (`phone_transaction_id`),
  UNIQUE INDEX `trans_code_UNIQUE` (`trans_code` ASC) VISIBLE)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `lakydb`.`Phone_prices` (
  `phone_price_id` INT NOT NULL,
  `sp` VARCHAR(45) NULL,
  `Phone_pricescol` VARCHAR(45) NULL,
  `tax` VARCHAR(45) NULL,
  `date` VARCHAR(45) NULL,
  `phone_transaction_phone_transaction_id` INT NOT NULL,
  `Sale_phone_Sale_phone_id` INT NOT NULL,
  PRIMARY KEY (`phone_price_id`, `Sale_phone_Sale_phone_id`),
  INDEX `fk_Phone_prices_phone_transaction1_idx` (`phone_transaction_phone_transaction_id` ASC) VISIBLE,
  INDEX `fk_Phone_prices_Sale_phone1_idx` (`Sale_phone_Sale_phone_id` ASC) VISIBLE,
  CONSTRAINT `fk_Phone_prices_phone_transaction1`
    FOREIGN KEY (`phone_transaction_phone_transaction_id`)
    REFERENCES `lakydb`.`phone_transaction` (`phone_transaction_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Phone_prices_Sale_phone1`
    FOREIGN KEY (`Sale_phone_Sale_phone_id`)
    REFERENCES `lakydb`.`Sale_phone` (`Sale_phone_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;
        """
        return exec_str

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

