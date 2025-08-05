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
    QScrollArea, QSizePolicy, QSlider, QStackedWidget,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 799)
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
        self.BackgroundWidget.setStyleSheet(u"QPushButton {\n"
"    padding: 6px 12px;\n"
"    background-color: #000000;\n"
"    color: white;\n"
"    border: 1px solid #444;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(11, 118, 160, 0.3); /* soft blue overlay */\n"
"    border: 1px solid #0B76A0;\n"
"}\n"
"\n"
"\n"
"QPushButton:checked {\n"
"    background-color: #0B76A0;\n"
"    border: 1px solid #0B76A0;\n"
"}\n"
"\n"
"QLabel {\n"
"	color:white;\n"
"}")
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
        self.SystemSettingsButton.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/icons/white/settings.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
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
        self.DeltaLogo.setPixmap(QPixmap(u":/images/delta-logo.png"))
        self.DeltaLogo.setScaledContents(True)
        self.MenuButtons = QWidget(self.BackgroundWidget)
        self.MenuButtons.setObjectName(u"MenuButtons")
        self.MenuButtons.setGeometry(QRect(10, 170, 221, 461))
        self.verticalLayout_11 = QVBoxLayout(self.MenuButtons)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.MainPageButton = QPushButton(self.MenuButtons)
        self.MenuButtonGroup.addButton(self.MainPageButton)
        self.MainPageButton.setObjectName(u"MainPageButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MainPageButton.sizePolicy().hasHeightForWidth())
        self.MainPageButton.setSizePolicy(sizePolicy)
        self.MainPageButton.setFont(font)
        self.MainPageButton.setAutoFillBackground(False)
        self.MainPageButton.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/white/home-simple-door.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.MainPageButton.setIcon(icon1)
        self.MainPageButton.setCheckable(True)
        self.MainPageButton.setChecked(True)

        self.verticalLayout_11.addWidget(self.MainPageButton)

        self.ComponentControlButton = QPushButton(self.MenuButtons)
        self.MenuButtonGroup.addButton(self.ComponentControlButton)
        self.ComponentControlButton.setObjectName(u"ComponentControlButton")
        sizePolicy.setHeightForWidth(self.ComponentControlButton.sizePolicy().hasHeightForWidth())
        self.ComponentControlButton.setSizePolicy(sizePolicy)
        self.ComponentControlButton.setFont(font)
        self.ComponentControlButton.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/icons/white/dimmer-switch.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.ComponentControlButton.setIcon(icon2)
        self.ComponentControlButton.setCheckable(True)

        self.verticalLayout_11.addWidget(self.ComponentControlButton)

        self.ProductionRecordButton = QPushButton(self.MenuButtons)
        self.MenuButtonGroup.addButton(self.ProductionRecordButton)
        self.ProductionRecordButton.setObjectName(u"ProductionRecordButton")
        sizePolicy.setHeightForWidth(self.ProductionRecordButton.sizePolicy().hasHeightForWidth())
        self.ProductionRecordButton.setSizePolicy(sizePolicy)
        self.ProductionRecordButton.setFont(font)
        self.ProductionRecordButton.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/icons/white/page.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.ProductionRecordButton.setIcon(icon3)
        self.ProductionRecordButton.setCheckable(True)

        self.verticalLayout_11.addWidget(self.ProductionRecordButton)

        self.LogsButton = QPushButton(self.MenuButtons)
        self.MenuButtonGroup.addButton(self.LogsButton)
        self.LogsButton.setObjectName(u"LogsButton")
        sizePolicy.setHeightForWidth(self.LogsButton.sizePolicy().hasHeightForWidth())
        self.LogsButton.setSizePolicy(sizePolicy)
        self.LogsButton.setFont(font)
        self.LogsButton.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u":/icons/white/multiple-pages.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.LogsButton.setIcon(icon4)
        self.LogsButton.setCheckable(True)

        self.verticalLayout_11.addWidget(self.LogsButton)

        self.ParentStackedWidgetToChangeMenuOptions = QStackedWidget(self.BackgroundWidget)
        self.ParentStackedWidgetToChangeMenuOptions.setObjectName(u"ParentStackedWidgetToChangeMenuOptions")
        self.ParentStackedWidgetToChangeMenuOptions.setGeometry(QRect(240, 80, 1021, 691))
        font1 = QFont()
        font1.setPointSize(18)
        self.ParentStackedWidgetToChangeMenuOptions.setFont(font1)
        self.ParentStackedWidgetToChangeMenuOptions.setStyleSheet(u"")
        self.MainPagePage = QWidget()
        self.MainPagePage.setObjectName(u"MainPagePage")
        self.CameraWidget = QWidget(self.MainPagePage)
        self.CameraWidget.setObjectName(u"CameraWidget")
        self.CameraWidget.setGeometry(QRect(0, 10, 701, 481))
        self.CameraWidget.setStyleSheet(u"background-color: #000000;")
        self.horizontalLayout_2 = QHBoxLayout(self.CameraWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.VisionText = QLabel(self.CameraWidget)
        self.VisionText.setObjectName(u"VisionText")
        self.VisionText.setStyleSheet(u"color:white;")
        self.VisionText.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.VisionText, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

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
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Timeline.sizePolicy().hasHeightForWidth())
        self.Timeline.setSizePolicy(sizePolicy1)
        self.Timeline.setStyleSheet(u"")
        self.Timeline.setFrameShape(QFrame.Shape.StyledPanel)
        self.Timeline.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.Timeline)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.StartWidget = QWidget(self.Timeline)
        self.StartWidget.setObjectName(u"StartWidget")
        self.verticalLayout_2 = QVBoxLayout(self.StartWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.StartProcessText = QLabel(self.StartWidget)
        self.StartProcessText.setObjectName(u"StartProcessText")
        self.StartProcessText.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.StartProcessText)

        self.StartCircle = QLabel(self.StartWidget)
        self.StartCircle.setObjectName(u"StartCircle")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.StartCircle.sizePolicy().hasHeightForWidth())
        self.StartCircle.setSizePolicy(sizePolicy2)
        self.StartCircle.setPixmap(QPixmap(u":/icons/white/timeline-circle.svg"))
        self.StartCircle.setScaledContents(True)
        self.StartCircle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.StartCircle, 0, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout_3.addWidget(self.StartWidget, 0, Qt.AlignmentFlag.AlignVCenter)

        self.ConnectWidget = QWidget(self.Timeline)
        self.ConnectWidget.setObjectName(u"ConnectWidget")
        self.verticalLayout = QVBoxLayout(self.ConnectWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.ConnectProcessText = QLabel(self.ConnectWidget)
        self.ConnectProcessText.setObjectName(u"ConnectProcessText")
        self.ConnectProcessText.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.ConnectProcessText)

        self.ConnectCircle = QLabel(self.ConnectWidget)
        self.ConnectCircle.setObjectName(u"ConnectCircle")
        sizePolicy2.setHeightForWidth(self.ConnectCircle.sizePolicy().hasHeightForWidth())
        self.ConnectCircle.setSizePolicy(sizePolicy2)
        self.ConnectCircle.setPixmap(QPixmap(u":/icons/white/timeline-circle.svg"))
        self.ConnectCircle.setScaledContents(True)
        self.ConnectCircle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.ConnectCircle, 0, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout_3.addWidget(self.ConnectWidget, 0, Qt.AlignmentFlag.AlignVCenter)

        self.INITWidget = QWidget(self.Timeline)
        self.INITWidget.setObjectName(u"INITWidget")
        self.verticalLayout_3 = QVBoxLayout(self.INITWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.INITProcessText = QLabel(self.INITWidget)
        self.INITProcessText.setObjectName(u"INITProcessText")
        self.INITProcessText.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.INITProcessText)

        self.INITCircle = QLabel(self.INITWidget)
        self.INITCircle.setObjectName(u"INITCircle")
        sizePolicy2.setHeightForWidth(self.INITCircle.sizePolicy().hasHeightForWidth())
        self.INITCircle.setSizePolicy(sizePolicy2)
        self.INITCircle.setPixmap(QPixmap(u":/icons/white/timeline-circle.svg"))
        self.INITCircle.setScaledContents(True)
        self.INITCircle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.INITCircle, 0, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout_3.addWidget(self.INITWidget, 0, Qt.AlignmentFlag.AlignVCenter)

        self.IdleWidget = QWidget(self.Timeline)
        self.IdleWidget.setObjectName(u"IdleWidget")
        self.verticalLayout_6 = QVBoxLayout(self.IdleWidget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.IdleProcessText = QLabel(self.IdleWidget)
        self.IdleProcessText.setObjectName(u"IdleProcessText")
        self.IdleProcessText.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.IdleProcessText)

        self.IdleCircle = QLabel(self.IdleWidget)
        self.IdleCircle.setObjectName(u"IdleCircle")
        sizePolicy2.setHeightForWidth(self.IdleCircle.sizePolicy().hasHeightForWidth())
        self.IdleCircle.setSizePolicy(sizePolicy2)
        self.IdleCircle.setPixmap(QPixmap(u":/icons/white/timeline-circle.svg"))
        self.IdleCircle.setScaledContents(True)
        self.IdleCircle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.IdleCircle, 0, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout_3.addWidget(self.IdleWidget, 0, Qt.AlignmentFlag.AlignVCenter)

        self.ManualAlignWidget = QWidget(self.Timeline)
        self.ManualAlignWidget.setObjectName(u"ManualAlignWidget")
        self.verticalLayout_7 = QVBoxLayout(self.ManualAlignWidget)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.RoughAlignProcessText = QLabel(self.ManualAlignWidget)
        self.RoughAlignProcessText.setObjectName(u"RoughAlignProcessText")
        self.RoughAlignProcessText.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_7.addWidget(self.RoughAlignProcessText)

        self.RoughAlignCircle = QLabel(self.ManualAlignWidget)
        self.RoughAlignCircle.setObjectName(u"RoughAlignCircle")
        sizePolicy2.setHeightForWidth(self.RoughAlignCircle.sizePolicy().hasHeightForWidth())
        self.RoughAlignCircle.setSizePolicy(sizePolicy2)
        self.RoughAlignCircle.setPixmap(QPixmap(u":/icons/white/timeline-circle.svg"))
        self.RoughAlignCircle.setScaledContents(True)
        self.RoughAlignCircle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_7.addWidget(self.RoughAlignCircle, 0, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout_3.addWidget(self.ManualAlignWidget, 0, Qt.AlignmentFlag.AlignVCenter)

        self.AutoAlignWidget = QWidget(self.Timeline)
        self.AutoAlignWidget.setObjectName(u"AutoAlignWidget")
        self.verticalLayout_8 = QVBoxLayout(self.AutoAlignWidget)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.PreciseAlignProcessText = QLabel(self.AutoAlignWidget)
        self.PreciseAlignProcessText.setObjectName(u"PreciseAlignProcessText")
        self.PreciseAlignProcessText.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_8.addWidget(self.PreciseAlignProcessText)

        self.PreciseAlignCircle = QLabel(self.AutoAlignWidget)
        self.PreciseAlignCircle.setObjectName(u"PreciseAlignCircle")
        sizePolicy2.setHeightForWidth(self.PreciseAlignCircle.sizePolicy().hasHeightForWidth())
        self.PreciseAlignCircle.setSizePolicy(sizePolicy2)
        self.PreciseAlignCircle.setPixmap(QPixmap(u":/icons/white/timeline-circle.svg"))
        self.PreciseAlignCircle.setScaledContents(True)
        self.PreciseAlignCircle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_8.addWidget(self.PreciseAlignCircle, 0, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout_3.addWidget(self.AutoAlignWidget, 0, Qt.AlignmentFlag.AlignVCenter)

        self.AutoPickWidget = QWidget(self.Timeline)
        self.AutoPickWidget.setObjectName(u"AutoPickWidget")
        self.verticalLayout_9 = QVBoxLayout(self.AutoPickWidget)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.PickProcessText = QLabel(self.AutoPickWidget)
        self.PickProcessText.setObjectName(u"PickProcessText")
        self.PickProcessText.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_9.addWidget(self.PickProcessText)

        self.PickCircle = QLabel(self.AutoPickWidget)
        self.PickCircle.setObjectName(u"PickCircle")
        sizePolicy2.setHeightForWidth(self.PickCircle.sizePolicy().hasHeightForWidth())
        self.PickCircle.setSizePolicy(sizePolicy2)
        self.PickCircle.setPixmap(QPixmap(u":/icons/white/timeline-circle.svg"))
        self.PickCircle.setScaledContents(True)
        self.PickCircle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_9.addWidget(self.PickCircle, 0, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout_3.addWidget(self.AutoPickWidget, 0, Qt.AlignmentFlag.AlignVCenter)

        self.AssemblyWidget = QWidget(self.Timeline)
        self.AssemblyWidget.setObjectName(u"AssemblyWidget")
        self.verticalLayout_4 = QVBoxLayout(self.AssemblyWidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.AssemblyProcessText = QLabel(self.AssemblyWidget)
        self.AssemblyProcessText.setObjectName(u"AssemblyProcessText")
        self.AssemblyProcessText.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.AssemblyProcessText, 0, Qt.AlignmentFlag.AlignTop)

        self.AssemblyCircle = QLabel(self.AssemblyWidget)
        self.AssemblyCircle.setObjectName(u"AssemblyCircle")
        sizePolicy2.setHeightForWidth(self.AssemblyCircle.sizePolicy().hasHeightForWidth())
        self.AssemblyCircle.setSizePolicy(sizePolicy2)
        self.AssemblyCircle.setPixmap(QPixmap(u":/icons/white/timeline-circle.svg"))
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
        sizePolicy1.setHeightForWidth(self.CartesianPoseWidget.sizePolicy().hasHeightForWidth())
        self.CartesianPoseWidget.setSizePolicy(sizePolicy1)
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
        font2 = QFont()
        font2.setPointSize(9)
        self.y.setFont(font2)

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
        self.z.setFont(font2)

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
        self.yaw.setFont(font2)

        self.horizontalLayout_12.addWidget(self.yaw, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.yawText = QLabel(self.yawPosFrame)
        self.yawText.setObjectName(u"yawText")

        self.horizontalLayout_12.addWidget(self.yawText, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)


        self.gridLayout.addWidget(self.yawPosFrame, 2, 1, 1, 1)

        self.CartesianPoseText = QLabel(self.CartesianPoseWidget)
        self.CartesianPoseText.setObjectName(u"CartesianPoseText")
        font3 = QFont()
        font3.setPointSize(10)
        self.CartesianPoseText.setFont(font3)
        self.CartesianPoseText.setStyleSheet(u"border: 2px solid #FFFFFF;  /* white solid border */\n"
"border-radius: 6px;")

        self.gridLayout.addWidget(self.CartesianPoseText, 0, 0, 1, 2, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.xPosFrame = QFrame(self.CartesianPoseWidget)
        self.xPosFrame.setObjectName(u"xPosFrame")
        self.xPosFrame.setFont(font2)
        self.xPosFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.xPosFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.xPosFrame)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(9, -1, -1, 3)
        self.x = QLabel(self.xPosFrame)
        self.x.setObjectName(u"x")
        self.x.setFont(font2)

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
        self.MotorInfoText.setFont(font3)
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
        self.LaserInfoText.setFont(font3)
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
        sizePolicy1.setHeightForWidth(self.RecordDataButtonContainer.sizePolicy().hasHeightForWidth())
        self.RecordDataButtonContainer.setSizePolicy(sizePolicy1)
        self.verticalLayout_16 = QVBoxLayout(self.RecordDataButtonContainer)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(9, 9, -1, -1)
        self.RecordDataButton = QPushButton(self.RecordDataButtonContainer)
        self.RecordDataButton.setObjectName(u"RecordDataButton")
        sizePolicy1.setHeightForWidth(self.RecordDataButton.sizePolicy().hasHeightForWidth())
        self.RecordDataButton.setSizePolicy(sizePolicy1)
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
        self.AutoAndManualStackedWidget = QStackedWidget(self.MainPagePage)
        self.AutoAndManualStackedWidget.setObjectName(u"AutoAndManualStackedWidget")
        self.AutoAndManualStackedWidget.setGeometry(QRect(720, 10, 291, 681))
        self.AutoAndManualStackedWidget.setFrameShape(QFrame.Shape.StyledPanel)
        self.AutoAndManualStackedWidget.setFrameShadow(QFrame.Shadow.Raised)
        self.BeforeAutoAndManualPage = QWidget()
        self.BeforeAutoAndManualPage.setObjectName(u"BeforeAutoAndManualPage")
        self.verticalLayout_25 = QVBoxLayout(self.BeforeAutoAndManualPage)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.INITBefore = QPushButton(self.BeforeAutoAndManualPage)
        self.INITBefore.setObjectName(u"INITBefore")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.INITBefore.sizePolicy().hasHeightForWidth())
        self.INITBefore.setSizePolicy(sizePolicy3)
        self.INITBefore.setMinimumSize(QSize(0, 0))
        self.INITBefore.setMaximumSize(QSize(271, 150))
        self.INITBefore.setSizeIncrement(QSize(0, 0))
        self.INITBefore.setBaseSize(QSize(0, 0))
        self.INITBefore.setFont(font)
        self.INITBefore.setStyleSheet(u"")
        self.INITBefore.setCheckable(False)

        self.verticalLayout_25.addWidget(self.INITBefore)

        self.StopBefore = QPushButton(self.BeforeAutoAndManualPage)
        self.StopBefore.setObjectName(u"StopBefore")
        sizePolicy3.setHeightForWidth(self.StopBefore.sizePolicy().hasHeightForWidth())
        self.StopBefore.setSizePolicy(sizePolicy3)
        self.StopBefore.setMinimumSize(QSize(0, 0))
        self.StopBefore.setMaximumSize(QSize(271, 150))
        self.StopBefore.setSizeIncrement(QSize(0, 0))
        self.StopBefore.setBaseSize(QSize(0, 0))
        self.StopBefore.setFont(font)
        self.StopBefore.setStyleSheet(u"")
        self.StopBefore.setCheckable(False)

        self.verticalLayout_25.addWidget(self.StopBefore)

        self.AutoAndManualStackedWidget.addWidget(self.BeforeAutoAndManualPage)
        self.ChooseAutoOrManualPage = QWidget()
        self.ChooseAutoOrManualPage.setObjectName(u"ChooseAutoOrManualPage")
        self.verticalLayout_26 = QVBoxLayout(self.ChooseAutoOrManualPage)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.ChooseAutoButton = QPushButton(self.ChooseAutoOrManualPage)
        self.ChooseAutoButton.setObjectName(u"ChooseAutoButton")
        sizePolicy3.setHeightForWidth(self.ChooseAutoButton.sizePolicy().hasHeightForWidth())
        self.ChooseAutoButton.setSizePolicy(sizePolicy3)
        self.ChooseAutoButton.setMinimumSize(QSize(0, 0))
        self.ChooseAutoButton.setMaximumSize(QSize(271, 150))
        self.ChooseAutoButton.setSizeIncrement(QSize(0, 0))
        self.ChooseAutoButton.setBaseSize(QSize(0, 0))
        self.ChooseAutoButton.setFont(font)
        self.ChooseAutoButton.setStyleSheet(u"")
        self.ChooseAutoButton.setCheckable(False)

        self.verticalLayout_26.addWidget(self.ChooseAutoButton)

        self.ChooseManualButton = QPushButton(self.ChooseAutoOrManualPage)
        self.ChooseManualButton.setObjectName(u"ChooseManualButton")
        sizePolicy3.setHeightForWidth(self.ChooseManualButton.sizePolicy().hasHeightForWidth())
        self.ChooseManualButton.setSizePolicy(sizePolicy3)
        self.ChooseManualButton.setMinimumSize(QSize(0, 0))
        self.ChooseManualButton.setMaximumSize(QSize(271, 150))
        self.ChooseManualButton.setSizeIncrement(QSize(0, 0))
        self.ChooseManualButton.setBaseSize(QSize(0, 0))
        self.ChooseManualButton.setFont(font)
        self.ChooseManualButton.setStyleSheet(u"")
        self.ChooseManualButton.setCheckable(False)

        self.verticalLayout_26.addWidget(self.ChooseManualButton)

        self.AutoAndManualStackedWidget.addWidget(self.ChooseAutoOrManualPage)
        self.ActionButtonsMainPage = QWidget()
        self.ActionButtonsMainPage.setObjectName(u"ActionButtonsMainPage")
        self.verticalLayout_24 = QVBoxLayout(self.ActionButtonsMainPage)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.AutoManualButtons = QWidget(self.ActionButtonsMainPage)
        self.AutoManualButtons.setObjectName(u"AutoManualButtons")
        self.horizontalLayout_5 = QHBoxLayout(self.AutoManualButtons)
        self.horizontalLayout_5.setSpacing(25)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.AutoButton = QPushButton(self.AutoManualButtons)
        self.AutoAndManualButtonGroup = QButtonGroup(MainWindow)
        self.AutoAndManualButtonGroup.setObjectName(u"AutoAndManualButtonGroup")
        self.AutoAndManualButtonGroup.addButton(self.AutoButton)
        self.AutoButton.setObjectName(u"AutoButton")
        sizePolicy.setHeightForWidth(self.AutoButton.sizePolicy().hasHeightForWidth())
        self.AutoButton.setSizePolicy(sizePolicy)
        self.AutoButton.setMinimumSize(QSize(0, 74))
        self.AutoButton.setFont(font)
        self.AutoButton.setStyleSheet(u"")
        self.AutoButton.setCheckable(True)
        self.AutoButton.setChecked(False)

        self.horizontalLayout_5.addWidget(self.AutoButton)

        self.ManualButton = QPushButton(self.AutoManualButtons)
        self.AutoAndManualButtonGroup.addButton(self.ManualButton)
        self.ManualButton.setObjectName(u"ManualButton")
        sizePolicy.setHeightForWidth(self.ManualButton.sizePolicy().hasHeightForWidth())
        self.ManualButton.setSizePolicy(sizePolicy)
        self.ManualButton.setMinimumSize(QSize(0, 74))
        self.ManualButton.setFont(font)
        self.ManualButton.setStyleSheet(u"")
        self.ManualButton.setCheckable(True)
        self.ManualButton.setChecked(False)

        self.horizontalLayout_5.addWidget(self.ManualButton)


        self.verticalLayout_24.addWidget(self.AutoManualButtons)

        self.ActionButtons = QStackedWidget(self.ActionButtonsMainPage)
        self.ActionButtons.setObjectName(u"ActionButtons")
        self.ActionButtons.setStyleSheet(u"")
        self.ActionButtonsPage = QWidget()
        self.ActionButtonsPage.setObjectName(u"ActionButtonsPage")
        self.verticalLayout_12 = QVBoxLayout(self.ActionButtonsPage)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.INITButton = QPushButton(self.ActionButtonsPage)
        self.INITButton.setObjectName(u"INITButton")
        sizePolicy.setHeightForWidth(self.INITButton.sizePolicy().hasHeightForWidth())
        self.INITButton.setSizePolicy(sizePolicy)
        self.INITButton.setFont(font)
        self.INITButton.setStyleSheet(u"")

        self.verticalLayout_12.addWidget(self.INITButton)

        self.RunButton = QPushButton(self.ActionButtonsPage)
        self.RunButton.setObjectName(u"RunButton")
        sizePolicy.setHeightForWidth(self.RunButton.sizePolicy().hasHeightForWidth())
        self.RunButton.setSizePolicy(sizePolicy)
        self.RunButton.setFont(font)
        self.RunButton.setStyleSheet(u"")

        self.verticalLayout_12.addWidget(self.RunButton)

        self.verticalLayoutAutoPauseAndStop = QVBoxLayout()
        self.verticalLayoutAutoPauseAndStop.setSpacing(6)
        self.verticalLayoutAutoPauseAndStop.setObjectName(u"verticalLayoutAutoPauseAndStop")
        self.verticalLayoutAutoPauseAndStop.setContentsMargins(-1, 37, -1, -1)
        self.AutoPauseButton = QPushButton(self.ActionButtonsPage)
        self.AutoPauseButton.setObjectName(u"AutoPauseButton")
        sizePolicy.setHeightForWidth(self.AutoPauseButton.sizePolicy().hasHeightForWidth())
        self.AutoPauseButton.setSizePolicy(sizePolicy)
        self.AutoPauseButton.setFont(font)
        self.AutoPauseButton.setStyleSheet(u"")
        self.AutoPauseButton.setCheckable(True)

        self.verticalLayoutAutoPauseAndStop.addWidget(self.AutoPauseButton)

        self.AutoStopButton = QPushButton(self.ActionButtonsPage)
        self.AutoStopButton.setObjectName(u"AutoStopButton")
        sizePolicy.setHeightForWidth(self.AutoStopButton.sizePolicy().hasHeightForWidth())
        self.AutoStopButton.setSizePolicy(sizePolicy)
        self.AutoStopButton.setFont(font)
        self.AutoStopButton.setStyleSheet(u"")
        self.AutoStopButton.setCheckable(False)

        self.verticalLayoutAutoPauseAndStop.addWidget(self.AutoStopButton)


        self.verticalLayout_12.addLayout(self.verticalLayoutAutoPauseAndStop)

        self.ActionButtons.addWidget(self.ActionButtonsPage)
        self.ManualButtonsPage = QWidget()
        self.ManualButtonsPage.setObjectName(u"ManualButtonsPage")
        self.ManualButtonsPage.setStyleSheet(u"")
        self.verticalLayout_20 = QVBoxLayout(self.ManualButtonsPage)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.RoughAlignButton = QPushButton(self.ManualButtonsPage)
        self.ManualButtons = QButtonGroup(MainWindow)
        self.ManualButtons.setObjectName(u"ManualButtons")
        self.ManualButtons.addButton(self.RoughAlignButton)
        self.RoughAlignButton.setObjectName(u"RoughAlignButton")
        sizePolicy.setHeightForWidth(self.RoughAlignButton.sizePolicy().hasHeightForWidth())
        self.RoughAlignButton.setSizePolicy(sizePolicy)
        self.RoughAlignButton.setMaximumSize(QSize(16777215, 90))
        self.RoughAlignButton.setFont(font)
        self.RoughAlignButton.setStyleSheet(u"")
        self.RoughAlignButton.setCheckable(True)

        self.verticalLayout_20.addWidget(self.RoughAlignButton)

        self.PreciseAlignButton = QPushButton(self.ManualButtonsPage)
        self.ManualButtons.addButton(self.PreciseAlignButton)
        self.PreciseAlignButton.setObjectName(u"PreciseAlignButton")
        sizePolicy.setHeightForWidth(self.PreciseAlignButton.sizePolicy().hasHeightForWidth())
        self.PreciseAlignButton.setSizePolicy(sizePolicy)
        self.PreciseAlignButton.setMaximumSize(QSize(16777215, 90))
        self.PreciseAlignButton.setFont(font)
        self.PreciseAlignButton.setStyleSheet(u"")
        self.PreciseAlignButton.setCheckable(True)

        self.verticalLayout_20.addWidget(self.PreciseAlignButton)

        self.PickButton = QPushButton(self.ManualButtonsPage)
        self.ManualButtons.addButton(self.PickButton)
        self.PickButton.setObjectName(u"PickButton")
        sizePolicy.setHeightForWidth(self.PickButton.sizePolicy().hasHeightForWidth())
        self.PickButton.setSizePolicy(sizePolicy)
        self.PickButton.setMaximumSize(QSize(16777215, 90))
        self.PickButton.setFont(font)
        self.PickButton.setStyleSheet(u"")
        self.PickButton.setCheckable(True)

        self.verticalLayout_20.addWidget(self.PickButton)

        self.AssemblyButton = QPushButton(self.ManualButtonsPage)
        self.ManualButtons.addButton(self.AssemblyButton)
        self.AssemblyButton.setObjectName(u"AssemblyButton")
        sizePolicy.setHeightForWidth(self.AssemblyButton.sizePolicy().hasHeightForWidth())
        self.AssemblyButton.setSizePolicy(sizePolicy)
        self.AssemblyButton.setMaximumSize(QSize(16777215, 90))
        self.AssemblyButton.setFont(font)
        self.AssemblyButton.setStyleSheet(u"")
        self.AssemblyButton.setCheckable(True)

        self.verticalLayout_20.addWidget(self.AssemblyButton)

        self.verticalLayoutManualButtons = QVBoxLayout()
        self.verticalLayoutManualButtons.setObjectName(u"verticalLayoutManualButtons")
        self.verticalLayoutManualButtons.setContentsMargins(-1, 22, -1, -1)
        self.ManualPauseButton = QPushButton(self.ManualButtonsPage)
        self.ManualPauseButton.setObjectName(u"ManualPauseButton")
        sizePolicy.setHeightForWidth(self.ManualPauseButton.sizePolicy().hasHeightForWidth())
        self.ManualPauseButton.setSizePolicy(sizePolicy)
        self.ManualPauseButton.setMaximumSize(QSize(16777215, 90))
        self.ManualPauseButton.setFont(font)
        self.ManualPauseButton.setStyleSheet(u"")
        self.ManualPauseButton.setCheckable(True)

        self.verticalLayoutManualButtons.addWidget(self.ManualPauseButton)

        self.ManualStopButton = QPushButton(self.ManualButtonsPage)
        self.ManualStopButton.setObjectName(u"ManualStopButton")
        sizePolicy.setHeightForWidth(self.ManualStopButton.sizePolicy().hasHeightForWidth())
        self.ManualStopButton.setSizePolicy(sizePolicy)
        self.ManualStopButton.setMaximumSize(QSize(16777215, 90))
        self.ManualStopButton.setFont(font)
        self.ManualStopButton.setStyleSheet(u"")
        self.ManualStopButton.setCheckable(True)

        self.verticalLayoutManualButtons.addWidget(self.ManualStopButton)


        self.verticalLayout_20.addLayout(self.verticalLayoutManualButtons)

        self.ActionButtons.addWidget(self.ManualButtonsPage)

        self.verticalLayout_24.addWidget(self.ActionButtons)

        self.AutoAndManualStackedWidget.addWidget(self.ActionButtonsMainPage)
        self.ParentStackedWidgetToChangeMenuOptions.addWidget(self.MainPagePage)
        self.ComponentControlPage = QWidget()
        self.ComponentControlPage.setObjectName(u"ComponentControlPage")
        self.ComponentControlStackedWidget = QStackedWidget(self.ComponentControlPage)
        self.ComponentControlStackedWidget.setObjectName(u"ComponentControlStackedWidget")
        self.ComponentControlStackedWidget.setGeometry(QRect(710, 10, 311, 681))
        self.ComponentControlStackedWidget.setFrameShape(QFrame.Shape.StyledPanel)
        self.ComponentControlStackedWidget.setFrameShadow(QFrame.Shadow.Raised)
        self.BeforeComponentControl = QWidget()
        self.BeforeComponentControl.setObjectName(u"BeforeComponentControl")
        self.verticalLayout_28 = QVBoxLayout(self.BeforeComponentControl)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.ChooseListOptionsWidget = QWidget(self.BeforeComponentControl)
        self.ChooseListOptionsWidget.setObjectName(u"ChooseListOptionsWidget")
        sizePolicy1.setHeightForWidth(self.ChooseListOptionsWidget.sizePolicy().hasHeightForWidth())
        self.ChooseListOptionsWidget.setSizePolicy(sizePolicy1)
        self.verticalLayout_27 = QVBoxLayout(self.ChooseListOptionsWidget)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.ChooseMotor = QPushButton(self.ChooseListOptionsWidget)
        self.ChooseMotor.setObjectName(u"ChooseMotor")
        sizePolicy.setHeightForWidth(self.ChooseMotor.sizePolicy().hasHeightForWidth())
        self.ChooseMotor.setSizePolicy(sizePolicy)
        self.ChooseMotor.setStyleSheet(u"")

        self.verticalLayout_27.addWidget(self.ChooseMotor)

        self.ChooseVision = QPushButton(self.ChooseListOptionsWidget)
        self.ChooseVision.setObjectName(u"ChooseVision")
        sizePolicy.setHeightForWidth(self.ChooseVision.sizePolicy().hasHeightForWidth())
        self.ChooseVision.setSizePolicy(sizePolicy)
        self.ChooseVision.setStyleSheet(u"background-color: #000000;")

        self.verticalLayout_27.addWidget(self.ChooseVision)

        self.ChooseClipper = QPushButton(self.ChooseListOptionsWidget)
        self.ChooseClipper.setObjectName(u"ChooseClipper")
        sizePolicy.setHeightForWidth(self.ChooseClipper.sizePolicy().hasHeightForWidth())
        self.ChooseClipper.setSizePolicy(sizePolicy)
        self.ChooseClipper.setStyleSheet(u"")

        self.verticalLayout_27.addWidget(self.ChooseClipper)

        self.ChooseForklift = QPushButton(self.ChooseListOptionsWidget)
        self.ChooseForklift.setObjectName(u"ChooseForklift")
        sizePolicy.setHeightForWidth(self.ChooseForklift.sizePolicy().hasHeightForWidth())
        self.ChooseForklift.setSizePolicy(sizePolicy)
        self.ChooseForklift.setStyleSheet(u"")

        self.verticalLayout_27.addWidget(self.ChooseForklift)

        self.ChooseDIDO = QPushButton(self.ChooseListOptionsWidget)
        self.ChooseDIDO.setObjectName(u"ChooseDIDO")
        sizePolicy.setHeightForWidth(self.ChooseDIDO.sizePolicy().hasHeightForWidth())
        self.ChooseDIDO.setSizePolicy(sizePolicy)
        self.ChooseDIDO.setStyleSheet(u"")

        self.verticalLayout_27.addWidget(self.ChooseDIDO)


        self.verticalLayout_28.addWidget(self.ChooseListOptionsWidget)

        self.ComponentControlStackedWidget.addWidget(self.BeforeComponentControl)
        self.ComponentControlMain = QWidget()
        self.ComponentControlMain.setObjectName(u"ComponentControlMain")
        self.ComponentControlOptionsWidget = QWidget(self.ComponentControlMain)
        self.ComponentControlOptionsWidget.setObjectName(u"ComponentControlOptionsWidget")
        self.ComponentControlOptionsWidget.setGeometry(QRect(-10, -10, 291, 101))
        self.horizontalLayout_16 = QHBoxLayout(self.ComponentControlOptionsWidget)
        self.horizontalLayout_16.setSpacing(25)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.MotorStartedButton = QPushButton(self.ComponentControlOptionsWidget)
        self.MotorStartedButton.setObjectName(u"MotorStartedButton")
        sizePolicy1.setHeightForWidth(self.MotorStartedButton.sizePolicy().hasHeightForWidth())
        self.MotorStartedButton.setSizePolicy(sizePolicy1)
        self.MotorStartedButton.setStyleSheet(u"background-color: #0B76A0;")
        self.MotorStartedButton.setCheckable(False)
        self.MotorStartedButton.setChecked(False)

        self.horizontalLayout_16.addWidget(self.MotorStartedButton)

        self.HamburgerMenu = QPushButton(self.ComponentControlOptionsWidget)
        self.HamburgerMenu.setObjectName(u"HamburgerMenu")
        sizePolicy.setHeightForWidth(self.HamburgerMenu.sizePolicy().hasHeightForWidth())
        self.HamburgerMenu.setSizePolicy(sizePolicy)
        self.HamburgerMenu.setStyleSheet(u"")
        icon5 = QIcon()
        icon5.addFile(u":/icons/white/menu.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.HamburgerMenu.setIcon(icon5)
        self.HamburgerMenu.setIconSize(QSize(30, 30))

        self.horizontalLayout_16.addWidget(self.HamburgerMenu)

        self.ChangeComponentControlStackedWidget = QStackedWidget(self.ComponentControlMain)
        self.ChangeComponentControlStackedWidget.setObjectName(u"ChangeComponentControlStackedWidget")
        self.ChangeComponentControlStackedWidget.setGeometry(QRect(-10, 90, 321, 581))
        self.ChangeComponentControlStackedWidget.setStyleSheet(u"")
        self.MotorPage = QWidget()
        self.MotorPage.setObjectName(u"MotorPage")
        self.ControlUpCP = QPushButton(self.MotorPage)
        self.ControlUpCP.setObjectName(u"ControlUpCP")
        self.ControlUpCP.setGeometry(QRect(120, 40, 101, 91))
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.ControlUpCP.sizePolicy().hasHeightForWidth())
        self.ControlUpCP.setSizePolicy(sizePolicy4)
        self.ControlUpCP.setStyleSheet(u"background-color: transparent;\n"
"border: none;")
        icon6 = QIcon()
        icon6.addFile(u":/controlArrows/cartesian/up.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.ControlUpCP.setIcon(icon6)
        self.ControlUpCP.setIconSize(QSize(80, 80))
        self.ControlLeftCP = QPushButton(self.MotorPage)
        self.ControlLeftCP.setObjectName(u"ControlLeftCP")
        self.ControlLeftCP.setGeometry(QRect(20, 130, 101, 91))
        self.ControlLeftCP.setStyleSheet(u"background-color: transparent;\n"
"border: none;")
        icon7 = QIcon()
        icon7.addFile(u":/controlArrows/cartesian/left.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.ControlLeftCP.setIcon(icon7)
        self.ControlLeftCP.setIconSize(QSize(80, 80))
        self.ControlDownCP = QPushButton(self.MotorPage)
        self.ControlDownCP.setObjectName(u"ControlDownCP")
        self.ControlDownCP.setGeometry(QRect(120, 220, 101, 91))
        self.ControlDownCP.setStyleSheet(u"background-color: transparent;\n"
"border: none;")
        icon8 = QIcon()
        icon8.addFile(u":/controlArrows/cartesian/down.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.ControlDownCP.setIcon(icon8)
        self.ControlDownCP.setIconSize(QSize(80, 80))
        self.ControlRightCP = QPushButton(self.MotorPage)
        self.ControlRightCP.setObjectName(u"ControlRightCP")
        self.ControlRightCP.setGeometry(QRect(220, 130, 101, 91))
        self.ControlRightCP.setStyleSheet(u"background-color: transparent;\n"
"border: none;")
        icon9 = QIcon()
        icon9.addFile(u":/controlArrows/cartesian/right.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.ControlRightCP.setIcon(icon9)
        self.ControlRightCP.setIconSize(QSize(80, 80))
        self.YawPlusCP = QPushButton(self.MotorPage)
        self.YawPlusCP.setObjectName(u"YawPlusCP")
        self.YawPlusCP.setGeometry(QRect(220, 20, 101, 91))
        sizePolicy4.setHeightForWidth(self.YawPlusCP.sizePolicy().hasHeightForWidth())
        self.YawPlusCP.setSizePolicy(sizePolicy4)
        self.YawPlusCP.setStyleSheet(u"background-color: transparent;\n"
"border: none;")
        icon10 = QIcon()
        icon10.addFile(u":/controlArrows/cartesian/yawPlus.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.YawPlusCP.setIcon(icon10)
        self.YawPlusCP.setIconSize(QSize(80, 80))
        self.YawMinusCP = QPushButton(self.MotorPage)
        self.YawMinusCP.setObjectName(u"YawMinusCP")
        self.YawMinusCP.setGeometry(QRect(10, 240, 101, 91))
        sizePolicy4.setHeightForWidth(self.YawMinusCP.sizePolicy().hasHeightForWidth())
        self.YawMinusCP.setSizePolicy(sizePolicy4)
        self.YawMinusCP.setStyleSheet(u"background-color: transparent;\n"
"border: none;")
        icon11 = QIcon()
        icon11.addFile(u":/controlArrows/cartesian/yawMinus.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.YawMinusCP.setIcon(icon11)
        self.YawMinusCP.setIconSize(QSize(80, 80))
        self.YawMinusCP.setCheckable(False)
        self.ClipperAndResetWidget_3 = QWidget(self.MotorPage)
        self.ClipperAndResetWidget_3.setObjectName(u"ClipperAndResetWidget_3")
        self.ClipperAndResetWidget_3.setGeometry(QRect(0, 440, 311, 151))
        self.verticalLayout_10 = QVBoxLayout(self.ClipperAndResetWidget_3)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.ClipperButtonOnOff = QPushButton(self.ClipperAndResetWidget_3)
        self.ClipperButtonOnOff.setObjectName(u"ClipperButtonOnOff")
        self.ClipperButtonOnOff.setEnabled(True)
        sizePolicy.setHeightForWidth(self.ClipperButtonOnOff.sizePolicy().hasHeightForWidth())
        self.ClipperButtonOnOff.setSizePolicy(sizePolicy)
        self.ClipperButtonOnOff.setFont(font)
        self.ClipperButtonOnOff.setStyleSheet(u"QPushButton {\n"
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
        self.ClipperButtonOnOff.setCheckable(True)

        self.verticalLayout_10.addWidget(self.ClipperButtonOnOff)

        self.MotorResetButton = QPushButton(self.ClipperAndResetWidget_3)
        self.MotorResetButton.setObjectName(u"MotorResetButton")
        sizePolicy.setHeightForWidth(self.MotorResetButton.sizePolicy().hasHeightForWidth())
        self.MotorResetButton.setSizePolicy(sizePolicy)
        self.MotorResetButton.setFont(font)
        self.MotorResetButton.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout_10.addWidget(self.MotorResetButton)

        self.ChangeComponentControlStackedWidget.addWidget(self.MotorPage)
        self.VisionPage = QWidget()
        self.VisionPage.setObjectName(u"VisionPage")
        self.VisionOne = QPushButton(self.VisionPage)
        self.dete = QButtonGroup(MainWindow)
        self.dete.setObjectName(u"dete")
        self.dete.addButton(self.VisionOne)
        self.VisionOne.setObjectName(u"VisionOne")
        self.VisionOne.setGeometry(QRect(40, 150, 233, 79))
        sizePolicy.setHeightForWidth(self.VisionOne.sizePolicy().hasHeightForWidth())
        self.VisionOne.setSizePolicy(sizePolicy)
        self.VisionOne.setStyleSheet(u"")
        self.VisionOne.setCheckable(True)
        self.VisionTwo = QPushButton(self.VisionPage)
        self.dete.addButton(self.VisionTwo)
        self.VisionTwo.setObjectName(u"VisionTwo")
        self.VisionTwo.setGeometry(QRect(40, 260, 233, 79))
        sizePolicy.setHeightForWidth(self.VisionTwo.sizePolicy().hasHeightForWidth())
        self.VisionTwo.setSizePolicy(sizePolicy)
        self.VisionTwo.setStyleSheet(u"")
        self.VisionTwo.setCheckable(True)
        self.VisionThree = QPushButton(self.VisionPage)
        self.dete.addButton(self.VisionThree)
        self.VisionThree.setObjectName(u"VisionThree")
        self.VisionThree.setGeometry(QRect(40, 360, 233, 79))
        sizePolicy.setHeightForWidth(self.VisionThree.sizePolicy().hasHeightForWidth())
        self.VisionThree.setSizePolicy(sizePolicy)
        self.VisionThree.setStyleSheet(u"")
        self.VisionThree.setCheckable(True)
        self.ChangeComponentControlStackedWidget.addWidget(self.VisionPage)
        self.ClipperPage = QWidget()
        self.ClipperPage.setObjectName(u"ClipperPage")
        self.label_6 = QLabel(self.ClipperPage)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(130, 320, 67, 17))
        self.ChangeComponentControlStackedWidget.addWidget(self.ClipperPage)
        self.ForkliftPage = QWidget()
        self.ForkliftPage.setObjectName(u"ForkliftPage")
        self.LiftUp = QPushButton(self.ForkliftPage)
        self.buttonGroup_2 = QButtonGroup(MainWindow)
        self.buttonGroup_2.setObjectName(u"buttonGroup_2")
        self.buttonGroup_2.addButton(self.LiftUp)
        self.LiftUp.setObjectName(u"LiftUp")
        self.LiftUp.setGeometry(QRect(30, 490, 101, 91))
        sizePolicy4.setHeightForWidth(self.LiftUp.sizePolicy().hasHeightForWidth())
        self.LiftUp.setSizePolicy(sizePolicy4)
        self.LiftUp.setStyleSheet(u"background-color: transparent;\n"
"border: none;")
        icon12 = QIcon()
        icon12.addFile(u":/controlArrows/lift.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.LiftUp.setIcon(icon12)
        self.LiftUp.setIconSize(QSize(80, 80))
        self.LiftUp.setCheckable(False)
        self.LowerDown = QPushButton(self.ForkliftPage)
        self.buttonGroup_2.addButton(self.LowerDown)
        self.LowerDown.setObjectName(u"LowerDown")
        self.LowerDown.setGeometry(QRect(190, 490, 101, 91))
        sizePolicy4.setHeightForWidth(self.LowerDown.sizePolicy().hasHeightForWidth())
        self.LowerDown.setSizePolicy(sizePolicy4)
        self.LowerDown.setStyleSheet(u"background-color: transparent;\n"
"border: none;")
        icon13 = QIcon()
        icon13.addFile(u":/controlArrows/lower.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.LowerDown.setIcon(icon13)
        self.LowerDown.setIconSize(QSize(80, 80))
        self.LowerDown.setCheckable(False)
        self.SliderLift = QSlider(self.ForkliftPage)
        self.SliderLift.setObjectName(u"SliderLift")
        self.SliderLift.setGeometry(QRect(50, 320, 231, 41))
        self.SliderLift.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    height: 20px;\n"
"    background: #ccc;\n"
"    border-radius: 10px;\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background: #000000;\n"
"    border: 2px solid white;\n"
"    width: 40px;\n"
"    margin: -10px 0; /* center handle */\n"
"    border-radius: 10px;\n"
"}")
        self.SliderLift.setMinimum(80)
        self.SliderLift.setMaximum(1500)
        self.SliderLift.setSingleStep(10)
        self.SliderLift.setValue(123)
        self.SliderLift.setSliderPosition(123)
        self.SliderLift.setOrientation(Qt.Orientation.Horizontal)
        self.FastForktLiftButton = QPushButton(self.ForkliftPage)
        self.buttonGroup = QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.FastForktLiftButton)
        self.FastForktLiftButton.setObjectName(u"FastForktLiftButton")
        self.FastForktLiftButton.setGeometry(QRect(20, 190, 88, 71))
        self.FastForktLiftButton.setCheckable(True)
        self.SlowLiftButton = QPushButton(self.ForkliftPage)
        self.buttonGroup.addButton(self.SlowLiftButton)
        self.SlowLiftButton.setObjectName(u"SlowLiftButton")
        self.SlowLiftButton.setGeometry(QRect(220, 190, 88, 71))
        self.SlowLiftButton.setCheckable(True)
        self.RunForkliftButton = QPushButton(self.ForkliftPage)
        self.RunForkliftButton.setObjectName(u"RunForkliftButton")
        self.RunForkliftButton.setGeometry(QRect(30, 60, 111, 71))
        self.RunForkliftButton.setCheckable(True)
        self.StopForkliftButton = QPushButton(self.ForkliftPage)
        self.StopForkliftButton.setObjectName(u"StopForkliftButton")
        self.StopForkliftButton.setGeometry(QRect(170, 60, 121, 81))
        self.StopForkliftButton.setCheckable(False)
        self.label_2 = QLabel(self.ForkliftPage)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(130, 30, 67, 17))
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_4 = QLabel(self.ForkliftPage)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(130, 150, 67, 17))
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.SendForkliftCommand = QPushButton(self.ForkliftPage)
        self.SendForkliftCommand.setObjectName(u"SendForkliftCommand")
        self.SendForkliftCommand.setGeometry(QRect(40, 380, 241, 81))
        self.SendForkliftCommand.setCheckable(False)
        self.MediumLiftButton = QPushButton(self.ForkliftPage)
        self.buttonGroup.addButton(self.MediumLiftButton)
        self.MediumLiftButton.setObjectName(u"MediumLiftButton")
        self.MediumLiftButton.setGeometry(QRect(120, 190, 88, 71))
        self.MediumLiftButton.setCheckable(True)
        self.label_7 = QLabel(self.ForkliftPage)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(90, 280, 141, 20))
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ChangeComponentControlStackedWidget.addWidget(self.ForkliftPage)
        self.DIDOPage = QWidget()
        self.DIDOPage.setObjectName(u"DIDOPage")
        self.ChangeComponentControlStackedWidget.addWidget(self.DIDOPage)
        self.ListOptionsWidget = QWidget(self.ComponentControlMain)
        self.ListOptionsWidget.setObjectName(u"ListOptionsWidget")
        self.ListOptionsWidget.setGeometry(QRect(20, 100, 251, 391))
        sizePolicy1.setHeightForWidth(self.ListOptionsWidget.sizePolicy().hasHeightForWidth())
        self.ListOptionsWidget.setSizePolicy(sizePolicy1)
        self.verticalLayout_5 = QVBoxLayout(self.ListOptionsWidget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.MotorOption = QPushButton(self.ListOptionsWidget)
        self.MotorOption.setObjectName(u"MotorOption")
        sizePolicy.setHeightForWidth(self.MotorOption.sizePolicy().hasHeightForWidth())
        self.MotorOption.setSizePolicy(sizePolicy)
        self.MotorOption.setStyleSheet(u"")

        self.verticalLayout_5.addWidget(self.MotorOption)

        self.VisionOption = QPushButton(self.ListOptionsWidget)
        self.VisionOption.setObjectName(u"VisionOption")
        sizePolicy.setHeightForWidth(self.VisionOption.sizePolicy().hasHeightForWidth())
        self.VisionOption.setSizePolicy(sizePolicy)
        self.VisionOption.setStyleSheet(u"background-color: #000000;")

        self.verticalLayout_5.addWidget(self.VisionOption)

        self.ClipperOption = QPushButton(self.ListOptionsWidget)
        self.ClipperOption.setObjectName(u"ClipperOption")
        sizePolicy.setHeightForWidth(self.ClipperOption.sizePolicy().hasHeightForWidth())
        self.ClipperOption.setSizePolicy(sizePolicy)
        self.ClipperOption.setStyleSheet(u"")

        self.verticalLayout_5.addWidget(self.ClipperOption)

        self.ForkliftOption = QPushButton(self.ListOptionsWidget)
        self.ForkliftOption.setObjectName(u"ForkliftOption")
        sizePolicy.setHeightForWidth(self.ForkliftOption.sizePolicy().hasHeightForWidth())
        self.ForkliftOption.setSizePolicy(sizePolicy)
        self.ForkliftOption.setStyleSheet(u"")

        self.verticalLayout_5.addWidget(self.ForkliftOption)

        self.DIDOOption = QPushButton(self.ListOptionsWidget)
        self.DIDOOption.setObjectName(u"DIDOOption")
        sizePolicy.setHeightForWidth(self.DIDOOption.sizePolicy().hasHeightForWidth())
        self.DIDOOption.setSizePolicy(sizePolicy)
        self.DIDOOption.setStyleSheet(u"")

        self.verticalLayout_5.addWidget(self.DIDOOption)

        self.ComponentControlStackedWidget.addWidget(self.ComponentControlMain)
        self.MiddleStackedWidget = QStackedWidget(self.ComponentControlPage)
        self.MiddleStackedWidget.setObjectName(u"MiddleStackedWidget")
        self.MiddleStackedWidget.setGeometry(QRect(0, 10, 701, 681))
        self.VisionAndInfoPage = QWidget()
        self.VisionAndInfoPage.setObjectName(u"VisionAndInfoPage")
        self.CameraWidgetInComponentControl = QWidget(self.VisionAndInfoPage)
        self.CameraWidgetInComponentControl.setObjectName(u"CameraWidgetInComponentControl")
        self.CameraWidgetInComponentControl.setGeometry(QRect(0, 0, 701, 491))
        self.CameraWidgetInComponentControl.setStyleSheet(u"background-color: #000000;")
        self.horizontalLayout_15 = QHBoxLayout(self.CameraWidgetInComponentControl)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.VisionTextInComponentControl = QLabel(self.CameraWidgetInComponentControl)
        self.VisionTextInComponentControl.setObjectName(u"VisionTextInComponentControl")
        self.VisionTextInComponentControl.setStyleSheet(u"color:white;")
        self.VisionTextInComponentControl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_15.addWidget(self.VisionTextInComponentControl)

        self.Info_2 = QFrame(self.VisionAndInfoPage)
        self.Info_2.setObjectName(u"Info_2")
        self.Info_2.setGeometry(QRect(0, 500, 701, 191))
        self.Info_2.setStyleSheet(u" background-color: #000000; color: white;")
        self.Info_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.Info_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.Info_2)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(-1, 0, -1, 9)
        self.CartesianPoseWidget_2 = QWidget(self.Info_2)
        self.CartesianPoseWidget_2.setObjectName(u"CartesianPoseWidget_2")
        sizePolicy1.setHeightForWidth(self.CartesianPoseWidget_2.sizePolicy().hasHeightForWidth())
        self.CartesianPoseWidget_2.setSizePolicy(sizePolicy1)
        self.CartesianPoseWidget_2.setMinimumSize(QSize(0, 0))
        self.gridLayout_4 = QGridLayout(self.CartesianPoseWidget_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(-1, 6, -1, -1)
        self.yPosFrame_2 = QFrame(self.CartesianPoseWidget_2)
        self.yPosFrame_2.setObjectName(u"yPosFrame_2")
        self.yPosFrame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.yPosFrame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.yPosFrame_2)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(-1, -1, -1, 3)
        self.y_2 = QLabel(self.yPosFrame_2)
        self.y_2.setObjectName(u"y_2")
        self.y_2.setFont(font2)

        self.horizontalLayout_22.addWidget(self.y_2, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.yText_2 = QLabel(self.yPosFrame_2)
        self.yText_2.setObjectName(u"yText_2")

        self.horizontalLayout_22.addWidget(self.yText_2, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)


        self.gridLayout_4.addWidget(self.yPosFrame_2, 1, 1, 1, 1)

        self.zPosFrame_2 = QFrame(self.CartesianPoseWidget_2)
        self.zPosFrame_2.setObjectName(u"zPosFrame_2")
        self.zPosFrame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.zPosFrame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.zPosFrame_2)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(-1, -1, -1, 14)
        self.z_2 = QLabel(self.zPosFrame_2)
        self.z_2.setObjectName(u"z_2")
        self.z_2.setFont(font2)

        self.horizontalLayout_27.addWidget(self.z_2, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.zText_2 = QLabel(self.zPosFrame_2)
        self.zText_2.setObjectName(u"zText_2")

        self.horizontalLayout_27.addWidget(self.zText_2, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)


        self.gridLayout_4.addWidget(self.zPosFrame_2, 2, 0, 1, 1)

        self.yawPosFrame_2 = QFrame(self.CartesianPoseWidget_2)
        self.yawPosFrame_2.setObjectName(u"yawPosFrame_2")
        self.yawPosFrame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.yawPosFrame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.yawPosFrame_2)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(-1, -1, -1, 14)
        self.yaw_2 = QLabel(self.yawPosFrame_2)
        self.yaw_2.setObjectName(u"yaw_2")
        self.yaw_2.setFont(font2)

        self.horizontalLayout_28.addWidget(self.yaw_2, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.yawText_2 = QLabel(self.yawPosFrame_2)
        self.yawText_2.setObjectName(u"yawText_2")

        self.horizontalLayout_28.addWidget(self.yawText_2, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)


        self.gridLayout_4.addWidget(self.yawPosFrame_2, 2, 1, 1, 1)

        self.CartesianPoseText_2 = QLabel(self.CartesianPoseWidget_2)
        self.CartesianPoseText_2.setObjectName(u"CartesianPoseText_2")
        self.CartesianPoseText_2.setFont(font3)
        self.CartesianPoseText_2.setStyleSheet(u"border: 2px solid #FFFFFF;  /* white solid border */\n"
"border-radius: 6px;")

        self.gridLayout_4.addWidget(self.CartesianPoseText_2, 0, 0, 1, 2, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.xPosFrame_2 = QFrame(self.CartesianPoseWidget_2)
        self.xPosFrame_2.setObjectName(u"xPosFrame_2")
        self.xPosFrame_2.setFont(font2)
        self.xPosFrame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.xPosFrame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.xPosFrame_2)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(9, -1, -1, 3)
        self.x_2 = QLabel(self.xPosFrame_2)
        self.x_2.setObjectName(u"x_2")
        self.x_2.setFont(font2)

        self.horizontalLayout_29.addWidget(self.x_2, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.xText_2 = QLabel(self.xPosFrame_2)
        self.xText_2.setObjectName(u"xText_2")

        self.horizontalLayout_29.addWidget(self.xText_2, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)


        self.gridLayout_4.addWidget(self.xPosFrame_2, 1, 0, 1, 1)


        self.horizontalLayout_19.addWidget(self.CartesianPoseWidget_2)

        self.MotorInfoWidget_2 = QWidget(self.Info_2)
        self.MotorInfoWidget_2.setObjectName(u"MotorInfoWidget_2")
        self.MotorInfoWidget_2.setStyleSheet(u"")
        self.gridLayout_5 = QGridLayout(self.MotorInfoWidget_2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(-1, 6, -1, -1)
        self.PositionFrame_2 = QFrame(self.MotorInfoWidget_2)
        self.PositionFrame_2.setObjectName(u"PositionFrame_2")
        self.PositionFrame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.PositionFrame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.PositionFrame_2)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.Position_2 = QLabel(self.PositionFrame_2)
        self.Position_2.setObjectName(u"Position_2")

        self.horizontalLayout_30.addWidget(self.Position_2)

        self.PositionText_2 = QLabel(self.PositionFrame_2)
        self.PositionText_2.setObjectName(u"PositionText_2")

        self.horizontalLayout_30.addWidget(self.PositionText_2)


        self.gridLayout_5.addWidget(self.PositionFrame_2, 2, 0, 1, 1)

        self.MotorInfoText_2 = QLabel(self.MotorInfoWidget_2)
        self.MotorInfoText_2.setObjectName(u"MotorInfoText_2")
        self.MotorInfoText_2.setFont(font3)
        self.MotorInfoText_2.setStyleSheet(u"border: 2px solid #FFFFFF;  /* white solid border */\n"
"border-radius: 6px;")

        self.gridLayout_5.addWidget(self.MotorInfoText_2, 0, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.CurrentFrame_2 = QFrame(self.MotorInfoWidget_2)
        self.CurrentFrame_2.setObjectName(u"CurrentFrame_2")
        self.CurrentFrame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.CurrentFrame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.CurrentFrame_2)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.Current_2 = QLabel(self.CurrentFrame_2)
        self.Current_2.setObjectName(u"Current_2")

        self.horizontalLayout_31.addWidget(self.Current_2)

        self.CurrentText_2 = QLabel(self.CurrentFrame_2)
        self.CurrentText_2.setObjectName(u"CurrentText_2")

        self.horizontalLayout_31.addWidget(self.CurrentText_2)


        self.gridLayout_5.addWidget(self.CurrentFrame_2, 3, 0, 1, 1)


        self.horizontalLayout_19.addWidget(self.MotorInfoWidget_2)

        self.RecordData_2 = QWidget(self.Info_2)
        self.RecordData_2.setObjectName(u"RecordData_2")
        self.gridLayout_6 = QGridLayout(self.RecordData_2)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(-1, 6, -1, -1)
        self.frame_12 = QFrame(self.RecordData_2)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_12)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(9, 9, -1, 0)
        self.d1_2 = QLabel(self.frame_12)
        self.d1_2.setObjectName(u"d1_2")

        self.verticalLayout_15.addWidget(self.d1_2)


        self.gridLayout_6.addWidget(self.frame_12, 1, 0, 1, 1)

        self.LaserInfoText_2 = QLabel(self.RecordData_2)
        self.LaserInfoText_2.setObjectName(u"LaserInfoText_2")
        self.LaserInfoText_2.setFont(font3)
        self.LaserInfoText_2.setStyleSheet(u"border: 2px solid #FFFFFF;  /* white solid border */\n"
"border-radius: 6px;")

        self.gridLayout_6.addWidget(self.LaserInfoText_2, 0, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.frame_7 = QFrame(self.RecordData_2)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(9, -1, -1, 0)
        self.d2_2 = QLabel(self.frame_7)
        self.d2_2.setObjectName(u"d2_2")

        self.horizontalLayout_32.addWidget(self.d2_2)

        self.currentHeight = QLabel(self.frame_7)
        self.currentHeight.setObjectName(u"currentHeight")

        self.horizontalLayout_32.addWidget(self.currentHeight)


        self.gridLayout_6.addWidget(self.frame_7, 3, 0, 1, 1)

        self.frame_8 = QFrame(self.RecordData_2)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(9, -1, -1, 0)
        self.h1_2 = QLabel(self.frame_8)
        self.h1_2.setObjectName(u"h1_2")

        self.horizontalLayout_25.addWidget(self.h1_2)

        self.HeightCommand = QLabel(self.frame_8)
        self.HeightCommand.setObjectName(u"HeightCommand")

        self.horizontalLayout_25.addWidget(self.HeightCommand)


        self.gridLayout_6.addWidget(self.frame_8, 4, 0, 1, 1)


        self.horizontalLayout_19.addWidget(self.RecordData_2)

        self.RecordDataButtonContainer_2 = QWidget(self.Info_2)
        self.RecordDataButtonContainer_2.setObjectName(u"RecordDataButtonContainer_2")
        sizePolicy1.setHeightForWidth(self.RecordDataButtonContainer_2.sizePolicy().hasHeightForWidth())
        self.RecordDataButtonContainer_2.setSizePolicy(sizePolicy1)
        self.verticalLayout_21 = QVBoxLayout(self.RecordDataButtonContainer_2)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(9, 9, -1, -1)
        self.RecordDataButton_2 = QPushButton(self.RecordDataButtonContainer_2)
        self.RecordDataButton_2.setObjectName(u"RecordDataButton_2")
        sizePolicy1.setHeightForWidth(self.RecordDataButton_2.sizePolicy().hasHeightForWidth())
        self.RecordDataButton_2.setSizePolicy(sizePolicy1)
        self.RecordDataButton_2.setFont(font)
        self.RecordDataButton_2.setStyleSheet(u"QPushButton {\n"
"    padding: 16px 24px;\n"
"}\n"
"\n"
"")

        self.verticalLayout_21.addWidget(self.RecordDataButton_2, 0, Qt.AlignmentFlag.AlignVCenter)


        self.horizontalLayout_19.addWidget(self.RecordDataButtonContainer_2)

        self.MiddleStackedWidget.addWidget(self.VisionAndInfoPage)
        self.DIDOContainerPage = QWidget()
        self.DIDOContainerPage.setObjectName(u"DIDOContainerPage")
        self.scrollArea = QScrollArea(self.DIDOContainerPage)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(0, 320, 701, 361))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 685, 568))
        self.horizontalLayout_34 = QHBoxLayout(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_34.setSpacing(9)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.widget_2 = QWidget(self.scrollAreaWidgetContents_2)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout_7 = QGridLayout(self.widget_2)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setHorizontalSpacing(0)
        self.gridLayout_7.setVerticalSpacing(10)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.y0_15 = QWidget(self.widget_2)
        self.y0_15.setObjectName(u"y0_15")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.y0_15.sizePolicy().hasHeightForWidth())
        self.y0_15.setSizePolicy(sizePolicy5)
        self.y0_15.setMinimumSize(QSize(90, 60))
        self.y0_15.setStyleSheet(u"    border: none;\n"
"    border-radius: 24px;\n"
"    background-color: #000000;\n"
"")
        self.horizontalLayout_47 = QHBoxLayout(self.y0_15)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.horizontalLayout_47.setContentsMargins(4, -1, -1, -1)
        self.CircleOff_15 = QPushButton(self.y0_15)
        self.CircleOff_15.setObjectName(u"CircleOff_15")
        sizePolicy2.setHeightForWidth(self.CircleOff_15.sizePolicy().hasHeightForWidth())
        self.CircleOff_15.setSizePolicy(sizePolicy2)
        self.CircleOff_15.setMinimumSize(QSize(0, 30))
        self.CircleOff_15.setMaximumSize(QSize(30, 30))
        font4 = QFont()
        font4.setPointSize(16)
        self.CircleOff_15.setFont(font4)
        self.CircleOff_15.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: white;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"	color: black;\n"
"}\n"
"")
        self.CircleOff_15.setCheckable(True)

        self.horizontalLayout_47.addWidget(self.CircleOff_15)

        self.CircleOn_15 = QPushButton(self.y0_15)
        self.CircleOn_15.setObjectName(u"CircleOn_15")
        sizePolicy2.setHeightForWidth(self.CircleOn_15.sizePolicy().hasHeightForWidth())
        self.CircleOn_15.setSizePolicy(sizePolicy2)
        self.CircleOn_15.setMaximumSize(QSize(30, 30))
        self.CircleOn_15.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: #000000;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"}\n"
"")
        self.CircleOn_15.setCheckable(True)

        self.horizontalLayout_47.addWidget(self.CircleOn_15)


        self.gridLayout_7.addWidget(self.y0_15, 3, 0, 1, 1)

        self.y0_32 = QWidget(self.widget_2)
        self.y0_32.setObjectName(u"y0_32")
        sizePolicy5.setHeightForWidth(self.y0_32.sizePolicy().hasHeightForWidth())
        self.y0_32.setSizePolicy(sizePolicy5)
        self.y0_32.setMinimumSize(QSize(90, 60))
        self.y0_32.setStyleSheet(u"    border: none;\n"
"    border-radius: 24px;\n"
"    background-color: #000000;\n"
"")
        self.horizontalLayout_64 = QHBoxLayout(self.y0_32)
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.horizontalLayout_64.setContentsMargins(4, -1, -1, -1)
        self.CircleOff_32 = QPushButton(self.y0_32)
        self.CircleOff_32.setObjectName(u"CircleOff_32")
        sizePolicy2.setHeightForWidth(self.CircleOff_32.sizePolicy().hasHeightForWidth())
        self.CircleOff_32.setSizePolicy(sizePolicy2)
        self.CircleOff_32.setMinimumSize(QSize(0, 30))
        self.CircleOff_32.setMaximumSize(QSize(30, 30))
        self.CircleOff_32.setFont(font4)
        self.CircleOff_32.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: white;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"	color: black;\n"
"}\n"
"")
        self.CircleOff_32.setCheckable(True)

        self.horizontalLayout_64.addWidget(self.CircleOff_32)

        self.CircleOn_32 = QPushButton(self.y0_32)
        self.CircleOn_32.setObjectName(u"CircleOn_32")
        sizePolicy2.setHeightForWidth(self.CircleOn_32.sizePolicy().hasHeightForWidth())
        self.CircleOn_32.setSizePolicy(sizePolicy2)
        self.CircleOn_32.setMaximumSize(QSize(30, 30))
        self.CircleOn_32.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: #000000;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"}\n"
"")
        self.CircleOn_32.setCheckable(True)

        self.horizontalLayout_64.addWidget(self.CircleOn_32)


        self.gridLayout_7.addWidget(self.y0_32, 5, 5, 1, 1)

        self.y0_14 = QWidget(self.widget_2)
        self.y0_14.setObjectName(u"y0_14")
        sizePolicy5.setHeightForWidth(self.y0_14.sizePolicy().hasHeightForWidth())
        self.y0_14.setSizePolicy(sizePolicy5)
        self.y0_14.setMinimumSize(QSize(90, 60))
        self.y0_14.setStyleSheet(u"    border: none;\n"
"    border-radius: 24px;\n"
"    background-color: #000000;\n"
"")
        self.horizontalLayout_46 = QHBoxLayout(self.y0_14)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.horizontalLayout_46.setContentsMargins(4, -1, -1, -1)
        self.CircleOff_14 = QPushButton(self.y0_14)
        self.CircleOff_14.setObjectName(u"CircleOff_14")
        sizePolicy2.setHeightForWidth(self.CircleOff_14.sizePolicy().hasHeightForWidth())
        self.CircleOff_14.setSizePolicy(sizePolicy2)
        self.CircleOff_14.setMinimumSize(QSize(0, 30))
        self.CircleOff_14.setMaximumSize(QSize(30, 30))
        self.CircleOff_14.setFont(font4)
        self.CircleOff_14.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: white;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"	color: black;\n"
"}\n"
"")
        self.CircleOff_14.setCheckable(True)

        self.horizontalLayout_46.addWidget(self.CircleOff_14)

        self.CircleOn_14 = QPushButton(self.y0_14)
        self.CircleOn_14.setObjectName(u"CircleOn_14")
        sizePolicy2.setHeightForWidth(self.CircleOn_14.sizePolicy().hasHeightForWidth())
        self.CircleOn_14.setSizePolicy(sizePolicy2)
        self.CircleOn_14.setMaximumSize(QSize(30, 30))
        self.CircleOn_14.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: #000000;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"}\n"
