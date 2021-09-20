# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from qt_core import *
from gui.core.json_settings import Settings

# IMPORT THEME COLORS
# ///////////////////////////////////////////////////////////////
from gui.core.json_themes import Themes



style = '''
QPushButton {{
        border:none;
        padding-left: 10px;
        padding-right: 5px;
        color: {_color};
        border-radius: {_radius};	
        background-color: {_bg_color};
    }}
    QPushButton:hover {{
        background-color: {_bg_color_hover};
        border: 2px solid {_bdcolor};
    }}
    QPushButton:pressed {{	
        background-color: {_bg_color_pressed};
    }}
'''


style2 = '''
QPushButton {{
        border:none;
        padding-left: 10px;
        padding-right: 5px;
        color: {_color};
        border-radius: {_radius};	
        background-color: {_bg_color};
        border: 2px solid {_bdcolor};

    }}
    QPushButton:hover {{
        background-color: {_bg_color_hover};
        border: 2px solid {_bdcolor};
    }}
    QPushButton:pressed {{	
        background-color: {_bg_color_pressed};
    }}
'''




# PY PUSH BUTTON
# ///////////////////////////////////////////////////////////////
class PyPushButton2(QPushButton):
    def __init__(
            self,
            text,
            radius,
            color,
            bg_color,
            bg_color_hover,
            bg_color_pressed,
            hover_border_color,
            parent=None,
            border_color = True,
            show_boader_color = False
    ):
        super().__init__()


        # SET PARAMETRES
        self.setText(text)
        if parent != None:
            self.setParent(parent)
        self.setCursor(Qt.PointingHandCursor)

        # SET STYLESHEET
        custom_style = style.format(
            _color=color,
            _radius=radius,
            _bg_color=bg_color,
            _bg_color_hover=bg_color_hover,
            _bg_color_pressed=bg_color_pressed,
            _bdcolor = hover_border_color
        )

        custom_style_show = style2.format(
            _color=color,
            _radius=radius,
            _bg_color=bg_color,
            _bg_color_hover=bg_color_hover,
            _bg_color_pressed=bg_color_pressed,
            _bdcolor=hover_border_color
        )

        if show_boader_color:
            self.setStyleSheet(custom_style_show)
        else:
            self.setStyleSheet(custom_style)


        # # icon test
        # # PAINT EVENT
        # # painting the button and the icon
        # # ///////////////////////////////////////////////////////////////
        # def paintEvent(self, event):
        #     # PAINTER
        #     paint = QPainter()
        #     paint.begin(self)
        #     paint.setRenderHint(QPainter.RenderHint.Antialiasing)
        #
        #     # if self._is_active:
        #     #     # BRUSH
        #     #     brush = QBrush(QColor(self._context_color))
        #     # else:
        #     #     # BRUSH
        #     #     brush = QBrush(QColor(self._set_bg_color))
        #     brush = QBrush(QColor(self.bg_color))
        #
        #     # CREATE RECTANGLE
        #     rect = QRect(0, 0, self.width(), self.height())
        #     paint.setPen(Qt.NoPen)
        #     paint.setBrush(brush)
        #     paint.drawRoundedRect(
        #         rect,
        #         self._set_border_radius,
        #         self._set_border_radius
        #     )
        #
        #     # DRAW ICONS
        #     self.icon_paint(paint, self._set_icon_path, rect)
        #
        #     # END PAINTER
        #     paint.end()
        #
        # # DRAW ICON WITH COLORS
        # # ///////////////////////////////////////////////////////////////
        # def icon_paint(self, qp, image, rect):
        #     icon = QPixmap(image)
        #     painter = QPainter(icon)
        #     painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
        #     if self._is_active:
        #         painter.fillRect(icon.rect(), self._icon_color_active)
        #     else:
        #         painter.fillRect(icon.rect(), self._set_icon_color)
        #     qp.drawPixmap(
        #         (rect.width() - icon.width()) / 2,
        #         (rect.height() - icon.height()) / 2,
        #         icon
        #     )
        #     painter.end()
        #
        # # SET ICON
        # # ///////////////////////////////////////////////////////////////
        # def set_icon(self, icon_path):
        #     self._set_icon_path = icon_path
        #     self.repaint()
