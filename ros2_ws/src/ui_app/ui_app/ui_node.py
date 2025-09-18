import sys
import math
from datetime import date
import cv2
from PySide6.QtCore import Qt, QEvent, QTimer, Signal, QPropertyAnimation, QSequentialAnimationGroup, QAbstractAnimation
from PySide6.QtGui import QIcon, QImage, QPixmap, QKeySequence, QShortcut
from PySide6.QtWidgets import QApplication, QMainWindow, QButtonGroup, QScroller, QLabel, QGraphicsOpacityEffect, QPushButton

from ui_app.ui_magic_cube import Ui_MainWindow # Import my design made in Qt Designer (already in .py)
import ui_app.resources_rc  # this includes the images and icons

#ui components
from ui_app.ui_components.ui_cabinets import CabinetsController
from ui_app.ui_components.ui_forklift import ForkliftController
from ui_app.ui_components.ui_motor import MotorController
from ui_app.ui_components.ui_gripper import GripperController
from ui_app.ui_components.ui_limit import LimitController
from ui_app.ui_components.ui_dido import DIDOController
# from ui_app.ui_components.ui_vision import VisionController
from ui_app.ui_components.ui_pages import PagesControl
from ui_app.ui_components.ui_style import StyleUI


#lib
from ui_app.libraries.fps import FPSCounter

#Vision
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

# for ROS2
import threading
import rclpy
from rclpy.node import Node
from std_msgs.msg import String, Int32, Float32MultiArray

from common_msgs.msg import StateCmd, ForkCmd, JogCmd, ComponentCmd, TaskCmd, TaskState, DIDOCmd, RunCmd, MotionCmd, MotionState, GripperCmd, MultipleM, MH2State, CurrentPose, Recipe, LimitCmd

from uros_interface.srv import ESMCmd


# pick_heights = {
#     "C1": [944.0, 824.0, 704.0, 586.0, 465.0, 344.0, 226.0, 113.0, 113.0],
#     "C2": [944.0, 824.0, 704.0, 586.0, 465.0, 344.0, 226.0, 113.0, 113.0],
# }

# # Assembly (4x9，高度獨立)
# assembly_heights = {
#     "C1": [944.0, 824.0, 704.0, 586.0, 465.0, 344.0, 226.0, 113.0, 113.0],
#     "C2": [944.0, 824.0, 704.0, 586.0, 465.0, 344.0, 226.0, 113.0, 113.0],
#     "C3": [944.0, 824.0, 704.0, 586.0, 465.0, 344.0, 226.0, 113.0, 113.0],
#     "C4": [944.0, 824.0, 704.0, 586.0, 465.0, 344.0, 226.0, 113.0, 113.0],
# }

