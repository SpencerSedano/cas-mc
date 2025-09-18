from PySide6.QtCore import QObject, Signal, QTimer, QPropertyAnimation, QSequentialAnimationGroup, QAbstractAnimation
from PySide6.QtGui import QIcon, QImage, QPixmap, QKeySequence, QShortcut
from PySide6.QtWidgets import QApplication, QMainWindow, QButtonGroup, QScroller, QLabel, QGraphicsOpacityEffect, QPushButton
from common_msgs.msg import StateCmd

class StyleUI(QObject):


    def __init__(self, ui, ros_node):
        super().__init__()

        self.ui = ui
        self.ros_node = ros_node

            # Build circle map once
        self._circles = {
            # "start":         self.ui.StartCircle,
            # "connect":       self.ui.ConnectCircle,
            "init":          self.ui.INITCircle,
            "idle":          self.ui.IdleCircle,
            "rough_align":   self.ui.RoughAlignCircle,
            "precise_align": self.ui.PreciseAlignCircle,
            "pick":          self.ui.PickCircle,
            "assembly":      self.ui.AssemblyCircle,
        }

        # Theme colors (match your palette if you like)
        self._COLORS = {
            "blue":   "#0B76A0",  # idle
            "yellow": "#FFB300",  # running
            "green":  "#2E7D32",  # done
            "red":    "#C62828",  # fail
            "off":    "#FFFFFF",  # dim/neutral
        }


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

    def add_style(self, widget, style):
        current = widget.styleSheet()
        widget.setStyleSheet(current + style)

        
    '''Animation'''        

    def opacity_animation(self, target):
        # create effect only once per target
        if not isinstance(target.graphicsEffect(), QGraphicsOpacityEffect):
            effect = QGraphicsOpacityEffect(target)
            target.setGraphicsEffect(effect)
        else:
            effect = target.graphicsEffect()

        self.fade_in = QPropertyAnimation(effect, b"opacity")
        self.fade_in.setStartValue(1.0)
        self.fade_in.setEndValue(0.2)
        self.fade_in.setDuration(1500)
        
        self.fade_out = QPropertyAnimation(effect, b"opacity")
        self.fade_out.setStartValue(0.2)
        self.fade_out.setEndValue(1.0)
        self.fade_out.setDuration(1500)

        self.opacity_group = QSequentialAnimationGroup()
        self.opacity_group.addAnimation(self.fade_in)
        self.opacity_group.addAnimation(self.fade_out)

        self.opacity_group.setLoopCount(-1)

        self.opacity_group.start()


    def stop_opacity_animation(self, target):
        if hasattr(self, "opacity_group") and self.opacity_group.state() == QAbstractAnimation.Running:
            self.opacity_group.stop()


    def _paint_only(self, stage: str, color_css: str):
        # Clear all
        for lbl in self._circles.values():
            if lbl is self._circles["init"]:
                continue

            self._paint_circle(lbl, self._COLORS["off"])

            # reset opacity for all
            effect = lbl.graphicsEffect()
            if isinstance(effect, QGraphicsOpacityEffect):
                effect.setOpacity(1.0)

        target = self._circles.get(stage)
        self.stop_opacity_animation(target)

        if target:
            self._paint_circle(target, color_css)

            if color_css == self._COLORS["yellow"]:
                self.opacity_animation(target)
            # else:
            #     self.stop_opacity_animation(target)


    def _handle_init_visual(self, phase: str):
        # phase ∈ {"running","done","fail","off"}
        if phase == "off":
            self._paint_circle(self.ui.INITCircle, self._COLORS["off"])
        elif phase == "done":
            # self._paint_only("init", self._COLORS["green"])
            self._paint_circle(self.ui.INITCircle, self._COLORS["green"])
        elif phase == "fail":
            self._paint_only("init", self._COLORS["red"])
        else:  # "running"
            self._paint_only("init", self._COLORS["yellow"])


    def _paint_circle(self, label, color_css: str):
        """Set background color; keep it round by using current size."""
        if not label:
            return
        
        if label == self.ui.INITCircle:
            effect = label.graphicsEffect()
            if isinstance(effect, QGraphicsOpacityEffect):
                effect.setOpacity(1.0)

        target = self._circles.get(label)
        self.stop_opacity_animation(target)

        radius = max(10, min(label.width(), label.height()) // 2)
        label.setStyleSheet(f"""
            QLabel {{
                background-color: {color_css};
                border: none;
                border-radius: {radius}px;
            }}
        """)


    def apply_task_state(self, mode: str, state: str):
        mode_l = (mode or "").strip().lower()
        state_l = (state or "").strip().lower()

        if mode_l not in self._circles:
            print(f"[TaskState/UI] Unknown mode '{mode_l}', state={state_l}")
            return

        if state_l == "idle":
            color = self._COLORS["blue"]
        elif state_l == "done":
            color = self._COLORS["green"]
        elif state_l == "fail":
            color = self._COLORS["red"]
        else:
            color = self._COLORS["yellow"]

        self._paint_only(mode_l, color)