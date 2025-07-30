import sys
from PySide6.QtCore import Qt, QEvent, QTimer, Signal
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow

from ui_app.ui_magic_cube import Ui_MainWindow # Import my design made in Qt Designer (already in .py)
import ui_app.resources_rc  # this includes the images and icons

# for ROS2
import threading
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from common_msgs.msg import StateCmd, ForkCmd

#other imports
from datetime import date


class ROSNode(Node):
    def __init__(self):
        super().__init__('ui_node')

        self.mode_cmd = {
            'auto': True,
            'manual': False,
        }

        self.task_cmd = {
            'connect': False,
            'init': False,            
            'rough_align': False,
            'precise_align': False,
            'pick': False,
            'assem': False,
        }

        # Subscriber to the same topic
        # self.subscription = self.create_subscription(StateCmd, '/state_cmd', self.ros_message_callback, 10)

        # mode cmd
        self.mode_cmd_publisher = self.create_publisher(String, '/mode_cmd', 10)

        # publisher using custom StateCmd message
        self.state_cmd_publisher = self.create_publisher(StateCmd, '/state_cmd', 10)

        #task cmd
        self.task_cmd_publisher = self.create_publisher(String, '/task_cmd', 10)

        #fork lift
        self.fork_cmd_publisher = self.create_publisher(ForkCmd, '/fork_cmd', 10)


    def publish_fork_cmd(self, mode, speed, direction, distance):
        msg = ForkCmd()
        msg.mode = mode
        msg.speed = speed
        msg.direction = direction
        msg.distance = distance
        self.fork_cmd_publisher.publish(msg)
        self.get_logger().info(f"Published ForkCmd: mode={mode}, speed={speed}, direction={direction}, distance={distance}")




