from .my_db import My_db


class Operations(My_db):
    def handle(self, fun):
        try:
            fun()
        except:
            pass