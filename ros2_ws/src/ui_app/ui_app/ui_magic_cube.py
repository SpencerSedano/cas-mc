# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_magic_cube.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QButtonGroup, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QSlider, QStackedWidget, QTabWidget,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 800)
        MainWindow.setMouseTracking(False)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet(u"background-color: #0E3D52;")
        self.horizontalLayout_4 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.BackgroundWidget = QWidget(self.centralwidget)
        self.BackgroundWidget.setObjectName(u"BackgroundWidget")
        self.BackgroundWidget.setEnabled(True)
        self.BackgroundWidget.setStyleSheet(u"")
        self.SystemSettingsButton = QPushButton(self.BackgroundWidget)
        self.MenuButtonGroup = QButtonGroup(MainWindow)
        self.MenuButtonGroup.setObjectName(u"MenuButtonGroup")
        self.MenuButtonGroup.addButton(self.SystemSettingsButton)
        self.SystemSettingsButton.setObjectName(u"SystemSettingsButton")
        self.SystemSettingsButton.setGeometry(QRect(10, 680, 223, 94))
        font = QFont()
        font.setPointSize(12)
        self.SystemSettingsButton.setFont(font)
        self.SystemSettingsButton.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.SystemSettingsButton.setStyleSheet(u"QPushButton {\n"
"    padding: 6px 12px;\n"
"    background-color: qlineargradient(\n"
"        x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #1a1a1a, stop:1 #000000\n"
"    );\n"
"    color: white;\n"
"    border: 1px solid #444;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: qlineargradient(\n"
"        x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #2a2a2a, stop:1 #111111\n"
"    );\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(\n"
"        x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #0f0f0f, stop:1 #000000\n"
"    );\n"
"    border-style: inset;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: #0B76A0;\n"
"    border: 1px solid #0B76A0;\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u"icons/white/settings.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.SystemSettingsButton.setIcon(icon)
        self.SystemSettingsButton.setCheckable(True)
        self.SignalLightsWidget = QWidget(self.BackgroundWidget)
        self.SignalLightsWidget.setObjectName(u"SignalLightsWidget")
        self.SignalLightsWidget.setGeometry(QRect(10, 90, 221, 81))
        self.SignalLightsWidget.setStyleSheet(u"background-color:#000000; ")
        self.horizontalLayout = QHBoxLayout(self.SignalLightsWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(22, 22, 22, 22)
        self.RedSignal = QLabel(self.SignalLightsWidget)
        self.RedSignal.setObjectName(u"RedSignal")
        self.RedSignal.setMaximumSize(QSize(30, 30))
        self.RedSignal.setStyleSheet(u"background-color: #660000; border-radius: 10px;")

        self.horizontalLayout.addWidget(self.RedSignal)

        self.YellowSignal = QLabel(self.SignalLightsWidget)
        self.YellowSignal.setObjectName(u"YellowSignal")
        self.YellowSignal.setMaximumSize(QSize(30, 30))
        self.YellowSignal.setStyleSheet(u"background-color: #666633; border-radius: 10px;")

        self.horizontalLayout.addWidget(self.YellowSignal)

        self.GreenSignal = QLabel(self.SignalLightsWidget)
        self.GreenSignal.setObjectName(u"GreenSignal")
        self.GreenSignal.setMaximumSize(QSize(30, 30))
        self.GreenSignal.setStyleSheet(u"background-color: #6FCF53; border-radius: 10px;")

        self.horizontalLayout.addWidget(self.GreenSignal)

        self.Line = QFrame(self.BackgroundWidget)
        self.Line.setObjectName(u"Line")
        self.Line.setGeometry(QRect(0, 74, 1271, 16))
        self.Line.setStyleSheet(u"border-top: 1px solid white;")
        self.Line.setFrameShape(QFrame.Shape.HLine)
        self.Line.setFrameShadow(QFrame.Shadow.Plain)
        self.Line.setLineWidth(1)
        self.DeltaLogo = QLabel(self.BackgroundWidget)
        self.DeltaLogo.setObjectName(u"DeltaLogo")
        self.DeltaLogo.setGeometry(QRect(20, 20, 131, 41))
        self.DeltaLogo.setPixmap(QPixmap(u"images/delta-logo.png"))
        self.DeltaLogo.setScaledContents(True)
        self.MenuButtons = QWidget(self.BackgroundWidget)
        self.MenuButtons.setObjectName(u"MenuButtons")
        self.MenuButtons.setGeometry(QRect(10, 180, 241, 481))
        self.verticalLayout_11 = QVBoxLayout(self.MenuButtons)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.ParentStackedWidgetToChangeMenuOptions = QStackedWidget(self.BackgroundWidget)
        self.ParentStackedWidgetToChangeMenuOptions.setObjectName(u"ParentStackedWidgetToChangeMenuOptions")
        self.ParentStackedWidgetToChangeMenuOptions.setGeometry(QRect(250, 80, 1011, 691))
        self.ParentStackedWidgetToChangeMenuOptions.setStyleSheet(u"QPushButton {\n"
"    padding: 6px 12px;\n"
"    background-color: qlineargradient(\n"
"        x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #1a1a1a, stop:1 #000000\n"
"    );\n"
"    color: white;\n"
"    border: 1px solid #444;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: qlineargradient(\n"
"        x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #2a2a2a, stop:1 #111111\n"
"    );\n"
"}")
        self.MainPagePage = QWidget()
        self.MainPagePage.setObjectName(u"MainPagePage")
        self.CameraWidget = QWidget(self.MainPagePage)
        self.CameraWidget.setObjectName(u"CameraWidget")
        self.CameraWidget.setGeometry(QRect(0, 0, 701, 491))
        self.CameraWidget.setStyleSheet(u"background-color: #000000;")
        self.horizontalLayout_2 = QHBoxLayout(self.CameraWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.VisionText = QLabel(self.CameraWidget)
        self.VisionText.setObjectName(u"VisionText")
        self.VisionText.setStyleSheet(u"color:white;")
        self.VisionText.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.VisionText, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.AutoManualButtons = QWidget(self.MainPagePage)
        self.AutoManualButtons.setObjectName(u"AutoManualButtons")
        self.AutoManualButtons.setGeometry(QRect(720, 0, 281, 101))
        self.horizontalLayout_5 = QHBoxLayout(self.AutoManualButtons)
        self.horizontalLayout_5.setSpacing(25)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.AutoButton = QPushButton(self.AutoManualButtons)
        self.AutoAndManualButtonGroup = QButtonGroup(MainWindow)
        self.AutoAndManualButtonGroup.setObjectName(u"AutoAndManualButtonGroup")
        self.AutoAndManualButtonGroup.addButton(self.AutoButton)
        self.AutoButton.setObjectName(u"AutoButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AutoButton.sizePolicy().hasHeightForWidth())
        self.AutoButton.setSizePolicy(sizePolicy)
        self.AutoButton.setFont(font)
        self.AutoButton.setStyleSheet(u"QPushButton {\n"
"    padding: 6px 12px;\n"
"    background-color: qlineargradient(\n"
"        x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #1a1a1a, stop:1 #000000\n"
"    );\n"
"    color: white;\n"
"    border: 1px solid #444;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: qlineargradient(\n"
"        x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #2a2a2a, stop:1 #111111\n"
"    );\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(\n"
"        x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #0f0f0f, stop:1 #000000\n"
"    );\n"
"    border-style: inset;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: #0B76A0;\n"
"    border: 1px solid #0B76A0;\n"
"}\n"
"")
        self.AutoButton.setCheckable(True)
        self.AutoButton.setChecked(True)

        self.horizontalLayout_5.addWidget(self.AutoButton)

        self.ManualButton = QPushButton(self.AutoManualButtons)
        self.AutoAndManualButtonGroup.addButton(self.ManualButton)
        self.ManualButton.setObjectName(u"ManualButton")
        sizePolicy.setHeightForWidth(self.ManualButton.sizePolicy().hasHeightForWidth())
        self.ManualButton.setSizePolicy(sizePolicy)
        self.ManualButton.setFont(font)
        self.ManualButton.setStyleSheet(u"QPushButton {\n"
"    padding: 6px 12px;\n"
"    background-color: qlineargradient(\n"
"        x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #1a1a1a, stop:1 #000000\n"
"    );\n"
"    color: white;\n"
"    border: 1px solid #444;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: qlineargradient(\n"
"        x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #2a2a2a, stop:1 #111111\n"
"    );\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(\n"
"        x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #0f0f0f, stop:1 #000000\n"
"    );\n"
"    border-style: inset;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: #0B76A0;\n"
"    border: 1px solid #0B76A0;\n"
"}\n"
"")
        self.ManualButton.setCheckable(True)

        self.horizontalLayout_5.addWidget(self.ManualButton)

        self.ActionButtons = QStackedWidget(self.MainPagePage)
        self.ActionButtons.setObjectName(u"ActionButtons")
        self.ActionButtons.setGeometry(QRect(710, 110, 291, 581))
        self.ActionButtons.setStyleSheet(u"")
        self.ActionButtonsPage = QWidget()
        self.ActionButtonsPage.setObjectName(u"ActionButtonsPage")
        self.verticalLayout_12 = QVBoxLayout(self.ActionButtonsPage)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.InitButton = QPushButton(self.ActionButtonsPage)
        self.InitButton.setObjectName(u"InitButton")
        sizePolicy.setHeightForWidth(self.InitButton.sizePolicy().hasHeightForWidth())
        self.InitButton.setSizePolicy(sizePolicy)
        self.InitButton.setFont(font)
        self.InitButton.setStyleSheet(u"QPushButton {\n"
"    padding: 6px 12px;\n"
"    background-color: qlineargradient(\n"
"        x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #1a1a1a, stop:1 #000000\n"
"    );\n"
"    color: white;\n"
"    border: 1px solid #444;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: qlineargradient(\n"
"        x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #2a2a2a, stop:1 #111111\n"
"    );\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(\n"
"        x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #0f0f0f, stop:1 #000000\n"
"    );\n"
"    border-style: inset;\n"
"	background-color: #0B76A0;\n"
"}")
        self.InitButton.setCheckable(False)

        self.verticalLayout_12.addWidget(self.InitButton)

        self.RunButton = QPushButton(self.ActionButtonsPage)
        self.RunButton.setObjectName(u"RunButton")
        sizePolicy.setHeightForWidth(self.RunButton.sizePolicy().hasHeightForWidth())
        self.RunButton.setSizePolicy(sizePolicy)
        self.RunButton.setFont(font)
        self.RunButton.setStyleSheet(u"QPushButton {\n"
"    padding: 6px 12px;\n"
"    background-color: qlineargradient(\n"
"        x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #1a1a1a, stop:1 #000000\n"
"    );\n"
"    color: white;\n"
"    border: 1px solid #444;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: qlineargradient(\n"
"        x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #2a2a2a, stop:1 #111111\n"
"    );\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(\n"
"        x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #0f0f0f, stop:1 #000000\n"
"    );\n"
"    border-style: inset;\n"
"	background-color: #0B76A0;\n"
"}\n"
"\n"
"\n"
"\n"
"")

        self.verticalLayout_12.addWidget(self.RunButton)

        self.StopButton = QPushButton(self.ActionButtonsPage)
        self.StopButton.setObjectName(u"StopButton")
        sizePolicy.setHeightForWidth(self.StopButton.sizePolicy().hasHeightForWidth())
        self.StopButton.setSizePolicy(sizePolicy)
        self.StopButton.setFont(font)
        self.StopButton.setStyleSheet(u"QPushButton {\n"
"    padding: 6px 12px;\n"
"    background-color: qlineargradient(\n"
"        x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #1a1a1a, stop:1 #000000\n"
"    );\n"
"    color: white;\n"
"    border: 1px solid #444;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: qlineargradient(\n"
"        x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #2a2a2a, stop:1 #111111\n"
"    );\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(\n"
"        x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #0f0f0f, stop:1 #000000\n"
"    );\n"
"    border-style: inset;\n"
"	background-color: #0B76A0;\n"
"}\n"
"\n"
"\n"
"\n"
"")

        self.verticalLayout_12.addWidget(self.StopButton)

        self.AutoResetButton = QPushButton(self.ActionButtonsPage)
        self.AutoResetButton.setObjectName(u"AutoResetButton")
        sizePolicy.setHeightForWidth(self.AutoResetButton.sizePolicy().hasHeightForWidth())
        self.AutoResetButton.setSizePolicy(sizePolicy)
        self.AutoResetButton.setFont(font)
        self.AutoResetButton.setStyleSheet(u"QPushButton {\n"
"    padding: 6px 12px;\n"
"    background-color: qlineargradient(\n"
"        x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #1a1a1a, stop:1 #000000\n"
"    );\n"
"    color: white;\n"
"    border: 1px solid #444;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: qlineargradient(\n"
"        x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #2a2a2a, stop:1 #111111\n"
"    );\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(\n"
"        x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #0f0f0f, stop:1 #000000\n"
"    );\n"
"    border-style: inset;\n"
"	background-color: #0B76A0;\n"
"}\n"
"\n"
"")

        self.verticalLayout_12.addWidget(self.AutoResetButton)

        self.ActionButtons.addWidget(self.ActionButtonsPage)
        self.ControlsPage = QWidget()
        self.ControlsPage.setObjectName(u"ControlsPage")
        self.ControlsPage.setStyleSheet(u"")
        self.ManualOptionsWidget = QTabWidget(self.ControlsPage)
        self.ManualOptionsWidget.setObjectName(u"ManualOptionsWidget")
        self.ManualOptionsWidget.setGeometry(QRect(0, 0, 291, 581))
        self.ManualOptionsWidget.setStyleSheet(u"QTabWidget::pane {\n"
"    border: 1px solid #CCCCCC;\n"
"    background: white;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    background: #E0E0E0;\n"
"    border: 1px solid #CCCCCC;\n"
"    padding: 12px 24px;       /* bigger padding for touch */\n"
"    border-bottom-left-radius: 15px;\n"
"    border-bottom-right-radius: 15px;\n"
"    /* Remove min-width to allow expanding */\n"
"    min-width: 0;\n"
"    /* Allow tabs to expand equally */\n"
"    width: 125%;\n"
"	height: 42px;\n"
"    font-size: 18px;    /* bigger font */\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background: #FFFFFF;\n"
"    border-top-color: white;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QTabBar::tab:hover {\n"
"    background: #F5F5F5;\n"
"}\n"
"\n"
"QTabBar::scroller {\n"
"	width: 100px;\n"
"}\n"
"\n"
"")
        self.ManualOptionsWidget.setTabPosition(QTabWidget.TabPosition.South)
        self.ManualOptionsWidget.setElideMode(Qt.TextElideMode.ElideNone)
        self.ManualOptionsWidget.setDocumentMode(True)
        self.ManualOptionsWidget.setTabsClosable(False)
        self.ManualOptionsWidget.setMovable(False)
        self.ManualAlignTab = QWidget()
        self.ManualAlignTab.setObjectName(u"ManualAlignTab")
        self.ManualOptionsWidget.addTab(self.ManualAlignTab, "")
        self.AutoAlignTab = QWidget()
        self.AutoAlignTab.setObjectName(u"AutoAlignTab")
        self.ManualOptionsWidget.addTab(self.AutoAlignTab, "")
        self.AutoPickTab = QWidget()
        self.AutoPickTab.setObjectName(u"AutoPickTab")
        self.ManualOptionsWidget.addTab(self.AutoPickTab, "")
        self.AutoAssemblyTab = QWidget()
        self.AutoAssemblyTab.setObjectName(u"AutoAssemblyTab")
        self.ManualOptionsWidget.addTab(self.AutoAssemblyTab, "")
        self.ControlTab = QWidget()
        self.ControlTab.setObjectName(u"ControlTab")
        self.YawMinus = QPushButton(self.ControlTab)
        self.YawMinus.setObjectName(u"YawMinus")
        self.YawMinus.setGeometry(QRect(0, 190, 101, 91))
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.YawMinus.sizePolicy().hasHeightForWidth())
        self.YawMinus.setSizePolicy(sizePolicy1)
        self.YawMinus.setStyleSheet(u"QPushButton {\n"
"	background-color:none;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #0B76A0;  /* when button is being pressed */\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u"controlArrows/yaw-.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.YawMinus.setIcon(icon1)
        self.YawMinus.setIconSize(QSize(80, 80))
        self.YawMinus.setCheckable(False)
        self.ControlRight = QPushButton(self.ControlTab)
        self.ControlRight.setObjectName(u"ControlRight")
        self.ControlRight.setGeometry(QRect(200, 100, 101, 91))
        self.ControlRight.setStyleSheet(u"QPushButton {\n"
"	background-color:none;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #0B76A0;  /* when button is being pressed */\n"
"}\n"
"")
        icon2 = QIcon()
        icon2.addFile(u"controlArrows/cartesian/right.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.ControlRight.setIcon(icon2)
        self.ControlRight.setIconSize(QSize(80, 80))
        self.ControlUp = QPushButton(self.ControlTab)
        self.ControlUp.setObjectName(u"ControlUp")
        self.ControlUp.setGeometry(QRect(100, 10, 101, 91))
        sizePolicy1.setHeightForWidth(self.ControlUp.sizePolicy().hasHeightForWidth())
        self.ControlUp.setSizePolicy(sizePolicy1)
        self.ControlUp.setStyleSheet(u"QPushButton {\n"
"	background-color:none;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #0B76A0;  /* when button is being pressed */\n"
"}\n"
"")
        icon3 = QIcon()
        icon3.addFile(u"controlArrows/cartesian/up.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.ControlUp.setIcon(icon3)
        self.ControlUp.setIconSize(QSize(80, 80))
        self.ControlDown = QPushButton(self.ControlTab)
        self.ControlDown.setObjectName(u"ControlDown")
        self.ControlDown.setGeometry(QRect(100, 190, 101, 91))
        self.ControlDown.setStyleSheet(u"QPushButton {\n"
"	background-color:none;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #0B76A0;  /* when button is being pressed */\n"
"}\n"
"")
        icon4 = QIcon()
        icon4.addFile(u"controlArrows/cartesian/down.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.ControlDown.setIcon(icon4)
        self.ControlDown.setIconSize(QSize(80, 80))
        self.YawPlus = QPushButton(self.ControlTab)
        self.YawPlus.setObjectName(u"YawPlus")
        self.YawPlus.setGeometry(QRect(200, 10, 101, 91))
        sizePolicy1.setHeightForWidth(self.YawPlus.sizePolicy().hasHeightForWidth())
        self.YawPlus.setSizePolicy(sizePolicy1)
        self.YawPlus.setStyleSheet(u"QPushButton {\n"
"	background-color:none;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #0B76A0;  /* when button is being pressed */\n"
"}\n"
"")
        icon5 = QIcon()
        icon5.addFile(u"controlArrows/yaw+.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.YawPlus.setIcon(icon5)
        self.YawPlus.setIconSize(QSize(80, 80))
        self.ControlLeft = QPushButton(self.ControlTab)
        self.ControlLeft.setObjectName(u"ControlLeft")
        self.ControlLeft.setGeometry(QRect(0, 100, 101, 91))
        self.ControlLeft.setStyleSheet(u"QPushButton {\n"
"	background-color:none;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #0B76A0;  /* when button is being pressed */\n"
"}\n"
"")
        icon6 = QIcon()
        icon6.addFile(u"controlArrows/cartesian/left.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.ControlLeft.setIcon(icon6)
        self.ControlLeft.setIconSize(QSize(80, 80))
        self.ClipperAndResetWidget = QWidget(self.ControlTab)
        self.ClipperAndResetWidget.setObjectName(u"ClipperAndResetWidget")
        self.ClipperAndResetWidget.setGeometry(QRect(0, 430, 291, 71))
        self.horizontalLayout_19 = QHBoxLayout(self.ClipperAndResetWidget)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.ManualResetButton = QPushButton(self.ClipperAndResetWidget)
        self.ManualResetButton.setObjectName(u"ManualResetButton")
        sizePolicy.setHeightForWidth(self.ManualResetButton.sizePolicy().hasHeightForWidth())
        self.ManualResetButton.setSizePolicy(sizePolicy)
        self.ManualResetButton.setFont(font)
        self.ManualResetButton.setStyleSheet(u"QPushButton {\n"
"    padding: 6px 12px;\n"
"    background-color: qlineargradient(\n"
"        x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #1a1a1a, stop:1 #000000\n"
"    );\n"
"    color: white;\n"
"    border: 1px solid #444;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: qlineargradient(\n"
"        x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #2a2a2a, stop:1 #111111\n"
"    );\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(\n"
"        x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #0f0f0f, stop:1 #000000\n"
"    );\n"
"    border-style: inset;\n"
"	background-color: #0B76A0;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_19.addWidget(self.ManualResetButton)

        self.ClipperButton = QPushButton(self.ClipperAndResetWidget)
        self.ClipperButton.setObjectName(u"ClipperButton")
        self.ClipperButton.setEnabled(True)
        sizePolicy.setHeightForWidth(self.ClipperButton.sizePolicy().hasHeightForWidth())
        self.ClipperButton.setSizePolicy(sizePolicy)
        self.ClipperButton.setFont(font)
        self.ClipperButton.setStyleSheet(u"QPushButton {\n"
"    padding: 6px 12px;\n"
"    background-color: qlineargradient(\n"
"        x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #1a1a1a, stop:1 #000000\n"
"    );\n"
"    color: white;\n"
"    border: 1px solid #444;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: qlineargradient(\n"
"        x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #2a2a2a, stop:1 #111111\n"
"    );\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: #0B76A0;\n"
"    border: 1px solid #0B76A0;\n"
"}\n"
"\n"
"")
        self.ClipperButton.setCheckable(True)

        self.horizontalLayout_19.addWidget(self.ClipperButton)

        self.Lift = QPushButton(self.ControlTab)
        self.Lift.setObjectName(u"Lift")
        self.Lift.setGeometry(QRect(10, 320, 101, 91))
        sizePolicy1.setHeightForWidth(self.Lift.sizePolicy().hasHeightForWidth())
        self.Lift.setSizePolicy(sizePolicy1)
        self.Lift.setStyleSheet(u"QPushButton {\n"
"	background-color:none;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #0B76A0;  /* when button is being pressed */\n"
"}\n"
"")
        icon7 = QIcon()
        icon7.addFile(u"controlArrows/lift.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Lift.setIcon(icon7)
        self.Lift.setIconSize(QSize(80, 80))
        self.Lower = QPushButton(self.ControlTab)
        self.Lower.setObjectName(u"Lower")
        self.Lower.setGeometry(QRect(190, 320, 101, 91))
        sizePolicy1.setHeightForWidth(self.Lower.sizePolicy().hasHeightForWidth())
        self.Lower.setSizePolicy(sizePolicy1)
        self.Lower.setStyleSheet(u"QPushButton {\n"
"	background-color:none;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #0B76A0;  /* when button is being pressed */\n"
"}\n"
"")
        icon8 = QIcon()
        icon8.addFile(u"controlArrows/lower.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Lower.setIcon(icon8)
        self.Lower.setIconSize(QSize(80, 80))
        self.ManualOptionsWidget.addTab(self.ControlTab, "")
        self.ActionButtons.addWidget(self.ControlsPage)
        self.ProcessAndInfoStackedWidget = QStackedWidget(self.MainPagePage)
        self.ProcessAndInfoStackedWidget.setObjectName(u"ProcessAndInfoStackedWidget")
        self.ProcessAndInfoStackedWidget.setGeometry(QRect(0, 500, 701, 191))
        self.ProcessAndInfoStackedWidget.setStyleSheet(u" background-color: #000000; color: white;")
        self.AutoProcessPage = QWidget()
        self.AutoProcessPage.setObjectName(u"AutoProcessPage")
        self.AutoProcessPage.setStyleSheet(u"")
        self.horizontalLayout_6 = QHBoxLayout(self.AutoProcessPage)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.Timeline = QFrame(self.AutoProcessPage)
        self.Timeline.setObjectName(u"Timeline")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.Timeline.sizePolicy().hasHeightForWidth())
        self.Timeline.setSizePolicy(sizePolicy2)
        self.Timeline.setStyleSheet(u"")
        self.Timeline.setFrameShape(QFrame.Shape.StyledPanel)
        self.Timeline.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.Timeline)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.StartWidget = QWidget(self.Timeline)
        self.StartWidget.setObjectName(u"StartWidget")
        self.verticalLayout_2 = QVBoxLayout(self.StartWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.StartText = QLabel(self.StartWidget)
        self.StartText.setObjectName(u"StartText")
        self.StartText.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.StartText)

        self.StartCircle = QLabel(self.StartWidget)
        self.StartCircle.setObjectName(u"StartCircle")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.StartCircle.sizePolicy().hasHeightForWidth())
        self.StartCircle.setSizePolicy(sizePolicy3)
        self.StartCircle.setPixmap(QPixmap(u"icons/white/timeline-circle.svg"))
        self.StartCircle.setScaledContents(True)
        self.StartCircle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.StartCircle, 0, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout_3.addWidget(self.StartWidget, 0, Qt.AlignmentFlag.AlignVCenter)

        self.ConnectWidget = QWidget(self.Timeline)
        self.ConnectWidget.setObjectName(u"ConnectWidget")
        self.verticalLayout = QVBoxLayout(self.ConnectWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.ConnectText = QLabel(self.ConnectWidget)
        self.ConnectText.setObjectName(u"ConnectText")
        self.ConnectText.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.ConnectText)

        self.ConnectCircle = QLabel(self.ConnectWidget)
        self.ConnectCircle.setObjectName(u"ConnectCircle")
        sizePolicy3.setHeightForWidth(self.ConnectCircle.sizePolicy().hasHeightForWidth())
        self.ConnectCircle.setSizePolicy(sizePolicy3)
        self.ConnectCircle.setPixmap(QPixmap(u"icons/white/timeline-circle.svg"))
        self.ConnectCircle.setScaledContents(True)
        self.ConnectCircle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.ConnectCircle, 0, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout_3.addWidget(self.ConnectWidget, 0, Qt.AlignmentFlag.AlignVCenter)

        self.INITWidget = QWidget(self.Timeline)
        self.INITWidget.setObjectName(u"INITWidget")
        self.verticalLayout_3 = QVBoxLayout(self.INITWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.INITText = QLabel(self.INITWidget)
        self.INITText.setObjectName(u"INITText")
        self.INITText.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.INITText)

        self.INITCircle = QLabel(self.INITWidget)
        self.INITCircle.setObjectName(u"INITCircle")
        sizePolicy3.setHeightForWidth(self.INITCircle.sizePolicy().hasHeightForWidth())
        self.INITCircle.setSizePolicy(sizePolicy3)
        self.INITCircle.setPixmap(QPixmap(u"icons/white/timeline-circle.svg"))
        self.INITCircle.setScaledContents(True)
        self.INITCircle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.INITCircle, 0, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout_3.addWidget(self.INITWidget, 0, Qt.AlignmentFlag.AlignVCenter)

        self.IdleWidget = QWidget(self.Timeline)
        self.IdleWidget.setObjectName(u"IdleWidget")
        self.verticalLayout_6 = QVBoxLayout(self.IdleWidget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.IdleText = QLabel(self.IdleWidget)
        self.IdleText.setObjectName(u"IdleText")
        self.IdleText.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.IdleText)

        self.IdleCircle = QLabel(self.IdleWidget)
        self.IdleCircle.setObjectName(u"IdleCircle")
        sizePolicy3.setHeightForWidth(self.IdleCircle.sizePolicy().hasHeightForWidth())
        self.IdleCircle.setSizePolicy(sizePolicy3)
        self.IdleCircle.setPixmap(QPixmap(u"icons/white/timeline-circle.svg"))
        self.IdleCircle.setScaledContents(True)
        self.IdleCircle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.IdleCircle, 0, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout_3.addWidget(self.IdleWidget, 0, Qt.AlignmentFlag.AlignVCenter)

        self.ManualAlignWidget = QWidget(self.Timeline)
        self.ManualAlignWidget.setObjectName(u"ManualAlignWidget")
        self.verticalLayout_7 = QVBoxLayout(self.ManualAlignWidget)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.ManualAlignText = QLabel(self.ManualAlignWidget)
        self.ManualAlignText.setObjectName(u"ManualAlignText")
        self.ManualAlignText.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_7.addWidget(self.ManualAlignText)

        self.ManualAlignCircle = QLabel(self.ManualAlignWidget)
        self.ManualAlignCircle.setObjectName(u"ManualAlignCircle")
        sizePolicy3.setHeightForWidth(self.ManualAlignCircle.sizePolicy().hasHeightForWidth())
        self.ManualAlignCircle.setSizePolicy(sizePolicy3)
        self.ManualAlignCircle.setPixmap(QPixmap(u"icons/white/timeline-circle.svg"))
        self.ManualAlignCircle.setScaledContents(True)
        self.ManualAlignCircle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_7.addWidget(self.ManualAlignCircle, 0, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout_3.addWidget(self.ManualAlignWidget, 0, Qt.AlignmentFlag.AlignVCenter)

        self.AutoAlignWidget = QWidget(self.Timeline)
        self.AutoAlignWidget.setObjectName(u"AutoAlignWidget")
        self.verticalLayout_8 = QVBoxLayout(self.AutoAlignWidget)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.AutoAlignText = QLabel(self.AutoAlignWidget)
        self.AutoAlignText.setObjectName(u"AutoAlignText")
        self.AutoAlignText.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_8.addWidget(self.AutoAlignText)

        self.AutoAlignCircle = QLabel(self.AutoAlignWidget)
        self.AutoAlignCircle.setObjectName(u"AutoAlignCircle")
        sizePolicy3.setHeightForWidth(self.AutoAlignCircle.sizePolicy().hasHeightForWidth())
        self.AutoAlignCircle.setSizePolicy(sizePolicy3)
        self.AutoAlignCircle.setPixmap(QPixmap(u"icons/white/timeline-circle.svg"))
        self.AutoAlignCircle.setScaledContents(True)
        self.AutoAlignCircle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_8.addWidget(self.AutoAlignCircle, 0, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout_3.addWidget(self.AutoAlignWidget, 0, Qt.AlignmentFlag.AlignVCenter)

        self.AutoPickWidget = QWidget(self.Timeline)
        self.AutoPickWidget.setObjectName(u"AutoPickWidget")
        self.verticalLayout_9 = QVBoxLayout(self.AutoPickWidget)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.AutoPickText = QLabel(self.AutoPickWidget)
        self.AutoPickText.setObjectName(u"AutoPickText")
        self.AutoPickText.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_9.addWidget(self.AutoPickText)

        self.AutoPickCircle = QLabel(self.AutoPickWidget)
        self.AutoPickCircle.setObjectName(u"AutoPickCircle")
        sizePolicy3.setHeightForWidth(self.AutoPickCircle.sizePolicy().hasHeightForWidth())
        self.AutoPickCircle.setSizePolicy(sizePolicy3)
        self.AutoPickCircle.setPixmap(QPixmap(u"icons/white/timeline-circle.svg"))
        self.AutoPickCircle.setScaledContents(True)
        self.AutoPickCircle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_9.addWidget(self.AutoPickCircle, 0, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout_3.addWidget(self.AutoPickWidget, 0, Qt.AlignmentFlag.AlignVCenter)

        self.AssemblyWidget = QWidget(self.Timeline)
        self.AssemblyWidget.setObjectName(u"AssemblyWidget")
        self.verticalLayout_4 = QVBoxLayout(self.AssemblyWidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.AssemblyText = QLabel(self.AssemblyWidget)
        self.AssemblyText.setObjectName(u"AssemblyText")
        self.AssemblyText.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.AssemblyText, 0, Qt.AlignmentFlag.AlignTop)

        self.AssemblyCircle = QLabel(self.AssemblyWidget)
        self.AssemblyCircle.setObjectName(u"AssemblyCircle")
        sizePolicy3.setHeightForWidth(self.AssemblyCircle.sizePolicy().hasHeightForWidth())
        self.AssemblyCircle.setSizePolicy(sizePolicy3)
        self.AssemblyCircle.setPixmap(QPixmap(u"icons/white/timeline-circle.svg"))
        self.AssemblyCircle.setScaledContents(True)
        self.AssemblyCircle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.AssemblyCircle, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)


        self.horizontalLayout_3.addWidget(self.AssemblyWidget, 0, Qt.AlignmentFlag.AlignVCenter)


        self.horizontalLayout_6.addWidget(self.Timeline)

        self.ProcessAndInfoStackedWidget.addWidget(self.AutoProcessPage)
        self.InformationPage = QWidget()
        self.InformationPage.setObjectName(u"InformationPage")
        self.InformationPage.setStyleSheet(u"")
        self.horizontalLayout_7 = QHBoxLayout(self.InformationPage)
        self.horizontalLayout_7.setSpacing(6)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.Info = QFrame(self.InformationPage)
        self.Info.setObjectName(u"Info")
        self.Info.setFrameShape(QFrame.Shape.StyledPanel)
        self.Info.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.Info)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(-1, 0, -1, 9)
        self.CartesianPoseWidget = QWidget(self.Info)
        self.CartesianPoseWidget.setObjectName(u"CartesianPoseWidget")
        sizePolicy2.setHeightForWidth(self.CartesianPoseWidget.sizePolicy().hasHeightForWidth())
        self.CartesianPoseWidget.setSizePolicy(sizePolicy2)
        self.CartesianPoseWidget.setMinimumSize(QSize(0, 0))
        self.gridLayout = QGridLayout(self.CartesianPoseWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, 6, -1, -1)
        self.yPosFrame = QFrame(self.CartesianPoseWidget)
        self.yPosFrame.setObjectName(u"yPosFrame")
        self.yPosFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.yPosFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.yPosFrame)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(-1, -1, -1, 3)
        self.y = QLabel(self.yPosFrame)
        self.y.setObjectName(u"y")
        font1 = QFont()
        font1.setPointSize(9)
        self.y.setFont(font1)

        self.horizontalLayout_9.addWidget(self.y, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.yText = QLabel(self.yPosFrame)
        self.yText.setObjectName(u"yText")

        self.horizontalLayout_9.addWidget(self.yText, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)


        self.gridLayout.addWidget(self.yPosFrame, 1, 1, 1, 1)

        self.zPosFrame = QFrame(self.CartesianPoseWidget)
        self.zPosFrame.setObjectName(u"zPosFrame")
        self.zPosFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.zPosFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.zPosFrame)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(-1, -1, -1, 14)
        self.z = QLabel(self.zPosFrame)
        self.z.setObjectName(u"z")
        self.z.setFont(font1)

        self.horizontalLayout_11.addWidget(self.z, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.zText = QLabel(self.zPosFrame)
        self.zText.setObjectName(u"zText")

        self.horizontalLayout_11.addWidget(self.zText, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)


        self.gridLayout.addWidget(self.zPosFrame, 2, 0, 1, 1)

        self.yawPosFrame = QFrame(self.CartesianPoseWidget)
        self.yawPosFrame.setObjectName(u"yawPosFrame")
        self.yawPosFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.yawPosFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.yawPosFrame)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(-1, -1, -1, 14)
        self.yaw = QLabel(self.yawPosFrame)
        self.yaw.setObjectName(u"yaw")
        self.yaw.setFont(font1)

        self.horizontalLayout_12.addWidget(self.yaw, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.yawText = QLabel(self.yawPosFrame)
        self.yawText.setObjectName(u"yawText")

        self.horizontalLayout_12.addWidget(self.yawText, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)


        self.gridLayout.addWidget(self.yawPosFrame, 2, 1, 1, 1)

        self.CartesianPoseText = QLabel(self.CartesianPoseWidget)
        self.CartesianPoseText.setObjectName(u"CartesianPoseText")
        font2 = QFont()
        font2.setPointSize(10)
        self.CartesianPoseText.setFont(font2)
        self.CartesianPoseText.setStyleSheet(u"border: 2px solid #FFFFFF;  /* white solid border */\n"
"border-radius: 6px;")

        self.gridLayout.addWidget(self.CartesianPoseText, 0, 0, 1, 2, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.xPosFrame = QFrame(self.CartesianPoseWidget)
        self.xPosFrame.setObjectName(u"xPosFrame")
        self.xPosFrame.setFont(font1)
        self.xPosFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.xPosFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.xPosFrame)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(9, -1, -1, 3)
        self.x = QLabel(self.xPosFrame)
        self.x.setObjectName(u"x")
        self.x.setFont(font1)

        self.horizontalLayout_8.addWidget(self.x, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.xText = QLabel(self.xPosFrame)
        self.xText.setObjectName(u"xText")

        self.horizontalLayout_8.addWidget(self.xText, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)


        self.gridLayout.addWidget(self.xPosFrame, 1, 0, 1, 1)


        self.horizontalLayout_10.addWidget(self.CartesianPoseWidget)

        self.MotorInfoWidget = QWidget(self.Info)
        self.MotorInfoWidget.setObjectName(u"MotorInfoWidget")
        self.MotorInfoWidget.setStyleSheet(u"")
        self.gridLayout_2 = QGridLayout(self.MotorInfoWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(-1, 6, -1, -1)
        self.PositionFrame = QFrame(self.MotorInfoWidget)
        self.PositionFrame.setObjectName(u"PositionFrame")
        self.PositionFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.PositionFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.PositionFrame)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.Position = QLabel(self.PositionFrame)
        self.Position.setObjectName(u"Position")

        self.horizontalLayout_13.addWidget(self.Position)

        self.PositionText = QLabel(self.PositionFrame)
        self.PositionText.setObjectName(u"PositionText")

        self.horizontalLayout_13.addWidget(self.PositionText)


        self.gridLayout_2.addWidget(self.PositionFrame, 2, 0, 1, 1)

        self.MotorInfoText = QLabel(self.MotorInfoWidget)
        self.MotorInfoText.setObjectName(u"MotorInfoText")
        self.MotorInfoText.setFont(font2)
        self.MotorInfoText.setStyleSheet(u"border: 2px solid #FFFFFF;  /* white solid border */\n"
"border-radius: 6px;")

        self.gridLayout_2.addWidget(self.MotorInfoText, 0, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.CurrentFrame = QFrame(self.MotorInfoWidget)
        self.CurrentFrame.setObjectName(u"CurrentFrame")
        self.CurrentFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.CurrentFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.CurrentFrame)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.Current = QLabel(self.CurrentFrame)
        self.Current.setObjectName(u"Current")

        self.horizontalLayout_14.addWidget(self.Current)

        self.CurrentText = QLabel(self.CurrentFrame)
        self.CurrentText.setObjectName(u"CurrentText")

        self.horizontalLayout_14.addWidget(self.CurrentText)


        self.gridLayout_2.addWidget(self.CurrentFrame, 3, 0, 1, 1)


        self.horizontalLayout_10.addWidget(self.MotorInfoWidget)

        self.RecordData = QWidget(self.Info)
        self.RecordData.setObjectName(u"RecordData")
        self.gridLayout_3 = QGridLayout(self.RecordData)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(-1, 6, -1, -1)
        self.frame_11 = QFrame(self.RecordData)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_11)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(9, 9, -1, 0)
        self.d1 = QLabel(self.frame_11)
        self.d1.setObjectName(u"d1")

        self.verticalLayout_13.addWidget(self.d1)


        self.gridLayout_3.addWidget(self.frame_11, 1, 0, 1, 1)

        self.LaserInfoText = QLabel(self.RecordData)
        self.LaserInfoText.setObjectName(u"LaserInfoText")
        self.LaserInfoText.setFont(font2)
        self.LaserInfoText.setStyleSheet(u"border: 2px solid #FFFFFF;  /* white solid border */\n"
"border-radius: 6px;")

        self.gridLayout_3.addWidget(self.LaserInfoText, 0, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.frame_6 = QFrame(self.RecordData)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_6)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(9, -1, -1, 0)
        self.d2 = QLabel(self.frame_6)
        self.d2.setObjectName(u"d2")

        self.verticalLayout_22.addWidget(self.d2)


        self.gridLayout_3.addWidget(self.frame_6, 3, 0, 1, 1)

        self.frame_5 = QFrame(self.RecordData)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_5)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(9, -1, -1, 0)
        self.h1 = QLabel(self.frame_5)
        self.h1.setObjectName(u"h1")

        self.verticalLayout_14.addWidget(self.h1)


        self.gridLayout_3.addWidget(self.frame_5, 4, 0, 1, 1)


        self.horizontalLayout_10.addWidget(self.RecordData)

        self.RecordDataButtonContainer = QWidget(self.Info)
        self.RecordDataButtonContainer.setObjectName(u"RecordDataButtonContainer")
        sizePolicy2.setHeightForWidth(self.RecordDataButtonContainer.sizePolicy().hasHeightForWidth())
        self.RecordDataButtonContainer.setSizePolicy(sizePolicy2)
        self.verticalLayout_16 = QVBoxLayout(self.RecordDataButtonContainer)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(9, 9, -1, -1)
        self.RecordDataButton = QPushButton(self.RecordDataButtonContainer)
        self.RecordDataButton.setObjectName(u"RecordDataButton")
        sizePolicy2.setHeightForWidth(self.RecordDataButton.sizePolicy().hasHeightForWidth())
        self.RecordDataButton.setSizePolicy(sizePolicy2)
        self.RecordDataButton.setFont(font)
        self.RecordDataButton.setStyleSheet(u"QPushButton {\n"
"    background-color: qlineargradient(\n"
"        x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #1a1a1a, stop:1 #000000\n"
"    );\n"
"    color: white;\n"
"    border: 1px solid #555;\n"
"    border-radius: 4px;\n"
"    padding: 16px 24px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: qlineargradient(\n"
"        x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #2a2a2a, stop:1 #111111\n"
"    );\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(\n"
"        x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #0f0f0f, stop:1 #000000\n"
"    );\n"
"	background-color: #0B76A0;\n"
"    border: 1px solid #555;\n"
"    border-radius: 4px;\n"
"    padding: 16px 24px;\n"
"}\n"
"")

        self.verticalLayout_16.addWidget(self.RecordDataButton, 0, Qt.AlignmentFlag.AlignVCenter)


        self.horizontalLayout_10.addWidget(self.RecordDataButtonContainer)


        self.horizontalLayout_7.addWidget(self.Info)

        self.ProcessAndInfoStackedWidget.addWidget(self.InformationPage)
        self.ParentStackedWidgetToChangeMenuOptions.addWidget(self.MainPagePage)
        self.ProductionRecordPage = QWidget()
        self.ProductionRecordPage.setObjectName(u"ProductionRecordPage")
        self.frame = QFrame(self.ProductionRecordPage)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(490, 250, 119, 36))
        self.frame.setStyleSheet(u"background-color: #000000; color:white;")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.verticalLayout_18.addWidget(self.label)

        self.ParentStackedWidgetToChangeMenuOptions.addWidget(self.ProductionRecordPage)
        self.ComponentControlPage = QWidget()
        self.ComponentControlPage.setObjectName(u"ComponentControlPage")
        self.ComponentControlPageMenu = QWidget(self.ComponentControlPage)
        self.ComponentControlPageMenu.setObjectName(u"ComponentControlPageMenu")
        self.ComponentControlPageMenu.setGeometry(QRect(0, 0, 1001, 91))
        self.ComponentControlPageMenu.setStyleSheet(u"")
        self.horizontalLayout_15 = QHBoxLayout(self.ComponentControlPageMenu)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.MotorPageButton = QPushButton(self.ComponentControlPageMenu)
        self.ComponentControlMenuButtonGroup = QButtonGroup(MainWindow)
        self.ComponentControlMenuButtonGroup.setObjectName(u"ComponentControlMenuButtonGroup")
        self.ComponentControlMenuButtonGroup.addButton(self.MotorPageButton)
        self.MotorPageButton.setObjectName(u"MotorPageButton")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.MotorPageButton.sizePolicy().hasHeightForWidth())
        self.MotorPageButton.setSizePolicy(sizePolicy4)
        self.MotorPageButton.setFont(font)
        self.MotorPageButton.setStyleSheet(u"QPushButton {\n"
"    background-color: #000;\n"
"    color: white;\n"
"    border: 1px solid #444;\n"
"    border-bottom: none;\n"
"    padding: 6px 12px;\n"
"    border-top-left-radius: 12px;\n"
"    border-top-right-radius: 12px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #111;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: #0B76A0;\n"
"    border: 1px solid #0B76A0;\n"
"    border-bottom: none;\n"
"    color: white;\n"
"}\n"
"")
        self.MotorPageButton.setCheckable(True)
        self.MotorPageButton.setChecked(True)

        self.horizontalLayout_15.addWidget(self.MotorPageButton)

        self.VisionPageButton = QPushButton(self.ComponentControlPageMenu)
        self.ComponentControlMenuButtonGroup.addButton(self.VisionPageButton)
        self.VisionPageButton.setObjectName(u"VisionPageButton")
        sizePolicy4.setHeightForWidth(self.VisionPageButton.sizePolicy().hasHeightForWidth())
        self.VisionPageButton.setSizePolicy(sizePolicy4)
        self.VisionPageButton.setFont(font)
        self.VisionPageButton.setStyleSheet(u"QPushButton {\n"
"    background-color: #000;\n"
"    color: white;\n"
"    border: 1px solid #444;\n"
"    border-bottom: none;\n"
"    padding: 6px 12px;\n"
"    border-top-left-radius: 12px;\n"
"    border-top-right-radius: 12px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #111;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: #0B76A0;\n"
"    border: 1px solid #0B76A0;\n"
"    border-bottom: none;\n"
"    color: white;\n"
"}\n"
"")
        self.VisionPageButton.setCheckable(True)

        self.horizontalLayout_15.addWidget(self.VisionPageButton)

        self.ClipperPageButton = QPushButton(self.ComponentControlPageMenu)
        self.ComponentControlMenuButtonGroup.addButton(self.ClipperPageButton)
        self.ClipperPageButton.setObjectName(u"ClipperPageButton")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Ignored)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.ClipperPageButton.sizePolicy().hasHeightForWidth())
        self.ClipperPageButton.setSizePolicy(sizePolicy5)
        self.ClipperPageButton.setFont(font)
        self.ClipperPageButton.setStyleSheet(u"QPushButton {\n"
"    background-color: #000;\n"
"    color: white;\n"
"    border: 1px solid #444;\n"
"    border-bottom: none;\n"
"    padding: 6px 12px;\n"
"    border-top-left-radius: 12px;\n"
"    border-top-right-radius: 12px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #111;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: #0B76A0;\n"
"    border: 1px solid #0B76A0;\n"
"    border-bottom: none;\n"
"    color: white;\n"
"}\n"
"")
        self.ClipperPageButton.setCheckable(True)

        self.horizontalLayout_15.addWidget(self.ClipperPageButton)

        self.ComponentControlStackedWidget = QStackedWidget(self.ComponentControlPage)
        self.ComponentControlStackedWidget.setObjectName(u"ComponentControlStackedWidget")
        self.ComponentControlStackedWidget.setGeometry(QRect(0, 100, 1011, 551))
        self.MotorPage = QWidget()
        self.MotorPage.setObjectName(u"MotorPage")
        self.horizontalSlider = QSlider(self.MotorPage)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setGeometry(QRect(280, 150, 160, 18))
        self.horizontalSlider.setOrientation(Qt.Orientation.Horizontal)
        self.label_2 = QLabel(self.MotorPage)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(310, 230, 49, 16))
        self.ComponentControlStackedWidget.addWidget(self.MotorPage)
        self.VisionPage = QWidget()
        self.VisionPage.setObjectName(u"VisionPage")
        self.VisionPageVisionFrame = QFrame(self.VisionPage)
        self.VisionPageVisionFrame.setObjectName(u"VisionPageVisionFrame")
        self.VisionPageVisionFrame.setGeometry(QRect(10, 10, 671, 531))
        self.VisionPageVisionFrame.setStyleSheet(u"background-color: #000000; color: white;\n"
"")
        self.VisionPageVisionFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.VisionPageVisionFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.VisionTextPlaceholder = QLabel(self.VisionPageVisionFrame)
        self.VisionTextPlaceholder.setObjectName(u"VisionTextPlaceholder")
        self.VisionTextPlaceholder.setGeometry(QRect(290, 270, 49, 16))
        self.VisionSettingsStackedWidget = QStackedWidget(self.VisionPage)
        self.VisionSettingsStackedWidget.setObjectName(u"VisionSettingsStackedWidget")
        self.VisionSettingsStackedWidget.setGeometry(QRect(700, 120, 271, 421))
        self.PicturePage = QWidget()
        self.PicturePage.setObjectName(u"PicturePage")
        self.verticalLayout_17 = QVBoxLayout(self.PicturePage)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.PictureWidget = QWidget(self.PicturePage)
        self.PictureWidget.setObjectName(u"PictureWidget")
        self.verticalLayout_23 = QVBoxLayout(self.PictureWidget)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.TakePictureButton = QPushButton(self.PictureWidget)
        self.TakePictureButton.setObjectName(u"TakePictureButton")
        sizePolicy.setHeightForWidth(self.TakePictureButton.sizePolicy().hasHeightForWidth())
        self.TakePictureButton.setSizePolicy(sizePolicy)
        self.TakePictureButton.setFont(font)
        self.TakePictureButton.setStyleSheet(u"QPushButton {\n"
"    padding: 6px 12px;\n"
"    background-color: qlineargradient(\n"
"        x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #1a1a1a, stop:1 #000000\n"
"    );\n"
"    color: white;\n"
"    border: 1px solid #444;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: qlineargradient(\n"
"        x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #2a2a2a, stop:1 #111111\n"
"    );\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(\n"
"        x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #0f0f0f, stop:1 #000000\n"
"    );\n"
"    border-style: inset;\n"
"	background-color: #0B76A0;\n"
"}")
        self.TakePictureButton.setCheckable(False)

        self.verticalLayout_23.addWidget(self.TakePictureButton)

        self.SaveButton = QPushButton(self.PictureWidget)
        self.SaveButton.setObjectName(u"SaveButton")
        sizePolicy.setHeightForWidth(self.SaveButton.sizePolicy().hasHeightForWidth())
        self.SaveButton.setSizePolicy(sizePolicy)
        self.SaveButton.setFont(font)
        self.SaveButton.setStyleSheet(u"QPushButton {\n"
"    padding: 6px 12px;\n"
"    background-color: qlineargradient(\n"
"        x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #1a1a1a, stop:1 #000000\n"
"    );\n"
"    color: white;\n"
"    border: 1px solid #444;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: qlineargradient(\n"
"        x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #2a2a2a, stop:1 #111111\n"
"    );\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(\n"
"        x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #0f0f0f, stop:1 #000000\n"
"    );\n"
"    border-style: inset;\n"
"	background-color: #0B76A0;\n"
"}\n"
"\n"
"\n"
"\n"
"")

        self.verticalLayout_23.addWidget(self.SaveButton)

        self.CancelButton = QPushButton(self.PictureWidget)
        self.CancelButton.setObjectName(u"CancelButton")
        sizePolicy.setHeightForWidth(self.CancelButton.sizePolicy().hasHeightForWidth())
        self.CancelButton.setSizePolicy(sizePolicy)
        self.CancelButton.setFont(font)
        self.CancelButton.setStyleSheet(u"QPushButton {\n"
"    padding: 6px 12px;\n"
"    background-color: qlineargradient(\n"
"        x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #1a1a1a, stop:1 #000000\n"
"    );\n"
"    color: white;\n"
"    border: 1px solid #444;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: qlineargradient(\n"
"        x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #2a2a2a, stop:1 #111111\n"
"    );\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(\n"
"        x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #0f0f0f, stop:1 #000000\n"
"    );\n"
"    border-style: inset;\n"
"	background-color: #0B76A0;\n"
"}\n"
"\n"
"\n"
"\n"
"")

        self.verticalLayout_23.addWidget(self.CancelButton)


        self.verticalLayout_17.addWidget(self.PictureWidget)

        self.VisionSettingsStackedWidget.addWidget(self.PicturePage)
        self.PictureOptionsPage = QWidget()
        self.PictureOptionsPage.setObjectName(u"PictureOptionsPage")
        self.verticalLayout_25 = QVBoxLayout(self.PictureOptionsPage)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.PictureOptionsWidget = QWidget(self.PictureOptionsPage)
        self.PictureOptionsWidget.setObjectName(u"PictureOptionsWidget")
        self.verticalLayout_24 = QVBoxLayout(self.PictureOptionsWidget)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.RougAlignmentButton = QPushButton(self.PictureOptionsWidget)
        self.RougAlignmentButton.setObjectName(u"RougAlignmentButton")
        sizePolicy.setHeightForWidth(self.RougAlignmentButton.sizePolicy().hasHeightForWidth())
        self.RougAlignmentButton.setSizePolicy(sizePolicy)
        self.RougAlignmentButton.setFont(font)
        self.RougAlignmentButton.setStyleSheet(u"QPushButton {\n"
"    padding: 6px 12px;\n"
"    background-color: qlineargradient(\n"
"        x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #1a1a1a, stop:1 #000000\n"
"    );\n"
"    color: white;\n"
"    border: 1px solid #444;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: qlineargradient(\n"
"        x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #2a2a2a, stop:1 #111111\n"
"    );\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: qlineargradient(\n"
"        x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #0f0f0f, stop:1 #000000\n"
"    );\n"
"    border-style: inset;\n"
"	background-color: #0B76A0;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.RougAlignmentButton.setCheckable(True)

        self.verticalLayout_24.addWidget(self.RougAlignmentButton)

        self.PreciseAlignmentButton = QPushButton(self.PictureOptionsWidget)
        self.PreciseAlignmentButton.setObjectName(u"PreciseAlignmentButton")
        sizePolicy.setHeightForWidth(self.PreciseAlignmentButton.sizePolicy().hasHeightForWidth())
        self.PreciseAlignmentButton.setSizePolicy(sizePolicy)
        self.PreciseAlignmentButton.setFont(font)
        self.PreciseAlignmentButton.setStyleSheet(u"QPushButton {\n"
"    padding: 6px 12px;\n"
"    background-color: qlineargradient(\n"
"        x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #1a1a1a, stop:1 #000000\n"
"    );\n"
"    color: white;\n"
"    border: 1px solid #444;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: qlineargradient(\n"
"        x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #2a2a2a, stop:1 #111111\n"
"    );\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: qlineargradient(\n"
"        x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #0f0f0f, stop:1 #000000\n"
"    );\n"
"    border-style: inset;\n"
"	background-color: #0B76A0;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.PreciseAlignmentButton.setCheckable(True)

        self.verticalLayout_24.addWidget(self.PreciseAlignmentButton)


        self.verticalLayout_25.addWidget(self.PictureOptionsWidget)

        self.VisionSettingsStackedWidget.addWidget(self.PictureOptionsPage)
        self.AutoManualButtons_2 = QWidget(self.VisionPage)
        self.AutoManualButtons_2.setObjectName(u"AutoManualButtons_2")
        self.AutoManualButtons_2.setGeometry(QRect(700, 10, 281, 101))
        self.horizontalLayout_16 = QHBoxLayout(self.AutoManualButtons_2)
        self.horizontalLayout_16.setSpacing(25)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.PictureButton = QPushButton(self.AutoManualButtons_2)
        self.PictureButton.setObjectName(u"PictureButton")
        sizePolicy.setHeightForWidth(self.PictureButton.sizePolicy().hasHeightForWidth())
        self.PictureButton.setSizePolicy(sizePolicy)
        self.PictureButton.setFont(font)
        self.PictureButton.setStyleSheet(u"QPushButton {\n"
"    padding: 6px 12px;\n"
"    background-color: qlineargradient(\n"
"        x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #1a1a1a, stop:1 #000000\n"
"    );\n"
"    color: white;\n"
"    border: 1px solid #444;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: qlineargradient(\n"
"        x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #2a2a2a, stop:1 #111111\n"
"    );\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(\n"
"        x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #0f0f0f, stop:1 #000000\n"
"    );\n"
"    border-style: inset;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: #0B76A0;\n"
"    border: 1px solid #0B76A0;\n"
"}\n"
"")
        self.PictureButton.setCheckable(True)
        self.PictureButton.setChecked(True)

        self.horizontalLayout_16.addWidget(self.PictureButton)

        self.OptionsButton = QPushButton(self.AutoManualButtons_2)
        self.OptionsButton.setObjectName(u"OptionsButton")
        sizePolicy.setHeightForWidth(self.OptionsButton.sizePolicy().hasHeightForWidth())
        self.OptionsButton.setSizePolicy(sizePolicy)
        self.OptionsButton.setFont(font)
        self.OptionsButton.setStyleSheet(u"QPushButton {\n"
"    padding: 6px 12px;\n"
"    background-color: qlineargradient(\n"
"        x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #1a1a1a, stop:1 #000000\n"
"    );\n"
"    color: white;\n"
"    border: 1px solid #444;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: qlineargradient(\n"
"        x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #2a2a2a, stop:1 #111111\n"
"    );\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(\n"
"        x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #0f0f0f, stop:1 #000000\n"
"    );\n"
"    border-style: inset;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: #0B76A0;\n"
"    border: 1px solid #0B76A0;\n"
"}\n"
"")
        self.OptionsButton.setCheckable(True)

        self.horizontalLayout_16.addWidget(self.OptionsButton)

        self.ComponentControlStackedWidget.addWidget(self.VisionPage)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.label_6 = QLabel(self.page_5)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(550, 240, 49, 16))
        self.ComponentControlStackedWidget.addWidget(self.page_5)
        self.ParentStackedWidgetToChangeMenuOptions.addWidget(self.ComponentControlPage)
        self.LogsPage = QWidget()
        self.LogsPage.setObjectName(u"LogsPage")
        self.frame_3 = QFrame(self.LogsPage)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(430, 260, 45, 36))
        self.frame_3.setStyleSheet(u"background-color: #000000; color: white;")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_3)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_19.addWidget(self.label_3)

        self.ParentStackedWidgetToChangeMenuOptions.addWidget(self.LogsPage)
        self.SystemSettingsPage = QWidget()
        self.SystemSettingsPage.setObjectName(u"SystemSettingsPage")
        self.frame_4 = QFrame(self.SystemSettingsPage)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(480, 280, 104, 36))
        self.frame_4.setStyleSheet(u"background-color: #000000; color: white;")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_4)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label_4 = QLabel(self.frame_4)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_20.addWidget(self.label_4)

        self.ParentStackedWidgetToChangeMenuOptions.addWidget(self.SystemSettingsPage)
        self.WorkOrderWidget = QWidget(self.BackgroundWidget)
        self.WorkOrderWidget.setObjectName(u"WorkOrderWidget")
        self.WorkOrderWidget.setGeometry(QRect(530, 0, 141, 41))
        self.WorkOrderWidget.setStyleSheet(u"color: white;")
        self.horizontalLayout_17 = QHBoxLayout(self.WorkOrderWidget)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.WorkOrderText = QLabel(self.WorkOrderWidget)
        self.WorkOrderText.setObjectName(u"WorkOrderText")
        font3 = QFont()
        font3.setBold(True)
        self.WorkOrderText.setFont(font3)

        self.horizontalLayout_17.addWidget(self.WorkOrderText)

        self.WorkOrderNumberInput = QLabel(self.WorkOrderWidget)
        self.WorkOrderNumberInput.setObjectName(u"WorkOrderNumberInput")

        self.horizontalLayout_17.addWidget(self.WorkOrderNumberInput)

        self.MainPageButton = QPushButton(self.BackgroundWidget)
        self.MenuButtonGroup.addButton(self.MainPageButton)
        self.MainPageButton.setObjectName(u"MainPageButton")
        self.MainPageButton.setGeometry(QRect(9, 189, 223, 111))
        sizePolicy.setHeightForWidth(self.MainPageButton.sizePolicy().hasHeightForWidth())
        self.MainPageButton.setSizePolicy(sizePolicy)
        self.MainPageButton.setFont(font)
        self.MainPageButton.setAutoFillBackground(False)
        self.MainPageButton.setStyleSheet(u"QPushButton {\n"
"    padding: 6px 12px;\n"
"    background-color: qlineargradient(\n"
"        x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #1a1a1a, stop:1 #000000\n"
"    );\n"
"    color: white;\n"
"    border: 1px solid #444;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: qlineargradient(\n"
"        x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #2a2a2a, stop:1 #111111\n"
"    );\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(\n"
"        x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #0f0f0f, stop:1 #000000\n"
"    );\n"
"    border-style: inset;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: #0B76A0;\n"
"    border: 1px solid #0B76A0;\n"
"}\n"
"")
        icon9 = QIcon()
        icon9.addFile(u"icons/white/home-simple-door.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.MainPageButton.setIcon(icon9)
        self.MainPageButton.setCheckable(True)
        self.MainPageButton.setChecked(True)
        self.LogsButton = QPushButton(self.BackgroundWidget)
        self.MenuButtonGroup.addButton(self.LogsButton)
        self.LogsButton.setObjectName(u"LogsButton")
        self.LogsButton.setGeometry(QRect(9, 541, 223, 111))
        sizePolicy.setHeightForWidth(self.LogsButton.sizePolicy().hasHeightForWidth())
        self.LogsButton.setSizePolicy(sizePolicy)
        self.LogsButton.setFont(font)
        self.LogsButton.setStyleSheet(u"QPushButton {\n"
"    padding: 6px 12px;\n"
"    background-color: qlineargradient(\n"
"        x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #1a1a1a, stop:1 #000000\n"
"    );\n"
"    color: white;\n"
"    border: 1px solid #444;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: qlineargradient(\n"
"        x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #2a2a2a, stop:1 #111111\n"
"    );\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(\n"
"        x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #0f0f0f, stop:1 #000000\n"
"    );\n"
"    border-style: inset;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: #0B76A0;\n"
"    border: 1px solid #0B76A0;\n"
"}\n"
"")
        icon10 = QIcon()
        icon10.addFile(u"icons/white/multiple-pages.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.LogsButton.setIcon(icon10)
        self.LogsButton.setCheckable(True)
        self.ProductionRecordButton = QPushButton(self.BackgroundWidget)
        self.MenuButtonGroup.addButton(self.ProductionRecordButton)
        self.ProductionRecordButton.setObjectName(u"ProductionRecordButton")
        self.ProductionRecordButton.setGeometry(QRect(9, 306, 223, 112))
        sizePolicy.setHeightForWidth(self.ProductionRecordButton.sizePolicy().hasHeightForWidth())
        self.ProductionRecordButton.setSizePolicy(sizePolicy)
        self.ProductionRecordButton.setFont(font)
        self.ProductionRecordButton.setStyleSheet(u"QPushButton {\n"
"    padding: 6px 12px;\n"
"    background-color: qlineargradient(\n"
"        x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #1a1a1a, stop:1 #000000\n"
"    );\n"
"    color: white;\n"
"    border: 1px solid #444;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: qlineargradient(\n"
"        x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #2a2a2a, stop:1 #111111\n"
"    );\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(\n"
"        x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #0f0f0f, stop:1 #000000\n"
"    );\n"
"    border-style: inset;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: #0B76A0;\n"
"    border: 1px solid #0B76A0;\n"
"}\n"
"")
        icon11 = QIcon()
        icon11.addFile(u"icons/white/page.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.ProductionRecordButton.setIcon(icon11)
        self.ProductionRecordButton.setCheckable(True)
        self.ComponentControlButton = QPushButton(self.BackgroundWidget)
        self.MenuButtonGroup.addButton(self.ComponentControlButton)
        self.ComponentControlButton.setObjectName(u"ComponentControlButton")
        self.ComponentControlButton.setGeometry(QRect(9, 424, 223, 111))
        sizePolicy.setHeightForWidth(self.ComponentControlButton.sizePolicy().hasHeightForWidth())
        self.ComponentControlButton.setSizePolicy(sizePolicy)
        self.ComponentControlButton.setFont(font)
        self.ComponentControlButton.setStyleSheet(u"QPushButton {\n"
"    padding: 6px 12px;\n"
"    background-color: qlineargradient(\n"
"        x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #1a1a1a, stop:1 #000000\n"
"    );\n"
"    color: white;\n"
"    border: 1px solid #444;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: qlineargradient(\n"
"        x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #2a2a2a, stop:1 #111111\n"
"    );\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(\n"
"        x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #0f0f0f, stop:1 #000000\n"
"    );\n"
"    border-style: inset;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: #0B76A0;\n"
"    border: 1px solid #0B76A0;\n"
"}\n"
"")
        icon12 = QIcon()
        icon12.addFile(u"icons/white/dimmer-switch.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.ComponentControlButton.setIcon(icon12)
        self.ComponentControlButton.setCheckable(True)
        self.RecipeWidget = QWidget(self.BackgroundWidget)
        self.RecipeWidget.setObjectName(u"RecipeWidget")
        self.RecipeWidget.setGeometry(QRect(530, 30, 171, 41))
        self.RecipeWidget.setStyleSheet(u"color: white;")
        self.horizontalLayout_18 = QHBoxLayout(self.RecipeWidget)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.RecipeText = QLabel(self.RecipeWidget)
        self.RecipeText.setObjectName(u"RecipeText")
        self.RecipeText.setFont(font3)

        self.horizontalLayout_18.addWidget(self.RecipeText)

        self.RecipeNameInput = QLabel(self.RecipeWidget)
        self.RecipeNameInput.setObjectName(u"RecipeNameInput")

        self.horizontalLayout_18.addWidget(self.RecipeNameInput)

        self.QuantityWidget = QWidget(self.BackgroundWidget)
        self.QuantityWidget.setObjectName(u"QuantityWidget")
        self.QuantityWidget.setGeometry(QRect(800, 0, 181, 41))
        self.QuantityWidget.setStyleSheet(u"color: white;")
        self.horizontalLayout_20 = QHBoxLayout(self.QuantityWidget)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.QuantityText = QLabel(self.QuantityWidget)
        self.QuantityText.setObjectName(u"QuantityText")
        self.QuantityText.setFont(font3)

        self.horizontalLayout_20.addWidget(self.QuantityText)

        self.QuantityNumberInput = QLabel(self.QuantityWidget)
        self.QuantityNumberInput.setObjectName(u"QuantityNumberInput")

        self.horizontalLayout_20.addWidget(self.QuantityNumberInput)

        self.WorkerNameWidget = QWidget(self.BackgroundWidget)
        self.WorkerNameWidget.setObjectName(u"WorkerNameWidget")
        self.WorkerNameWidget.setGeometry(QRect(800, 30, 171, 41))
        self.WorkerNameWidget.setStyleSheet(u"color: white;")
        self.horizontalLayout_21 = QHBoxLayout(self.WorkerNameWidget)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.WorkerNameText = QLabel(self.WorkerNameWidget)
        self.WorkerNameText.setObjectName(u"WorkerNameText")
        self.WorkerNameText.setFont(font3)

        self.horizontalLayout_21.addWidget(self.WorkerNameText)

        self.WorkerNameInput = QLabel(self.WorkerNameWidget)
        self.WorkerNameInput.setObjectName(u"WorkerNameInput")

        self.horizontalLayout_21.addWidget(self.WorkerNameInput)

        self.CartHeightWidget = QWidget(self.BackgroundWidget)
        self.CartHeightWidget.setObjectName(u"CartHeightWidget")
        self.CartHeightWidget.setGeometry(QRect(250, 30, 221, 41))
        self.CartHeightWidget.setStyleSheet(u"color: white;")
        self.horizontalLayout_23 = QHBoxLayout(self.CartHeightWidget)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.CartHeightText = QLabel(self.CartHeightWidget)
        self.CartHeightText.setObjectName(u"CartHeightText")
        self.CartHeightText.setFont(font3)

        self.horizontalLayout_23.addWidget(self.CartHeightText)

        self.CartHeightInput = QLabel(self.CartHeightWidget)
        self.CartHeightInput.setObjectName(u"CartHeightInput")

        self.horizontalLayout_23.addWidget(self.CartHeightInput)

        self.CartDepthWidget = QWidget(self.BackgroundWidget)
        self.CartDepthWidget.setObjectName(u"CartDepthWidget")
        self.CartDepthWidget.setGeometry(QRect(250, 0, 221, 41))
        self.CartDepthWidget.setStyleSheet(u"color: white;")
        self.horizontalLayout_24 = QHBoxLayout(self.CartDepthWidget)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.CartDepthText = QLabel(self.CartDepthWidget)
        self.CartDepthText.setObjectName(u"CartDepthText")
        self.CartDepthText.setFont(font3)

        self.horizontalLayout_24.addWidget(self.CartDepthText)

        self.CartDepthInput = QLabel(self.CartDepthWidget)
        self.CartDepthInput.setObjectName(u"CartDepthInput")

        self.horizontalLayout_24.addWidget(self.CartDepthInput)

        self.DateWidget = QWidget(self.BackgroundWidget)
        self.DateWidget.setObjectName(u"DateWidget")
        self.DateWidget.setGeometry(QRect(1050, 10, 151, 41))
        self.DateWidget.setStyleSheet(u"color: white;")
        self.horizontalLayout_26 = QHBoxLayout(self.DateWidget)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.DateText = QLabel(self.DateWidget)
        self.DateText.setObjectName(u"DateText")
        self.DateText.setFont(font3)

        self.horizontalLayout_26.addWidget(self.DateText)

        self.DateInput = QLabel(self.DateWidget)
        self.DateInput.setObjectName(u"DateInput")

        self.horizontalLayout_26.addWidget(self.DateInput)

        self.ParentStackedWidgetToChangeMenuOptions.raise_()
        self.Line.raise_()
        self.SystemSettingsButton.raise_()
        self.SignalLightsWidget.raise_()
        self.DeltaLogo.raise_()
        self.MenuButtons.raise_()
        self.WorkOrderWidget.raise_()
        self.MainPageButton.raise_()
        self.LogsButton.raise_()
        self.ProductionRecordButton.raise_()
        self.ComponentControlButton.raise_()
        self.RecipeWidget.raise_()
        self.QuantityWidget.raise_()
        self.WorkerNameWidget.raise_()
        self.CartHeightWidget.raise_()
        self.CartDepthWidget.raise_()
        self.DateWidget.raise_()

        self.horizontalLayout_4.addWidget(self.BackgroundWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.ParentStackedWidgetToChangeMenuOptions.setCurrentIndex(0)
        self.ActionButtons.setCurrentIndex(1)
        self.ManualOptionsWidget.setCurrentIndex(4)
        self.ProcessAndInfoStackedWidget.setCurrentIndex(0)
        self.ComponentControlStackedWidget.setCurrentIndex(0)
        self.VisionSettingsStackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.SystemSettingsButton.setText(QCoreApplication.translate("MainWindow", u"System\n"
"Settings", None))
        self.RedSignal.setText("")
        self.YellowSignal.setText("")
        self.GreenSignal.setText("")
        self.DeltaLogo.setText("")
        self.VisionText.setText(QCoreApplication.translate("MainWindow", u"Vision", None))
        self.AutoButton.setText(QCoreApplication.translate("MainWindow", u"Auto", None))
        self.ManualButton.setText(QCoreApplication.translate("MainWindow", u"Manual", None))
        self.InitButton.setText(QCoreApplication.translate("MainWindow", u"INIT", None))
        self.RunButton.setText(QCoreApplication.translate("MainWindow", u"RUN", None))
        self.StopButton.setText(QCoreApplication.translate("MainWindow", u"STOP", None))
        self.AutoResetButton.setText(QCoreApplication.translate("MainWindow", u"RESET", None))
        self.ManualOptionsWidget.setTabText(self.ManualOptionsWidget.indexOf(self.ManualAlignTab), QCoreApplication.translate("MainWindow", u"Manual Align", None))
        self.ManualOptionsWidget.setTabText(self.ManualOptionsWidget.indexOf(self.AutoAlignTab), QCoreApplication.translate("MainWindow", u"Auto Align", None))
        self.ManualOptionsWidget.setTabText(self.ManualOptionsWidget.indexOf(self.AutoPickTab), QCoreApplication.translate("MainWindow", u"Auto Pick", None))
        self.ManualOptionsWidget.setTabText(self.ManualOptionsWidget.indexOf(self.AutoAssemblyTab), QCoreApplication.translate("MainWindow", u"Auto Assembly", None))
        self.YawMinus.setText("")
        self.ControlRight.setText("")
        self.ControlUp.setText("")
        self.ControlDown.setText("")
        self.YawPlus.setText("")
        self.ControlLeft.setText("")
        self.ManualResetButton.setText(QCoreApplication.translate("MainWindow", u"RESET", None))
        self.ClipperButton.setText(QCoreApplication.translate("MainWindow", u"Clipper  Off", None))
        self.Lift.setText("")
        self.Lower.setText("")
        self.ManualOptionsWidget.setTabText(self.ManualOptionsWidget.indexOf(self.ControlTab), QCoreApplication.translate("MainWindow", u"Control", None))
        self.StartText.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.StartCircle.setText("")
        self.ConnectText.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.ConnectCircle.setText("")
        self.INITText.setText(QCoreApplication.translate("MainWindow", u"INIT", None))
        self.INITCircle.setText("")
        self.IdleText.setText(QCoreApplication.translate("MainWindow", u"Idle", None))
        self.IdleCircle.setText("")
        self.ManualAlignText.setText(QCoreApplication.translate("MainWindow", u"Manual Align", None))
        self.ManualAlignCircle.setText("")
        self.AutoAlignText.setText(QCoreApplication.translate("MainWindow", u"Auto Align", None))
        self.AutoAlignCircle.setText("")
        self.AutoPickText.setText(QCoreApplication.translate("MainWindow", u"Auto Pick", None))
        self.AutoPickCircle.setText("")
        self.AssemblyText.setText(QCoreApplication.translate("MainWindow", u"Auto ASSY", None))
        self.AssemblyCircle.setText("")
        self.y.setText(QCoreApplication.translate("MainWindow", u"y:", None))
        self.yText.setText(QCoreApplication.translate("MainWindow", u"pos", None))
        self.z.setText(QCoreApplication.translate("MainWindow", u"z:", None))
        self.zText.setText(QCoreApplication.translate("MainWindow", u"pos", None))
        self.yaw.setText(QCoreApplication.translate("MainWindow", u"yaw:", None))
        self.yawText.setText(QCoreApplication.translate("MainWindow", u"pos", None))
        self.CartesianPoseText.setText(QCoreApplication.translate("MainWindow", u"Cartesian Pose", None))
        self.x.setText(QCoreApplication.translate("MainWindow", u"x:", None))
        self.xText.setText(QCoreApplication.translate("MainWindow", u"pos", None))
        self.Position.setText(QCoreApplication.translate("MainWindow", u"Position:", None))
        self.PositionText.setText(QCoreApplication.translate("MainWindow", u"pos", None))
        self.MotorInfoText.setText(QCoreApplication.translate("MainWindow", u"Motor Info", None))
        self.Current.setText(QCoreApplication.translate("MainWindow", u"Current: ", None))
        self.CurrentText.setText(QCoreApplication.translate("MainWindow", u"pos", None))
        self.d1.setText(QCoreApplication.translate("MainWindow", u"D1: ", None))
        self.LaserInfoText.setText(QCoreApplication.translate("MainWindow", u"Laser Info", None))
        self.d2.setText(QCoreApplication.translate("MainWindow", u"D2: ", None))
        self.h1.setText(QCoreApplication.translate("MainWindow", u"H1: ", None))
        self.RecordDataButton.setText(QCoreApplication.translate("MainWindow", u"Record Data", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Production Record", None))
        self.MotorPageButton.setText(QCoreApplication.translate("MainWindow", u"Motor", None))
        self.VisionPageButton.setText(QCoreApplication.translate("MainWindow", u"Vision", None))
        self.ClipperPageButton.setText(QCoreApplication.translate("MainWindow", u"Clipper", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"MOTOR", None))
        self.VisionTextPlaceholder.setText(QCoreApplication.translate("MainWindow", u"Vision", None))
        self.TakePictureButton.setText(QCoreApplication.translate("MainWindow", u"TAKE PICTURE", None))
        self.SaveButton.setText(QCoreApplication.translate("MainWindow", u"SAVE", None))
        self.CancelButton.setText(QCoreApplication.translate("MainWindow", u"CANCEL", None))
        self.RougAlignmentButton.setText(QCoreApplication.translate("MainWindow", u"Rough Alignment", None))
        self.PreciseAlignmentButton.setText(QCoreApplication.translate("MainWindow", u"Precise Alignment", None))
        self.PictureButton.setText(QCoreApplication.translate("MainWindow", u"Picture", None))
        self.OptionsButton.setText(QCoreApplication.translate("MainWindow", u"Options", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Clipper", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Logs", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"System Settings", None))
        self.WorkOrderText.setText(QCoreApplication.translate("MainWindow", u"\u5de5\u55ae:", None))
        self.WorkOrderNumberInput.setText(QCoreApplication.translate("MainWindow", u"12345678", None))
        self.MainPageButton.setText(QCoreApplication.translate("MainWindow", u"Main Page", None))
        self.LogsButton.setText(QCoreApplication.translate("MainWindow", u"Logs", None))
        self.ProductionRecordButton.setText(QCoreApplication.translate("MainWindow", u"Production\n"
"Record", None))
        self.ComponentControlButton.setText(QCoreApplication.translate("MainWindow", u"Component\n"
"Control", None))
        self.RecipeText.setText(QCoreApplication.translate("MainWindow", u"Recipe:", None))
        self.RecipeNameInput.setText(QCoreApplication.translate("MainWindow", u"Battery ASSY", None))
        self.QuantityText.setText(QCoreApplication.translate("MainWindow", u"Quantity:", None))
        self.QuantityNumberInput.setText(QCoreApplication.translate("MainWindow", u"200", None))
        self.WorkerNameText.setText(QCoreApplication.translate("MainWindow", u"\u7d44\u88dd\u4eba\u54e1:", None))
        self.WorkerNameInput.setText(QCoreApplication.translate("MainWindow", u"Carlos", None))
        self.CartHeightText.setText(QCoreApplication.translate("MainWindow", u"Cart Height:", None))
        self.CartHeightInput.setText(QCoreApplication.translate("MainWindow", u"153.3 mm", None))
        self.CartDepthText.setText(QCoreApplication.translate("MainWindow", u"Cart Depth:", None))
        self.CartDepthInput.setText(QCoreApplication.translate("MainWindow", u"200.1 mm", None))
        self.DateText.setText(QCoreApplication.translate("MainWindow", u"Date:", None))
        self.DateInput.setText(QCoreApplication.translate("MainWindow", u"7/25/2025", None))
    # retranslateUi

