from qt_core import *

custom_pict_style = '''
QLabel {{
        border:none;
        border-radius: 120;	
       

    }}
'''

class PyPicture(QLabel):
    def __init__(self):
        super().__init__()
        self.setPixmap(QPixmap(u"D:/PICTURE/ME/ice_2021-02-20-12-00-31-381.jpg"))
        self.setScaledContents(True)
        self.setStyleSheet(custom_pict_style)