# from PySide6.QtSql import QSqlDatabase, QSqlQuery, QSqlError
import json
import sys
import  mysql.connector
from mysql.connector import errorcode
import sqlite3

sys.path.append("..")
# from  import Custom_json
from json_util import custom_deserializer, custom_serializer


class DB_Meta(type):
    def __new__(cls, name,base, class_dict):
        obj = super().__new__(cls, name, base, class_dict)

        try:
            # we must read json file to populate the  class
            obj.initial_args = dict(custom_deserializer())  # dict obj
            print("everything cool, file exit and is valid, done reading")
        except FileNotFoundError :
            # file not in folder
            print("file not found please activate")
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


class My_db(metaclass=DB_Meta):

    def connect(self):
        if self.initial_args["Default"] == "sqlite":
            self.con = sqlite3.connect(self.initial_args["mysql"]["dbname"] + ".sqlite")
            print("sqlite success")
            return self.con.cursor()

        if self.initial_args["Default"] == "mysql":

            try:
                self.con = mysql.connector.connect(
                    host= self.initial_args["mysql"]["hostname"],
                    user=self.initial_args["mysql"]['user'],
                    password=self.initial_args["mysql"]['password'],
                    database=self.initial_args["mysql"]["dbname"]
                )
                print('db aready on server')

            except mysql.connector.Error as err:

                if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                    return "Something is wrong with your user name or password"
                elif err.errno == errorcode.ER_BAD_DB_ERROR:
                    print("Database does not exist")
                    self.con = mysql.connector.connect(
                        host=self.initial_args["mysql"]["hostname"],
                        user=self.initial_args["mysql"]['user'],
                        password=self.initial_args["mysql"]['password'],

                    )
                    a = self.con.cursor()
                    a.execute(self.create_tables(), multi=True)
                    print(a)
                    a.close()
            except:
                print("error occured")

            return self.con.cursor()

            # self.db = QSqlDatabase.addDatabase(str(self.initial_args["Default"]))
            # self.db.setHostName(self.initial_args["QMYSQL"]["hostname"])
            # self.db.setDatabaseName()
            # self.db.setUserName(self.initial_args["QMYSQL"]['user'])
            # # TODO: password should be well handled
            # self.db.setPassword(self.initial_args["QMYSQL"]['password'])
            # print("mysql sucess")
            # return self.db.open()
        else:
            raise NotImplemented("Database specified currently not supported")


    @classmethod
    def save_changes(cls, host,user,password,dbname= "lakydb", default_engin ="sqlite"):

        # change the class parameter and save change to use be used the next type
        if  default_engin == "sqlite":
            cls.initial_args["Default"] = default_engin
            cls.initial_args["sqlite"]["dbname"] = dbname

            custom_serializer(cls.initial_args)
            return
        elif default_engin == "mysql":
            cls.initial_args["Default"] = default_engin
            cls.initial_args["mysql"]["dbname"] = dbname
            cls.initial_args["mysql"]["hostname"] = host
            cls.initial_args["mysql"]['user'] = user
            # Todo : get proper way to handle password
            cls.initial_args["mysql"]['password'] =password

            custom_serializer(cls.initial_args)
            return
        else:
            raise NotImplemented("Database specified currently not supported")

    @classmethod
    def restore_to_default(cls):
        # TODO: authenticate if the software is activated
        custom_serializer({
            "Default": "sqlite",
            "sqlite": {
                "dbname": "lakydb"
                },
            "mysql": {
                "hostname": "localhost",
                "user": "root",
                "dbname": "lakydb",
                "password": "Laky@689393"
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
              `User_Password` VARCHAR(15) NOT NULL,
              `User_Email` VARCHAR(45) NULL,
              PRIMARY KEY (`idUsers`),
              UNIQUE INDEX `idUsers_UNIQUE` (`idUsers` ASC) VISIBLE,
              UNIQUE INDEX `User_Name_UNIQUE` (`User_Name` ASC) VISIBLE)
            
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
        """
        return exec_str


if __name__ == "__main__":
    dic = My_db()
    a =dic.connect()
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

