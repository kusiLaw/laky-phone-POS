from PySide6.QtSql import QSqlDatabase, QSqlDriver
import json
import mysql.connector


# class db_meta(type):
#     def __new__(cls, name,base, class_dict, sql_engine= "QSQLITE"):
#         obj = super().__new__(cls, name,base,class_dict)
#
#         obj.bd = QSqlDatabase.addDatabase(sql_engine)
#
#         return obj

class My_BaseDB:
    db = QSqlDatabase.addDatabase("QSQLITE")



class My_db:
    # __slots__ = "_db"

    # TODO: read default from  json file to populate the class parameter
    # db = QSqlDatabase.addDatabase("QSQLITE")


    def __init__(self, database_engin = "QSQLITE"):
        # overwrite this class "Qsql" object is mysql is used

        if  database_engin == "QMYSQL":
            self.class_initilzer(database_engin)

        # try:
        #     # we must read json file each instanciated since we want most current agrs
        #     self.initial_args = dict(My_db.deserialize())  # dict obj
        #     print("everything cool, file exit and is valid, done reading")
        # except FileNotFoundError :
        #     # file not in folder
        #     # Todo: I will generator object that send and recieve obj
        #     print("file not found please activate")
        # except json.JSONDecodeError:
        #     print("File exist but not valid")

        # except:
        #     print("didnt find it try defaul")
        #     try:
        #         print("reading file from default in init")
        #         self.initial_args = self.restore_default()
        #     except:
        #         print("Error initilising object")

    @classmethod
    def class_initilzer(cls, engine):
        cls.db = QSqlDatabase.addDatabase(engine)


    def connect(self):
        # TODO: read from file config to get the connection para, if file error use defualt settings
        self.db.setHostName(self.initial_args["hostname"])
        self.db.setDatabaseName(self.initial_args["dbname"])
        self.db.setUserName(self.initial_args['user'])
        self.db.setPassword(self.initial_args['password'])
        return self.db.open()

    def save_changes(self, host,dbname,user,password, database_engin ="Sqlite"):
        para = {
            "db_type" : database_engin,
            "hostname": host,
            "user": user,
            "dbname": dbname,
            "password": password
        }
        # write the default setting to file, and load new para to class
        # print(para)
        self.serialize(para)

        # manually call init to apply change
        print("reinitailings")
        self.__init__()

    def restore_default(self):
        self.initial_args ={
            "sqlLite": {
                "dbname": "myQtdb",
            },
            "local": {
                "hostname": "localhost",
                "user": "root",
                "dbname": "myQtdb",
                "password": "Laky@689393"
            }
        }

        self.serialize(self.initial_args)

        # # manually call init to apply change
        #  print("reinitailings")
        #  self.__init__()

    @staticmethod
    def serialize(obj):
        # WRITE JSON FILE
        with open("dbsettings.json", "w", encoding='utf-8') as writer:
            # json.dump(obj, writer,indent=2)
            writer.write(json.dumps(obj, indent=2))
            # My_db.deserialize()

    @staticmethod
    def deserialize():
        # READ JSON FILE
        with open("dbsettings.json", "r", encoding='utf-8') as reader:
            return json.loads(reader.read())





if __name__ == "__main__":
    dic = My_db()
    # dic2 = My_db()
    # dic3 = My_db()
    # dic4 = My_db()

    # print(
    #     dic.connect(),
    #     # dic2.connect(),
    #
    # )
    print(vars(dic))

    dic.save_changes("127.0.0.1", "mydb", 'law', 'weedT', "QMYSQL")
    print(vars(dic))
    dic.restore_default()
    print(vars(dic))