class MainWindow(QMainWindow):
    ros_msg_received = Signal(str)  # Thread-safe signal to update UI

    def __init__(self, ros_node):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #Start ROS2 Node
        self.ros_node = ros_node

        # Connect Qt signal to UI handler
        self.ros_msg_received.connect(self.handle_ros_message)

        # connect buttons to send data to another node (ROS2)
        self.ui.InitButton.clicked.connect(lambda: self.send_state_cmd("init"))
        self.ui.RunButton.clicked.connect(lambda: self.send_state_cmd("run"))
        self.ui.StopButton.clicked.connect(lambda: self.send_state_cmd("stop"))
        self.ui.AutoResetButton.clicked.connect(lambda: self.send_state_cmd("reset"))

        self.ui.AutoButtonOption.clicked.connect(lambda: self.send_mode_cmd("auto"))
        self.ui.ManualButton.clicked.connect(lambda: self.send_mode_cmd("manual"))

        self.ui.RoughAlignButton.clicked.connect(lambda: self.send_task_cmd("rough align"))
        self.ui.PreciseAlignButton.clicked.connect(lambda: self.send_task_cmd("precise align"))
        self.ui.PickButton.clicked.connect(lambda: self.send_task_cmd("pick"))
        self.ui.AssemblyButton.clicked.connect(lambda: self.send_task_cmd("assembly"))

        self.ui.LiftUp.clicked.connect(lambda: self.send_fork_cmd("up"))
        self.ui.LowerDown.clicked.connect(lambda: self.send_fork_cmd("down"))

        # Get Today's date
        today = date.today()
        formatted_date = today.strftime("%m/%d/%Y")
        self.ui.DateInput.setText(formatted_date)

        #By Default
        self.ui.ListOptionsWidget.setVisible(False)
        self.ui.HamburgerMenuInMainPageOptions.setVisible(False)
        self.ui.ManualOptionsWidget.setVisible(False)

        # Touchscreen style handlers in Main Page - Auto
        self.ui.InitButton.clicked.connect(lambda: self.on_touch_buttons(self.ui.InitButton))
        self.ui.RunButton.clicked.connect(lambda: self.on_touch_buttons(self.ui.RunButton))
        self.ui.StopButton.clicked.connect(lambda: self.on_touch_buttons(self.ui.StopButton))
        self.ui.AutoResetButton.clicked.connect(lambda: self.on_touch_buttons(self.ui.AutoResetButton))

        #Touchscreen style handlers in Motor
        self.ui.MotorResetButton.clicked.connect(lambda: self.on_touch_buttons(self.ui.MotorResetButton))

        self.ui.ControlUpCP.clicked.connect(lambda: self.on_touch_controls(self.ui.ControlUpCP))
        self.ui.ControlLeftCP.clicked.connect(lambda: self.on_touch_controls(self.ui.ControlLeftCP))
        self.ui.ControlDownCP.clicked.connect(lambda: self.on_touch_controls(self.ui.ControlDownCP))
        self.ui.ControlRightCP.clicked.connect(lambda: self.on_touch_controls(self.ui.ControlRightCP))
        self.ui.YawPlusCP.clicked.connect(lambda: self.on_touch_controls(self.ui.YawPlusCP))
        self.ui.YawMinusCP.clicked.connect(lambda: self.on_touch_controls(self.ui.YawMinusCP))

        self.ui.LiftUp.clicked.connect(lambda: self.on_touch_buttons(self.ui.LiftUp))
        self.ui.LowerDown.clicked.connect(lambda: self.on_touch_buttons(self.ui.LowerDown))

        # self.ui.RecordDataButton.clicked.connect(lambda: self.on_record_data_clicked(self.ui.RecordDataButton))
        self.ui.ClipperButtonOnOff.toggled.connect(lambda: self.update_clipper_state(self.ui.ClipperButtonOnOff))

        #Main Page, go to other pages
        self.ui.MainPageButton.clicked.connect(self.change_to_main_page)
        self.ui.ProductionRecordButton.clicked.connect(self.change_to_production_record_page)
        self.ui.ComponentControlButton.clicked.connect(self.change_to_component_control_page)
        self.ui.LogsButton.clicked.connect(self.change_to_logs_page)
        self.ui.SystemSettingsButton.clicked.connect(self.change_to_system_settings_page)

        # Main Page, Auto and Manual options
        self.ui.HamburgerMenuMainPage.clicked.connect(self.toggle_manual_menu)

        self.ui.AutoButtonOption.clicked.connect(lambda: self.main_page_manual_switch_page("Auto", 0))
        self.ui.ManualButton.clicked.connect(self.toggle_manual_button_menu)  # show submenu

        self.ui.RoughAlignButton.clicked.connect(lambda: self.main_page_manual_switch_page("Manual", 1))
        self.ui.PreciseAlignButton.clicked.connect(lambda: self.main_page_manual_switch_page("Manual", 2))
        self.ui.PickButton.clicked.connect(lambda: self.main_page_manual_switch_page("Manual", 3))
        self.ui.AssemblyButton.clicked.connect(lambda: self.main_page_manual_switch_page("Manual", 4))


        #Component Control, List Menu
        self.ui.HamburgerMenu.clicked.connect(self.toggle_menu)
 

        self.ui.MotorOption.clicked.connect(lambda: self.component_control_switch_page("Motor", 0))
        self.ui.VisionOption.clicked.connect(lambda: self.component_control_switch_page("Vision", 1))
        self.ui.ClipperOption.clicked.connect(lambda: self.component_control_switch_page("Clipper", 2))
        self.ui.ForkLiftOption.clicked.connect(lambda: self.component_control_switch_page("Fork Lift", 3))



    #ROS2 Flag
    def send_state_cmd(self, flag):
        msg = StateCmd()

        # Reset all flags
        msg.pause_button = False
        msg.init_button = False
        msg.run_button = False
        msg.reset_button = False

        if flag == "init":
            msg.init_button = True
        elif flag == "run":
            msg.run_button = True
        elif flag == "stop":
            msg.pause_button = True
        elif flag == "reset":
            msg.reset_button = True

        print(f"[DEBUG] Publishing StateCmd: {msg}")
        self.ros_node.state_cmd_publisher.publish(msg)
        print(f"[UI] Sent StateCmd: {flag}")

    def send_mode_cmd(self, flag):
        msg = String()

        msg.data = flag
        
        if flag == "auto":
            msg.data = "auto"
        elif flag == "manual":
            msg.data = "manual"

        self.ros_node.mode_cmd_publisher.publish(msg)
        print(f"[UI] Sent ModeCmd: {msg.data}")

    def send_task_cmd(self, flag):
        msg = String()

        msg.data = flag

        if flag == "rough align":
            msg.data = "rough align"
        elif flag == "precise align":
            msg.data = "precise align"
        elif flag == "pick":
            msg.data = "pick"
        elif flag == "assembly":
            msg.data = "assembly"
        
        self.ros_node.task_cmd_publisher.publish(msg)
        print(f"[UI] Sent TaskCmd: {msg.data}")

    def send_fork_cmd(self, direction):
        mode_button = self.ui.buttonGroup_2.checkedButton()
        speed_button = self.ui.buttonGroup.checkedButton()

        mode = mode_button.text().lower() if mode_button else "run"
        speed = speed_button.text().lower() if speed_button else "slow"
        distance = float(self.ui.SliderLift.value())

        self.ros_node.publish_fork_cmd(mode, speed, direction, distance)
        print(f"[UI] Sent ForkCmd: {mode}, {speed}, {direction}, {distance}")




    def update_clipper_state(self, button):
        if button.isChecked():
            button.setText("Clipper ON")
        else:
            button.setText("Clipper OFF")
    
    #Principal Menu - StackedWidget
    def change_to_main_page(self):
        self.ui.ParentStackedWidgetToChangeMenuOptions.setCurrentIndex(0)

    def change_to_component_control_page(self):
        self.ui.ParentStackedWidgetToChangeMenuOptions.setCurrentIndex(1)

    def change_to_production_record_page(self):
        self.ui.ParentStackedWidgetToChangeMenuOptions.setCurrentIndex(2)

    def change_to_logs_page(self):
        self.ui.ParentStackedWidgetToChangeMenuOptions.setCurrentIndex(3)

    def change_to_system_settings_page(self):
        self.ui.ParentStackedWidgetToChangeMenuOptions.setCurrentIndex(4)

    
    #Main Page - Manual
    def toggle_manual_menu(self):
        is_visible = self.ui.HamburgerMenuInMainPageOptions.isVisible()
        
        if is_visible:
            # Hide everything
            self.ui.HamburgerMenuInMainPageOptions.setVisible(False)
            self.ui.ManualOptionsWidget.setVisible(False)
        else:
            # Show hamburger menu
            self.ui.HamburgerMenuInMainPageOptions.setVisible(True)

            # Always show Auto & Manual buttons initially
            self.ui.AutoButtonOption.setVisible(True)
            self.ui.ManualButton.setVisible(True)

            # Hide manual submenu
            self.ui.ManualOptionsWidget.setVisible(False)


    def toggle_manual_button_menu(self):
        # Hide the top-level hamburger options
        self.ui.AutoButtonOption.setVisible(False)
        self.ui.ManualButton.setVisible(False)

        self.ui.AutoButton.setText("Manual")

        # Show the manual submenu
        self.ui.ManualOptionsWidget.setVisible(True)


    def main_page_manual_switch_page(self, name, index):
        self.ui.AutoButton.setText(name)
        self.ui.ActionButtons.setCurrentIndex(index)

        if name == "Auto":
            self.ui.ProcessAndInfoStackedWidget.setCurrentIndex(0)  # switch to Auto page
        elif name == "Manual":
            self.ui.ProcessAndInfoStackedWidget.setCurrentIndex(1)  # switch to Manual page

        # Close dropdowns
        self.ui.HamburgerMenuInMainPageOptions.setVisible(False)
        self.ui.ManualOptionsWidget.setVisible(False)


    #Component Control - Motor
    def toggle_menu(self):
        self.ui.ListOptionsWidget.setVisible(not self.ui.ListOptionsWidget.isVisible())

    def component_control_switch_page(self, name, index):
        self.ui.MotorStartedButton.setText(name)
        self.ui.ChangeComponentControlStackedWidget.setCurrentIndex(index)
        self.ui.ListOptionsWidget.setVisible(False)


    def on_touch_controls(self, button):
        # 1. Visual press feedback
        button.setStyleSheet("""
        QPushButton {
            background-color: rgba(11, 118, 160, 0.3); /* soft blue overlay */
            border: 1px solid #0B76A0;
            color: white;
        }
        """)
        
        # 2. Reset after 200ms
        QTimer.singleShot(200, lambda: button.setStyleSheet("""
        QPushButton {
            background-color: transparent;
            border: none;
            color: white;
        }
        """))

    def on_touch_buttons(self, button):
        # 1. Visual press feedback
        button.setStyleSheet("""
        QPushButton {
            background-color: rgba(11, 118, 160, 0.3); /* soft blue overlay */
            border: 1px solid #0B76A0;
            color: white;
        }
        """)
        
        # 2. Reset after 200ms
        QTimer.singleShot(200, lambda: button.setStyleSheet("""
        QPushButton {
            color: white;
        }
        """))


    def on_ros_message(self, text):
        self.ros_msg_received.emit(text)

    def handle_ros_message(self, text):
        print("ROS message:", text)
        # Update UI labels here if needed

    def closeEvent(self, event):
        self.ros_node.destroy_node()
        rclpy.shutdown()
        event.accept()

    def move_to_second_screen_and_fullscreen(self):
        screens = QApplication.screens()
        if len(screens) > 1:
            second_screen = screens[1]  # Use the actual second screen
            second_geom = second_screen.geometry()
            self.setGeometry(second_geom)  # Move and resize in one step
            self.showFullScreen()
            print("Moved to second screen and fullscreen")
        else:
            self.showMaximized()
            print("Only one screen, maximized")


def ros_spin(node):
    rclpy.spin(node)


def main():
    rclpy.init()
    ros_node = ROSNode()



    app = QApplication(sys.argv)

    window = MainWindow(ros_node)

    # Delay moving and fullscreen until after show()
    QTimer.singleShot(100, window.move_to_second_screen_and_fullscreen)

    threading.Thread(target=ros_spin, args=(ros_node,), daemon=True).start()

    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