"")
        self.CircleOn_14.setCheckable(True)

        self.horizontalLayout_46.addWidget(self.CircleOn_14)


        self.gridLayout_7.addWidget(self.y0_14, 2, 5, 1, 1)

        self.y0_24 = QWidget(self.widget_2)
        self.y0_24.setObjectName(u"y0_24")
        sizePolicy5.setHeightForWidth(self.y0_24.sizePolicy().hasHeightForWidth())
        self.y0_24.setSizePolicy(sizePolicy5)
        self.y0_24.setMinimumSize(QSize(90, 60))
        self.y0_24.setStyleSheet(u"    border: none;\n"
"    border-radius: 24px;\n"
"    background-color: #000000;\n"
"")
        self.horizontalLayout_56 = QHBoxLayout(self.y0_24)
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.horizontalLayout_56.setContentsMargins(4, -1, -1, -1)
        self.CircleOff_24 = QPushButton(self.y0_24)
        self.CircleOff_24.setObjectName(u"CircleOff_24")
        sizePolicy2.setHeightForWidth(self.CircleOff_24.sizePolicy().hasHeightForWidth())
        self.CircleOff_24.setSizePolicy(sizePolicy2)
        self.CircleOff_24.setMinimumSize(QSize(0, 30))
        self.CircleOff_24.setMaximumSize(QSize(30, 30))
        self.CircleOff_24.setFont(font4)
        self.CircleOff_24.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: white;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"	color: black;\n"
