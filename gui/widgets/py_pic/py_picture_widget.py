from qt_core import *

custom_pict_style = '''
QLabel {{
        border:none;
        border-radius: 120;	
       

    }}
'''

class PyPicture(QLabel):
    def __init__(self, loc = ''):
        super().__init__()
        self.setPixmap(QPixmap(u"{0}".format(loc)))
        self.setScaledContents(True)
        self.setStyleSheet(custom_pict_style)