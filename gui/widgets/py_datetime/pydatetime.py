from qt_core import *
from datetime import datetime
style = '''
QDateTimeEdit {{
	background-color: {_bg_color};
	border-radius: {_radius}px;
	border: {_border_size}px solid transparent;
	padding-left: 10px;
    padding-right: 10px;
	selection-color: {_selection_color};
	selection-background-color: {_context_color};
    color: {_color};
}}
QDateTimeEdit:focus {{
	border: {_border_size}px solid {_context_color};
    background-color: {_bg_color_active};
}}
'''


class Py_datetime(QDateTimeEdit):
    def __init__(self,
                 radius=8,
                 border_size=2,
                 color="#FFF",
                 selection_color="#FFF",
                 bg_color="#333",
                 bg_color_active="#222",
                 context_color="#00ABE8",

                 ):
        super(Py_datetime, self).__init__()

        self.setCalendarPopup(True)

        # SET STYLESHEET
        self.set_stylesheet(
            radius,
            border_size,
            color,
            selection_color,
            bg_color,
            bg_color_active,
            context_color
        )




 # SET STYLESHEET
    def set_stylesheet(
        self,
        radius,
        border_size,
        color,
        selection_color,
        bg_color,
        bg_color_active,
        context_color
    ):
        # APPLY STYLESHEET
        style_format = style.format(
            _radius = radius,
            _border_size = border_size,
            _color = color,
            _selection_color = selection_color,
            _bg_color = bg_color,
            _bg_color_active = bg_color_active,
            _context_color = context_color
        )
        self.setStyleSheet(style_format)
        self.setDisplayFormat("d-MM-yyyy")
        self.setMinimumDate(datetime(2020, 1,1))


    def toPydate(self):
        return datetime(self.date().year(),self.date().month(),self.date().day())