"}\n"
"")
        self.CircleOff_24.setCheckable(True)

        self.horizontalLayout_56.addWidget(self.CircleOff_24)

        self.CircleOn_24 = QPushButton(self.y0_24)
        self.CircleOn_24.setObjectName(u"CircleOn_24")
        sizePolicy2.setHeightForWidth(self.CircleOn_24.sizePolicy().hasHeightForWidth())
        self.CircleOn_24.setSizePolicy(sizePolicy2)
        self.CircleOn_24.setMaximumSize(QSize(30, 30))
        self.CircleOn_24.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: #000000;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"}\n"
"")
        self.CircleOn_24.setCheckable(True)

        self.horizontalLayout_56.addWidget(self.CircleOn_24)


        self.gridLayout_7.addWidget(self.y0_24, 4, 3, 1, 1)

        self.y0_9 = QWidget(self.widget_2)
        self.y0_9.setObjectName(u"y0_9")
        sizePolicy5.setHeightForWidth(self.y0_9.sizePolicy().hasHeightForWidth())
        self.y0_9.setSizePolicy(sizePolicy5)
        self.y0_9.setMinimumSize(QSize(90, 60))
        self.y0_9.setStyleSheet(u"    border: none;\n"
"    border-radius: 24px;\n"
"    background-color: #000000;\n"
"")
        self.horizontalLayout_41 = QHBoxLayout(self.y0_9)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.horizontalLayout_41.setContentsMargins(4, -1, -1, -1)
        self.CircleOff_9 = QPushButton(self.y0_9)
        self.CircleOff_9.setObjectName(u"CircleOff_9")
        sizePolicy2.setHeightForWidth(self.CircleOff_9.sizePolicy().hasHeightForWidth())
        self.CircleOff_9.setSizePolicy(sizePolicy2)
        self.CircleOff_9.setMinimumSize(QSize(0, 30))
        self.CircleOff_9.setMaximumSize(QSize(30, 30))
        self.CircleOff_9.setFont(font4)
        self.CircleOff_9.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: white;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"	color: black;\n"
"}\n"
"")
        self.CircleOff_9.setCheckable(True)

        self.horizontalLayout_41.addWidget(self.CircleOff_9)

        self.CircleOn_9 = QPushButton(self.y0_9)
        self.CircleOn_9.setObjectName(u"CircleOn_9")
        sizePolicy2.setHeightForWidth(self.CircleOn_9.sizePolicy().hasHeightForWidth())
        self.CircleOn_9.setSizePolicy(sizePolicy2)
        self.CircleOn_9.setMaximumSize(QSize(30, 30))
        self.CircleOn_9.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: #000000;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"}\n"
"")
        self.CircleOn_9.setCheckable(True)

        self.horizontalLayout_41.addWidget(self.CircleOn_9)


        self.gridLayout_7.addWidget(self.y0_9, 2, 0, 1, 1)

        self.y0_6 = QWidget(self.widget_2)
        self.y0_6.setObjectName(u"y0_6")
        sizePolicy5.setHeightForWidth(self.y0_6.sizePolicy().hasHeightForWidth())
        self.y0_6.setSizePolicy(sizePolicy5)
        self.y0_6.setMinimumSize(QSize(90, 60))
        self.y0_6.setStyleSheet(u"    border: none;\n"
"    border-radius: 24px;\n"
"    background-color: #000000;\n"
"")
        self.horizontalLayout_38 = QHBoxLayout(self.y0_6)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(4, -1, -1, -1)
        self.CircleOff_6 = QPushButton(self.y0_6)
        self.CircleOff_6.setObjectName(u"CircleOff_6")
        sizePolicy2.setHeightForWidth(self.CircleOff_6.sizePolicy().hasHeightForWidth())
        self.CircleOff_6.setSizePolicy(sizePolicy2)
        self.CircleOff_6.setMinimumSize(QSize(0, 30))
        self.CircleOff_6.setMaximumSize(QSize(30, 30))
        self.CircleOff_6.setFont(font4)
        self.CircleOff_6.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: white;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"	color: black;\n"
"}\n"
"")
        self.CircleOff_6.setCheckable(True)

        self.horizontalLayout_38.addWidget(self.CircleOff_6)

        self.CircleOn_6 = QPushButton(self.y0_6)
        self.CircleOn_6.setObjectName(u"CircleOn_6")
        sizePolicy2.setHeightForWidth(self.CircleOn_6.sizePolicy().hasHeightForWidth())
        self.CircleOn_6.setSizePolicy(sizePolicy2)
        self.CircleOn_6.setMaximumSize(QSize(30, 30))
        self.CircleOn_6.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: #000000;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"}\n"
"")
        self.CircleOn_6.setCheckable(True)

        self.horizontalLayout_38.addWidget(self.CircleOn_6)


        self.gridLayout_7.addWidget(self.y0_6, 1, 3, 1, 1)

        self.y0_23 = QWidget(self.widget_2)
        self.y0_23.setObjectName(u"y0_23")
        sizePolicy5.setHeightForWidth(self.y0_23.sizePolicy().hasHeightForWidth())
        self.y0_23.setSizePolicy(sizePolicy5)
        self.y0_23.setMinimumSize(QSize(90, 60))
        self.y0_23.setStyleSheet(u"    border: none;\n"
"    border-radius: 24px;\n"
"    background-color: #000000;\n"
"")
        self.horizontalLayout_55 = QHBoxLayout(self.y0_23)
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.horizontalLayout_55.setContentsMargins(4, -1, -1, -1)
        self.CircleOff_23 = QPushButton(self.y0_23)
        self.CircleOff_23.setObjectName(u"CircleOff_23")
        sizePolicy2.setHeightForWidth(self.CircleOff_23.sizePolicy().hasHeightForWidth())
        self.CircleOff_23.setSizePolicy(sizePolicy2)
        self.CircleOff_23.setMinimumSize(QSize(0, 30))
        self.CircleOff_23.setMaximumSize(QSize(30, 30))
        self.CircleOff_23.setFont(font4)
        self.CircleOff_23.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: white;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"	color: black;\n"
"}\n"
"")
        self.CircleOff_23.setCheckable(True)

        self.horizontalLayout_55.addWidget(self.CircleOff_23)

        self.CircleOn_23 = QPushButton(self.y0_23)
        self.CircleOn_23.setObjectName(u"CircleOn_23")
        sizePolicy2.setHeightForWidth(self.CircleOn_23.sizePolicy().hasHeightForWidth())
        self.CircleOn_23.setSizePolicy(sizePolicy2)
        self.CircleOn_23.setMaximumSize(QSize(30, 30))
        self.CircleOn_23.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: #000000;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"}\n"
"")
        self.CircleOn_23.setCheckable(True)

        self.horizontalLayout_55.addWidget(self.CircleOn_23)


        self.gridLayout_7.addWidget(self.y0_23, 4, 2, 1, 1)

        self.y0_33 = QWidget(self.widget_2)
        self.y0_33.setObjectName(u"y0_33")
        sizePolicy5.setHeightForWidth(self.y0_33.sizePolicy().hasHeightForWidth())
        self.y0_33.setSizePolicy(sizePolicy5)
        self.y0_33.setMinimumSize(QSize(90, 60))
        self.y0_33.setStyleSheet(u"    border: none;\n"
"    border-radius: 24px;\n"
"    background-color: #000000;\n"
"")
        self.horizontalLayout_67 = QHBoxLayout(self.y0_33)
        self.horizontalLayout_67.setObjectName(u"horizontalLayout_67")
        self.horizontalLayout_67.setContentsMargins(4, -1, -1, -1)
        self.CircleOff_35 = QPushButton(self.y0_33)
        self.CircleOff_35.setObjectName(u"CircleOff_35")
        sizePolicy2.setHeightForWidth(self.CircleOff_35.sizePolicy().hasHeightForWidth())
        self.CircleOff_35.setSizePolicy(sizePolicy2)
        self.CircleOff_35.setMinimumSize(QSize(0, 30))
        self.CircleOff_35.setMaximumSize(QSize(30, 30))
        self.CircleOff_35.setFont(font4)
        self.CircleOff_35.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: white;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"	color: black;\n"
"}\n"
"")
        self.CircleOff_35.setCheckable(True)

        self.horizontalLayout_67.addWidget(self.CircleOff_35)

        self.CircleOn_35 = QPushButton(self.y0_33)
        self.CircleOn_35.setObjectName(u"CircleOn_35")
        sizePolicy2.setHeightForWidth(self.CircleOn_35.sizePolicy().hasHeightForWidth())
        self.CircleOn_35.setSizePolicy(sizePolicy2)
        self.CircleOn_35.setMaximumSize(QSize(30, 30))
        self.CircleOn_35.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: #000000;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"}\n"
"")
        self.CircleOn_35.setCheckable(True)

        self.horizontalLayout_67.addWidget(self.CircleOn_35)


        self.gridLayout_7.addWidget(self.y0_33, 6, 0, 1, 1)

        self.y0_18 = QWidget(self.widget_2)
        self.y0_18.setObjectName(u"y0_18")
        sizePolicy5.setHeightForWidth(self.y0_18.sizePolicy().hasHeightForWidth())
        self.y0_18.setSizePolicy(sizePolicy5)
        self.y0_18.setMinimumSize(QSize(90, 60))
        self.y0_18.setStyleSheet(u"    border: none;\n"
"    border-radius: 24px;\n"
"    background-color: #000000;\n"
"")
        self.horizontalLayout_50 = QHBoxLayout(self.y0_18)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.horizontalLayout_50.setContentsMargins(4, -1, -1, -1)
        self.CircleOff_18 = QPushButton(self.y0_18)
        self.CircleOff_18.setObjectName(u"CircleOff_18")
        sizePolicy2.setHeightForWidth(self.CircleOff_18.sizePolicy().hasHeightForWidth())
        self.CircleOff_18.setSizePolicy(sizePolicy2)
        self.CircleOff_18.setMinimumSize(QSize(0, 30))
        self.CircleOff_18.setMaximumSize(QSize(30, 30))
        self.CircleOff_18.setFont(font4)
        self.CircleOff_18.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: white;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"	color: black;\n"
"}\n"
"")
        self.CircleOff_18.setCheckable(True)

        self.horizontalLayout_50.addWidget(self.CircleOff_18)

        self.CircleOn_18 = QPushButton(self.y0_18)
        self.CircleOn_18.setObjectName(u"CircleOn_18")
        sizePolicy2.setHeightForWidth(self.CircleOn_18.sizePolicy().hasHeightForWidth())
        self.CircleOn_18.setSizePolicy(sizePolicy2)
        self.CircleOn_18.setMaximumSize(QSize(30, 30))
        self.CircleOn_18.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: #000000;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"}\n"