class ROSNode(Node):
    def __init__(self):
        super().__init__('ui_node')

        self.fps_counter = FPSCounter()

        self.depth_data_callback_ui = None 

        self.compensate_update_callback = None

        self.mh2_state_callback_ui = None

        self.height_update_callback = None

        self.forklift_controller = None

        self.di_update_callback = None
        self.do_update_callback = None

        self.current_pose_callback_ui = None

        self.motion_state_callback_ui = None
        
        self.motor_info_update_callback_ui = None

        self.current_motor_len = [10.0, 0.0, 0.0]
        
        self.task_state_callback_ui = None

        self.task_state_rough_align_ui = None
        self.task_state_precise_align_ui = None
        self.task_state_pick_ui = None
        self.task_state_assembly_ui = None
        self.task_state_run_ui = None


        '''Publishers 發布'''

        self.mode_cmd_publisher = self.create_publisher(String, '/mode_cmd', 10)

        self.state_cmd_publisher = self.create_publisher(StateCmd, '/state_cmd', 10)

        self.component_cmd_publisher = self.create_publisher(ComponentCmd, "/component_control_cmd", 10)

        self.motion_cmd_publisher = self.create_publisher(MotionCmd, '/motion_cmd', 10)

        self.task_cmd_publisher = self.create_publisher(TaskCmd, '/task_cmd', 10)

        self.fork_cmd_publisher = self.create_publisher(ForkCmd, '/fork_cmd', 10)

        self.jog_cmd_publisher = self.create_publisher(JogCmd, '/jog_cmd', 10)

        self.component_control_publisher = self.create_publisher(RunCmd, '/run_cmd', 10)

        self.vision_control_publisher = self.create_publisher(String, '/detection_task', 10)

        self.dido_control_publisher = self.create_publisher(DIDOCmd, '/test_dido', 10)

        self.y_motor_cmd_publisher = self.create_publisher(String, '/test_y_motor_cmd', 10)

        self.gripper_cmd_publisher = self.create_publisher(GripperCmd, '/gripper_cmd', 10)

        self.limit_cmd_publisher = self.create_publisher(LimitCmd, "/limit_cmd", 10)  

        self.recipe_publisher = self.create_publisher(Recipe, '/recipe_cmd', 10)



        '''Subscribers 訂閱'''

        self.depth_data_subscriber = self.create_subscription(
            Float32MultiArray,
            "depth_data",
            self.depth_data_callback,
            10
        )

        self.mh2_state_subscriber = self.create_subscription(
            MH2State,
            "mh2_state",
            self.mh2_state_callback,
            10
        )

        self.current_pose_subscriber = self.create_subscription(
            CurrentPose,
            "current_pose",
            self.current_pose_callback,
            10
        )

        self.height_info_subscriber = self.create_subscription(
            Int32,
            'lr_distance',
            self.height_info_callback,
            10
        )

        self.color_image_subscriber = self.create_subscription(
            Image,
            '/color_image',
            self.image_callback,
            10
        )

        self.compensate_pose_subscriber = self.create_subscription(
            Float32MultiArray,
            'compensate_pose',
            self.compensate_pose_callback,
            10
        )

        self.motors_info_sub = self.create_subscription(
            MultipleM,
            '/multi_motor_info',
            self.motors_info_callback,
            10
        )

        self.dido_control_subscriber = self.create_subscription(
            DIDOCmd,
            '/dido_cmd',
            self.dido_callback,
            10
        )

        self.motion_state_subscriber = self.create_subscription(
            MotionState,
            '/motion_state',
            self.motion_state_callback,
            10
        )

        self.task_state_rough_align = self.create_subscription(
            TaskState,
            '/task_state_rough_align',
            self.task_state_rough_align_callback,
            10
        )

        self.task_state_precise_align = self.create_subscription(
            TaskState,
            '/task_state_precise_align',
            self.task_state_precise_align_callback,
            10
        )

        self.task_state_pick = self.create_subscription(
            TaskState,
            '/task_state_pick',
            self.task_state_pick_callback,
            10
        )

        self.task_state_assembly = self.create_subscription(
            TaskState,
            '/task_state_assembly',
            self.task_state_assembly_callback,
            10
        )

        self.task_state_run = self.create_subscription(
            TaskState,
            '/task_state_run',
            self.task_state_run_callback,
            10
        )

        self.bridge = CvBridge()

        self.detection_task_callback_ui = None
        self.image_update_callback = None


    '''Callbacks 回調'''

    def depth_data_callback(self, msg: Float32MultiArray):
        self.get_logger().info(f"Received Depth data: {msg.data}")
        if self.depth_data_callback_ui:
            self.depth_data_callback_ui(list(msg.data))  # hand off to UI

    def mh2_state_callback(self, msg: MH2State):
        self.get_logger().info(f"Received MH2State: \n servo_state: {msg.servo_state} \n alarm_code: {msg.alarm_code}")
        
        if self.mh2_state_callback_ui:
            self.mh2_state_callback_ui(msg)  # hand off to UI layer

    def task_state_rough_align_callback(self, msg: TaskState):
        # msg.mode in {"rough_align","precise_align","pick","assembly","idle", ...}
        # msg.state in {"idle","done","fail", else->running}
        self.get_logger().info(f"[TaskStateRoughAlign] mode={msg.mode} state={msg.state}")
        if self.task_state_rough_align_ui:
            # Push clean strings to UI layer
            try:
                self.task_state_rough_align_ui(str(msg.mode).strip(), str(msg.state).strip())
            except Exception as e:
                self.get_logger().error(f"TaskStateRoughAlign → UI error: {e}")  

    def task_state_precise_align_callback(self, msg: TaskState):
        # msg.mode in {"rough_align","precise_align","pick","assembly","idle", ...}
        # msg.state in {"idle","done","fail", else->running}
        self.get_logger().info(f"[TaskStatePreciseAlign] mode={msg.mode} state={msg.state}")
        if self.task_state_precise_align_ui:
            # Push clean strings to UI layer
            try:
                self.task_state_precise_align_ui(str(msg.mode).strip(), str(msg.state).strip())
            except Exception as e:
                self.get_logger().error(f"TaskStatePreciseAlign → UI error: {e}")        
      
    def task_state_pick_callback(self, msg: TaskState):
        # msg.mode in {"rough_align","precise_align","pick","assembly","idle", ...}
        # msg.state in {"idle","done","fail", else->running}
        self.get_logger().info(f"[TaskStatePick] mode={msg.mode} state={msg.state}")
        if self.task_state_pick_ui:
            # Push clean strings to UI layer
            try:
                self.task_state_pick_ui(str(msg.mode).strip(), str(msg.state).strip())
            except Exception as e:
                self.get_logger().error(f"TaskStatePick → UI error: {e}")    

    def task_state_assembly_callback(self, msg: TaskState):
        # msg.mode in {"rough_align","precise_align","pick","assembly","idle", ...}
        # msg.state in {"idle","done","fail", else->running}
        self.get_logger().info(f"[TaskStateAssembly] mode={msg.mode} state={msg.state}")
        if self.task_state_assembly_ui:
            # Push clean strings to UI layer
            try:
                self.task_state_assembly_ui(str(msg.mode).strip(), str(msg.state).strip())
            except Exception as e:
                self.get_logger().error(f"TaskStateAssembly → UI error: {e}")      
    
    def task_state_run_callback(self, msg: TaskState):
        # msg.mode in {"rough_align","precise_align","pick","assembly","idle", ...}
        # msg.state in {"idle","done","fail", else->running}
        self.get_logger().info(f"[TaskStateRun] mode={msg.mode} state={msg.state}")
        if self.task_state_run_ui:
            # Push clean strings to UI layer
            try:
                self.task_state_run_ui(str(msg.mode).strip(), str(msg.state).strip())
            except Exception as e:
                self.get_logger().error(f"TaskStateRun → UI error: {e}")    

    def current_pose_callback(self, msg: CurrentPose):
        self.get_logger().info(f"Received CurrentPose: \n pose_data: {msg.pose_data}")
        if self.current_pose_callback_ui:
            data = list(msg.pose_data) if hasattr(msg, "pose_data") else []
            while len(data) < 3:
                data.append(0.0)
            self.current_pose_callback_ui(float(data[0]), float(data[1]), float(data[2]))

    def height_info_callback(self, msg: Int32):
        self.get_logger().info(f"Received height info: {msg.data} mm")

        if self.height_update_callback:
            self.height_update_callback(msg.data)

    def compensate_pose_callback(self, msg: Float32MultiArray):
        self.get_logger().info(f"Received compensate_pose: {msg.data}")

        if self.compensate_update_callback:
            self.compensate_update_callback(list(msg.data))

    def motion_state_callback(self, msg: MotionState):
        print(f"[ROS] /motion_state -> init={msg.init_finish}, motion={msg.motion_finish}")
        if self.motion_state_callback_ui:
            self.motion_state_callback_ui(bool(msg.init_finish), bool(msg.motion_finish))

    
    '''Vision 視覺'''

    def image_callback(self, msg):
        self.fps_counter.update() 

        try:
            cv_img = self.bridge.imgmsg_to_cv2(msg, desired_encoding="bgr8")
        except Exception as e:
            self.get_logger().error(f"Failed to convert image: {e}")
            return
        
        # Pass to Qt
        if self.image_update_callback:
            self.image_update_callback(cv_img)

    def detection_task_callback(self, msg: String):
        if self.detection_task_callback_ui:
            self.detection_task_callback_ui(msg.data)

    
    '''Motor 馬達'''

    def motors_info_callback(self, msg: MultipleM):
            m1 = msg.motor_info[0].fb_position
            m2 = msg.motor_info[1].fb_position
            m3 = msg.motor_info[2].fb_position

            if self.motor_info_update_callback_ui:
                # This runs in the ROS thread; it's fine to emit a Qt Signal from here
                # because Qt will queue delivery to the UI thread.
                self.motor_info_update_callback_ui(m1, m2, m3)

    
    '''DI/DO'''

    def dido_callback(self, msg: DIDOCmd):
        name = msg.name.strip().upper()
        state = bool(msg.state)

        if name.startswith("DI"):
            if self.di_update_callback:
                self.di_update_callback(name, state)
        elif name.startswith("DO"):
            if self.do_update_callback:
                self.do_update_callback(name, state)



