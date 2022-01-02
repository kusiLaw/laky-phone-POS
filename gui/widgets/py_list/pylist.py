from qt_core import *


style = '''
QListWidget {{
	background-color: {_bg_color};
	border-radius: {_radius}px;
	border: {_border_size}px solid transparent;
	padding-left: 10px;
    padding-right: 10px;
	selection-color: {_selection_color};
	selection-background-color: {_context_color};
    color: {_color};
}}
QListWidget:focus {{
	border: {_border_size}px solid {_context_color};
    background-color: {_bg_color_active};
}}
'''

class Pylist(QListWidget):
    def __init__(self,
        text = "",
        place_holder_text = "",
        radius = 8,
        border_size = 2,
        color = "#FFF",
        selection_color = "#FFF",
        bg_color = "#333",
        bg_color_active = "#222",
        context_color = "#00ABE8",
        sort = True
                 ):
        super(Pylist, self).__init__()

        # if sort:
        #     self.setSortingEnabled(True)

        style_format = style.format(
            _radius=radius,
            _border_size=border_size,
            _color=color,
            _selection_color=selection_color,
            _bg_color=bg_color,
            _bg_color_active=bg_color_active,
            _context_color=context_color
        )
        self.setStyleSheet(style_format)