"")
        self.CircleOn_18.setCheckable(True)

        self.horizontalLayout_50.addWidget(self.CircleOn_18)


        self.gridLayout_7.addWidget(self.y0_18, 3, 3, 1, 1)

        self.y0_20 = QWidget(self.widget_2)
        self.y0_20.setObjectName(u"y0_20")
        sizePolicy5.setHeightForWidth(self.y0_20.sizePolicy().hasHeightForWidth())
        self.y0_20.setSizePolicy(sizePolicy5)
        self.y0_20.setMinimumSize(QSize(90, 60))
        self.y0_20.setStyleSheet(u"    border: none;\n"
"    border-radius: 24px;\n"
"    background-color: #000000;\n"
"")
        self.horizontalLayout_52 = QHBoxLayout(self.y0_20)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.horizontalLayout_52.setContentsMargins(4, -1, -1, -1)
        self.CircleOff_20 = QPushButton(self.y0_20)
        self.CircleOff_20.setObjectName(u"CircleOff_20")
        sizePolicy2.setHeightForWidth(self.CircleOff_20.sizePolicy().hasHeightForWidth())
        self.CircleOff_20.setSizePolicy(sizePolicy2)
        self.CircleOff_20.setMinimumSize(QSize(0, 30))
        self.CircleOff_20.setMaximumSize(QSize(30, 30))
        self.CircleOff_20.setFont(font4)
        self.CircleOff_20.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: white;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"	color: black;\n"
"}\n"
"")
        self.CircleOff_20.setCheckable(True)

        self.horizontalLayout_52.addWidget(self.CircleOff_20)

        self.CircleOn_20 = QPushButton(self.y0_20)
        self.CircleOn_20.setObjectName(u"CircleOn_20")
        sizePolicy2.setHeightForWidth(self.CircleOn_20.sizePolicy().hasHeightForWidth())
        self.CircleOn_20.setSizePolicy(sizePolicy2)
        self.CircleOn_20.setMaximumSize(QSize(30, 30))
        self.CircleOn_20.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: #000000;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"}\n"
"")
        self.CircleOn_20.setCheckable(True)

        self.horizontalLayout_52.addWidget(self.CircleOn_20)


        self.gridLayout_7.addWidget(self.y0_20, 3, 5, 1, 1)

        self.y0_30 = QWidget(self.widget_2)
        self.y0_30.setObjectName(u"y0_30")
        sizePolicy5.setHeightForWidth(self.y0_30.sizePolicy().hasHeightForWidth())
        self.y0_30.setSizePolicy(sizePolicy5)
        self.y0_30.setMinimumSize(QSize(90, 60))
        self.y0_30.setStyleSheet(u"    border: none;\n"
"    border-radius: 24px;\n"
"    background-color: #000000;\n"
"")
        self.horizontalLayout_62 = QHBoxLayout(self.y0_30)
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.horizontalLayout_62.setContentsMargins(4, -1, -1, -1)
        self.CircleOff_30 = QPushButton(self.y0_30)
        self.CircleOff_30.setObjectName(u"CircleOff_30")
        sizePolicy2.setHeightForWidth(self.CircleOff_30.sizePolicy().hasHeightForWidth())
        self.CircleOff_30.setSizePolicy(sizePolicy2)
        self.CircleOff_30.setMinimumSize(QSize(0, 30))
        self.CircleOff_30.setMaximumSize(QSize(30, 30))
        self.CircleOff_30.setFont(font4)
        self.CircleOff_30.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: white;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"	color: black;\n"
"}\n"
"")
        self.CircleOff_30.setCheckable(True)

        self.horizontalLayout_62.addWidget(self.CircleOff_30)

        self.CircleOn_30 = QPushButton(self.y0_30)
        self.CircleOn_30.setObjectName(u"CircleOn_30")
        sizePolicy2.setHeightForWidth(self.CircleOn_30.sizePolicy().hasHeightForWidth())
        self.CircleOn_30.setSizePolicy(sizePolicy2)
        self.CircleOn_30.setMaximumSize(QSize(30, 30))
        self.CircleOn_30.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: #000000;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"}\n"
"")
        self.CircleOn_30.setCheckable(True)

        self.horizontalLayout_62.addWidget(self.CircleOn_30)


        self.gridLayout_7.addWidget(self.y0_30, 5, 3, 1, 1)

        self.y0_39 = QWidget(self.widget_2)
        self.y0_39.setObjectName(u"y0_39")
        sizePolicy5.setHeightForWidth(self.y0_39.sizePolicy().hasHeightForWidth())
        self.y0_39.setSizePolicy(sizePolicy5)
        self.y0_39.setMinimumSize(QSize(90, 60))
        self.y0_39.setStyleSheet(u"    border: none;\n"
"    border-radius: 24px;\n"
"    background-color: #000000;\n"
"")
        self.horizontalLayout_79 = QHBoxLayout(self.y0_39)
        self.horizontalLayout_79.setObjectName(u"horizontalLayout_79")
        self.horizontalLayout_79.setContentsMargins(4, -1, -1, -1)
        self.CircleOff_47 = QPushButton(self.y0_39)
        self.CircleOff_47.setObjectName(u"CircleOff_47")
        sizePolicy2.setHeightForWidth(self.CircleOff_47.sizePolicy().hasHeightForWidth())
        self.CircleOff_47.setSizePolicy(sizePolicy2)
        self.CircleOff_47.setMinimumSize(QSize(0, 30))
        self.CircleOff_47.setMaximumSize(QSize(30, 30))
        self.CircleOff_47.setFont(font4)
        self.CircleOff_47.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: white;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"	color: black;\n"
"}\n"
"")
        self.CircleOff_47.setCheckable(True)

        self.horizontalLayout_79.addWidget(self.CircleOff_47)

        self.CircleOn_47 = QPushButton(self.y0_39)
        self.CircleOn_47.setObjectName(u"CircleOn_47")
        sizePolicy2.setHeightForWidth(self.CircleOn_47.sizePolicy().hasHeightForWidth())
        self.CircleOn_47.setSizePolicy(sizePolicy2)
        self.CircleOn_47.setMaximumSize(QSize(30, 30))
        self.CircleOn_47.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: #000000;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"}\n"
"")
        self.CircleOn_47.setCheckable(True)

        self.horizontalLayout_79.addWidget(self.CircleOn_47)


        self.gridLayout_7.addWidget(self.y0_39, 7, 0, 1, 1)

        self.y0_10 = QWidget(self.widget_2)
        self.y0_10.setObjectName(u"y0_10")
        sizePolicy5.setHeightForWidth(self.y0_10.sizePolicy().hasHeightForWidth())
        self.y0_10.setSizePolicy(sizePolicy5)
        self.y0_10.setMinimumSize(QSize(90, 60))
        self.y0_10.setStyleSheet(u"    border: none;\n"
"    border-radius: 24px;\n"
"    background-color: #000000;\n"
"")
        self.horizontalLayout_42 = QHBoxLayout(self.y0_10)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.horizontalLayout_42.setContentsMargins(4, -1, -1, -1)
        self.CircleOff_10 = QPushButton(self.y0_10)
        self.CircleOff_10.setObjectName(u"CircleOff_10")
        sizePolicy2.setHeightForWidth(self.CircleOff_10.sizePolicy().hasHeightForWidth())
        self.CircleOff_10.setSizePolicy(sizePolicy2)
        self.CircleOff_10.setMinimumSize(QSize(0, 30))
        self.CircleOff_10.setMaximumSize(QSize(30, 30))
        self.CircleOff_10.setFont(font4)
        self.CircleOff_10.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: white;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"	color: black;\n"
"}\n"
"")
        self.CircleOff_10.setCheckable(True)

        self.horizontalLayout_42.addWidget(self.CircleOff_10)

        self.CircleOn_10 = QPushButton(self.y0_10)
        self.CircleOn_10.setObjectName(u"CircleOn_10")
        sizePolicy2.setHeightForWidth(self.CircleOn_10.sizePolicy().hasHeightForWidth())
        self.CircleOn_10.setSizePolicy(sizePolicy2)
        self.CircleOn_10.setMaximumSize(QSize(30, 30))
        self.CircleOn_10.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: #000000;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"}\n"
"")
        self.CircleOn_10.setCheckable(True)

        self.horizontalLayout_42.addWidget(self.CircleOn_10)


        self.gridLayout_7.addWidget(self.y0_10, 2, 1, 1, 1)

        self.y0_50 = QWidget(self.widget_2)
        self.y0_50.setObjectName(u"y0_50")
        sizePolicy5.setHeightForWidth(self.y0_50.sizePolicy().hasHeightForWidth())
        self.y0_50.setSizePolicy(sizePolicy5)
        self.y0_50.setMinimumSize(QSize(90, 60))
        self.y0_50.setStyleSheet(u"    border: none;\n"
"    border-radius: 24px;\n"
"    background-color: #000000;\n"
"")
        self.horizontalLayout_90 = QHBoxLayout(self.y0_50)
        self.horizontalLayout_90.setObjectName(u"horizontalLayout_90")
        self.horizontalLayout_90.setContentsMargins(4, -1, -1, -1)
        self.CircleOff_58 = QPushButton(self.y0_50)
        self.CircleOff_58.setObjectName(u"CircleOff_58")
        sizePolicy2.setHeightForWidth(self.CircleOff_58.sizePolicy().hasHeightForWidth())
        self.CircleOff_58.setSizePolicy(sizePolicy2)
        self.CircleOff_58.setMinimumSize(QSize(0, 30))
        self.CircleOff_58.setMaximumSize(QSize(30, 30))
        self.CircleOff_58.setFont(font4)
        self.CircleOff_58.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: white;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"	color: black;\n"
"}\n"
"")
        self.CircleOff_58.setCheckable(True)

        self.horizontalLayout_90.addWidget(self.CircleOff_58)

        self.CircleOn_58 = QPushButton(self.y0_50)
        self.CircleOn_58.setObjectName(u"CircleOn_58")
        sizePolicy2.setHeightForWidth(self.CircleOn_58.sizePolicy().hasHeightForWidth())
        self.CircleOn_58.setSizePolicy(sizePolicy2)
        self.CircleOn_58.setMaximumSize(QSize(30, 30))
        self.CircleOn_58.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: #000000;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"}\n"
"")
        self.CircleOn_58.setCheckable(True)

        self.horizontalLayout_90.addWidget(self.CircleOn_58)


        self.gridLayout_7.addWidget(self.y0_50, 8, 5, 1, 1)

        self.y0_48 = QWidget(self.widget_2)
        self.y0_48.setObjectName(u"y0_48")
        sizePolicy5.setHeightForWidth(self.y0_48.sizePolicy().hasHeightForWidth())
        self.y0_48.setSizePolicy(sizePolicy5)
        self.y0_48.setMinimumSize(QSize(90, 60))
        self.y0_48.setStyleSheet(u"    border: none;\n"
"    border-radius: 24px;\n"
"    background-color: #000000;\n"
"")
        self.horizontalLayout_88 = QHBoxLayout(self.y0_48)
        self.horizontalLayout_88.setObjectName(u"horizontalLayout_88")
        self.horizontalLayout_88.setContentsMargins(4, -1, -1, -1)
        self.CircleOff_56 = QPushButton(self.y0_48)
        self.CircleOff_56.setObjectName(u"CircleOff_56")
        sizePolicy2.setHeightForWidth(self.CircleOff_56.sizePolicy().hasHeightForWidth())
        self.CircleOff_56.setSizePolicy(sizePolicy2)
        self.CircleOff_56.setMinimumSize(QSize(0, 30))
        self.CircleOff_56.setMaximumSize(QSize(30, 30))
        self.CircleOff_56.setFont(font4)
        self.CircleOff_56.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: white;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"	color: black;\n"
"}\n"
"")
        self.CircleOff_56.setCheckable(True)

        self.horizontalLayout_88.addWidget(self.CircleOff_56)

        self.CircleOn_56 = QPushButton(self.y0_48)
        self.CircleOn_56.setObjectName(u"CircleOn_56")
        sizePolicy2.setHeightForWidth(self.CircleOn_56.sizePolicy().hasHeightForWidth())
        self.CircleOn_56.setSizePolicy(sizePolicy2)
        self.CircleOn_56.setMaximumSize(QSize(30, 30))
        self.CircleOn_56.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: #000000;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"}\n"
"")
        self.CircleOn_56.setCheckable(True)

        self.horizontalLayout_88.addWidget(self.CircleOn_56)


        self.gridLayout_7.addWidget(self.y0_48, 8, 3, 1, 1)

        self.y0_11 = QWidget(self.widget_2)
        self.y0_11.setObjectName(u"y0_11")
        sizePolicy5.setHeightForWidth(self.y0_11.sizePolicy().hasHeightForWidth())
        self.y0_11.setSizePolicy(sizePolicy5)
        self.y0_11.setMinimumSize(QSize(90, 60))
        self.y0_11.setStyleSheet(u"    border: none;\n"
"    border-radius: 24px;\n"
"    background-color: #000000;\n"
"")
        self.horizontalLayout_43 = QHBoxLayout(self.y0_11)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.horizontalLayout_43.setContentsMargins(4, -1, -1, -1)
        self.CircleOff_11 = QPushButton(self.y0_11)
        self.CircleOff_11.setObjectName(u"CircleOff_11")
        sizePolicy2.setHeightForWidth(self.CircleOff_11.sizePolicy().hasHeightForWidth())
        self.CircleOff_11.setSizePolicy(sizePolicy2)
        self.CircleOff_11.setMinimumSize(QSize(0, 30))
        self.CircleOff_11.setMaximumSize(QSize(30, 30))
        self.CircleOff_11.setFont(font4)
        self.CircleOff_11.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: white;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"	color: black;\n"
"}\n"
"")
        self.CircleOff_11.setCheckable(True)

        self.horizontalLayout_43.addWidget(self.CircleOff_11)

        self.CircleOn_11 = QPushButton(self.y0_11)
        self.CircleOn_11.setObjectName(u"CircleOn_11")
        sizePolicy2.setHeightForWidth(self.CircleOn_11.sizePolicy().hasHeightForWidth())
        self.CircleOn_11.setSizePolicy(sizePolicy2)
        self.CircleOn_11.setMaximumSize(QSize(30, 30))
        self.CircleOn_11.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: #000000;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"}\n"
"")
        self.CircleOn_11.setCheckable(True)

        self.horizontalLayout_43.addWidget(self.CircleOn_11)


        self.gridLayout_7.addWidget(self.y0_11, 2, 2, 1, 1)

        self.y0_22 = QWidget(self.widget_2)
        self.y0_22.setObjectName(u"y0_22")
        sizePolicy5.setHeightForWidth(self.y0_22.sizePolicy().hasHeightForWidth())
        self.y0_22.setSizePolicy(sizePolicy5)
        self.y0_22.setMinimumSize(QSize(90, 60))
        self.y0_22.setStyleSheet(u"    border: none;\n"
"    border-radius: 24px;\n"
"    background-color: #000000;\n"
"")
        self.horizontalLayout_54 = QHBoxLayout(self.y0_22)
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.horizontalLayout_54.setContentsMargins(4, -1, -1, -1)
        self.CircleOff_22 = QPushButton(self.y0_22)
        self.CircleOff_22.setObjectName(u"CircleOff_22")
        sizePolicy2.setHeightForWidth(self.CircleOff_22.sizePolicy().hasHeightForWidth())
        self.CircleOff_22.setSizePolicy(sizePolicy2)
        self.CircleOff_22.setMinimumSize(QSize(0, 30))
        self.CircleOff_22.setMaximumSize(QSize(30, 30))
        self.CircleOff_22.setFont(font4)
        self.CircleOff_22.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: white;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"	color: black;\n"
"}\n"
"")
        self.CircleOff_22.setCheckable(True)

        self.horizontalLayout_54.addWidget(self.CircleOff_22)

        self.CircleOn_22 = QPushButton(self.y0_22)
        self.CircleOn_22.setObjectName(u"CircleOn_22")
        sizePolicy2.setHeightForWidth(self.CircleOn_22.sizePolicy().hasHeightForWidth())
        self.CircleOn_22.setSizePolicy(sizePolicy2)
        self.CircleOn_22.setMaximumSize(QSize(30, 30))
        self.CircleOn_22.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: #000000;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"}\n"
"")
        self.CircleOn_22.setCheckable(True)

        self.horizontalLayout_54.addWidget(self.CircleOn_22)


        self.gridLayout_7.addWidget(self.y0_22, 4, 1, 1, 1)

        self.y0_8 = QWidget(self.widget_2)
        self.y0_8.setObjectName(u"y0_8")
        sizePolicy5.setHeightForWidth(self.y0_8.sizePolicy().hasHeightForWidth())
        self.y0_8.setSizePolicy(sizePolicy5)
        self.y0_8.setMinimumSize(QSize(90, 60))
        self.y0_8.setStyleSheet(u"    border: none;\n"
"    border-radius: 24px;\n"
"    background-color: #000000;\n"
"")
        self.horizontalLayout_40 = QHBoxLayout(self.y0_8)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.horizontalLayout_40.setContentsMargins(4, -1, -1, -1)
        self.CircleOff_8 = QPushButton(self.y0_8)
        self.CircleOff_8.setObjectName(u"CircleOff_8")
        sizePolicy2.setHeightForWidth(self.CircleOff_8.sizePolicy().hasHeightForWidth())
        self.CircleOff_8.setSizePolicy(sizePolicy2)
        self.CircleOff_8.setMinimumSize(QSize(0, 30))
        self.CircleOff_8.setMaximumSize(QSize(30, 30))
        self.CircleOff_8.setFont(font4)
        self.CircleOff_8.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: white;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"	color: black;\n"
"}\n"
"")
        self.CircleOff_8.setCheckable(True)

        self.horizontalLayout_40.addWidget(self.CircleOff_8)

        self.CircleOn_8 = QPushButton(self.y0_8)
        self.CircleOn_8.setObjectName(u"CircleOn_8")
        sizePolicy2.setHeightForWidth(self.CircleOn_8.sizePolicy().hasHeightForWidth())
        self.CircleOn_8.setSizePolicy(sizePolicy2)
        self.CircleOn_8.setMaximumSize(QSize(30, 30))
        self.CircleOn_8.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: #000000;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"}\n"
"")
        self.CircleOn_8.setCheckable(True)

        self.horizontalLayout_40.addWidget(self.CircleOn_8)


        self.gridLayout_7.addWidget(self.y0_8, 1, 5, 1, 1)

        self.y0_25 = QWidget(self.widget_2)
        self.y0_25.setObjectName(u"y0_25")
        sizePolicy5.setHeightForWidth(self.y0_25.sizePolicy().hasHeightForWidth())
        self.y0_25.setSizePolicy(sizePolicy5)
        self.y0_25.setMinimumSize(QSize(90, 60))
        self.y0_25.setStyleSheet(u"    border: none;\n"
"    border-radius: 24px;\n"
"    background-color: #000000;\n"
"")
        self.horizontalLayout_57 = QHBoxLayout(self.y0_25)
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.horizontalLayout_57.setContentsMargins(4, -1, -1, -1)
        self.CircleOff_25 = QPushButton(self.y0_25)
        self.CircleOff_25.setObjectName(u"CircleOff_25")
        sizePolicy2.setHeightForWidth(self.CircleOff_25.sizePolicy().hasHeightForWidth())
        self.CircleOff_25.setSizePolicy(sizePolicy2)
        self.CircleOff_25.setMinimumSize(QSize(0, 30))
        self.CircleOff_25.setMaximumSize(QSize(30, 30))
        self.CircleOff_25.setFont(font4)
        self.CircleOff_25.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: white;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"	color: black;\n"
"}\n"
"")
        self.CircleOff_25.setCheckable(True)

        self.horizontalLayout_57.addWidget(self.CircleOff_25)

        self.CircleOn_25 = QPushButton(self.y0_25)
        self.CircleOn_25.setObjectName(u"CircleOn_25")
        sizePolicy2.setHeightForWidth(self.CircleOn_25.sizePolicy().hasHeightForWidth())
        self.CircleOn_25.setSizePolicy(sizePolicy2)
        self.CircleOn_25.setMaximumSize(QSize(30, 30))
        self.CircleOn_25.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: #000000;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"}\n"
"")
        self.CircleOn_25.setCheckable(True)

        self.horizontalLayout_57.addWidget(self.CircleOn_25)


        self.gridLayout_7.addWidget(self.y0_25, 4, 4, 1, 1)

        self.y0_49 = QWidget(self.widget_2)
        self.y0_49.setObjectName(u"y0_49")
        sizePolicy5.setHeightForWidth(self.y0_49.sizePolicy().hasHeightForWidth())
        self.y0_49.setSizePolicy(sizePolicy5)
        self.y0_49.setMinimumSize(QSize(90, 60))
        self.y0_49.setStyleSheet(u"    border: none;\n"
"    border-radius: 24px;\n"
"    background-color: #000000;\n"
"")
        self.horizontalLayout_89 = QHBoxLayout(self.y0_49)
        self.horizontalLayout_89.setObjectName(u"horizontalLayout_89")
        self.horizontalLayout_89.setContentsMargins(4, -1, -1, -1)
        self.CircleOff_57 = QPushButton(self.y0_49)
        self.CircleOff_57.setObjectName(u"CircleOff_57")
        sizePolicy2.setHeightForWidth(self.CircleOff_57.sizePolicy().hasHeightForWidth())
        self.CircleOff_57.setSizePolicy(sizePolicy2)
        self.CircleOff_57.setMinimumSize(QSize(0, 30))
        self.CircleOff_57.setMaximumSize(QSize(30, 30))
        self.CircleOff_57.setFont(font4)
        self.CircleOff_57.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: white;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"	color: black;\n"
"}\n"
"")
        self.CircleOff_57.setCheckable(True)

        self.horizontalLayout_89.addWidget(self.CircleOff_57)

        self.CircleOn_57 = QPushButton(self.y0_49)
        self.CircleOn_57.setObjectName(u"CircleOn_57")
        sizePolicy2.setHeightForWidth(self.CircleOn_57.sizePolicy().hasHeightForWidth())
        self.CircleOn_57.setSizePolicy(sizePolicy2)
        self.CircleOn_57.setMaximumSize(QSize(30, 30))
        self.CircleOn_57.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: #000000;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"}\n"
"")
        self.CircleOn_57.setCheckable(True)

        self.horizontalLayout_89.addWidget(self.CircleOn_57)


        self.gridLayout_7.addWidget(self.y0_49, 8, 4, 1, 1)

        self.y0_40 = QWidget(self.widget_2)
        self.y0_40.setObjectName(u"y0_40")
        sizePolicy5.setHeightForWidth(self.y0_40.sizePolicy().hasHeightForWidth())
        self.y0_40.setSizePolicy(sizePolicy5)
        self.y0_40.setMinimumSize(QSize(90, 60))
        self.y0_40.setStyleSheet(u"    border: none;\n"
"    border-radius: 24px;\n"
"    background-color: #000000;\n"
"")
        self.horizontalLayout_80 = QHBoxLayout(self.y0_40)
        self.horizontalLayout_80.setObjectName(u"horizontalLayout_80")
        self.horizontalLayout_80.setContentsMargins(4, -1, -1, -1)
        self.CircleOff_48 = QPushButton(self.y0_40)
        self.CircleOff_48.setObjectName(u"CircleOff_48")
        sizePolicy2.setHeightForWidth(self.CircleOff_48.sizePolicy().hasHeightForWidth())
        self.CircleOff_48.setSizePolicy(sizePolicy2)
        self.CircleOff_48.setMinimumSize(QSize(0, 30))
        self.CircleOff_48.setMaximumSize(QSize(30, 30))
        self.CircleOff_48.setFont(font4)
        self.CircleOff_48.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: white;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"	color: black;\n"
"}\n"
"")
        self.CircleOff_48.setCheckable(True)

        self.horizontalLayout_80.addWidget(self.CircleOff_48)

        self.CircleOn_48 = QPushButton(self.y0_40)
        self.CircleOn_48.setObjectName(u"CircleOn_48")
        sizePolicy2.setHeightForWidth(self.CircleOn_48.sizePolicy().hasHeightForWidth())
        self.CircleOn_48.setSizePolicy(sizePolicy2)
        self.CircleOn_48.setMaximumSize(QSize(30, 30))
        self.CircleOn_48.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: #000000;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"}\n"
"")
        self.CircleOn_48.setCheckable(True)

        self.horizontalLayout_80.addWidget(self.CircleOn_48)


        self.gridLayout_7.addWidget(self.y0_40, 8, 0, 1, 1)

        self.y0_5 = QWidget(self.widget_2)
        self.y0_5.setObjectName(u"y0_5")
        sizePolicy5.setHeightForWidth(self.y0_5.sizePolicy().hasHeightForWidth())
        self.y0_5.setSizePolicy(sizePolicy5)
        self.y0_5.setMinimumSize(QSize(90, 60))
        self.y0_5.setStyleSheet(u"    border: none;\n"
"    border-radius: 24px;\n"
"    background-color: #000000;\n"
"")
        self.horizontalLayout_37 = QHBoxLayout(self.y0_5)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_37.setContentsMargins(4, -1, -1, -1)
        self.CircleOff_5 = QPushButton(self.y0_5)
        self.CircleOff_5.setObjectName(u"CircleOff_5")
        sizePolicy2.setHeightForWidth(self.CircleOff_5.sizePolicy().hasHeightForWidth())
        self.CircleOff_5.setSizePolicy(sizePolicy2)
        self.CircleOff_5.setMinimumSize(QSize(0, 30))
        self.CircleOff_5.setMaximumSize(QSize(30, 30))
        self.CircleOff_5.setFont(font4)
        self.CircleOff_5.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: white;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"	color: black;\n"
"}\n"
"")
        self.CircleOff_5.setCheckable(True)

        self.horizontalLayout_37.addWidget(self.CircleOff_5)

        self.CircleOn_5 = QPushButton(self.y0_5)
        self.CircleOn_5.setObjectName(u"CircleOn_5")
        sizePolicy2.setHeightForWidth(self.CircleOn_5.sizePolicy().hasHeightForWidth())
        self.CircleOn_5.setSizePolicy(sizePolicy2)
        self.CircleOn_5.setMaximumSize(QSize(30, 30))
        self.CircleOn_5.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: #000000;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"}\n"
"")
        self.CircleOn_5.setCheckable(True)

        self.horizontalLayout_37.addWidget(self.CircleOn_5)


        self.gridLayout_7.addWidget(self.y0_5, 1, 2, 1, 1)

        self.y0_34 = QWidget(self.widget_2)
        self.y0_34.setObjectName(u"y0_34")
        sizePolicy5.setHeightForWidth(self.y0_34.sizePolicy().hasHeightForWidth())
        self.y0_34.setSizePolicy(sizePolicy5)
        self.y0_34.setMinimumSize(QSize(90, 60))
        self.y0_34.setStyleSheet(u"    border: none;\n"
"    border-radius: 24px;\n"
"    background-color: #000000;\n"
"")
        self.horizontalLayout_68 = QHBoxLayout(self.y0_34)
        self.horizontalLayout_68.setObjectName(u"horizontalLayout_68")
        self.horizontalLayout_68.setContentsMargins(4, -1, -1, -1)
        self.CircleOff_36 = QPushButton(self.y0_34)
        self.CircleOff_36.setObjectName(u"CircleOff_36")
        sizePolicy2.setHeightForWidth(self.CircleOff_36.sizePolicy().hasHeightForWidth())
        self.CircleOff_36.setSizePolicy(sizePolicy2)
        self.CircleOff_36.setMinimumSize(QSize(0, 30))
        self.CircleOff_36.setMaximumSize(QSize(30, 30))
        self.CircleOff_36.setFont(font4)
        self.CircleOff_36.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: white;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"	color: black;\n"