class MainWindow(QMainWindow):

    '''GUI Threads'''

    task_state_update = Signal(str, str)

    depth_data_update = Signal(float, float)

    compensate_pose_update = Signal(float, float, float)

    mh2_state_update = Signal(bool, int)

    height_update = Signal(int)

    di_update = Signal(str, bool)
    do_update = Signal(str, bool)

    image_update = Signal(object)
    vision_mode_update = Signal(str)

    motion_state_update = Signal(bool, bool)

    current_pose_update = Signal(float, float, float)

    motor_info_update = Signal(float, float, float)


    def __init__(self, ros_node):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle("Magic Cube UI")
        print("No extermal vision controller")

        # shortcut keys
        QShortcut(QKeySequence(Qt.Key_Escape), self, activated=self.close)

        #Scroll
        QScroller.grabGesture(self.ui.ScrollAreaDIDO.viewport(), QScroller.LeftMouseButtonGesture)


        #Start ROS2 Node
        self.ros_node = ros_node

        self._vision_comp = {"x": float('nan'), "y": float('nan'), "yaw": float('nan')}


        #ui_pages.py
        self.ui_pages = PagesControl(self.ui, self.ros_node)

        self.ui_pages.component_cmd_requested.connect(self.send_component_cmd)

        self.ui_pages.run_cmd_requested.connect(self.send_run_cmd)

        #ui_style.py
        self.ui_style = StyleUI(self.ui, self.ros_node)



        #ui_cabinets.py
        self.cabinets_controller = CabinetsController(self.ui, self.ros_node)


        #Circles
        self.task_state_update.connect(self.ui_style.apply_task_state)

        self.ros_node.task_state_rough_align_ui = self.task_state_update.emit

        self.ros_node.task_state_precise_align_ui = self.task_state_update.emit

        self.ros_node.task_state_pick_ui = self.task_state_update.emit

        self.ros_node.task_state_assembly_ui = self.task_state_update.emit

        self.ros_node.task_state_run_ui = self.task_state_update.emit

        #vision ui
        self.ros_node.image_update_callback = self.update_image
        self.ros_node.detection_task_callback_ui = self.update_detection_mode
        # self.vision_controller = VisionController(self.ui, self.ros_node)

        # # Bridge ROS → GUI via signals (thread-safe)
        # self.image_update.connect(self.vision_controller.update_image)
        # self.vision_mode_update.connect(self.vision_controller.update_mode)

        # self.ros_node.image_update_callback = lambda cv: self.image_update.emit(cv)
        # self.ros_node.detection_task_callback_ui = lambda s: self.vision_mode_update.emit(s)

        #depth data
        self.depth_data_update.connect(self.update_depth_label)

        self.ros_node.depth_data_callback_ui = \
            (lambda arr: self.depth_data_update.emit(
                float(arr[0]) if len(arr) > 0 else float('nan'),
                float(arr[1]) if len(arr) > 1 else float('nan'),
            ))
        
        
        #vision compensate pose
        self.compensate_pose_update.connect(self.update_compensate_pose_label)

        self.ros_node.compensate_update_callback = \
            (lambda arr: self.compensate_pose_update.emit(
                float(arr[0]) if len(arr) > 0 else float('nan'),
                float(arr[1]) if len(arr) > 1 else float('nan'),
                float(arr[2] if len(arr) > 2 else float('nan')),
                # float(arr[3] if len(arr) > 3 else float('nan'))
            ))
    

        #motor ui
        self.motor_controller = MotorController(self.ui, self.ros_node)
        self.motor_info_update.connect(self.motor_controller.on_motor_info)
        self.ros_node.motor_info_update_callback_ui = \
            lambda m1, m2, m3: self.motor_info_update.emit(m1, m2, m3)

        self.motion_state_update.connect(self.motor_controller.apply_motion_state)
        self.ros_node.motion_state_callback_ui = self.motion_state_update.emit

        self.mh2_state_update.connect(self.motor_controller._on_mh2_state_ui)
        self.ros_node.mh2_state_callback_ui = \
            (lambda msg: self.mh2_state_update.emit(bool(msg.servo_state), int(msg.alarm_code)))
        
        self.current_pose_update.connect(self.motor_controller.current_pose)
        self.ros_node.current_pose_callback_ui = self.current_pose_update.emit

        # Motor → UI notifier for INIT
        self.motor_controller.init_visual_cb = self.ui_style._handle_init_visual

        #forklift ui
        self.forklift_controller = ForkliftController(self.ui, self.ros_node)
        self.height_update.connect(self.forklift_controller.update_height_display)
        self.ros_node.height_update_callback = lambda v: self.height_update.emit(v)

        #gripper ui
        self.gripper_controller = GripperController(self.ui, self.ros_node)

        #limit ui
        self.limit_controller = LimitController(self.ui, self.ros_node)

        # DI/DO UI Controller
        self.dido_controller = DIDOController(self.ui, self.ros_node)
        
        self.di_update.connect(self.dido_controller.update_di)
        # self.do_update.connect(self.dido_controller.update_do)    

        # Make ROS -> emit the signal instead of touching widgets directly
        self.ros_node.di_update_callback = lambda name, state: self.di_update.emit(name, state)
        # self.ros_node.do_update_callback = lambda name, state: self.do_update.emit(name, state)


        # Get Today's date
        today = date.today()
        formatted_date = today.strftime("%m/%d/%Y")
        self.ui.DateInput.setText(formatted_date)
        

        #Servo Button
        self.ui.ServoONOFFButton.setStyleSheet("""
        QPushButton#ServoONOFFButton {
            color: black;
            border-radius: 8px;
            background-color: #A0A0A0; /* OFF (default) */
        }
        QPushButton#ServoONOFFButton:checked {
            background-color: #4CAF50; /* ON */
        }
        """)

        self.ui.ServoONOFFButton.setCheckable(True)

        self.ui.ServoONOFFButton.clicked.connect(lambda checked: self.on_servo_click(checked))

        # auto
        self.ui.AutoButton.toggled.connect(self.on_auto_toggled)

        self.ui.INITButton.clicked.connect(lambda: self.send_state_cmd("init"))
        self.ui.INITButton.clicked.connect(self.motor_controller.on_init_commanded)

        self.ui.RunButton.clicked.connect(lambda: self.send_state_cmd("run"))

        self.ui.AutoPauseButton.toggled.connect(self.on_pause_toggled)
        self.ui.AutoStopButton.clicked.connect(lambda: self.send_state_cmd("stop"))

        # manual
        self.ui.ManualButton.toggled.connect(self.on_manual_toggled)

        self.ui.RoughAlignButton.toggled.connect(lambda checked: self.on_task_toggled("rough_align", checked))
        self.ui.PreciseAlignButton.toggled.connect(lambda checked: self.on_task_toggled("precise_align", checked))
        self.ui.PickButton.toggled.connect(lambda checked: self.on_task_toggled("pick", checked))
        self.ui.AssemblyButton.toggled.connect(lambda checked: self.on_task_toggled("assembly", checked))  

        # by default
        self.ui.ListOptionsWidget.setVisible(False)

        # Touchscreen style in Main Page - Auto
        self.ui.INITButton.clicked.connect(lambda: self.ui_style.on_touch_different_color(self.ui.INITButton, "#FFB300","#000000", "#000000","#000000"))
        self.ui.RunButton.clicked.connect(lambda: self.ui_style.on_touch_different_color(self.ui.RunButton, "#1E7E34","#000000","#000000","#000000"))
        self.ui.AutoStopButton.clicked.connect(lambda: self.ui_style.on_touch_different_color(self.ui.AutoStopButton, "#990000", "#9A0007", "#D32F2F", "#7F0000"))


        '''Change Pages 切畫面'''

        # Menu
        self.ui.MainPageButton.toggled.connect(self.ui_pages.change_to_main_page)
        self.ui.ComponentControlButton.toggled.connect(self.ui_pages.change_to_component_control_page)

        self.ui.ProductionRecordButton.clicked.connect(self.ui_pages.change_to_production_record_page)
        self.ui.LogsButton.clicked.connect(self.ui_pages.change_to_logs_page)
        self.ui.SystemSettingsButton.clicked.connect(self.ui_pages.change_to_system_settings_page)

        # Main Page - Auto and Manual options
        self.ui.AutoButton.clicked.connect(lambda: self.ui_pages.change_auto_or_manual("Auto", 0))
        self.ui.ManualButton.clicked.connect(lambda: self.ui_pages.change_auto_or_manual("Manual", 1))

        #Component Control Choose Page
        self.ui.ChooseMotor.clicked.connect(lambda: self.ui_pages.component_control_choose_page("Motor", 0))
        self.ui.ChooseVision.clicked.connect(lambda: self.ui_pages.component_control_choose_page("Vision", 1))
        self.ui.ChooseGripper.clicked.connect(lambda: self.ui_pages.component_control_choose_page("Gripper", 2))
        self.ui.ChooseForklift.clicked.connect(lambda: self.ui_pages.component_control_choose_page("Forklift", 3))
        self.ui.ChooseDIDO.clicked.connect(lambda: self.ui_pages.component_control_choose_page("DI/DO", 4))

        #Component Control, List Menu
        self.ui.HamburgerMenu.clicked.connect(self.ui_pages.toggle_menu)

        self.ui.MotorOption.clicked.connect(lambda: self.ui_pages.component_control_switch_page("Motor", 0))
        self.ui.VisionOption.clicked.connect(lambda: self.ui_pages.component_control_switch_page("Vision", 1))
        self.ui.GripperOption.clicked.connect(lambda: self.ui_pages.component_control_switch_page("Gripper", 2))
        self.ui.ForkliftOption.clicked.connect(lambda: self.ui_pages.component_control_switch_page("Forklift", 3))
        self.ui.DIDOOption.clicked.connect(lambda: self.ui_pages.component_control_switch_page("DI/DO", 4))

        #Motor component next
        self.ui.MotorConfigNextButton.clicked.connect(lambda: self.ui_pages.go_to_next_page_motor(1))
        self.ui.MotorJogNextButton.clicked.connect(lambda: self.ui_pages.go_to_next_page_motor(2))
        self.ui.MotorYAxisNextButton.clicked.connect(lambda: self.ui_pages.go_to_next_page_motor(0))

        self.ui.VisionSendButton.clicked.connect(self.send_vision_compensate_pose)

        for btn in self.ui.ManualButtons.buttons():
            btn.toggled.connect(lambda checked, b=btn: self.on_manual_button_toggled(b, checked))

        # after setupUi(...)
        self._vision_buttons = [
            (self.ui.VisionOne,   "screw"),
            (self.ui.VisionTwo,   "l_shape"),
            (self.ui.VisionThree, "icp_fit"),
        ]

        # Make sure they’re checkable and not in an exclusive QButtonGroup
        for btn, mode in self._vision_buttons:
            btn.setCheckable(True)
            # 1) publishing: start/stop per button
            btn.toggled.connect(lambda checked, m=mode: self.on_vision_toggled(m, checked))
            # 2) manual exclusivity: when one is clicked on, turn others off; clicking again turns it off
            btn.clicked.connect(lambda checked, b=btn: self._on_vision_clicked(b, checked))


        QTimer.singleShot(5000, lambda: self.ui_style.add_style(self.ui.StartCircle, "background-color: green;"))
        QTimer.singleShot(10000, lambda: self.ui_style.add_style(self.ui.ConnectCircle, "background-color: green;"))


    def on_servo_click(self, checked: bool):
        btn = self.ui.ServoONOFFButton
        prev = not checked            # this was the state before the click
        desired = checked             # what the user asked for

        # Revert UI until ROS confirms
        btn.blockSignals(True)
        btn.setChecked(prev)          # undo the automatic toggle -> stays gray/green as before
        btn.blockSignals(False)

        # btn.setEnabled(False)         # avoid double clicks
        self.motor_controller.call_servo(desired)


    '''Vision 視覺'''

    def update_image(self, cv_img):
        qt_img = convert_cv_to_qt(cv_img)
        pixmap = QPixmap.fromImage(qt_img)

        current_index = self.ui.ParentStackedWidgetToChangeMenuOptions.currentIndex()

        if current_index == 0:  # Main Page
            self.ui.VisionText.setPixmap(pixmap)
            self.ui.VisionTextInComponentControl.clear()
        elif current_index == 1:  # Component Control
            self.ui.VisionTextInComponentControl.setPixmap(pixmap)
            self.ui.VisionText.clear()
        else:
            self.ui.VisionText.clear()
            self.ui.VisionTextInComponentControl.clear()
            

    def update_detection_mode(self, mode):
        print(f"[UI] Detection mode is now: {mode}")


    def _on_vision_clicked(self, btn, checked):
        if checked:
            # Turn others off (this will trigger their toggled(False) → publish "<mode>_off")
            for other, _ in self._vision_buttons:
                if other is not btn and other.isChecked():
                    other.setChecked(False)
        else:
            # User clicked the same button to turn it off → no mode selected; nothing else to do
            pass


    def on_vision_toggled(self, vision_name, checked):
        if checked:
            self.send_vision_cmd(f"{vision_name}")
            print(f"[UI] {vision_name} started")
        else:
            self.send_vision_cmd(f"{vision_name}_off")
            print(f"[UI] {vision_name} stopped")

    
    '''Calculate and Update 計算和更新'''
    
    def update_depth_label(self, left: float, right: float):
        if math.isnan(left):
            result_left = "-"
        elif left > 1000:
            result_left = "OOR"
        else:
            result_left = f"{left:.2f}"

        self.ui.CartDepthLeftInput.setText(f"L: {result_left}")
        self.ui.LeftDepthText.setText(result_left)

        if math.isnan(right):
            result_right = "-"
        elif right > 1000:
            result_right = "OOR"
        else:
            result_right = f"{right:.2f}"

        self.ui.CartDepthRightInput.setText(f"R: {result_right}")
        self.ui.RightDepthText.setText(result_right)


    def update_compensate_pose_label(self, x: float, y: float, yaw: float):
        self._vision_comp["x"] = x
        self._vision_comp["y"] = y
        self._vision_comp["yaw"] = yaw
        # self._vision_comp["z"]  = z

        self.ui.xVisionLabel.setText("-" if math.isnan(x) else f"{x:.2f}")
        self.ui.yVisionLabel.setText("-" if math.isnan(y) else f"{y:.2f}")
        self.ui.YawVisionLabel.setText("-" if math.isnan(yaw) else f"{yaw:.2f}")
        # self.ui.zVisionLabel.setText("-" if z != z else f"{z:.2f}")


    '''Send publishers 發送發布'''

    def send_run_cmd(self, flag):
        msg = RunCmd()

        # msg.main_page = False
        msg.mode = flag
        
        print(f"[DEBUG] Publishing RunCmd: {msg}")
        self.ros_node.component_control_publisher.publish(msg)
        print(f"[UI] Sent RunCmd: {flag}")


    def on_manual_toggled(self, checked: bool):
        if checked:
            self.send_run_cmd("manual")
            # if not self._any_manual_task_active():
            #     self.ui.MainPageAutoAndManualStackedWidget.setCurrentIndex(0)
        else:
            self.send_task_cmd("idle")


    def on_auto_toggled(self, checked):
        if checked:
            self.send_run_cmd("auto")
            # self.ui.MainPageAutoAndManualStackedWidget.setCurrentIndex(1)
        else:
            self.send_task_cmd("idle")


    def on_pause_toggled(self, checked):
        if checked:
            # Button is pressed → machine should pause
            self.send_state_cmd("pause")
            
            self.ui.AutoPauseButton.setText("Paused")

            print("[UI] Pause engaged")
        else:
            # Button released → machine should resume running
            self.send_state_cmd("run")

            self.ui.AutoPauseButton.setText("Pause")

            print("[UI] Pause released, resuming run")


    def on_task_toggled(self, task_name, checked):
        if checked:
            self.send_task_cmd(task_name)
            print(f"[UI] {task_name} started")
        else:
            # Since buttons are exclusive, unchecking means no task is active
            # Optional: send a stop/idle command
            self.send_task_cmd("idle")
            print(f"[UI] {task_name} stopped")


    def send_state_cmd(self, flag):
        msg = StateCmd()

        # Reset all flags
        msg.init_button = False
        msg.run_button = False
        msg.pause_button = False
        msg.stop_button = False

        if flag == "init":
            msg.init_button = True
        elif flag == "run":
            msg.run_button = True

        elif flag == "pause":
            msg.pause_button = True
        elif flag == "stop":
            msg.stop_button = True

        # print(f"[DEBUG] Publishing StateCmd: {msg}")
        self.ros_node.state_cmd_publisher.publish(msg)
        print(f"[UI] Sent StateCmd: {flag}")


    def send_task_cmd(self, flag):
        msg = TaskCmd()
        msg.mode = flag
        
        self.ros_node.task_cmd_publisher.publish(msg)
        print(f"[UI] Sent TaskCmd: {msg.mode}")


    def send_component_cmd(self, flag):
        msg = ComponentCmd()
        msg.mode = flag

        self.ros_node.component_cmd_publisher.publish(msg)
        print(f"[UI] Sent ComponentCmd: {msg.mode}")


    def send_jog_cmd(self, axis, direction):
        msg = JogCmd()
        msg.target = axis
        msg.direction = direction  # 1.0 for + direction, -1.0 for - direction
        msg.distance = 5.0         # fixed distance
        msg.speed = 50.0           # fixed speed
        self.ros_node.jog_cmd_publisher.publish(msg)
        print(f"[UI] Sent JogCmd: axis={axis}, direction={direction}")

    def send_vision_cmd(self, mode):
        print(f"[DEBUG] Trying to publish: {mode}")  

        if hasattr(self, 'last_vision_mode') and self.last_vision_mode == mode:
            return
        self.last_vision_mode = mode
        msg = String()
        msg.data = mode
        self.ros_node.vision_control_publisher.publish(msg)
        print(f"[UI] Sent VisionCmd: {mode}")

    def send_vision_compensate_pose(self):
        x = self._vision_comp["x"]
        y = self._vision_comp["y"]
        yaw = self._vision_comp["yaw"]
        # z = self._vision_comp["z"]

        # Guard: don’t send if any value is NaN
        if any(math.isnan(v) for v in (x, y, yaw)):
            print("[Vision] compensate_pose has NaN; not sending MotionCmd.")
            return

        msg = MotionCmd()
        msg.command_type = MotionCmd.TYPE_GOTO
        msg.pose_data = [x, y, yaw]
        msg.speed = 5.0
        self.ros_node.motion_cmd_publisher.publish(msg)
        print(f"[Vision] Sent MotionCmd → pose:{msg.pose_data} speed:{msg.speed}")



    '''Config button states 按鈕設定狀態'''
    
    def on_manual_button_toggled(self, button, checked):
        if checked:
            for other in self.ui.ManualButtons.buttons():
                if other != button:
                    other.setChecked(False)

  
    def _manual_task_buttons(self):
    # Add any other manual-task buttons here
        return [
            self.ui.RoughAlignButton,
            self.ui.PreciseAlignButton,
            self.ui.PickButton,
            self.ui.AssemblyButton,
        ]

    def _any_manual_task_active(self) -> bool:
        return any(btn.isChecked() for btn in self._manual_task_buttons())


    #Component Control - Motor
    def toggle_menu(self):
        self.ui.ListOptionsWidget.setVisible(not self.ui.ListOptionsWidget.isVisible())


    '''Helper functions 輔助函數'''

    def move_to_second_screen_and_fullscreen(self):
        screens = QApplication.screens()
        if len(screens) > 1:
            second_screen = screens[1]  # Use the actual second screen
            second_geom = second_screen.geometry()
            self.setGeometry(second_geom)  # Move and resize in one step
            # self.setMaximumWidth(1280)
            # self.setMaximumHeight(800)
            # print("Fixed size: 1280 x 800")
            self.showFullScreen()
        else:
            self.showMaximized()
            print("Only one screen, screen fullscreen anyways")

    def closeEvent(self, event):
        self.ros_node.destroy_node()
        rclpy.shutdown()
        event.accept()


'''Helper functions 輔助函數'''

def convert_cv_to_qt(cv_img):
    rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
    h, w, ch = rgb_image.shape
    bytes_per_line = ch * w
    return QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)


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

