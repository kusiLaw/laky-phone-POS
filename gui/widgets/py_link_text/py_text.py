# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from qt_core import *
style = '''
    
    color: {_color};

QPushButton:hover,
QPushButton:link{{
	background-color: {_bg_color_hover};
}}
QPushButton:pressed {{	
	background-color: {_bg_color_pressed};
}}
'''