"}\n"
"")
        self.CircleOff_36.setCheckable(True)

        self.horizontalLayout_68.addWidget(self.CircleOff_36)

        self.CircleOn_36 = QPushButton(self.y0_34)
        self.CircleOn_36.setObjectName(u"CircleOn_36")
        sizePolicy2.setHeightForWidth(self.CircleOn_36.sizePolicy().hasHeightForWidth())
        self.CircleOn_36.setSizePolicy(sizePolicy2)
        self.CircleOn_36.setMaximumSize(QSize(30, 30))
        self.CircleOn_36.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: #000000;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"}\n"
"")
        self.CircleOn_36.setCheckable(True)

        self.horizontalLayout_68.addWidget(self.CircleOn_36)


        self.gridLayout_7.addWidget(self.y0_34, 6, 1, 1, 1)

        self.y0_44 = QWidget(self.widget_2)
        self.y0_44.setObjectName(u"y0_44")
        sizePolicy5.setHeightForWidth(self.y0_44.sizePolicy().hasHeightForWidth())
        self.y0_44.setSizePolicy(sizePolicy5)
        self.y0_44.setMinimumSize(QSize(90, 60))
        self.y0_44.setStyleSheet(u"    border: none;\n"
"    border-radius: 24px;\n"
"    background-color: #000000;\n"
"")
        self.horizontalLayout_84 = QHBoxLayout(self.y0_44)
        self.horizontalLayout_84.setObjectName(u"horizontalLayout_84")
        self.horizontalLayout_84.setContentsMargins(4, -1, -1, -1)
        self.CircleOff_52 = QPushButton(self.y0_44)
        self.CircleOff_52.setObjectName(u"CircleOff_52")
        sizePolicy2.setHeightForWidth(self.CircleOff_52.sizePolicy().hasHeightForWidth())
        self.CircleOff_52.setSizePolicy(sizePolicy2)
        self.CircleOff_52.setMinimumSize(QSize(0, 30))
        self.CircleOff_52.setMaximumSize(QSize(30, 30))
        self.CircleOff_52.setFont(font4)
        self.CircleOff_52.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: white;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"	color: black;\n"
"}\n"
"")
        self.CircleOff_52.setCheckable(True)

        self.horizontalLayout_84.addWidget(self.CircleOff_52)

        self.CircleOn_52 = QPushButton(self.y0_44)
        self.CircleOn_52.setObjectName(u"CircleOn_52")
        sizePolicy2.setHeightForWidth(self.CircleOn_52.sizePolicy().hasHeightForWidth())
        self.CircleOn_52.setSizePolicy(sizePolicy2)
        self.CircleOn_52.setMaximumSize(QSize(30, 30))
        self.CircleOn_52.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: #000000;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"}\n"
"")
        self.CircleOn_52.setCheckable(True)

        self.horizontalLayout_84.addWidget(self.CircleOn_52)


        self.gridLayout_7.addWidget(self.y0_44, 7, 4, 1, 1)

        self.y0_35 = QWidget(self.widget_2)
        self.y0_35.setObjectName(u"y0_35")
        sizePolicy5.setHeightForWidth(self.y0_35.sizePolicy().hasHeightForWidth())
        self.y0_35.setSizePolicy(sizePolicy5)
        self.y0_35.setMinimumSize(QSize(90, 60))
        self.y0_35.setStyleSheet(u"    border: none;\n"
"    border-radius: 24px;\n"
"    background-color: #000000;\n"
"")
        self.horizontalLayout_69 = QHBoxLayout(self.y0_35)
        self.horizontalLayout_69.setObjectName(u"horizontalLayout_69")
        self.horizontalLayout_69.setContentsMargins(4, -1, -1, -1)
        self.CircleOff_37 = QPushButton(self.y0_35)
        self.CircleOff_37.setObjectName(u"CircleOff_37")
        sizePolicy2.setHeightForWidth(self.CircleOff_37.sizePolicy().hasHeightForWidth())
        self.CircleOff_37.setSizePolicy(sizePolicy2)
        self.CircleOff_37.setMinimumSize(QSize(0, 30))
        self.CircleOff_37.setMaximumSize(QSize(30, 30))
        self.CircleOff_37.setFont(font4)
        self.CircleOff_37.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: white;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"	color: black;\n"
"}\n"
"")
        self.CircleOff_37.setCheckable(True)

        self.horizontalLayout_69.addWidget(self.CircleOff_37)

        self.CircleOn_37 = QPushButton(self.y0_35)
        self.CircleOn_37.setObjectName(u"CircleOn_37")
        sizePolicy2.setHeightForWidth(self.CircleOn_37.sizePolicy().hasHeightForWidth())
        self.CircleOn_37.setSizePolicy(sizePolicy2)
        self.CircleOn_37.setMaximumSize(QSize(30, 30))
        self.CircleOn_37.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: #000000;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"}\n"
"")
        self.CircleOn_37.setCheckable(True)

        self.horizontalLayout_69.addWidget(self.CircleOn_37)


        self.gridLayout_7.addWidget(self.y0_35, 6, 2, 1, 1)

        self.y0_4 = QWidget(self.widget_2)
        self.y0_4.setObjectName(u"y0_4")
        sizePolicy5.setHeightForWidth(self.y0_4.sizePolicy().hasHeightForWidth())
        self.y0_4.setSizePolicy(sizePolicy5)
        self.y0_4.setMinimumSize(QSize(90, 60))
        self.y0_4.setStyleSheet(u"    border: none;\n"
"    border-radius: 24px;\n"
"    background-color: #000000;\n"
"")
        self.horizontalLayout_36 = QHBoxLayout(self.y0_4)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(4, -1, -1, -1)
        self.CircleOff_4 = QPushButton(self.y0_4)
        self.CircleOff_4.setObjectName(u"CircleOff_4")
        sizePolicy2.setHeightForWidth(self.CircleOff_4.sizePolicy().hasHeightForWidth())
        self.CircleOff_4.setSizePolicy(sizePolicy2)
        self.CircleOff_4.setMinimumSize(QSize(0, 30))
        self.CircleOff_4.setMaximumSize(QSize(30, 30))
        self.CircleOff_4.setFont(font4)
        self.CircleOff_4.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: white;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"	color: black;\n"
"}\n"
"")
        self.CircleOff_4.setCheckable(True)

        self.horizontalLayout_36.addWidget(self.CircleOff_4)

        self.CircleOn_4 = QPushButton(self.y0_4)
        self.CircleOn_4.setObjectName(u"CircleOn_4")
        sizePolicy2.setHeightForWidth(self.CircleOn_4.sizePolicy().hasHeightForWidth())
        self.CircleOn_4.setSizePolicy(sizePolicy2)
        self.CircleOn_4.setMaximumSize(QSize(30, 30))
        self.CircleOn_4.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: #000000;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"}\n"
"")
        self.CircleOn_4.setCheckable(True)

        self.horizontalLayout_36.addWidget(self.CircleOn_4)


        self.gridLayout_7.addWidget(self.y0_4, 1, 1, 1, 1)

        self.y0_41 = QWidget(self.widget_2)
        self.y0_41.setObjectName(u"y0_41")
        sizePolicy5.setHeightForWidth(self.y0_41.sizePolicy().hasHeightForWidth())
        self.y0_41.setSizePolicy(sizePolicy5)
        self.y0_41.setMinimumSize(QSize(90, 60))
        self.y0_41.setStyleSheet(u"    border: none;\n"
"    border-radius: 24px;\n"
"    background-color: #000000;\n"
"")
        self.horizontalLayout_81 = QHBoxLayout(self.y0_41)
        self.horizontalLayout_81.setObjectName(u"horizontalLayout_81")
        self.horizontalLayout_81.setContentsMargins(4, -1, -1, -1)
        self.CircleOff_49 = QPushButton(self.y0_41)
        self.CircleOff_49.setObjectName(u"CircleOff_49")
        sizePolicy2.setHeightForWidth(self.CircleOff_49.sizePolicy().hasHeightForWidth())
        self.CircleOff_49.setSizePolicy(sizePolicy2)
        self.CircleOff_49.setMinimumSize(QSize(0, 30))
        self.CircleOff_49.setMaximumSize(QSize(30, 30))
        self.CircleOff_49.setFont(font4)
        self.CircleOff_49.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: white;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"	color: black;\n"
"}\n"
"")
        self.CircleOff_49.setCheckable(True)

        self.horizontalLayout_81.addWidget(self.CircleOff_49)

        self.CircleOn_49 = QPushButton(self.y0_41)
        self.CircleOn_49.setObjectName(u"CircleOn_49")
        sizePolicy2.setHeightForWidth(self.CircleOn_49.sizePolicy().hasHeightForWidth())
        self.CircleOn_49.setSizePolicy(sizePolicy2)
        self.CircleOn_49.setMaximumSize(QSize(30, 30))
        self.CircleOn_49.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: #000000;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"}\n"
"")
        self.CircleOn_49.setCheckable(True)

        self.horizontalLayout_81.addWidget(self.CircleOn_49)


        self.gridLayout_7.addWidget(self.y0_41, 7, 1, 1, 1)

        self.y0_42 = QWidget(self.widget_2)
        self.y0_42.setObjectName(u"y0_42")
        sizePolicy5.setHeightForWidth(self.y0_42.sizePolicy().hasHeightForWidth())
        self.y0_42.setSizePolicy(sizePolicy5)
        self.y0_42.setMinimumSize(QSize(90, 60))
        self.y0_42.setStyleSheet(u"    border: none;\n"
"    border-radius: 24px;\n"
"    background-color: #000000;\n"
"")
        self.horizontalLayout_82 = QHBoxLayout(self.y0_42)
        self.horizontalLayout_82.setObjectName(u"horizontalLayout_82")
        self.horizontalLayout_82.setContentsMargins(4, -1, -1, -1)
        self.CircleOff_50 = QPushButton(self.y0_42)
        self.CircleOff_50.setObjectName(u"CircleOff_50")
        sizePolicy2.setHeightForWidth(self.CircleOff_50.sizePolicy().hasHeightForWidth())
        self.CircleOff_50.setSizePolicy(sizePolicy2)
        self.CircleOff_50.setMinimumSize(QSize(0, 30))
        self.CircleOff_50.setMaximumSize(QSize(30, 30))
        self.CircleOff_50.setFont(font4)
        self.CircleOff_50.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: white;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"	color: black;\n"
"}\n"
"")
        self.CircleOff_50.setCheckable(True)

        self.horizontalLayout_82.addWidget(self.CircleOff_50)

        self.CircleOn_50 = QPushButton(self.y0_42)
        self.CircleOn_50.setObjectName(u"CircleOn_50")
        sizePolicy2.setHeightForWidth(self.CircleOn_50.sizePolicy().hasHeightForWidth())
        self.CircleOn_50.setSizePolicy(sizePolicy2)
        self.CircleOn_50.setMaximumSize(QSize(30, 30))
        self.CircleOn_50.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: #000000;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"}\n"
"")
        self.CircleOn_50.setCheckable(True)

        self.horizontalLayout_82.addWidget(self.CircleOn_50)


        self.gridLayout_7.addWidget(self.y0_42, 7, 2, 1, 1)

        self.y0_43 = QWidget(self.widget_2)
        self.y0_43.setObjectName(u"y0_43")
        sizePolicy5.setHeightForWidth(self.y0_43.sizePolicy().hasHeightForWidth())
        self.y0_43.setSizePolicy(sizePolicy5)
        self.y0_43.setMinimumSize(QSize(90, 60))
        self.y0_43.setStyleSheet(u"    border: none;\n"
"    border-radius: 24px;\n"
"    background-color: #000000;\n"
"")
        self.horizontalLayout_83 = QHBoxLayout(self.y0_43)
        self.horizontalLayout_83.setObjectName(u"horizontalLayout_83")
        self.horizontalLayout_83.setContentsMargins(4, -1, -1, -1)
        self.CircleOff_51 = QPushButton(self.y0_43)
        self.CircleOff_51.setObjectName(u"CircleOff_51")
        sizePolicy2.setHeightForWidth(self.CircleOff_51.sizePolicy().hasHeightForWidth())
        self.CircleOff_51.setSizePolicy(sizePolicy2)
        self.CircleOff_51.setMinimumSize(QSize(0, 30))
        self.CircleOff_51.setMaximumSize(QSize(30, 30))
        self.CircleOff_51.setFont(font4)
        self.CircleOff_51.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: white;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"	color: black;\n"
"}\n"
"")
        self.CircleOff_51.setCheckable(True)

        self.horizontalLayout_83.addWidget(self.CircleOff_51)

        self.CircleOn_51 = QPushButton(self.y0_43)
        self.CircleOn_51.setObjectName(u"CircleOn_51")
        sizePolicy2.setHeightForWidth(self.CircleOn_51.sizePolicy().hasHeightForWidth())
        self.CircleOn_51.setSizePolicy(sizePolicy2)
        self.CircleOn_51.setMaximumSize(QSize(30, 30))
        self.CircleOn_51.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: #000000;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"}\n"
"")
        self.CircleOn_51.setCheckable(True)

        self.horizontalLayout_83.addWidget(self.CircleOn_51)


        self.gridLayout_7.addWidget(self.y0_43, 7, 3, 1, 1)

        self.y0_38 = QWidget(self.widget_2)
        self.y0_38.setObjectName(u"y0_38")
        sizePolicy5.setHeightForWidth(self.y0_38.sizePolicy().hasHeightForWidth())
        self.y0_38.setSizePolicy(sizePolicy5)
        self.y0_38.setMinimumSize(QSize(90, 60))
        self.y0_38.setStyleSheet(u"    border: none;\n"
"    border-radius: 24px;\n"
"    background-color: #000000;\n"
"")
        self.horizontalLayout_77 = QHBoxLayout(self.y0_38)
        self.horizontalLayout_77.setObjectName(u"horizontalLayout_77")
        self.horizontalLayout_77.setContentsMargins(4, -1, -1, -1)
        self.CircleOff_45 = QPushButton(self.y0_38)
        self.CircleOff_45.setObjectName(u"CircleOff_45")
        sizePolicy2.setHeightForWidth(self.CircleOff_45.sizePolicy().hasHeightForWidth())
        self.CircleOff_45.setSizePolicy(sizePolicy2)
        self.CircleOff_45.setMinimumSize(QSize(0, 30))
        self.CircleOff_45.setMaximumSize(QSize(30, 30))
        self.CircleOff_45.setFont(font4)
        self.CircleOff_45.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: white;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"	color: black;\n"
"}\n"
"")
        self.CircleOff_45.setCheckable(True)

        self.horizontalLayout_77.addWidget(self.CircleOff_45)

        self.CircleOn_45 = QPushButton(self.y0_38)
        self.CircleOn_45.setObjectName(u"CircleOn_45")
        sizePolicy2.setHeightForWidth(self.CircleOn_45.sizePolicy().hasHeightForWidth())
        self.CircleOn_45.setSizePolicy(sizePolicy2)
        self.CircleOn_45.setMaximumSize(QSize(30, 30))
        self.CircleOn_45.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: #000000;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"}\n"
"")
        self.CircleOn_45.setCheckable(True)

        self.horizontalLayout_77.addWidget(self.CircleOn_45)


        self.gridLayout_7.addWidget(self.y0_38, 6, 5, 1, 1)

        self.y0_16 = QWidget(self.widget_2)
        self.y0_16.setObjectName(u"y0_16")
        sizePolicy5.setHeightForWidth(self.y0_16.sizePolicy().hasHeightForWidth())
        self.y0_16.setSizePolicy(sizePolicy5)
        self.y0_16.setMinimumSize(QSize(90, 60))
        self.y0_16.setStyleSheet(u"    border: none;\n"
"    border-radius: 24px;\n"
"    background-color: #000000;\n"
"")
        self.horizontalLayout_48 = QHBoxLayout(self.y0_16)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.horizontalLayout_48.setContentsMargins(4, -1, -1, -1)
        self.CircleOff_16 = QPushButton(self.y0_16)
        self.CircleOff_16.setObjectName(u"CircleOff_16")
        sizePolicy2.setHeightForWidth(self.CircleOff_16.sizePolicy().hasHeightForWidth())
        self.CircleOff_16.setSizePolicy(sizePolicy2)
        self.CircleOff_16.setMinimumSize(QSize(0, 30))
        self.CircleOff_16.setMaximumSize(QSize(30, 30))
        self.CircleOff_16.setFont(font4)
        self.CircleOff_16.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: white;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"	color: black;\n"
"}\n"
"")
        self.CircleOff_16.setCheckable(True)

        self.horizontalLayout_48.addWidget(self.CircleOff_16)

        self.CircleOn_16 = QPushButton(self.y0_16)
        self.CircleOn_16.setObjectName(u"CircleOn_16")
        sizePolicy2.setHeightForWidth(self.CircleOn_16.sizePolicy().hasHeightForWidth())
        self.CircleOn_16.setSizePolicy(sizePolicy2)
        self.CircleOn_16.setMaximumSize(QSize(30, 30))
        self.CircleOn_16.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: #000000;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"}\n"
"")
        self.CircleOn_16.setCheckable(True)

        self.horizontalLayout_48.addWidget(self.CircleOn_16)


        self.gridLayout_7.addWidget(self.y0_16, 3, 1, 1, 1)

        self.y0_19 = QWidget(self.widget_2)
        self.y0_19.setObjectName(u"y0_19")
        sizePolicy5.setHeightForWidth(self.y0_19.sizePolicy().hasHeightForWidth())
        self.y0_19.setSizePolicy(sizePolicy5)
        self.y0_19.setMinimumSize(QSize(90, 60))
        self.y0_19.setStyleSheet(u"    border: none;\n"
"    border-radius: 24px;\n"
"    background-color: #000000;\n"
"")
        self.horizontalLayout_51 = QHBoxLayout(self.y0_19)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.horizontalLayout_51.setContentsMargins(4, -1, -1, -1)
        self.CircleOff_19 = QPushButton(self.y0_19)
        self.CircleOff_19.setObjectName(u"CircleOff_19")
        sizePolicy2.setHeightForWidth(self.CircleOff_19.sizePolicy().hasHeightForWidth())
        self.CircleOff_19.setSizePolicy(sizePolicy2)
        self.CircleOff_19.setMinimumSize(QSize(0, 30))
        self.CircleOff_19.setMaximumSize(QSize(30, 30))
        self.CircleOff_19.setFont(font4)
        self.CircleOff_19.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: white;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"	color: black;\n"
"}\n"
"")
        self.CircleOff_19.setCheckable(True)

        self.horizontalLayout_51.addWidget(self.CircleOff_19)

        self.CircleOn_19 = QPushButton(self.y0_19)
        self.CircleOn_19.setObjectName(u"CircleOn_19")
        sizePolicy2.setHeightForWidth(self.CircleOn_19.sizePolicy().hasHeightForWidth())
        self.CircleOn_19.setSizePolicy(sizePolicy2)
        self.CircleOn_19.setMaximumSize(QSize(30, 30))
        self.CircleOn_19.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: #000000;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"}\n"
"")
        self.CircleOn_19.setCheckable(True)

        self.horizontalLayout_51.addWidget(self.CircleOn_19)


        self.gridLayout_7.addWidget(self.y0_19, 3, 4, 1, 1)

        self.y0_31 = QWidget(self.widget_2)
        self.y0_31.setObjectName(u"y0_31")
        sizePolicy5.setHeightForWidth(self.y0_31.sizePolicy().hasHeightForWidth())
        self.y0_31.setSizePolicy(sizePolicy5)
        self.y0_31.setMinimumSize(QSize(90, 60))
        self.y0_31.setStyleSheet(u"    border: none;\n"
"    border-radius: 24px;\n"
"    background-color: #000000;\n"
"")
        self.horizontalLayout_63 = QHBoxLayout(self.y0_31)
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.horizontalLayout_63.setContentsMargins(4, -1, -1, -1)
        self.CircleOff_31 = QPushButton(self.y0_31)
        self.CircleOff_31.setObjectName(u"CircleOff_31")
        sizePolicy2.setHeightForWidth(self.CircleOff_31.sizePolicy().hasHeightForWidth())
        self.CircleOff_31.setSizePolicy(sizePolicy2)
        self.CircleOff_31.setMinimumSize(QSize(0, 30))
        self.CircleOff_31.setMaximumSize(QSize(30, 30))
        self.CircleOff_31.setFont(font4)
        self.CircleOff_31.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: white;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"	color: black;\n"
"}\n"
"")
        self.CircleOff_31.setCheckable(True)

        self.horizontalLayout_63.addWidget(self.CircleOff_31)

        self.CircleOn_31 = QPushButton(self.y0_31)
        self.CircleOn_31.setObjectName(u"CircleOn_31")
        sizePolicy2.setHeightForWidth(self.CircleOn_31.sizePolicy().hasHeightForWidth())
        self.CircleOn_31.setSizePolicy(sizePolicy2)
        self.CircleOn_31.setMaximumSize(QSize(30, 30))
        self.CircleOn_31.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: #000000;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"}\n"
"")
        self.CircleOn_31.setCheckable(True)

        self.horizontalLayout_63.addWidget(self.CircleOn_31)


        self.gridLayout_7.addWidget(self.y0_31, 5, 4, 1, 1)

        self.y0_7 = QWidget(self.widget_2)
        self.y0_7.setObjectName(u"y0_7")
        sizePolicy5.setHeightForWidth(self.y0_7.sizePolicy().hasHeightForWidth())
        self.y0_7.setSizePolicy(sizePolicy5)
        self.y0_7.setMinimumSize(QSize(90, 60))
        self.y0_7.setStyleSheet(u"    border: none;\n"
"    border-radius: 24px;\n"
"    background-color: #000000;\n"
"")
        self.horizontalLayout_39 = QHBoxLayout(self.y0_7)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalLayout_39.setContentsMargins(4, -1, -1, -1)
        self.CircleOff_7 = QPushButton(self.y0_7)
        self.CircleOff_7.setObjectName(u"CircleOff_7")
        sizePolicy2.setHeightForWidth(self.CircleOff_7.sizePolicy().hasHeightForWidth())
        self.CircleOff_7.setSizePolicy(sizePolicy2)
        self.CircleOff_7.setMinimumSize(QSize(0, 30))
        self.CircleOff_7.setMaximumSize(QSize(30, 30))
        self.CircleOff_7.setFont(font4)
        self.CircleOff_7.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: white;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"	color: black;\n"
"}\n"
"")
        self.CircleOff_7.setCheckable(True)

        self.horizontalLayout_39.addWidget(self.CircleOff_7)

        self.CircleOn_7 = QPushButton(self.y0_7)
        self.CircleOn_7.setObjectName(u"CircleOn_7")
        sizePolicy2.setHeightForWidth(self.CircleOn_7.sizePolicy().hasHeightForWidth())
        self.CircleOn_7.setSizePolicy(sizePolicy2)
        self.CircleOn_7.setMaximumSize(QSize(30, 30))
        self.CircleOn_7.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: #000000;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"}\n"
"")
        self.CircleOn_7.setCheckable(True)

        self.horizontalLayout_39.addWidget(self.CircleOn_7)


        self.gridLayout_7.addWidget(self.y0_7, 1, 4, 1, 1)

        self.y0_47 = QWidget(self.widget_2)
        self.y0_47.setObjectName(u"y0_47")
        sizePolicy5.setHeightForWidth(self.y0_47.sizePolicy().hasHeightForWidth())
        self.y0_47.setSizePolicy(sizePolicy5)
        self.y0_47.setMinimumSize(QSize(90, 60))
        self.y0_47.setStyleSheet(u"    border: none;\n"
"    border-radius: 24px;\n"
"    background-color: #000000;\n"
"")
        self.horizontalLayout_87 = QHBoxLayout(self.y0_47)
        self.horizontalLayout_87.setObjectName(u"horizontalLayout_87")
        self.horizontalLayout_87.setContentsMargins(4, -1, -1, -1)
        self.CircleOff_55 = QPushButton(self.y0_47)
        self.CircleOff_55.setObjectName(u"CircleOff_55")
        sizePolicy2.setHeightForWidth(self.CircleOff_55.sizePolicy().hasHeightForWidth())
        self.CircleOff_55.setSizePolicy(sizePolicy2)
        self.CircleOff_55.setMinimumSize(QSize(0, 30))
        self.CircleOff_55.setMaximumSize(QSize(30, 30))
        self.CircleOff_55.setFont(font4)
        self.CircleOff_55.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: white;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"	color: black;\n"
"}\n"
"")
        self.CircleOff_55.setCheckable(True)

        self.horizontalLayout_87.addWidget(self.CircleOff_55)

        self.CircleOn_55 = QPushButton(self.y0_47)
        self.CircleOn_55.setObjectName(u"CircleOn_55")
        sizePolicy2.setHeightForWidth(self.CircleOn_55.sizePolicy().hasHeightForWidth())
        self.CircleOn_55.setSizePolicy(sizePolicy2)
        self.CircleOn_55.setMaximumSize(QSize(30, 30))
        self.CircleOn_55.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: #000000;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"}\n"
"")
        self.CircleOn_55.setCheckable(True)

        self.horizontalLayout_87.addWidget(self.CircleOn_55)


        self.gridLayout_7.addWidget(self.y0_47, 8, 2, 1, 1)

        self.y0_36 = QWidget(self.widget_2)
        self.y0_36.setObjectName(u"y0_36")
        sizePolicy5.setHeightForWidth(self.y0_36.sizePolicy().hasHeightForWidth())
        self.y0_36.setSizePolicy(sizePolicy5)
        self.y0_36.setMinimumSize(QSize(90, 60))
        self.y0_36.setStyleSheet(u"    border: none;\n"
"    border-radius: 24px;\n"
"    background-color: #000000;\n"
"")
        self.horizontalLayout_70 = QHBoxLayout(self.y0_36)
        self.horizontalLayout_70.setObjectName(u"horizontalLayout_70")
        self.horizontalLayout_70.setContentsMargins(4, -1, -1, -1)
        self.CircleOff_38 = QPushButton(self.y0_36)
        self.CircleOff_38.setObjectName(u"CircleOff_38")
        sizePolicy2.setHeightForWidth(self.CircleOff_38.sizePolicy().hasHeightForWidth())
        self.CircleOff_38.setSizePolicy(sizePolicy2)
        self.CircleOff_38.setMinimumSize(QSize(0, 30))
        self.CircleOff_38.setMaximumSize(QSize(30, 30))
        self.CircleOff_38.setFont(font4)
        self.CircleOff_38.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: white;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"	color: black;\n"
"}\n"
"")
        self.CircleOff_38.setCheckable(True)

        self.horizontalLayout_70.addWidget(self.CircleOff_38)

        self.CircleOn_38 = QPushButton(self.y0_36)
        self.CircleOn_38.setObjectName(u"CircleOn_38")
        sizePolicy2.setHeightForWidth(self.CircleOn_38.sizePolicy().hasHeightForWidth())
        self.CircleOn_38.setSizePolicy(sizePolicy2)
        self.CircleOn_38.setMaximumSize(QSize(30, 30))
        self.CircleOn_38.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: #000000;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"}\n"
