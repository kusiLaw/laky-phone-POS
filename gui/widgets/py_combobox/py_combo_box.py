from qt_core import *

style = '''
    QComboBox {{
        border: none;
        padding-left: 10px;
        padding-right: 5px;
        color: {_color};
        border-radius: {_radius}px;	
        background-color: {_bg_color};
    }}
    QComboBox:hover {{
        border: 2px solid {_bg_color_hover};
    }}
    QComboBox:editable {{	
        background-color: {_bg_color} ;
    }}



'''

class PyComBox(QComboBox):
    def __init__(
            self,
            color,
            radius,
            bg_color,
            bg_color_hover,
            items = None,
            editable = True,
            height = 30,
            maxlen= None
    ):
        super().__init__()

        # set Properties
        self.setEditable(editable)  # make it editable
        self.setMinimumHeight(height)
        if items:
            self.addItems(items)

        if editable:
            # calling completer class to autocomplete
            self.completer = QCompleter(items)
            self.completer.setCaseSensitivity(Qt.CaseInsensitive)
            self.setCompleter(self.completer)
            # set stylesheet

            if maxlen:
                self.lineEdit().setMaxLength(maxlen)
        else:
            self.setCursor(Qt.PointingHandCursor)

        custom_style = style.format(
            _color=color,
           _radius=radius,
            _bg_color=bg_color,
            _bg_color_hover=bg_color_hover,

        )

        self.setStyleSheet(custom_style)