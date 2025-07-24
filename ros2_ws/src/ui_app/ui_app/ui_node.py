import sys
from PySide6.QtCore import Qt, QEvent, QTimer, Signal
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from ui_app.ui_magic_cube_columns_timeline import Ui_MainWindow
# import resources_rc  # this includes the images

# for ROS2
import threading
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from common_msgs.msg import StateCmd


class ROSNode(Node):
    def __init__(self):
        super().__init__('ui_node')

        # Subscriber to the same topic
        # self.subscription = self.create_subscription(StateCmd, '/state_cmd', self.ros_message_callback, 10)

        # Publisher using custom StateCmd message
        self.publisher = self.create_publisher(StateCmd, '/state_cmd', 10)



        self._ui_callback = None

    def set_ui_callback(self, callback):
        self._ui_callback = callback

    # def ros_message_callback(self, msg):
    #     text = f"init: {msg.init_button}, run: {msg.run_button}, pause: {msg.pause_button}"
    #     print(f"ROSNode received: {text}")
    #     self.get_logger().info(f"ROSNode received: {text}")
    #     if self._ui_callback:
    #         self._ui_callback(text)


class MainWindow(QMainWindow):
    ros_msg_received = Signal(str)  # Thread-safe signal to update UI

    def __init__(self, ros_node):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ros_node = ros_node

        # Connect ROSNode callback to UI slot
        self.ros_node.set_ui_callback(self.on_ros_message)
        # Connect Qt signal to UI handler
        self.ros_msg_received.connect(self.handle_ros_message)

        # Start ROS spinning in a separate thread
        self._ros_thread = threading.Thread(target=rclpy.spin, args=(self.ros_node,), daemon=True)
        self._ros_thread.start()

        # Move window to 2nd screen if available or maximize
        screens = QApplication.screens()
        if len(screens) > 1:
            second_screen = screens[1]
            self.move(second_screen.geometry().topLeft())
            self.showFullScreen()
            print("full screen")
        else:
            self.showMaximized()
            print("screen maximized")

        # Connect buttons to send_flag
        self.ui.InitButton.clicked.connect(lambda: self.send_flag("init"))
        self.ui.RunButton.clicked.connect(lambda: self.send_flag("run"))
        self.ui.StopButton.clicked.connect(lambda: self.send_flag("stop"))

        # Touchscreen style handlers
        self.ui.InitButton.clicked.connect(lambda: self.on_menu_buttons_clicked(self.ui.InitButton))
        self.ui.RunButton.clicked.connect(lambda: self.on_menu_buttons_clicked(self.ui.RunButton))
        self.ui.StopButton.clicked.connect(lambda: self.on_menu_buttons_clicked(self.ui.StopButton))
        self.ui.ResetButton.clicked.connect(lambda: self.on_menu_buttons_clicked(self.ui.ResetButton))

        self.ui.ControlUp.clicked.connect(lambda: self.on_control_arrows_clicked(self.ui.ControlUp))
        self.ui.ControlLeft.clicked.connect(lambda: self.on_control_arrows_clicked(self.ui.ControlLeft))
        self.ui.ControlDown.clicked.connect(lambda: self.on_control_arrows_clicked(self.ui.ControlDown))
        self.ui.ControlRight.clicked.connect(lambda: self.on_control_arrows_clicked(self.ui.ControlRight))
        self.ui.YawPlus.clicked.connect(lambda: self.on_control_arrows_clicked(self.ui.YawPlus))
        self.ui.YawMinus.clicked.connect(lambda: self.on_control_arrows_clicked(self.ui.YawMinus))

        self.ui.RecordDataButton.clicked.connect(lambda: self.on_record_data_clicked(self.ui.RecordDataButton))
        self.ui.ClipperButton.toggled.connect(lambda: self.update_clipper_state(self.ui.ClipperButton))

        self.ui.AutoButton.clicked.connect(self.change_auto_page)
        self.ui.ManualButton.clicked.connect(self.change_manual_page)

        self.ui.MainPageButton.clicked.connect(self.change_to_main_page)
        self.ui.ProductionRecordButton.clicked.connect(self.change_to_production_record_page)
        self.ui.ComponentControlButton.clicked.connect(self.change_to_component_control_page)
        self.ui.LogsButton.clicked.connect(self.change_to_logs_page)
        self.ui.SystemSettingsButton.clicked.connect(self.change_to_system_settings_page)

        self.ui.MotorPageButton.clicked.connect(self.change_to_motor_page)
        self.ui.VisionPageButton.clicked.connect(self.change_to_vision_page)
        self.ui.ClipperPageButton.clicked.connect(self.change_to_clipper_page)

    def send_flag(self, flag):
        msg = StateCmd()

        # Reset all flags
        msg.pause_button = False
        msg.init_button = False
        msg.run_button = False

        if flag == "init":
            msg.init_button = True
        elif flag == "run":
            msg.run_button = True
        elif flag == "stop":
            msg.pause_button = True

        print(f"[DEBUG] Publishing StateCmd: {msg}")
        self.ros_node.publisher.publish(msg)
        print(f"[UI] Sent StateCmd: {flag}")

    def update_clipper_state(self, button):
        if button.isChecked():
            button.setText("Clipper ON")
        else:
            button.setText("Clipper OFF")

    def change_auto_page(self):
        self.ui.ActionButtons.setCurrentIndex(0)
        self.ui.ProcessAndInfoStackedWidget.setCurrentIndex(0)

    def change_manual_page(self):
        self.ui.ActionButtons.setCurrentIndex(1)
        self.ui.ProcessAndInfoStackedWidget.setCurrentIndex(1)

    def change_to_main_page(self):
        self.ui.ParentStackedWidgetToChangeMenuOptions.setCurrentIndex(0)

    def change_to_production_record_page(self):
        self.ui.ParentStackedWidgetToChangeMenuOptions.setCurrentIndex(1)

    def change_to_component_control_page(self):
        self.ui.ParentStackedWidgetToChangeMenuOptions.setCurrentIndex(2)

    def change_to_logs_page(self):
        self.ui.ParentStackedWidgetToChangeMenuOptions.setCurrentIndex(3)

    def change_to_system_settings_page(self):
        self.ui.ParentStackedWidgetToChangeMenuOptions.setCurrentIndex(4)

    def change_to_motor_page(self):
        self.ui.ComponentControlStackedWidget.setCurrentIndex(0)

    def change_to_vision_page(self):
        self.ui.ComponentControlStackedWidget.setCurrentIndex(1)

    def change_to_clipper_page(self):
        self.ui.ComponentControlStackedWidget.setCurrentIndex(2)

    def on_menu_buttons_clicked(self, button):
        button.setStyleSheet("""
        QPushButton {
            background-color: #0B76A0;
            color: White;
            padding: 5px;
        }
        """)
        QTimer.singleShot(150, lambda: button.setStyleSheet("""
        QPushButton {
            color: white;
            padding: 5px;
        }
        """))

    def on_control_arrows_clicked(self, button):
        button.setStyleSheet("""
        QPushButton {
            background-color: #0B76A0;
            color: White;
        }
        """)
        QTimer.singleShot(150, lambda: button.setStyleSheet("""
        QPushButton {
            background-color: none;
            color: white;
        }
        """))

    def on_record_data_clicked(self, button):
        button.setStyleSheet("""
        QPushButton {
            background-color: #0B76A0;
            color: White;
            padding: 16px 24px;
        }
        """)
        QTimer.singleShot(150, lambda: button.setStyleSheet("""
        QPushButton {
            color: white;
            padding: 16px 24px;
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


def ros_spin(node):
    rclpy.spin(node)


def main():
    rclpy.init()
    ros_node = ROSNode()

    app = QApplication(sys.argv)
    window = MainWindow(ros_node)

    threading.Thread(target=ros_spin, args=(ros_node,), daemon=True).start()

    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