"")
        self.CircleOn_38.setCheckable(True)

        self.horizontalLayout_70.addWidget(self.CircleOn_38)


        self.gridLayout_7.addWidget(self.y0_36, 6, 3, 1, 1)

        self.y0_3 = QWidget(self.widget_2)
        self.y0_3.setObjectName(u"y0_3")
        sizePolicy5.setHeightForWidth(self.y0_3.sizePolicy().hasHeightForWidth())
        self.y0_3.setSizePolicy(sizePolicy5)
        self.y0_3.setMinimumSize(QSize(90, 60))
        self.y0_3.setStyleSheet(u"    border: none;\n"
"    border-radius: 24px;\n"
"    background-color: #000000;\n"
"")
        self.horizontalLayout_35 = QHBoxLayout(self.y0_3)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(4, -1, -1, -1)
        self.CircleOff_3 = QPushButton(self.y0_3)
        self.CircleOff_3.setObjectName(u"CircleOff_3")
        sizePolicy2.setHeightForWidth(self.CircleOff_3.sizePolicy().hasHeightForWidth())
        self.CircleOff_3.setSizePolicy(sizePolicy2)
        self.CircleOff_3.setMinimumSize(QSize(0, 30))
        self.CircleOff_3.setMaximumSize(QSize(30, 30))
        self.CircleOff_3.setFont(font4)
        self.CircleOff_3.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: white;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"	color: black;\n"
"}\n"
"")
        self.CircleOff_3.setCheckable(True)

        self.horizontalLayout_35.addWidget(self.CircleOff_3)

        self.CircleOn_3 = QPushButton(self.y0_3)
        self.CircleOn_3.setObjectName(u"CircleOn_3")
        sizePolicy2.setHeightForWidth(self.CircleOn_3.sizePolicy().hasHeightForWidth())
        self.CircleOn_3.setSizePolicy(sizePolicy2)
        self.CircleOn_3.setMaximumSize(QSize(30, 30))
        self.CircleOn_3.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: #000000;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"}\n"
"")
        self.CircleOn_3.setCheckable(True)

        self.horizontalLayout_35.addWidget(self.CircleOn_3)


        self.gridLayout_7.addWidget(self.y0_3, 1, 0, 1, 1)

        self.y0_17 = QWidget(self.widget_2)
        self.y0_17.setObjectName(u"y0_17")
        sizePolicy5.setHeightForWidth(self.y0_17.sizePolicy().hasHeightForWidth())
        self.y0_17.setSizePolicy(sizePolicy5)
        self.y0_17.setMinimumSize(QSize(90, 60))
        self.y0_17.setStyleSheet(u"    border: none;\n"
"    border-radius: 24px;\n"
"    background-color: #000000;\n"
"")
        self.horizontalLayout_49 = QHBoxLayout(self.y0_17)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.horizontalLayout_49.setContentsMargins(4, -1, -1, -1)
        self.CircleOff_17 = QPushButton(self.y0_17)
        self.CircleOff_17.setObjectName(u"CircleOff_17")
        sizePolicy2.setHeightForWidth(self.CircleOff_17.sizePolicy().hasHeightForWidth())
        self.CircleOff_17.setSizePolicy(sizePolicy2)
        self.CircleOff_17.setMinimumSize(QSize(0, 30))
        self.CircleOff_17.setMaximumSize(QSize(30, 30))
        self.CircleOff_17.setFont(font4)
        self.CircleOff_17.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: white;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"	color: black;\n"
"}\n"
"")
        self.CircleOff_17.setCheckable(True)

        self.horizontalLayout_49.addWidget(self.CircleOff_17)

        self.CircleOn_17 = QPushButton(self.y0_17)
        self.CircleOn_17.setObjectName(u"CircleOn_17")
        sizePolicy2.setHeightForWidth(self.CircleOn_17.sizePolicy().hasHeightForWidth())
        self.CircleOn_17.setSizePolicy(sizePolicy2)
        self.CircleOn_17.setMaximumSize(QSize(30, 30))
        self.CircleOn_17.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: #000000;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"}\n"
"")
        self.CircleOn_17.setCheckable(True)

        self.horizontalLayout_49.addWidget(self.CircleOn_17)


        self.gridLayout_7.addWidget(self.y0_17, 3, 2, 1, 1)

        self.y0_45 = QWidget(self.widget_2)
        self.y0_45.setObjectName(u"y0_45")
        sizePolicy5.setHeightForWidth(self.y0_45.sizePolicy().hasHeightForWidth())
        self.y0_45.setSizePolicy(sizePolicy5)
        self.y0_45.setMinimumSize(QSize(90, 60))
        self.y0_45.setStyleSheet(u"    border: none;\n"
"    border-radius: 24px;\n"
"    background-color: #000000;\n"
"")
        self.horizontalLayout_85 = QHBoxLayout(self.y0_45)
        self.horizontalLayout_85.setObjectName(u"horizontalLayout_85")
        self.horizontalLayout_85.setContentsMargins(4, -1, -1, -1)
        self.CircleOff_53 = QPushButton(self.y0_45)
        self.CircleOff_53.setObjectName(u"CircleOff_53")
        sizePolicy2.setHeightForWidth(self.CircleOff_53.sizePolicy().hasHeightForWidth())
        self.CircleOff_53.setSizePolicy(sizePolicy2)
        self.CircleOff_53.setMinimumSize(QSize(0, 30))
        self.CircleOff_53.setMaximumSize(QSize(30, 30))
        self.CircleOff_53.setFont(font4)
        self.CircleOff_53.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: white;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"	color: black;\n"
"}\n"
"")
        self.CircleOff_53.setCheckable(True)

        self.horizontalLayout_85.addWidget(self.CircleOff_53)

        self.CircleOn_53 = QPushButton(self.y0_45)
        self.CircleOn_53.setObjectName(u"CircleOn_53")
        sizePolicy2.setHeightForWidth(self.CircleOn_53.sizePolicy().hasHeightForWidth())
        self.CircleOn_53.setSizePolicy(sizePolicy2)
        self.CircleOn_53.setMaximumSize(QSize(30, 30))
        self.CircleOn_53.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: #000000;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"}\n"
"")
        self.CircleOn_53.setCheckable(True)

        self.horizontalLayout_85.addWidget(self.CircleOn_53)


        self.gridLayout_7.addWidget(self.y0_45, 7, 5, 1, 1)

        self.y0_37 = QWidget(self.widget_2)
        self.y0_37.setObjectName(u"y0_37")
        sizePolicy5.setHeightForWidth(self.y0_37.sizePolicy().hasHeightForWidth())
        self.y0_37.setSizePolicy(sizePolicy5)
        self.y0_37.setMinimumSize(QSize(90, 60))
        self.y0_37.setStyleSheet(u"    border: none;\n"
"    border-radius: 24px;\n"
"    background-color: #000000;\n"
"")
        self.horizontalLayout_76 = QHBoxLayout(self.y0_37)
        self.horizontalLayout_76.setObjectName(u"horizontalLayout_76")
        self.horizontalLayout_76.setContentsMargins(4, -1, -1, -1)
        self.CircleOff_44 = QPushButton(self.y0_37)
        self.CircleOff_44.setObjectName(u"CircleOff_44")
        sizePolicy2.setHeightForWidth(self.CircleOff_44.sizePolicy().hasHeightForWidth())
        self.CircleOff_44.setSizePolicy(sizePolicy2)
        self.CircleOff_44.setMinimumSize(QSize(0, 30))
        self.CircleOff_44.setMaximumSize(QSize(30, 30))
        self.CircleOff_44.setFont(font4)
        self.CircleOff_44.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: white;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"	color: black;\n"
"}\n"
"")
        self.CircleOff_44.setCheckable(True)

        self.horizontalLayout_76.addWidget(self.CircleOff_44)

        self.CircleOn_44 = QPushButton(self.y0_37)
        self.CircleOn_44.setObjectName(u"CircleOn_44")
        sizePolicy2.setHeightForWidth(self.CircleOn_44.sizePolicy().hasHeightForWidth())
        self.CircleOn_44.setSizePolicy(sizePolicy2)
        self.CircleOn_44.setMaximumSize(QSize(30, 30))
        self.CircleOn_44.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: #000000;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"}\n"
"")
        self.CircleOn_44.setCheckable(True)

        self.horizontalLayout_76.addWidget(self.CircleOn_44)


        self.gridLayout_7.addWidget(self.y0_37, 6, 4, 1, 1)

        self.y0_13 = QWidget(self.widget_2)
        self.y0_13.setObjectName(u"y0_13")
        sizePolicy5.setHeightForWidth(self.y0_13.sizePolicy().hasHeightForWidth())
        self.y0_13.setSizePolicy(sizePolicy5)
        self.y0_13.setMinimumSize(QSize(90, 60))
        self.y0_13.setStyleSheet(u"    border: none;\n"
"    border-radius: 24px;\n"
"    background-color: #000000;\n"
"")
        self.horizontalLayout_45 = QHBoxLayout(self.y0_13)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.horizontalLayout_45.setContentsMargins(4, -1, -1, -1)
        self.CircleOff_13 = QPushButton(self.y0_13)
        self.CircleOff_13.setObjectName(u"CircleOff_13")
        sizePolicy2.setHeightForWidth(self.CircleOff_13.sizePolicy().hasHeightForWidth())
        self.CircleOff_13.setSizePolicy(sizePolicy2)
        self.CircleOff_13.setMinimumSize(QSize(0, 30))
        self.CircleOff_13.setMaximumSize(QSize(30, 30))
        self.CircleOff_13.setFont(font4)
        self.CircleOff_13.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: white;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"	color: black;\n"
"}\n"
"")
        self.CircleOff_13.setCheckable(True)

        self.horizontalLayout_45.addWidget(self.CircleOff_13)

        self.CircleOn_13 = QPushButton(self.y0_13)
        self.CircleOn_13.setObjectName(u"CircleOn_13")
        sizePolicy2.setHeightForWidth(self.CircleOn_13.sizePolicy().hasHeightForWidth())
        self.CircleOn_13.setSizePolicy(sizePolicy2)
        self.CircleOn_13.setMaximumSize(QSize(30, 30))
        self.CircleOn_13.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: #000000;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"}\n"
"")
        self.CircleOn_13.setCheckable(True)

        self.horizontalLayout_45.addWidget(self.CircleOn_13)


        self.gridLayout_7.addWidget(self.y0_13, 2, 4, 1, 1)

        self.y0_28 = QWidget(self.widget_2)
        self.y0_28.setObjectName(u"y0_28")
        sizePolicy5.setHeightForWidth(self.y0_28.sizePolicy().hasHeightForWidth())
        self.y0_28.setSizePolicy(sizePolicy5)
        self.y0_28.setMinimumSize(QSize(90, 60))
        self.y0_28.setStyleSheet(u"    border: none;\n"
"    border-radius: 24px;\n"
"    background-color: #000000;\n"
"")
        self.horizontalLayout_60 = QHBoxLayout(self.y0_28)
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.horizontalLayout_60.setContentsMargins(4, -1, -1, -1)
        self.CircleOff_28 = QPushButton(self.y0_28)
        self.CircleOff_28.setObjectName(u"CircleOff_28")
        sizePolicy2.setHeightForWidth(self.CircleOff_28.sizePolicy().hasHeightForWidth())
        self.CircleOff_28.setSizePolicy(sizePolicy2)
        self.CircleOff_28.setMinimumSize(QSize(0, 30))
        self.CircleOff_28.setMaximumSize(QSize(30, 30))
        self.CircleOff_28.setFont(font4)
        self.CircleOff_28.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: white;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"	color: black;\n"
"}\n"
"")
        self.CircleOff_28.setCheckable(True)

        self.horizontalLayout_60.addWidget(self.CircleOff_28)

        self.CircleOn_28 = QPushButton(self.y0_28)
        self.CircleOn_28.setObjectName(u"CircleOn_28")
        sizePolicy2.setHeightForWidth(self.CircleOn_28.sizePolicy().hasHeightForWidth())
        self.CircleOn_28.setSizePolicy(sizePolicy2)
        self.CircleOn_28.setMaximumSize(QSize(30, 30))
        self.CircleOn_28.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: #000000;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"}\n"
"")
        self.CircleOn_28.setCheckable(True)

        self.horizontalLayout_60.addWidget(self.CircleOn_28)


        self.gridLayout_7.addWidget(self.y0_28, 5, 1, 1, 1)

        self.y0_27 = QWidget(self.widget_2)
        self.y0_27.setObjectName(u"y0_27")
        sizePolicy5.setHeightForWidth(self.y0_27.sizePolicy().hasHeightForWidth())
        self.y0_27.setSizePolicy(sizePolicy5)
        self.y0_27.setMinimumSize(QSize(90, 60))
        self.y0_27.setStyleSheet(u"    border: none;\n"
"    border-radius: 24px;\n"
"    background-color: #000000;\n"
"")
        self.horizontalLayout_59 = QHBoxLayout(self.y0_27)
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.horizontalLayout_59.setContentsMargins(4, -1, -1, -1)
        self.CircleOff_27 = QPushButton(self.y0_27)
        self.CircleOff_27.setObjectName(u"CircleOff_27")
        sizePolicy2.setHeightForWidth(self.CircleOff_27.sizePolicy().hasHeightForWidth())
        self.CircleOff_27.setSizePolicy(sizePolicy2)
        self.CircleOff_27.setMinimumSize(QSize(0, 30))
        self.CircleOff_27.setMaximumSize(QSize(30, 30))
        self.CircleOff_27.setFont(font4)
        self.CircleOff_27.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: white;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"	color: black;\n"
"}\n"
"")
        self.CircleOff_27.setCheckable(True)

        self.horizontalLayout_59.addWidget(self.CircleOff_27)

        self.CircleOn_27 = QPushButton(self.y0_27)
        self.CircleOn_27.setObjectName(u"CircleOn_27")
        sizePolicy2.setHeightForWidth(self.CircleOn_27.sizePolicy().hasHeightForWidth())
        self.CircleOn_27.setSizePolicy(sizePolicy2)
        self.CircleOn_27.setMaximumSize(QSize(30, 30))
        self.CircleOn_27.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: #000000;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"}\n"
"")
        self.CircleOn_27.setCheckable(True)

        self.horizontalLayout_59.addWidget(self.CircleOn_27)


        self.gridLayout_7.addWidget(self.y0_27, 5, 0, 1, 1)

        self.y0_29 = QWidget(self.widget_2)
        self.y0_29.setObjectName(u"y0_29")
        sizePolicy5.setHeightForWidth(self.y0_29.sizePolicy().hasHeightForWidth())
        self.y0_29.setSizePolicy(sizePolicy5)
        self.y0_29.setMinimumSize(QSize(90, 60))
        self.y0_29.setStyleSheet(u"    border: none;\n"
"    border-radius: 24px;\n"
"    background-color: #000000;\n"
"")
        self.horizontalLayout_61 = QHBoxLayout(self.y0_29)
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.horizontalLayout_61.setContentsMargins(4, -1, -1, -1)
        self.CircleOff_29 = QPushButton(self.y0_29)
        self.CircleOff_29.setObjectName(u"CircleOff_29")
        sizePolicy2.setHeightForWidth(self.CircleOff_29.sizePolicy().hasHeightForWidth())
        self.CircleOff_29.setSizePolicy(sizePolicy2)
        self.CircleOff_29.setMinimumSize(QSize(0, 30))
        self.CircleOff_29.setMaximumSize(QSize(30, 30))
        self.CircleOff_29.setFont(font4)
        self.CircleOff_29.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: white;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"	color: black;\n"
"}\n"
"")
        self.CircleOff_29.setCheckable(True)

        self.horizontalLayout_61.addWidget(self.CircleOff_29)

        self.CircleOn_29 = QPushButton(self.y0_29)
        self.CircleOn_29.setObjectName(u"CircleOn_29")
        sizePolicy2.setHeightForWidth(self.CircleOn_29.sizePolicy().hasHeightForWidth())
        self.CircleOn_29.setSizePolicy(sizePolicy2)
        self.CircleOn_29.setMaximumSize(QSize(30, 30))
        self.CircleOn_29.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: #000000;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"}\n"
"")
        self.CircleOn_29.setCheckable(True)

        self.horizontalLayout_61.addWidget(self.CircleOn_29)


        self.gridLayout_7.addWidget(self.y0_29, 5, 2, 1, 1)

        self.y0_26 = QWidget(self.widget_2)
        self.y0_26.setObjectName(u"y0_26")
        sizePolicy5.setHeightForWidth(self.y0_26.sizePolicy().hasHeightForWidth())
        self.y0_26.setSizePolicy(sizePolicy5)
        self.y0_26.setMinimumSize(QSize(90, 60))
        self.y0_26.setStyleSheet(u"    border: none;\n"
"    border-radius: 24px;\n"
"    background-color: #000000;\n"
"")
        self.horizontalLayout_58 = QHBoxLayout(self.y0_26)
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.horizontalLayout_58.setContentsMargins(4, -1, -1, -1)
        self.CircleOff_26 = QPushButton(self.y0_26)
        self.CircleOff_26.setObjectName(u"CircleOff_26")
        sizePolicy2.setHeightForWidth(self.CircleOff_26.sizePolicy().hasHeightForWidth())
        self.CircleOff_26.setSizePolicy(sizePolicy2)
        self.CircleOff_26.setMinimumSize(QSize(0, 30))
        self.CircleOff_26.setMaximumSize(QSize(30, 30))
        self.CircleOff_26.setFont(font4)
        self.CircleOff_26.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: white;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"	color: black;\n"
"}\n"
"")
        self.CircleOff_26.setCheckable(True)

        self.horizontalLayout_58.addWidget(self.CircleOff_26)

        self.CircleOn_26 = QPushButton(self.y0_26)
        self.CircleOn_26.setObjectName(u"CircleOn_26")
        sizePolicy2.setHeightForWidth(self.CircleOn_26.sizePolicy().hasHeightForWidth())
        self.CircleOn_26.setSizePolicy(sizePolicy2)
        self.CircleOn_26.setMaximumSize(QSize(30, 30))
        self.CircleOn_26.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: #000000;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"}\n"
"")
        self.CircleOn_26.setCheckable(True)

        self.horizontalLayout_58.addWidget(self.CircleOn_26)


        self.gridLayout_7.addWidget(self.y0_26, 4, 5, 1, 1)

        self.y0_46 = QWidget(self.widget_2)
        self.y0_46.setObjectName(u"y0_46")
        sizePolicy5.setHeightForWidth(self.y0_46.sizePolicy().hasHeightForWidth())
        self.y0_46.setSizePolicy(sizePolicy5)
        self.y0_46.setMinimumSize(QSize(90, 60))
        self.y0_46.setStyleSheet(u"    border: none;\n"
"    border-radius: 24px;\n"
"    background-color: #000000;\n"
"")
        self.horizontalLayout_86 = QHBoxLayout(self.y0_46)
        self.horizontalLayout_86.setObjectName(u"horizontalLayout_86")
        self.horizontalLayout_86.setContentsMargins(4, -1, -1, -1)
        self.CircleOff_54 = QPushButton(self.y0_46)
        self.CircleOff_54.setObjectName(u"CircleOff_54")
        sizePolicy2.setHeightForWidth(self.CircleOff_54.sizePolicy().hasHeightForWidth())
        self.CircleOff_54.setSizePolicy(sizePolicy2)
        self.CircleOff_54.setMinimumSize(QSize(0, 30))
        self.CircleOff_54.setMaximumSize(QSize(30, 30))
        self.CircleOff_54.setFont(font4)
        self.CircleOff_54.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: white;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"	color: black;\n"
"}\n"
"")
        self.CircleOff_54.setCheckable(True)

        self.horizontalLayout_86.addWidget(self.CircleOff_54)

        self.CircleOn_54 = QPushButton(self.y0_46)
        self.CircleOn_54.setObjectName(u"CircleOn_54")
        sizePolicy2.setHeightForWidth(self.CircleOn_54.sizePolicy().hasHeightForWidth())
        self.CircleOn_54.setSizePolicy(sizePolicy2)
        self.CircleOn_54.setMaximumSize(QSize(30, 30))
        self.CircleOn_54.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: #000000;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"}\n"
"")
        self.CircleOn_54.setCheckable(True)

        self.horizontalLayout_86.addWidget(self.CircleOn_54)


        self.gridLayout_7.addWidget(self.y0_46, 8, 1, 1, 1)

        self.y0_12 = QWidget(self.widget_2)
        self.y0_12.setObjectName(u"y0_12")
        sizePolicy5.setHeightForWidth(self.y0_12.sizePolicy().hasHeightForWidth())
        self.y0_12.setSizePolicy(sizePolicy5)
        self.y0_12.setMinimumSize(QSize(90, 60))
        self.y0_12.setStyleSheet(u"    border: none;\n"
"    border-radius: 24px;\n"
"    background-color: #000000;\n"
"")
        self.horizontalLayout_44 = QHBoxLayout(self.y0_12)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.horizontalLayout_44.setContentsMargins(4, -1, -1, -1)
        self.CircleOff_12 = QPushButton(self.y0_12)
        self.CircleOff_12.setObjectName(u"CircleOff_12")
        sizePolicy2.setHeightForWidth(self.CircleOff_12.sizePolicy().hasHeightForWidth())
        self.CircleOff_12.setSizePolicy(sizePolicy2)
        self.CircleOff_12.setMinimumSize(QSize(0, 30))
        self.CircleOff_12.setMaximumSize(QSize(30, 30))
        self.CircleOff_12.setFont(font4)
        self.CircleOff_12.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: white;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"	color: black;\n"
"}\n"
"")
        self.CircleOff_12.setCheckable(True)

        self.horizontalLayout_44.addWidget(self.CircleOff_12)

        self.CircleOn_12 = QPushButton(self.y0_12)
        self.CircleOn_12.setObjectName(u"CircleOn_12")
        sizePolicy2.setHeightForWidth(self.CircleOn_12.sizePolicy().hasHeightForWidth())
        self.CircleOn_12.setSizePolicy(sizePolicy2)
        self.CircleOn_12.setMaximumSize(QSize(30, 30))
        self.CircleOn_12.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: #000000;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"}\n"
"")
        self.CircleOn_12.setCheckable(True)

        self.horizontalLayout_44.addWidget(self.CircleOn_12)


        self.gridLayout_7.addWidget(self.y0_12, 2, 3, 1, 1)

        self.y0_21 = QWidget(self.widget_2)
        self.y0_21.setObjectName(u"y0_21")
        sizePolicy5.setHeightForWidth(self.y0_21.sizePolicy().hasHeightForWidth())
        self.y0_21.setSizePolicy(sizePolicy5)
        self.y0_21.setMinimumSize(QSize(90, 60))
        self.y0_21.setStyleSheet(u"    border: none;\n"
"    border-radius: 24px;\n"
"    background-color: #000000;\n"
"")
        self.horizontalLayout_53 = QHBoxLayout(self.y0_21)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.horizontalLayout_53.setContentsMargins(4, -1, -1, -1)
        self.CircleOff_21 = QPushButton(self.y0_21)
        self.CircleOff_21.setObjectName(u"CircleOff_21")
        sizePolicy2.setHeightForWidth(self.CircleOff_21.sizePolicy().hasHeightForWidth())
        self.CircleOff_21.setSizePolicy(sizePolicy2)
        self.CircleOff_21.setMinimumSize(QSize(0, 30))
        self.CircleOff_21.setMaximumSize(QSize(30, 30))
        self.CircleOff_21.setFont(font4)
        self.CircleOff_21.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: white;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"	color: black;\n"
"}\n"
"")
        self.CircleOff_21.setCheckable(True)

        self.horizontalLayout_53.addWidget(self.CircleOff_21)

        self.CircleOn_21 = QPushButton(self.y0_21)
        self.CircleOn_21.setObjectName(u"CircleOn_21")
        sizePolicy2.setHeightForWidth(self.CircleOn_21.sizePolicy().hasHeightForWidth())
        self.CircleOn_21.setSizePolicy(sizePolicy2)
        self.CircleOn_21.setMaximumSize(QSize(30, 30))
        self.CircleOn_21.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: #000000;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"}\n"
"")
        self.CircleOn_21.setCheckable(True)

        self.horizontalLayout_53.addWidget(self.CircleOn_21)


        self.gridLayout_7.addWidget(self.y0_21, 4, 0, 1, 1)


        self.horizontalLayout_34.addWidget(self.widget_2)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayoutWidget = QWidget(self.DIDOContainerPage)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(20, 30, 661, 260))
        self.gridLayout_8 = QGridLayout(self.gridLayoutWidget)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.y0_58 = QWidget(self.gridLayoutWidget)
        self.y0_58.setObjectName(u"y0_58")
        sizePolicy5.setHeightForWidth(self.y0_58.sizePolicy().hasHeightForWidth())
        self.y0_58.setSizePolicy(sizePolicy5)
        self.y0_58.setMinimumSize(QSize(90, 60))
        self.y0_58.setStyleSheet(u"    border: none;\n"
"    border-radius: 24px;\n"
"    background-color: #000000;\n"
"")
        self.horizontalLayout_65 = QHBoxLayout(self.y0_58)
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.horizontalLayout_65.setContentsMargins(4, -1, -1, -1)
        self.CircleOff_33 = QPushButton(self.y0_58)
        self.CircleOff_33.setObjectName(u"CircleOff_33")
        sizePolicy2.setHeightForWidth(self.CircleOff_33.sizePolicy().hasHeightForWidth())
        self.CircleOff_33.setSizePolicy(sizePolicy2)
        self.CircleOff_33.setMinimumSize(QSize(0, 30))
        self.CircleOff_33.setMaximumSize(QSize(30, 30))
        self.CircleOff_33.setFont(font4)
        self.CircleOff_33.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: white;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"	color: black;\n"
"}\n"
"")
        self.CircleOff_33.setCheckable(True)

        self.horizontalLayout_65.addWidget(self.CircleOff_33)

        self.CircleOn_33 = QPushButton(self.y0_58)
        self.CircleOn_33.setObjectName(u"CircleOn_33")
        sizePolicy2.setHeightForWidth(self.CircleOn_33.sizePolicy().hasHeightForWidth())
        self.CircleOn_33.setSizePolicy(sizePolicy2)
        self.CircleOn_33.setMaximumSize(QSize(30, 30))
        self.CircleOn_33.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: #000000;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"}\n"
"")
        self.CircleOn_33.setCheckable(True)

        self.horizontalLayout_65.addWidget(self.CircleOn_33)


        self.gridLayout_8.addWidget(self.y0_58, 2, 2, 1, 1)

        self.y0_52 = QWidget(self.gridLayoutWidget)
        self.y0_52.setObjectName(u"y0_52")
        sizePolicy5.setHeightForWidth(self.y0_52.sizePolicy().hasHeightForWidth())
        self.y0_52.setSizePolicy(sizePolicy5)
        self.y0_52.setMinimumSize(QSize(90, 60))
        self.y0_52.setStyleSheet(u"    border: none;\n"
"    border-radius: 24px;\n"
"    background-color: #000000;\n"
"")
        self.horizontalLayout_92 = QHBoxLayout(self.y0_52)
        self.horizontalLayout_92.setObjectName(u"horizontalLayout_92")
        self.horizontalLayout_92.setContentsMargins(4, -1, -1, -1)
        self.CircleOff_60 = QPushButton(self.y0_52)
        self.CircleOff_60.setObjectName(u"CircleOff_60")
        sizePolicy2.setHeightForWidth(self.CircleOff_60.sizePolicy().hasHeightForWidth())
        self.CircleOff_60.setSizePolicy(sizePolicy2)
        self.CircleOff_60.setMinimumSize(QSize(0, 30))
        self.CircleOff_60.setMaximumSize(QSize(30, 30))
        self.CircleOff_60.setFont(font4)
        self.CircleOff_60.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: white;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"	color: black;\n"
