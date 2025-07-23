import sys
from PySide6.QtCore import Qt, QEvent, QTimer
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from ui_magic_cube_columns_timeline import Ui_MainWindow
import resources_rc  # this includes the images

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #self.showFullScreen()

        screens = QApplication.screens()
        if len(screens) > 1:
            second_screen = screens[1]
            self.move(second_screen.geometry().topLeft())  # move to 2nd screen
            self.showFullScreen()
            print("full screen")
        else:
            self.showMaximized()
            print("screen maximized")

        #for touchscreens style (ActionButtons)
        self.ui.InitButton.clicked.connect(lambda: self.on_menu_buttons_clicked(self.ui.InitButton))
        self.ui.RunButton.clicked.connect(lambda: self.on_menu_buttons_clicked(self.ui.RunButton))
        self.ui.StopButton.clicked.connect(lambda: self.on_menu_buttons_clicked(self.ui.StopButton))
        self.ui.ResetButton.clicked.connect(lambda: self.on_menu_buttons_clicked(self.ui.ResetButton))

        #for touchscreens style (ControlButton)
        self.ui.ControlUp.clicked.connect(lambda: self.on_control_arrows_clicked(self.ui.ControlUp))
        self.ui.ControlLeft.clicked.connect(lambda: self.on_control_arrows_clicked(self.ui.ControlLeft))
        self.ui.ControlDown.clicked.connect(lambda: self.on_control_arrows_clicked(self.ui.ControlDown))
        self.ui.ControlRight.clicked.connect(lambda: self.on_control_arrows_clicked(self.ui.ControlRight))
        self.ui.YawPlus.clicked.connect(lambda: self.on_control_arrows_clicked(self.ui.YawPlus))
        self.ui.YawMinus.clicked.connect(lambda: self.on_control_arrows_clicked(self.ui.YawMinus))

        #for touchscreen style (RecordDataButton)
        self.ui.RecordDataButton.clicked.connect(lambda: self.on_record_data_clicked(self.ui.RecordDataButton))

        #Clipper ON and OFF
        self.ui.ClipperButton.toggled.connect(lambda: self.update_clipper_state(self.ui.ClipperButton))
        
        #change auto | manual page
        self.ui.AutoButton.clicked.connect(self.change_auto_page)
        self.ui.ManualButton.clicked.connect(self.change_manual_page)

        #change to another menu page
        self.ui.MainPageButton.clicked.connect(self.change_to_main_page)
        self.ui.ProductionRecordButton.clicked.connect(self.change_to_production_record_page)
        self.ui.ComponentControlButton.clicked.connect(self.change_to_component_control_page)
        self.ui.LogsButton.clicked.connect(self.change_to_logs_page)
        self.ui.SystemSettingsButton.clicked.connect(self.change_to_system_settings_page)

        #change of Component Control -> Motor | Vision | Clipper
        self.ui.MotorPageButton.clicked.connect(self.change_to_motor_page)
        self.ui.VisionPageButton.clicked.connect(self.change_to_vision_page)
        self.ui.ClipperPageButton.clicked.connect(self.change_to_clipper_page)

    #clipper button state
    def update_clipper_state(self, button):
        if button.isChecked():
            button.setText("Clipper ON")
        else:
            button.setText("Clipper OFF")

    
    #change pages
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


    #Design for touchscreen
    def on_menu_buttons_clicked(self, buttonName):
        buttonName.setStyleSheet("""
        QPushButton {
            background-color: #0B76A0;
            color:White;
            padding: 5px;                                
        }
        """)

        QTimer.singleShot(150, lambda: buttonName.setStyleSheet("""                                         
        QPushButton {
            color:white;
            padding:5px;                                                               
        }
        """))

        
    def on_control_arrows_clicked(self, buttonName):
        buttonName.setStyleSheet("""
        QPushButton {
            background-color: #0B76A0;
            color:White;                                
        }
        """)

        QTimer.singleShot(150, lambda: buttonName.setStyleSheet("""                                         
        QPushButton {
            background-color:none;
            color:white;                                                           
        }
        """))

    def on_record_data_clicked(self, buttonName):
        buttonName.setStyleSheet("""
        QPushButton {
            background-color: #0B76A0;
            color:White;  
            padding: 16px 24px;                           
        }
        """)

        QTimer.singleShot(150, lambda: buttonName.setStyleSheet("""                                         
        QPushButton {
            color:white;     
            padding: 16px 24px;                                                        
        }
        """))

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
