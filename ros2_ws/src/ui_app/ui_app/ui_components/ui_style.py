from PySide6.QtCore import QObject, Signal, QTimer
from PySide6.QtGui import QIcon, QImage, QPixmap, QKeySequence, QShortcut
from PySide6.QtWidgets import QApplication, QMainWindow, QButtonGroup, QScroller, QLabel, QGraphicsOpacityEffect, QPushButton
from common_msgs.msg import StateCmd

class StyleUI(QObject):

    def __init__(self, ui, ros_node):
        super().__init__()

        self.ui = ui
        self.ros_node = ros_node


    def on_touch_different_color(self, button, color, border, colorPressed, borderPressed):
        # 1. Apply pressed style immediately
        button.setStyleSheet(f"""
        QPushButton {{
            background-color: {color};
            color: white;
            border: 2px solid {border};
        }}
        """)

        # 2. Reset back to normal style after 300ms (with :disabled included)
        QTimer.singleShot(300, lambda: button.setStyleSheet(f"""
        QPushButton {{
            background-color: {colorPressed};       /* Darker pressed red */
            border: 2px inset {borderPressed};      /* Inset border for "sunken" effect */
            color: white;
 
        }}

        QPushButton:disabled {{
            background-color: #BDBDBD;
            border: 2px solid #9E9E9E;
            color: #616161;
        }}
        """))