"}\n"
"")
        self.CircleOff_60.setCheckable(True)

        self.horizontalLayout_92.addWidget(self.CircleOff_60)

        self.CircleOn_60 = QPushButton(self.y0_52)
        self.CircleOn_60.setObjectName(u"CircleOn_60")
        sizePolicy2.setHeightForWidth(self.CircleOn_60.sizePolicy().hasHeightForWidth())
        self.CircleOn_60.setSizePolicy(sizePolicy2)
        self.CircleOn_60.setMaximumSize(QSize(30, 30))
        self.CircleOn_60.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: #000000;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"}\n"
"")
        self.CircleOn_60.setCheckable(True)

        self.horizontalLayout_92.addWidget(self.CircleOn_60)


        self.gridLayout_8.addWidget(self.y0_52, 0, 1, 1, 1)

        self.y0_57 = QWidget(self.gridLayoutWidget)
        self.y0_57.setObjectName(u"y0_57")
        sizePolicy5.setHeightForWidth(self.y0_57.sizePolicy().hasHeightForWidth())
        self.y0_57.setSizePolicy(sizePolicy5)
        self.y0_57.setMinimumSize(QSize(90, 60))
        self.y0_57.setStyleSheet(u"    border: none;\n"
"    border-radius: 24px;\n"
"    background-color: #000000;\n"
"")
        self.horizontalLayout_99 = QHBoxLayout(self.y0_57)
        self.horizontalLayout_99.setObjectName(u"horizontalLayout_99")
        self.horizontalLayout_99.setContentsMargins(4, -1, -1, -1)
        self.CircleOff_67 = QPushButton(self.y0_57)
        self.CircleOff_67.setObjectName(u"CircleOff_67")
        sizePolicy2.setHeightForWidth(self.CircleOff_67.sizePolicy().hasHeightForWidth())
        self.CircleOff_67.setSizePolicy(sizePolicy2)
        self.CircleOff_67.setMinimumSize(QSize(0, 30))
        self.CircleOff_67.setMaximumSize(QSize(30, 30))
        self.CircleOff_67.setFont(font4)
        self.CircleOff_67.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: white;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"	color: black;\n"
"}\n"
"")
        self.CircleOff_67.setCheckable(True)

        self.horizontalLayout_99.addWidget(self.CircleOff_67)

        self.CircleOn_67 = QPushButton(self.y0_57)
        self.CircleOn_67.setObjectName(u"CircleOn_67")
        sizePolicy2.setHeightForWidth(self.CircleOn_67.sizePolicy().hasHeightForWidth())
        self.CircleOn_67.setSizePolicy(sizePolicy2)
        self.CircleOn_67.setMaximumSize(QSize(30, 30))
        self.CircleOn_67.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: #000000;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"}\n"
"")
        self.CircleOn_67.setCheckable(True)

        self.horizontalLayout_99.addWidget(self.CircleOn_67)


        self.gridLayout_8.addWidget(self.y0_57, 1, 2, 1, 1)

        self.y0_53 = QWidget(self.gridLayoutWidget)
        self.y0_53.setObjectName(u"y0_53")
        sizePolicy5.setHeightForWidth(self.y0_53.sizePolicy().hasHeightForWidth())
        self.y0_53.setSizePolicy(sizePolicy5)
        self.y0_53.setMinimumSize(QSize(90, 60))
        self.y0_53.setStyleSheet(u"    border: none;\n"
"    border-radius: 24px;\n"
"    background-color: #000000;\n"
"")
        self.horizontalLayout_93 = QHBoxLayout(self.y0_53)
        self.horizontalLayout_93.setObjectName(u"horizontalLayout_93")
        self.horizontalLayout_93.setContentsMargins(4, -1, -1, -1)
        self.CircleOff_61 = QPushButton(self.y0_53)
        self.CircleOff_61.setObjectName(u"CircleOff_61")
        sizePolicy2.setHeightForWidth(self.CircleOff_61.sizePolicy().hasHeightForWidth())
        self.CircleOff_61.setSizePolicy(sizePolicy2)
        self.CircleOff_61.setMinimumSize(QSize(0, 30))
        self.CircleOff_61.setMaximumSize(QSize(30, 30))
        self.CircleOff_61.setFont(font4)
        self.CircleOff_61.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: white;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"	color: black;\n"
"}\n"
"")
        self.CircleOff_61.setCheckable(True)

        self.horizontalLayout_93.addWidget(self.CircleOff_61)

        self.CircleOn_61 = QPushButton(self.y0_53)
        self.CircleOn_61.setObjectName(u"CircleOn_61")
        sizePolicy2.setHeightForWidth(self.CircleOn_61.sizePolicy().hasHeightForWidth())
        self.CircleOn_61.setSizePolicy(sizePolicy2)
        self.CircleOn_61.setMaximumSize(QSize(30, 30))
        self.CircleOn_61.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: #000000;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"}\n"
"")
        self.CircleOn_61.setCheckable(True)

        self.horizontalLayout_93.addWidget(self.CircleOn_61)


        self.gridLayout_8.addWidget(self.y0_53, 0, 2, 1, 1)

        self.y0_115 = QWidget(self.gridLayoutWidget)
        self.y0_115.setObjectName(u"y0_115")
        sizePolicy5.setHeightForWidth(self.y0_115.sizePolicy().hasHeightForWidth())
        self.y0_115.setSizePolicy(sizePolicy5)
        self.y0_115.setMinimumSize(QSize(90, 60))
        self.y0_115.setStyleSheet(u"    border: none;\n"
"    border-radius: 24px;\n"
"    background-color: #000000;\n"
"")
        self.horizontalLayout_157 = QHBoxLayout(self.y0_115)
        self.horizontalLayout_157.setObjectName(u"horizontalLayout_157")
        self.horizontalLayout_157.setContentsMargins(4, -1, -1, -1)
        self.CircleOff_125 = QPushButton(self.y0_115)
        self.CircleOff_125.setObjectName(u"CircleOff_125")
        sizePolicy2.setHeightForWidth(self.CircleOff_125.sizePolicy().hasHeightForWidth())
        self.CircleOff_125.setSizePolicy(sizePolicy2)
        self.CircleOff_125.setMinimumSize(QSize(0, 30))
        self.CircleOff_125.setMaximumSize(QSize(30, 30))
        self.CircleOff_125.setFont(font4)
        self.CircleOff_125.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: white;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"	color: black;\n"
"}\n"
"")
        self.CircleOff_125.setCheckable(True)

        self.horizontalLayout_157.addWidget(self.CircleOff_125)

        self.CircleOn_125 = QPushButton(self.y0_115)
        self.CircleOn_125.setObjectName(u"CircleOn_125")
        sizePolicy2.setHeightForWidth(self.CircleOn_125.sizePolicy().hasHeightForWidth())
        self.CircleOn_125.setSizePolicy(sizePolicy2)
        self.CircleOn_125.setMaximumSize(QSize(30, 30))
        self.CircleOn_125.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: #000000;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"}\n"
"")
        self.CircleOn_125.setCheckable(True)

        self.horizontalLayout_157.addWidget(self.CircleOn_125)


        self.gridLayout_8.addWidget(self.y0_115, 2, 1, 1, 1)

        self.y0_114 = QWidget(self.gridLayoutWidget)
        self.y0_114.setObjectName(u"y0_114")
        sizePolicy5.setHeightForWidth(self.y0_114.sizePolicy().hasHeightForWidth())
        self.y0_114.setSizePolicy(sizePolicy5)
        self.y0_114.setMinimumSize(QSize(90, 60))
        self.y0_114.setStyleSheet(u"    border: none;\n"
"    border-radius: 24px;\n"
"    background-color: #000000;\n"
"")
        self.horizontalLayout_156 = QHBoxLayout(self.y0_114)
        self.horizontalLayout_156.setObjectName(u"horizontalLayout_156")
        self.horizontalLayout_156.setContentsMargins(4, -1, -1, -1)
        self.CircleOff_124 = QPushButton(self.y0_114)
        self.CircleOff_124.setObjectName(u"CircleOff_124")
        sizePolicy2.setHeightForWidth(self.CircleOff_124.sizePolicy().hasHeightForWidth())
        self.CircleOff_124.setSizePolicy(sizePolicy2)
        self.CircleOff_124.setMinimumSize(QSize(0, 30))
        self.CircleOff_124.setMaximumSize(QSize(30, 30))
        self.CircleOff_124.setFont(font4)
        self.CircleOff_124.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: white;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"	color: black;\n"
"}\n"
"")
        self.CircleOff_124.setCheckable(True)

        self.horizontalLayout_156.addWidget(self.CircleOff_124)

        self.CircleOn_124 = QPushButton(self.y0_114)
        self.CircleOn_124.setObjectName(u"CircleOn_124")
        sizePolicy2.setHeightForWidth(self.CircleOn_124.sizePolicy().hasHeightForWidth())
        self.CircleOn_124.setSizePolicy(sizePolicy2)
        self.CircleOn_124.setMaximumSize(QSize(30, 30))
        self.CircleOn_124.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: #000000;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"}\n"
"")
        self.CircleOn_124.setCheckable(True)

        self.horizontalLayout_156.addWidget(self.CircleOn_124)


        self.gridLayout_8.addWidget(self.y0_114, 2, 0, 1, 1)

        self.y0_113 = QWidget(self.gridLayoutWidget)
        self.y0_113.setObjectName(u"y0_113")
        sizePolicy5.setHeightForWidth(self.y0_113.sizePolicy().hasHeightForWidth())
        self.y0_113.setSizePolicy(sizePolicy5)
        self.y0_113.setMinimumSize(QSize(90, 60))
        self.y0_113.setStyleSheet(u"    border: none;\n"
"    border-radius: 24px;\n"
"    background-color: #000000;\n"
"")
        self.horizontalLayout_155 = QHBoxLayout(self.y0_113)
        self.horizontalLayout_155.setObjectName(u"horizontalLayout_155")
        self.horizontalLayout_155.setContentsMargins(4, -1, -1, -1)
        self.CircleOff_123 = QPushButton(self.y0_113)
        self.CircleOff_123.setObjectName(u"CircleOff_123")
        sizePolicy2.setHeightForWidth(self.CircleOff_123.sizePolicy().hasHeightForWidth())
        self.CircleOff_123.setSizePolicy(sizePolicy2)
        self.CircleOff_123.setMinimumSize(QSize(0, 30))
        self.CircleOff_123.setMaximumSize(QSize(30, 30))
        self.CircleOff_123.setFont(font4)
        self.CircleOff_123.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: white;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"	color: black;\n"
"}\n"
"")
        self.CircleOff_123.setCheckable(True)

        self.horizontalLayout_155.addWidget(self.CircleOff_123)

        self.CircleOn_123 = QPushButton(self.y0_113)
        self.CircleOn_123.setObjectName(u"CircleOn_123")
        sizePolicy2.setHeightForWidth(self.CircleOn_123.sizePolicy().hasHeightForWidth())
        self.CircleOn_123.setSizePolicy(sizePolicy2)
        self.CircleOn_123.setMaximumSize(QSize(30, 30))
        self.CircleOn_123.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: #000000;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"}\n"
"")
        self.CircleOn_123.setCheckable(True)

        self.horizontalLayout_155.addWidget(self.CircleOn_123)


        self.gridLayout_8.addWidget(self.y0_113, 1, 3, 1, 1)

        self.y0_56 = QWidget(self.gridLayoutWidget)
        self.y0_56.setObjectName(u"y0_56")
        sizePolicy5.setHeightForWidth(self.y0_56.sizePolicy().hasHeightForWidth())
        self.y0_56.setSizePolicy(sizePolicy5)
        self.y0_56.setMinimumSize(QSize(90, 60))
        self.y0_56.setStyleSheet(u"    border: none;\n"
"    border-radius: 24px;\n"
"    background-color: #000000;\n"
"")
        self.horizontalLayout_98 = QHBoxLayout(self.y0_56)
        self.horizontalLayout_98.setObjectName(u"horizontalLayout_98")
        self.horizontalLayout_98.setContentsMargins(4, -1, -1, -1)
        self.CircleOff_66 = QPushButton(self.y0_56)
        self.CircleOff_66.setObjectName(u"CircleOff_66")
        sizePolicy2.setHeightForWidth(self.CircleOff_66.sizePolicy().hasHeightForWidth())
        self.CircleOff_66.setSizePolicy(sizePolicy2)
        self.CircleOff_66.setMinimumSize(QSize(0, 30))
        self.CircleOff_66.setMaximumSize(QSize(30, 30))
        self.CircleOff_66.setFont(font4)
        self.CircleOff_66.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: white;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"	color: black;\n"
"}\n"
"")
        self.CircleOff_66.setCheckable(True)

        self.horizontalLayout_98.addWidget(self.CircleOff_66)

        self.CircleOn_66 = QPushButton(self.y0_56)
        self.CircleOn_66.setObjectName(u"CircleOn_66")
        sizePolicy2.setHeightForWidth(self.CircleOn_66.sizePolicy().hasHeightForWidth())
        self.CircleOn_66.setSizePolicy(sizePolicy2)
        self.CircleOn_66.setMaximumSize(QSize(30, 30))
        self.CircleOn_66.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: #000000;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"}\n"
"")
        self.CircleOn_66.setCheckable(True)

        self.horizontalLayout_98.addWidget(self.CircleOn_66)


        self.gridLayout_8.addWidget(self.y0_56, 1, 1, 1, 1)

        self.y0_51 = QWidget(self.gridLayoutWidget)
        self.y0_51.setObjectName(u"y0_51")
        sizePolicy5.setHeightForWidth(self.y0_51.sizePolicy().hasHeightForWidth())
        self.y0_51.setSizePolicy(sizePolicy5)
        self.y0_51.setMinimumSize(QSize(90, 60))
        self.y0_51.setStyleSheet(u"    border: none;\n"
"    border-radius: 24px;\n"
"    background-color: #000000;\n"
"")
        self.horizontalLayout_91 = QHBoxLayout(self.y0_51)
        self.horizontalLayout_91.setObjectName(u"horizontalLayout_91")
        self.horizontalLayout_91.setContentsMargins(4, -1, -1, -1)
        self.CircleOff_59 = QPushButton(self.y0_51)
        self.CircleOff_59.setObjectName(u"CircleOff_59")
        sizePolicy2.setHeightForWidth(self.CircleOff_59.sizePolicy().hasHeightForWidth())
        self.CircleOff_59.setSizePolicy(sizePolicy2)
        self.CircleOff_59.setMinimumSize(QSize(0, 30))
        self.CircleOff_59.setMaximumSize(QSize(30, 30))
        self.CircleOff_59.setFont(font4)
        self.CircleOff_59.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: white;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"	color: black;\n"
"}\n"
"")
        self.CircleOff_59.setCheckable(True)

        self.horizontalLayout_91.addWidget(self.CircleOff_59)

        self.CircleOn_59 = QPushButton(self.y0_51)
        self.CircleOn_59.setObjectName(u"CircleOn_59")
        sizePolicy2.setHeightForWidth(self.CircleOn_59.sizePolicy().hasHeightForWidth())
        self.CircleOn_59.setSizePolicy(sizePolicy2)
        self.CircleOn_59.setMaximumSize(QSize(30, 30))
        self.CircleOn_59.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: #000000;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"}\n"
"")
        self.CircleOn_59.setCheckable(True)

        self.horizontalLayout_91.addWidget(self.CircleOn_59)


        self.gridLayout_8.addWidget(self.y0_51, 0, 0, 1, 1)

        self.y0_54 = QWidget(self.gridLayoutWidget)
        self.y0_54.setObjectName(u"y0_54")
        sizePolicy5.setHeightForWidth(self.y0_54.sizePolicy().hasHeightForWidth())
        self.y0_54.setSizePolicy(sizePolicy5)
        self.y0_54.setMinimumSize(QSize(90, 60))
        self.y0_54.setStyleSheet(u"    border: none;\n"
"    border-radius: 24px;\n"
"    background-color: #000000;\n"
"")
        self.horizontalLayout_96 = QHBoxLayout(self.y0_54)
        self.horizontalLayout_96.setObjectName(u"horizontalLayout_96")
        self.horizontalLayout_96.setContentsMargins(4, -1, -1, -1)
        self.CircleOff_64 = QPushButton(self.y0_54)
        self.CircleOff_64.setObjectName(u"CircleOff_64")
        sizePolicy2.setHeightForWidth(self.CircleOff_64.sizePolicy().hasHeightForWidth())
        self.CircleOff_64.setSizePolicy(sizePolicy2)
        self.CircleOff_64.setMinimumSize(QSize(0, 30))
        self.CircleOff_64.setMaximumSize(QSize(30, 30))
        self.CircleOff_64.setFont(font4)
        self.CircleOff_64.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: white;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"	color: black;\n"
"}\n"
"")
        self.CircleOff_64.setCheckable(True)

        self.horizontalLayout_96.addWidget(self.CircleOff_64)

        self.CircleOn_64 = QPushButton(self.y0_54)
        self.CircleOn_64.setObjectName(u"CircleOn_64")
        sizePolicy2.setHeightForWidth(self.CircleOn_64.sizePolicy().hasHeightForWidth())
        self.CircleOn_64.setSizePolicy(sizePolicy2)
        self.CircleOn_64.setMaximumSize(QSize(30, 30))
        self.CircleOn_64.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: #000000;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"}\n"
"")
        self.CircleOn_64.setCheckable(True)

        self.horizontalLayout_96.addWidget(self.CircleOn_64)


        self.gridLayout_8.addWidget(self.y0_54, 0, 3, 1, 1)

        self.y0_59 = QWidget(self.gridLayoutWidget)
        self.y0_59.setObjectName(u"y0_59")
        sizePolicy5.setHeightForWidth(self.y0_59.sizePolicy().hasHeightForWidth())
        self.y0_59.setSizePolicy(sizePolicy5)
        self.y0_59.setMinimumSize(QSize(90, 60))
        self.y0_59.setStyleSheet(u"    border: none;\n"
"    border-radius: 24px;\n"
"    background-color: #000000;\n"
"")
        self.horizontalLayout_66 = QHBoxLayout(self.y0_59)
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.horizontalLayout_66.setContentsMargins(4, -1, -1, -1)
        self.CircleOff_34 = QPushButton(self.y0_59)
        self.CircleOff_34.setObjectName(u"CircleOff_34")
        sizePolicy2.setHeightForWidth(self.CircleOff_34.sizePolicy().hasHeightForWidth())
        self.CircleOff_34.setSizePolicy(sizePolicy2)
        self.CircleOff_34.setMinimumSize(QSize(0, 30))
        self.CircleOff_34.setMaximumSize(QSize(30, 30))
        self.CircleOff_34.setFont(font4)
        self.CircleOff_34.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: white;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"	color: black;\n"
"}\n"
"")
        self.CircleOff_34.setCheckable(True)

        self.horizontalLayout_66.addWidget(self.CircleOff_34)

        self.CircleOn_34 = QPushButton(self.y0_59)
        self.CircleOn_34.setObjectName(u"CircleOn_34")
        sizePolicy2.setHeightForWidth(self.CircleOn_34.sizePolicy().hasHeightForWidth())
        self.CircleOn_34.setSizePolicy(sizePolicy2)
        self.CircleOn_34.setMaximumSize(QSize(30, 30))
        self.CircleOn_34.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: #000000;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"}\n"
"")
        self.CircleOn_34.setCheckable(True)

        self.horizontalLayout_66.addWidget(self.CircleOn_34)


        self.gridLayout_8.addWidget(self.y0_59, 2, 3, 1, 1)

        self.y0_55 = QWidget(self.gridLayoutWidget)
        self.y0_55.setObjectName(u"y0_55")
        sizePolicy5.setHeightForWidth(self.y0_55.sizePolicy().hasHeightForWidth())
        self.y0_55.setSizePolicy(sizePolicy5)
        self.y0_55.setMinimumSize(QSize(90, 60))
        self.y0_55.setStyleSheet(u"    border: none;\n"
"    border-radius: 24px;\n"
"    background-color: #000000;\n"
"")
        self.horizontalLayout_97 = QHBoxLayout(self.y0_55)
        self.horizontalLayout_97.setObjectName(u"horizontalLayout_97")
        self.horizontalLayout_97.setContentsMargins(4, -1, -1, -1)
        self.CircleOff_65 = QPushButton(self.y0_55)
        self.CircleOff_65.setObjectName(u"CircleOff_65")
        sizePolicy2.setHeightForWidth(self.CircleOff_65.sizePolicy().hasHeightForWidth())
        self.CircleOff_65.setSizePolicy(sizePolicy2)
        self.CircleOff_65.setMinimumSize(QSize(0, 30))
        self.CircleOff_65.setMaximumSize(QSize(30, 30))
        self.CircleOff_65.setFont(font4)
        self.CircleOff_65.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: white;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"	color: black;\n"
"}\n"
"")
        self.CircleOff_65.setCheckable(True)

        self.horizontalLayout_97.addWidget(self.CircleOff_65)

        self.CircleOn_65 = QPushButton(self.y0_55)
        self.CircleOn_65.setObjectName(u"CircleOn_65")
        sizePolicy2.setHeightForWidth(self.CircleOn_65.sizePolicy().hasHeightForWidth())
        self.CircleOn_65.setSizePolicy(sizePolicy2)
        self.CircleOn_65.setMaximumSize(QSize(30, 30))
        self.CircleOn_65.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: #000000;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"}\n"
"")
        self.CircleOn_65.setCheckable(True)

        self.horizontalLayout_97.addWidget(self.CircleOn_65)


        self.gridLayout_8.addWidget(self.y0_55, 1, 0, 1, 1)

        self.y0_60 = QWidget(self.gridLayoutWidget)
        self.y0_60.setObjectName(u"y0_60")
        sizePolicy5.setHeightForWidth(self.y0_60.sizePolicy().hasHeightForWidth())
        self.y0_60.setSizePolicy(sizePolicy5)
        self.y0_60.setMinimumSize(QSize(90, 60))
        self.y0_60.setStyleSheet(u"    border: none;\n"
"    border-radius: 24px;\n"
"    background-color: #000000;\n"
"")
        self.horizontalLayout_71 = QHBoxLayout(self.y0_60)
        self.horizontalLayout_71.setObjectName(u"horizontalLayout_71")
        self.horizontalLayout_71.setContentsMargins(4, -1, -1, -1)
        self.CircleOff_39 = QPushButton(self.y0_60)
        self.CircleOff_39.setObjectName(u"CircleOff_39")
        sizePolicy2.setHeightForWidth(self.CircleOff_39.sizePolicy().hasHeightForWidth())
        self.CircleOff_39.setSizePolicy(sizePolicy2)
        self.CircleOff_39.setMinimumSize(QSize(0, 30))
        self.CircleOff_39.setMaximumSize(QSize(30, 30))
        self.CircleOff_39.setFont(font4)
        self.CircleOff_39.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: white;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"	color: black;\n"
"}\n"
"")
        self.CircleOff_39.setCheckable(True)

        self.horizontalLayout_71.addWidget(self.CircleOff_39)

        self.CircleOn_39 = QPushButton(self.y0_60)
        self.CircleOn_39.setObjectName(u"CircleOn_39")
        sizePolicy2.setHeightForWidth(self.CircleOn_39.sizePolicy().hasHeightForWidth())
        self.CircleOn_39.setSizePolicy(sizePolicy2)
        self.CircleOn_39.setMaximumSize(QSize(30, 30))
        self.CircleOn_39.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: #000000;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"}\n"
"")
        self.CircleOn_39.setCheckable(True)

        self.horizontalLayout_71.addWidget(self.CircleOn_39)


        self.gridLayout_8.addWidget(self.y0_60, 3, 0, 1, 1)

        self.y0_71 = QWidget(self.gridLayoutWidget)
        self.y0_71.setObjectName(u"y0_71")
        sizePolicy5.setHeightForWidth(self.y0_71.sizePolicy().hasHeightForWidth())
        self.y0_71.setSizePolicy(sizePolicy5)
        self.y0_71.setMinimumSize(QSize(90, 60))
        self.y0_71.setStyleSheet(u"    border: none;\n"
"    border-radius: 24px;\n"
"    background-color: #000000;\n"
"")
        self.horizontalLayout_75 = QHBoxLayout(self.y0_71)
        self.horizontalLayout_75.setObjectName(u"horizontalLayout_75")
        self.horizontalLayout_75.setContentsMargins(4, -1, -1, -1)
        self.CircleOff_43 = QPushButton(self.y0_71)
        self.CircleOff_43.setObjectName(u"CircleOff_43")
        sizePolicy2.setHeightForWidth(self.CircleOff_43.sizePolicy().hasHeightForWidth())
        self.CircleOff_43.setSizePolicy(sizePolicy2)
        self.CircleOff_43.setMinimumSize(QSize(0, 30))
        self.CircleOff_43.setMaximumSize(QSize(30, 30))
        self.CircleOff_43.setFont(font4)
        self.CircleOff_43.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: white;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"	color: black;\n"
"}\n"
"")
        self.CircleOff_43.setCheckable(True)

        self.horizontalLayout_75.addWidget(self.CircleOff_43)

        self.CircleOn_43 = QPushButton(self.y0_71)
        self.CircleOn_43.setObjectName(u"CircleOn_43")
        sizePolicy2.setHeightForWidth(self.CircleOn_43.sizePolicy().hasHeightForWidth())
        self.CircleOn_43.setSizePolicy(sizePolicy2)
        self.CircleOn_43.setMaximumSize(QSize(30, 30))
        self.CircleOn_43.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: #000000;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"}\n"
"")
        self.CircleOn_43.setCheckable(True)

        self.horizontalLayout_75.addWidget(self.CircleOn_43)


        self.gridLayout_8.addWidget(self.y0_71, 3, 1, 1, 1)

        self.y0_72 = QWidget(self.gridLayoutWidget)
        self.y0_72.setObjectName(u"y0_72")
        sizePolicy5.setHeightForWidth(self.y0_72.sizePolicy().hasHeightForWidth())
        self.y0_72.setSizePolicy(sizePolicy5)
        self.y0_72.setMinimumSize(QSize(90, 60))
        self.y0_72.setStyleSheet(u"    border: none;\n"
"    border-radius: 24px;\n"
"    background-color: #000000;\n"
"")
        self.horizontalLayout_78 = QHBoxLayout(self.y0_72)
        self.horizontalLayout_78.setObjectName(u"horizontalLayout_78")
        self.horizontalLayout_78.setContentsMargins(4, -1, -1, -1)
        self.CircleOff_46 = QPushButton(self.y0_72)
        self.CircleOff_46.setObjectName(u"CircleOff_46")
        sizePolicy2.setHeightForWidth(self.CircleOff_46.sizePolicy().hasHeightForWidth())
        self.CircleOff_46.setSizePolicy(sizePolicy2)
        self.CircleOff_46.setMinimumSize(QSize(0, 30))
        self.CircleOff_46.setMaximumSize(QSize(30, 30))
        self.CircleOff_46.setFont(font4)
        self.CircleOff_46.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: white;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"	color: black;\n"
