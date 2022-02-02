
# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from qt_core import *

# STYLE
# ///////////////////////////////////////////////////////////////
style = '''
QMessageBox {{
	background-color: {_bg_color};
	padding-left: 10px;
	font-size: 20px;
    padding-right: 10px;
	selection-color: {_selection_color};
	selection-background-color: {_context_color};
    color: {_color};
}}

'''

# PY PUSH BUTTON
# ///////////////////////////////////////////////////////////////
class MessageBox(QMessageBox):
    def __init__(
        cls,
        text ,
        title = "Error Reporting",
        icon = QMessageBox.Information,
        button = None, #QMessageBox.Ok | QMessageBox.Cancel, #None ,#
        windicon =None,
        # show = False
        # color = "#dce1ec",
        # selection_color = "#dce1ec",
        # bg_color = "#1b1e23",
        # bg_color_active = "#222",
        # context_color = "#dce1ec",

    ):
        super().__init__()

        cls.setIcon(icon)
        cls.setWindowTitle(title)
        cls.setText(text)
        cls.setWindowIcon(QPixmap(windicon))

        if button:
            cls.setStandardButtons(button)

        cls.setStyleSheet(
            f'font-size: 18px;'
            f'padding-left: 0px;'
            f' padding-right: 10px;'
            f'text-align: left;'
        )
        # PARAMETERS

        if button:
            cls.setStandardButtons(button)
            result =  cls.exec_()
            print(result)
            return

        cls.exec_()


    # def show(cls):
    #     cls.exec_()

    #
    #     # # SET STYLESHEET
    #     self.set_stylesheet(
    #         color,
    #         selection_color,
    #         bg_color,
    #         bg_color_active,
    #         context_color
    #     )
    #
    # # # SET STYLESHEET
    # def set_stylesheet(
    #     self,
    #     color,
    #     selection_color,
    #     bg_color,
    #     bg_color_active,
    #     context_color
    # ):
    #     # APPLY STYLESHEET
    #     style_format = style.format(
    #         _color = color,
    #         _selection_color = selection_color,
    #         _bg_color = bg_color,
    #         _bg_color_active = bg_color_active,
    #         _context_color = context_color
    #     )
    #     self.setStyleSheet(style_format)