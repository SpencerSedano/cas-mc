from PySide6.QtCore import QObject, Signal
from PySide6.QtGui import QIcon, QImage, QPixmap, QKeySequence, QShortcut
from PySide6.QtWidgets import QApplication, QMainWindow, QButtonGroup, QScroller, QLabel, QGraphicsOpacityEffect, QPushButton
from common_msgs.msg import StateCmd

class PagesControl(QObject):

    run_cmd_requested = Signal(str)

    component_cmd_requested = Signal(str)
    

    def __init__(self, ui, ros_node):
        super().__init__()

        self.ui = ui
        self.ros_node = ros_node



    '''Menu'''

    def change_to_main_page(self, checked):
        if checked:
            # Buttons for Main Page reset
            main_page_buttons = [
                self.ui.AutoPauseButton,

                self.ui.RoughAlignButton,
                self.ui.PreciseAlignButton,
                self.ui.PickButton,
                self.ui.AssemblyButton,
                # self.ui.ManualPauseButton
            ]
            self.reset_buttons_and_machine(main_page_buttons, send_pause=False)

            self.ui.ParentStackedWidgetToChangeMenuOptions.setCurrentIndex(0)

        self.ui.AutoButton.setChecked(True)
        # self.change_to_auto_page()
        self.run_cmd_requested.emit("auto")


    def change_to_component_control_page(self, checked):
        if checked:
            component_control_buttons = [
                 self.ui.VisionOne,
                 self.ui.VisionTwo,
                 self.ui.VisionThree,

                 self.ui.buttonGroup
            ]
            self.reset_buttons_and_machine(component_control_buttons, send_pause=False)

            self.ui.ParentStackedWidgetToChangeMenuOptions.setCurrentIndex(1)
            self.ui.ComponentControlStackedWidget.setCurrentIndex(0)
            self.ui.MiddleStackedWidget.setCurrentIndex(0)
            self.run_cmd_requested.emit("component_control")


    def change_to_production_record_page(self):
        self.ui.ParentStackedWidgetToChangeMenuOptions.setCurrentIndex(2)

    def change_to_logs_page(self):
        self.ui.ParentStackedWidgetToChangeMenuOptions.setCurrentIndex(3)

    def change_to_system_settings_page(self):
        self.ui.ParentStackedWidgetToChangeMenuOptions.setCurrentIndex(4)


    '''Main Page'''
    
    def change_auto_or_manual(self, name, index): 
        if name == "Auto":
            self.ui.ActionButtons.setCurrentIndex(index)

        elif name == "Manual":
            self.ui.ActionButtons.setCurrentIndex(index)



    '''Component Control'''

    def toggle_menu(self):
        self.ui.ListOptionsWidget.setVisible(not self.ui.ListOptionsWidget.isVisible())

    def component_control_choose_page(self, name, index):
        self.ui.ComponentControlStackedWidget.setCurrentIndex(1)
        self.ui.MotorStartedButton.setText(name)
        self.ui.ChangeComponentControlStackedWidget.setCurrentIndex(index)

        if name == "DI/DO":
            self.component_cmd_requested.emit("dido_control")
            self.ui.MiddleStackedWidget.setCurrentIndex(1)
        elif name == "Motor":
            self.component_cmd_requested.emit("pose_control")
            self.ui.MiddleStackedWidget.setCurrentIndex(0)
        elif name == "Vision":
            self.component_cmd_requested.emit("vision_control")
            self.ui.MiddleStackedWidget.setCurrentIndex(0)
        elif name == "Gripper":
            self.component_cmd_requested.emit("cliper_control")
            self.ui.MiddleStackedWidget.setCurrentIndex(0)
        elif name == "Forklift":
            self.component_cmd_requested.emit("forklift_control")
            self.ui.MiddleStackedWidget.setCurrentIndex(0)

    def component_control_switch_page(self, name, index):
        self.ui.MotorStartedButton.setText(name)
        self.ui.ChangeComponentControlStackedWidget.setCurrentIndex(index)
        self.ui.ListOptionsWidget.setVisible(False)

        if name == "DI/DO":
            self.component_cmd_requested.emit("dido_control")
            self.ui.MiddleStackedWidget.setCurrentIndex(1)
        elif name == "Motor":
            self.component_cmd_requested.emit("pose_control")
            self.ui.MiddleStackedWidget.setCurrentIndex(0)
        elif name == "Vision":
            self.component_cmd_requested.emit("vision_control")
            self.ui.MiddleStackedWidget.setCurrentIndex(0)
        elif name == "Gripper":
            self.component_cmd_requested.emit("cliper_control")
            self.ui.MiddleStackedWidget.setCurrentIndex(0)
        elif name == "Forklift":
            self.component_cmd_requested.emit("forklift_control")
            self.ui.MiddleStackedWidget.setCurrentIndex(0)

    def go_to_next_page_motor(self, index):
        self.ui.MotorStackedWidget.setCurrentIndex(index)

    
    '''Helper functions'''

    def reset_buttons_and_machine(self, buttons_or_groups, send_pause=False):
        for item in buttons_or_groups:
            if isinstance(item, QButtonGroup):
                # Temporarily disable exclusivity to allow all buttons to uncheck
                item.setExclusive(False)
                for btn in item.buttons():
                    btn.setChecked(False)
                item.setExclusive(True)
            else:
                # Normal single button
                item.setChecked(False)

        if send_pause:
            msg = StateCmd()
            msg.init_button = False
            msg.run_button = False
            msg.pause_button = True
            msg.stop_button = False
            self.ros_node.state_cmd_publisher.publish(msg)