"}\n"
"")
        self.CircleOff_46.setCheckable(True)

        self.horizontalLayout_78.addWidget(self.CircleOff_46)

        self.CircleOn_46 = QPushButton(self.y0_72)
        self.CircleOn_46.setObjectName(u"CircleOn_46")
        sizePolicy2.setHeightForWidth(self.CircleOn_46.sizePolicy().hasHeightForWidth())
        self.CircleOn_46.setSizePolicy(sizePolicy2)
        self.CircleOn_46.setMaximumSize(QSize(30, 30))
        self.CircleOn_46.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: #000000;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"}\n"
"")
        self.CircleOn_46.setCheckable(True)

        self.horizontalLayout_78.addWidget(self.CircleOn_46)


        self.gridLayout_8.addWidget(self.y0_72, 3, 2, 1, 1)

        self.y0_73 = QWidget(self.gridLayoutWidget)
        self.y0_73.setObjectName(u"y0_73")
        sizePolicy5.setHeightForWidth(self.y0_73.sizePolicy().hasHeightForWidth())
        self.y0_73.setSizePolicy(sizePolicy5)
        self.y0_73.setMinimumSize(QSize(90, 60))
        self.y0_73.setStyleSheet(u"    border: none;\n"
"    border-radius: 24px;\n"
"    background-color: #000000;\n"
"")
        self.horizontalLayout_105 = QHBoxLayout(self.y0_73)
        self.horizontalLayout_105.setObjectName(u"horizontalLayout_105")
        self.horizontalLayout_105.setContentsMargins(4, -1, -1, -1)
        self.CircleOff_73 = QPushButton(self.y0_73)
        self.CircleOff_73.setObjectName(u"CircleOff_73")
        sizePolicy2.setHeightForWidth(self.CircleOff_73.sizePolicy().hasHeightForWidth())
        self.CircleOff_73.setSizePolicy(sizePolicy2)
        self.CircleOff_73.setMinimumSize(QSize(0, 30))
        self.CircleOff_73.setMaximumSize(QSize(30, 30))
        self.CircleOff_73.setFont(font4)
        self.CircleOff_73.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: white;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"	color: black;\n"
"}\n"
"")
        self.CircleOff_73.setCheckable(True)

        self.horizontalLayout_105.addWidget(self.CircleOff_73)

        self.CircleOn_73 = QPushButton(self.y0_73)
        self.CircleOn_73.setObjectName(u"CircleOn_73")
        sizePolicy2.setHeightForWidth(self.CircleOn_73.sizePolicy().hasHeightForWidth())
        self.CircleOn_73.setSizePolicy(sizePolicy2)
        self.CircleOn_73.setMaximumSize(QSize(30, 30))
        self.CircleOn_73.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 15px;\n"
"    background-color: #000000;\n"
"    max-width: 30px;\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"    padding: 0;\n"
"}\n"
"")
        self.CircleOn_73.setCheckable(True)

        self.horizontalLayout_105.addWidget(self.CircleOn_73)


        self.gridLayout_8.addWidget(self.y0_73, 3, 3, 1, 1)

        self.label_5 = QLabel(self.DIDOContainerPage)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(320, 0, 67, 17))
        self.label_5.setFont(font4)
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_8 = QLabel(self.DIDOContainerPage)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(320, 300, 67, 17))
        self.label_8.setFont(font4)
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.MiddleStackedWidget.addWidget(self.DIDOContainerPage)
        self.ParentStackedWidgetToChangeMenuOptions.addWidget(self.ComponentControlPage)
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
        self.ChangeLanguageText = QLabel(self.SystemSettingsPage)
        self.ChangeLanguageText.setObjectName(u"ChangeLanguageText")
        self.ChangeLanguageText.setGeometry(QRect(410, 20, 201, 31))
        self.ChangeLanguageText.setFont(font1)
        self.ChangeLanguageText.setStyleSheet(u"color: white;")
        self.ChangeLanguageText.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.FontSizeText = QLabel(self.SystemSettingsPage)
        self.FontSizeText.setObjectName(u"FontSizeText")
        self.FontSizeText.setGeometry(QRect(410, 210, 201, 31))
        self.FontSizeText.setFont(font1)
        self.FontSizeText.setStyleSheet(u"color: white;")
        self.FontSizeText.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ThemeText = QLabel(self.SystemSettingsPage)
        self.ThemeText.setObjectName(u"ThemeText")
        self.ThemeText.setGeometry(QRect(410, 400, 201, 31))
        self.ThemeText.setFont(font1)
        self.ThemeText.setStyleSheet(u"color: white;")
        self.ThemeText.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.SaveChangesButton = QPushButton(self.SystemSettingsPage)
        self.SaveChangesButton.setObjectName(u"SaveChangesButton")
        self.SaveChangesButton.setGeometry(QRect(430, 620, 161, 61))
        self.EnglishLanguageButton = QPushButton(self.SystemSettingsPage)
        self.LanguageButtonGroup = QButtonGroup(MainWindow)
        self.LanguageButtonGroup.setObjectName(u"LanguageButtonGroup")
        self.LanguageButtonGroup.addButton(self.EnglishLanguageButton)
        self.EnglishLanguageButton.setObjectName(u"EnglishLanguageButton")
        self.EnglishLanguageButton.setGeometry(QRect(240, 80, 151, 71))
        self.EnglishLanguageButton.setCheckable(True)
        self.EnglishLanguageButton.setChecked(True)
        self.ChineseLanguageButton = QPushButton(self.SystemSettingsPage)
        self.LanguageButtonGroup.addButton(self.ChineseLanguageButton)
        self.ChineseLanguageButton.setObjectName(u"ChineseLanguageButton")
        self.ChineseLanguageButton.setGeometry(QRect(430, 80, 151, 71))
        self.ChineseLanguageButton.setCheckable(True)
        self.ThaiLanguageButton = QPushButton(self.SystemSettingsPage)
        self.LanguageButtonGroup.addButton(self.ThaiLanguageButton)
        self.ThaiLanguageButton.setObjectName(u"ThaiLanguageButton")
        self.ThaiLanguageButton.setGeometry(QRect(620, 80, 151, 71))
        self.ThaiLanguageButton.setCheckable(True)
        self.BigFontSizeButton = QPushButton(self.SystemSettingsPage)
        self.FontSizeButtonGroup = QButtonGroup(MainWindow)
        self.FontSizeButtonGroup.setObjectName(u"FontSizeButtonGroup")
        self.FontSizeButtonGroup.addButton(self.BigFontSizeButton)
        self.BigFontSizeButton.setObjectName(u"BigFontSizeButton")
        self.BigFontSizeButton.setGeometry(QRect(620, 270, 151, 71))
        self.BigFontSizeButton.setCheckable(True)
        self.NormalFontSizeButton = QPushButton(self.SystemSettingsPage)
        self.FontSizeButtonGroup.addButton(self.NormalFontSizeButton)
        self.NormalFontSizeButton.setObjectName(u"NormalFontSizeButton")
        self.NormalFontSizeButton.setGeometry(QRect(430, 270, 151, 71))
        self.NormalFontSizeButton.setCheckable(True)
        self.NormalFontSizeButton.setChecked(True)
        self.SmallFontSizeButton = QPushButton(self.SystemSettingsPage)
        self.FontSizeButtonGroup.addButton(self.SmallFontSizeButton)
        self.SmallFontSizeButton.setObjectName(u"SmallFontSizeButton")
        self.SmallFontSizeButton.setGeometry(QRect(240, 270, 151, 71))
        self.SmallFontSizeButton.setCheckable(True)
        self.DarkThemeButton = QPushButton(self.SystemSettingsPage)
        self.ThemeButtonGroup = QButtonGroup(MainWindow)
        self.ThemeButtonGroup.setObjectName(u"ThemeButtonGroup")
        self.ThemeButtonGroup.addButton(self.DarkThemeButton)
        self.DarkThemeButton.setObjectName(u"DarkThemeButton")
        self.DarkThemeButton.setGeometry(QRect(340, 460, 151, 71))
        self.DarkThemeButton.setCheckable(True)
        self.DarkThemeButton.setChecked(True)
        self.LightThemeButton = QPushButton(self.SystemSettingsPage)
        self.ThemeButtonGroup.addButton(self.LightThemeButton)
        self.LightThemeButton.setObjectName(u"LightThemeButton")
        self.LightThemeButton.setGeometry(QRect(530, 460, 151, 71))
        self.LightThemeButton.setCheckable(True)
        self.ParentStackedWidgetToChangeMenuOptions.addWidget(self.SystemSettingsPage)
        self.WorkOrderWidget = QWidget(self.BackgroundWidget)
        self.WorkOrderWidget.setObjectName(u"WorkOrderWidget")
        self.WorkOrderWidget.setGeometry(QRect(530, 0, 141, 41))
        self.WorkOrderWidget.setStyleSheet(u"color: white;")
        self.horizontalLayout_17 = QHBoxLayout(self.WorkOrderWidget)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.WorkOrderText = QLabel(self.WorkOrderWidget)
        self.WorkOrderText.setObjectName(u"WorkOrderText")
        font5 = QFont()
        font5.setBold(True)
        self.WorkOrderText.setFont(font5)

        self.horizontalLayout_17.addWidget(self.WorkOrderText)

        self.WorkOrderNumberInput = QLabel(self.WorkOrderWidget)
        self.WorkOrderNumberInput.setObjectName(u"WorkOrderNumberInput")

        self.horizontalLayout_17.addWidget(self.WorkOrderNumberInput)

        self.RecipeWidget = QWidget(self.BackgroundWidget)
        self.RecipeWidget.setObjectName(u"RecipeWidget")
        self.RecipeWidget.setGeometry(QRect(530, 30, 171, 41))
        self.RecipeWidget.setStyleSheet(u"color: white;")
        self.horizontalLayout_18 = QHBoxLayout(self.RecipeWidget)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.RecipeText = QLabel(self.RecipeWidget)
        self.RecipeText.setObjectName(u"RecipeText")
        self.RecipeText.setFont(font5)

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
        self.QuantityText.setFont(font5)

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
        self.WorkerNameText.setFont(font5)

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
        self.CartHeightText.setFont(font5)

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
        self.CartDepthText.setFont(font5)

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
        self.DateText.setFont(font5)

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
        self.ProcessAndInfoStackedWidget.setCurrentIndex(0)
        self.AutoAndManualStackedWidget.setCurrentIndex(0)
        self.ActionButtons.setCurrentIndex(1)
        self.ComponentControlStackedWidget.setCurrentIndex(1)
        self.ChangeComponentControlStackedWidget.setCurrentIndex(3)
        self.MiddleStackedWidget.setCurrentIndex(0)


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
        self.MainPageButton.setText(QCoreApplication.translate("MainWindow", u"Main Page", None))
        self.ComponentControlButton.setText(QCoreApplication.translate("MainWindow", u"Component\n"
"Control", None))
        self.ProductionRecordButton.setText(QCoreApplication.translate("MainWindow", u"Production\n"
"Record", None))
        self.LogsButton.setText(QCoreApplication.translate("MainWindow", u"Logs", None))
        self.VisionText.setText(QCoreApplication.translate("MainWindow", u"Vision", None))
        self.StartProcessText.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.StartCircle.setText("")
        self.ConnectProcessText.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.ConnectCircle.setText("")
        self.INITProcessText.setText(QCoreApplication.translate("MainWindow", u"INIT", None))
        self.INITCircle.setText("")
        self.IdleProcessText.setText(QCoreApplication.translate("MainWindow", u"Idle", None))
        self.IdleCircle.setText("")
        self.RoughAlignProcessText.setText(QCoreApplication.translate("MainWindow", u"Rough Align", None))
        self.RoughAlignCircle.setText("")
        self.PreciseAlignProcessText.setText(QCoreApplication.translate("MainWindow", u"Precise Align", None))
        self.PreciseAlignCircle.setText("")
        self.PickProcessText.setText(QCoreApplication.translate("MainWindow", u"Pick", None))
        self.PickCircle.setText("")
        self.AssemblyProcessText.setText(QCoreApplication.translate("MainWindow", u"Assembly", None))
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
        self.INITBefore.setText(QCoreApplication.translate("MainWindow", u"INIT", None))
        self.StopBefore.setText(QCoreApplication.translate("MainWindow", u"STOP", None))
        self.ChooseAutoButton.setText(QCoreApplication.translate("MainWindow", u"Auto", None))
        self.ChooseManualButton.setText(QCoreApplication.translate("MainWindow", u"Manual", None))
        self.AutoButton.setText(QCoreApplication.translate("MainWindow", u"Auto", None))
        self.ManualButton.setText(QCoreApplication.translate("MainWindow", u"Manual", None))
        self.INITButton.setText(QCoreApplication.translate("MainWindow", u"INIT", None))
        self.RunButton.setText(QCoreApplication.translate("MainWindow", u"RUN", None))
        self.AutoPauseButton.setText(QCoreApplication.translate("MainWindow", u"Pause", None))
        self.AutoStopButton.setText(QCoreApplication.translate("MainWindow", u"STOP", None))
        self.RoughAlignButton.setText(QCoreApplication.translate("MainWindow", u"Rough Align", None))
        self.PreciseAlignButton.setText(QCoreApplication.translate("MainWindow", u"Precise Align", None))
        self.PickButton.setText(QCoreApplication.translate("MainWindow", u"Pick", None))
        self.AssemblyButton.setText(QCoreApplication.translate("MainWindow", u"Assembly", None))
        self.ManualPauseButton.setText(QCoreApplication.translate("MainWindow", u"Pause", None))
        self.ManualStopButton.setText(QCoreApplication.translate("MainWindow", u"STOP", None))
        self.ChooseMotor.setText(QCoreApplication.translate("MainWindow", u"Motor", None))
        self.ChooseVision.setText(QCoreApplication.translate("MainWindow", u"Vision", None))
        self.ChooseClipper.setText(QCoreApplication.translate("MainWindow", u"Clipper", None))
        self.ChooseForklift.setText(QCoreApplication.translate("MainWindow", u"Forklift", None))
        self.ChooseDIDO.setText(QCoreApplication.translate("MainWindow", u"DI/DO", None))
        self.MotorStartedButton.setText(QCoreApplication.translate("MainWindow", u"Motor", None))
        self.HamburgerMenu.setText("")
        self.ControlUpCP.setText("")
        self.ControlLeftCP.setText("")
        self.ControlDownCP.setText("")
        self.ControlRightCP.setText("")
        self.YawPlusCP.setText("")
        self.YawMinusCP.setText("")
        self.ClipperButtonOnOff.setText(QCoreApplication.translate("MainWindow", u"Clipper  Off", None))
        self.MotorResetButton.setText(QCoreApplication.translate("MainWindow", u"RESET", None))
        self.VisionOne.setText(QCoreApplication.translate("MainWindow", u"Screw", None))
        self.VisionTwo.setText(QCoreApplication.translate("MainWindow", u"LShape", None))
        self.VisionThree.setText(QCoreApplication.translate("MainWindow", u"ICP Fit", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Clipper Page", None))
        self.LiftUp.setText("")
        self.LowerDown.setText("")
        self.FastForktLiftButton.setText(QCoreApplication.translate("MainWindow", u"Fast", None))
        self.SlowLiftButton.setText(QCoreApplication.translate("MainWindow", u"Slow", None))
        self.RunForkliftButton.setText(QCoreApplication.translate("MainWindow", u"Run", None))
        self.StopForkliftButton.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Mode", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Speed", None))
        self.SendForkliftCommand.setText(QCoreApplication.translate("MainWindow", u"Send Cmd", None))
        self.MediumLiftButton.setText(QCoreApplication.translate("MainWindow", u"Medium", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Distance (manual)", None))
        self.MotorOption.setText(QCoreApplication.translate("MainWindow", u"Motor", None))
        self.VisionOption.setText(QCoreApplication.translate("MainWindow", u"Vision", None))
        self.ClipperOption.setText(QCoreApplication.translate("MainWindow", u"Clipper", None))
        self.ForkliftOption.setText(QCoreApplication.translate("MainWindow", u"Forklift", None))
        self.DIDOOption.setText(QCoreApplication.translate("MainWindow", u"DI/DO", None))
        self.VisionTextInComponentControl.setText(QCoreApplication.translate("MainWindow", u"Vision", None))
        self.y_2.setText(QCoreApplication.translate("MainWindow", u"y:", None))
        self.yText_2.setText(QCoreApplication.translate("MainWindow", u"pos", None))
        self.z_2.setText(QCoreApplication.translate("MainWindow", u"z:", None))
        self.zText_2.setText(QCoreApplication.translate("MainWindow", u"pos", None))
        self.yaw_2.setText(QCoreApplication.translate("MainWindow", u"yaw:", None))
        self.yawText_2.setText(QCoreApplication.translate("MainWindow", u"pos", None))
        self.CartesianPoseText_2.setText(QCoreApplication.translate("MainWindow", u"Cartesian Pose", None))
        self.x_2.setText(QCoreApplication.translate("MainWindow", u"x:", None))
        self.xText_2.setText(QCoreApplication.translate("MainWindow", u"pos", None))
        self.Position_2.setText(QCoreApplication.translate("MainWindow", u"Position:", None))
        self.PositionText_2.setText(QCoreApplication.translate("MainWindow", u"pos", None))
        self.MotorInfoText_2.setText(QCoreApplication.translate("MainWindow", u"Motor Info", None))
        self.Current_2.setText(QCoreApplication.translate("MainWindow", u"Current: ", None))
        self.CurrentText_2.setText(QCoreApplication.translate("MainWindow", u"pos", None))
        self.d1_2.setText(QCoreApplication.translate("MainWindow", u"D1: ", None))
        self.LaserInfoText_2.setText(QCoreApplication.translate("MainWindow", u"Laser Info", None))
        self.d2_2.setText(QCoreApplication.translate("MainWindow", u"Current Height: ", None))
        self.currentHeight.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.h1_2.setText(QCoreApplication.translate("MainWindow", u"Height Cmd: ", None))
        self.HeightCommand.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.RecordDataButton_2.setText(QCoreApplication.translate("MainWindow", u"Record Data", None))
        self.CircleOff_15.setText(QCoreApplication.translate("MainWindow", u"13", None))
        self.CircleOn_15.setText("")
        self.CircleOff_32.setText(QCoreApplication.translate("MainWindow", u"30", None))
        self.CircleOn_32.setText("")
        self.CircleOff_14.setText(QCoreApplication.translate("MainWindow", u"12", None))
        self.CircleOn_14.setText("")
        self.CircleOff_24.setText(QCoreApplication.translate("MainWindow", u"22", None))
        self.CircleOn_24.setText("")
        self.CircleOff_9.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.CircleOn_9.setText("")
        self.CircleOff_6.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.CircleOn_6.setText("")
        self.CircleOff_23.setText(QCoreApplication.translate("MainWindow", u"21", None))
        self.CircleOn_23.setText("")
        self.CircleOff_35.setText(QCoreApplication.translate("MainWindow", u"31", None))
        self.CircleOn_35.setText("")
        self.CircleOff_18.setText(QCoreApplication.translate("MainWindow", u"16", None))
        self.CircleOn_18.setText("")
        self.CircleOff_20.setText(QCoreApplication.translate("MainWindow", u"18", None))
        self.CircleOn_20.setText("")
        self.CircleOff_30.setText(QCoreApplication.translate("MainWindow", u"28", None))
        self.CircleOn_30.setText("")
        self.CircleOff_47.setText(QCoreApplication.translate("MainWindow", u"37", None))
        self.CircleOn_47.setText("")
        self.CircleOff_10.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.CircleOn_10.setText("")
        self.CircleOff_58.setText(QCoreApplication.translate("MainWindow", u"48", None))
        self.CircleOn_58.setText("")
        self.CircleOff_56.setText(QCoreApplication.translate("MainWindow", u"46", None))
        self.CircleOn_56.setText("")
        self.CircleOff_11.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.CircleOn_11.setText("")
        self.CircleOff_22.setText(QCoreApplication.translate("MainWindow", u"20", None))
        self.CircleOn_22.setText("")
        self.CircleOff_8.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.CircleOn_8.setText("")
        self.CircleOff_25.setText(QCoreApplication.translate("MainWindow", u"23", None))
        self.CircleOn_25.setText("")
        self.CircleOff_57.setText(QCoreApplication.translate("MainWindow", u"47", None))
        self.CircleOn_57.setText("")
        self.CircleOff_48.setText(QCoreApplication.translate("MainWindow", u"43", None))
        self.CircleOn_48.setText("")
        self.CircleOff_5.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.CircleOn_5.setText("")
        self.CircleOff_36.setText(QCoreApplication.translate("MainWindow", u"32", None))
        self.CircleOn_36.setText("")
        self.CircleOff_52.setText(QCoreApplication.translate("MainWindow", u"41", None))
        self.CircleOn_52.setText("")
        self.CircleOff_37.setText(QCoreApplication.translate("MainWindow", u"33", None))
        self.CircleOn_37.setText("")
        self.CircleOff_4.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.CircleOn_4.setText("")
        self.CircleOff_49.setText(QCoreApplication.translate("MainWindow", u"38", None))
        self.CircleOn_49.setText("")
        self.CircleOff_50.setText(QCoreApplication.translate("MainWindow", u"39", None))
        self.CircleOn_50.setText("")
        self.CircleOff_51.setText(QCoreApplication.translate("MainWindow", u"40", None))
        self.CircleOn_51.setText("")
        self.CircleOff_45.setText(QCoreApplication.translate("MainWindow", u"36", None))
        self.CircleOn_45.setText("")
        self.CircleOff_16.setText(QCoreApplication.translate("MainWindow", u"14", None))
        self.CircleOn_16.setText("")
        self.CircleOff_19.setText(QCoreApplication.translate("MainWindow", u"17", None))
        self.CircleOn_19.setText("")
        self.CircleOff_31.setText(QCoreApplication.translate("MainWindow", u"29", None))
        self.CircleOn_31.setText("")
        self.CircleOff_7.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.CircleOn_7.setText("")
        self.CircleOff_55.setText(QCoreApplication.translate("MainWindow", u"45", None))
        self.CircleOn_55.setText("")
        self.CircleOff_38.setText(QCoreApplication.translate("MainWindow", u"34", None))
        self.CircleOn_38.setText("")
        self.CircleOff_3.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.CircleOn_3.setText("")
        self.CircleOff_17.setText(QCoreApplication.translate("MainWindow", u"15", None))
        self.CircleOn_17.setText("")
        self.CircleOff_53.setText(QCoreApplication.translate("MainWindow", u"42", None))
        self.CircleOn_53.setText("")
        self.CircleOff_44.setText(QCoreApplication.translate("MainWindow", u"35", None))
        self.CircleOn_44.setText("")
        self.CircleOff_13.setText(QCoreApplication.translate("MainWindow", u"11", None))
        self.CircleOn_13.setText("")
        self.CircleOff_28.setText(QCoreApplication.translate("MainWindow", u"26", None))
        self.CircleOn_28.setText("")
        self.CircleOff_27.setText(QCoreApplication.translate("MainWindow", u"25", None))
        self.CircleOn_27.setText("")
        self.CircleOff_29.setText(QCoreApplication.translate("MainWindow", u"27", None))
        self.CircleOn_29.setText("")
        self.CircleOff_26.setText(QCoreApplication.translate("MainWindow", u"24", None))
        self.CircleOn_26.setText("")
        self.CircleOff_54.setText(QCoreApplication.translate("MainWindow", u"44", None))
        self.CircleOn_54.setText("")
        self.CircleOff_12.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.CircleOn_12.setText("")
        self.CircleOff_21.setText(QCoreApplication.translate("MainWindow", u"19", None))
        self.CircleOn_21.setText("")
        self.CircleOff_33.setText(QCoreApplication.translate("MainWindow", u"11", None))
        self.CircleOn_33.setText("")
        self.CircleOff_60.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.CircleOn_60.setText("")
        self.CircleOff_67.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.CircleOn_67.setText("")
        self.CircleOff_61.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.CircleOn_61.setText("")
        self.CircleOff_125.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.CircleOn_125.setText("")
        self.CircleOff_124.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.CircleOn_124.setText("")
        self.CircleOff_123.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.CircleOn_123.setText("")
        self.CircleOff_66.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.CircleOn_66.setText("")
        self.CircleOff_59.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.CircleOn_59.setText("")
        self.CircleOff_64.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.CircleOn_64.setText("")
        self.CircleOff_34.setText(QCoreApplication.translate("MainWindow", u"12", None))
        self.CircleOn_34.setText("")
        self.CircleOff_65.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.CircleOn_65.setText("")
        self.CircleOff_39.setText(QCoreApplication.translate("MainWindow", u"13", None))
        self.CircleOn_39.setText("")
        self.CircleOff_43.setText(QCoreApplication.translate("MainWindow", u"14", None))
        self.CircleOn_43.setText("")
        self.CircleOff_46.setText(QCoreApplication.translate("MainWindow", u"15", None))
        self.CircleOn_46.setText("")
        self.CircleOff_73.setText(QCoreApplication.translate("MainWindow", u"16", None))
        self.CircleOn_73.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"DI", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"DO", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Production Record", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Logs", None))
        self.ChangeLanguageText.setText(QCoreApplication.translate("MainWindow", u"Change Language", None))
        self.FontSizeText.setText(QCoreApplication.translate("MainWindow", u"Font Size", None))
        self.ThemeText.setText(QCoreApplication.translate("MainWindow", u"Theme", None))
        self.SaveChangesButton.setText(QCoreApplication.translate("MainWindow", u"Save Changes", None))
        self.EnglishLanguageButton.setText(QCoreApplication.translate("MainWindow", u"English", None))
        self.ChineseLanguageButton.setText(QCoreApplication.translate("MainWindow", u"Chinese", None))
        self.ThaiLanguageButton.setText(QCoreApplication.translate("MainWindow", u"Thai", None))
        self.BigFontSizeButton.setText(QCoreApplication.translate("MainWindow", u"Big", None))
        self.NormalFontSizeButton.setText(QCoreApplication.translate("MainWindow", u"Normal", None))
        self.SmallFontSizeButton.setText(QCoreApplication.translate("MainWindow", u"Small", None))
        self.DarkThemeButton.setText(QCoreApplication.translate("MainWindow", u"Dark", None))
        self.LightThemeButton.setText(QCoreApplication.translate("MainWindow", u"Light", None))
        self.WorkOrderText.setText(QCoreApplication.translate("MainWindow", u"\u5de5\u55ae:", None))
        self.WorkOrderNumberInput.setText(QCoreApplication.translate("MainWindow", u"12345678", None))
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
