# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'my_main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QScrollArea, QSizePolicy, QSlider,
    QTabWidget, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 675)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"*{\n"
"	color: #000;\n"
"	border: none;\n"
"}\n"
"#centralwidget, #overviewData, #autoTab, #dataTab, #settingTab, #scrollAreaWidgetContents{\n"
"	background-color: #D5EEF7;\n"
"}\n"
"\n"
"\n"
"#headerInfoFrame, #footerFrame{\n"
"	background-color: #76C7E4;\n"
"}\n"
"\n"
"#runningData, #viewSettingLabel{\n"
"	background-color: #fff\n"
"}\n"
"\n"
"\n"
"QTextBrowser{\n"
"	background-color: #EBF7FB;\n"
"}\n"
"\n"
"#autoTabBtn, #dataTabBtn, #settingTabBtn{\n"
"	background-color: #B8E3F2;\n"
"	margin: 0,0,5,0;\n"
"	text-align: center;\n"
"\n"
"}\n"
"\n"
"#selectFeatureBtn, #selectModelBtn, #exposSaveBtn, #lightSaveBtn, #manualBtn, #stopBtn, #saveConfigBtn, #restartBtn, #toggleLightBtn{\n"
"	background-color: #2596bf;\n"
"	color: #fff;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"#select, #config, #adjust, #viewSetting{\n"
"	background-color: #EBF7FB;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 2px solid #fff;    /* Darker border on hover */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    bo"
                        "rder: 2px solid #2980b9;    /* Darker border on hover */\n"
"}\n"
"\n"
"#frame_7, #frame_8,#frame_9{\n"
"    background-color: rgba(63, 0, 200, 80); /* m\u00e0u \u0111en m\u1edd (opacity 80/255) */\n"
"    max-height: 1px;   /* ch\u1ec9 d\u00e0y 1 pixel */\n"
"    min-height: 1px;\n"
"    border: none;\n"
"}\n"
"#frame_10, #frame_11, #frame_12{\n"
"    background-color: rgba(63, 0, 200, 50); /* m\u00e0u \u0111en m\u1edd (opacity 80/255) */\n"
"    max-height: 55px;   /* ch\u1ec9 d\u00e0y 1 pixel */\n"
"    min-height: 50px;\n"
"    min-width: 2px;\n"
"    border: none;\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.headerFrame = QWidget(self.centralwidget)
        self.headerFrame.setObjectName(u"headerFrame")
        self.headerFrame.setMinimumSize(QSize(500, 54))
        self.headerFrame.setMaximumSize(QSize(16777215, 54))
        self.horizontalLayout = QHBoxLayout(self.headerFrame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.headerInfoFrame = QFrame(self.headerFrame)
        self.headerInfoFrame.setObjectName(u"headerInfoFrame")
        self.headerInfoFrame.setMinimumSize(QSize(0, 54))
        self.headerInfoFrame.setMaximumSize(QSize(16777215, 53))
        self.headerInfoFrame.setFrameShape(QFrame.StyledPanel)
        self.headerInfoFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.headerInfoFrame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.logo = QFrame(self.headerInfoFrame)
        self.logo.setObjectName(u"logo")
        self.logo.setMinimumSize(QSize(180, 0))
        self.logo.setMaximumSize(QSize(180, 16777215))
        self.logo.setFrameShape(QFrame.StyledPanel)
        self.logo.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.logo)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.logoMeg = QLabel(self.logo)
        self.logoMeg.setObjectName(u"logoMeg")
        self.logoMeg.setMinimumSize(QSize(180, 0))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.logoMeg.setFont(font)
        self.logoMeg.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.logoMeg)


        self.horizontalLayout_2.addWidget(self.logo)

        self.frame_10 = QFrame(self.headerInfoFrame)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(2, 50))
        self.frame_10.setBaseSize(QSize(0, 0))
        self.frame_10.setFrameShape(QFrame.Box)
        self.frame_10.setFrameShadow(QFrame.Sunken)
        self.frame_10.setLineWidth(1)

        self.horizontalLayout_2.addWidget(self.frame_10)

        self.pgmName = QFrame(self.headerInfoFrame)
        self.pgmName.setObjectName(u"pgmName")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pgmName.sizePolicy().hasHeightForWidth())
        self.pgmName.setSizePolicy(sizePolicy)
        self.pgmName.setFrameShape(QFrame.StyledPanel)
        self.pgmName.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.pgmName)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.pgmName)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(15)
        font1.setBold(True)
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_2, 0, Qt.AlignHCenter)


        self.horizontalLayout_2.addWidget(self.pgmName)

        self.frame_11 = QFrame(self.headerInfoFrame)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.frame_11)

        self.infoFrame = QFrame(self.headerInfoFrame)
        self.infoFrame.setObjectName(u"infoFrame")
        self.infoFrame.setMinimumSize(QSize(400, 0))
        self.infoFrame.setMaximumSize(QSize(400, 16777215))
        self.infoFrame.setFrameShape(QFrame.StyledPanel)
        self.infoFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.infoFrame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.version = QFrame(self.infoFrame)
        self.version.setObjectName(u"version")
        self.version.setMinimumSize(QSize(200, 0))
        self.version.setFrameShape(QFrame.StyledPanel)
        self.version.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.version)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.exeVer = QLabel(self.version)
        self.exeVer.setObjectName(u"exeVer")
        self.exeVer.setMinimumSize(QSize(150, 0))
        font2 = QFont()
        font2.setPointSize(8)
        font2.setBold(True)
        self.exeVer.setFont(font2)
        self.exeVer.setIndent(2)

        self.gridLayout.addWidget(self.exeVer, 0, 2, 1, 1)

        self.mdFile = QLabel(self.version)
        self.mdFile.setObjectName(u"mdFile")
        self.mdFile.setMinimumSize(QSize(150, 0))
        self.mdFile.setFont(font2)
        self.mdFile.setIndent(2)

        self.gridLayout.addWidget(self.mdFile, 2, 2, 1, 1)

        self.label_3 = QLabel(self.version)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(90, 20))
        self.label_3.setMaximumSize(QSize(90, 20))
        self.label_3.setFont(font2)
        self.label_3.setIndent(2)

        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)

        self.label_5 = QLabel(self.version)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(90, 20))
        self.label_5.setMaximumSize(QSize(90, 20))
        self.label_5.setFont(font2)
        self.label_5.setIndent(2)

        self.gridLayout.addWidget(self.label_5, 2, 1, 1, 1)

        self.frame_8 = QFrame(self.version)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.frame_8, 1, 1, 1, 1)

        self.frame_7 = QFrame(self.version)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy1)
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.frame_7, 1, 2, 1, 1)


        self.horizontalLayout_3.addWidget(self.version)

        self.frame_12 = QFrame(self.infoFrame)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_3.addWidget(self.frame_12)

        self.other = QFrame(self.infoFrame)
        self.other.setObjectName(u"other")
        self.other.setFrameShape(QFrame.StyledPanel)
        self.other.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.other)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.timeInfo = QLabel(self.other)
        self.timeInfo.setObjectName(u"timeInfo")
        self.timeInfo.setMinimumSize(QSize(150, 20))
        self.timeInfo.setMaximumSize(QSize(150, 20))
        font3 = QFont()
        font3.setBold(True)
        self.timeInfo.setFont(font3)
        self.timeInfo.setIndent(2)

        self.gridLayout_3.addWidget(self.timeInfo, 0, 0, 1, 1)

        self.frame_9 = QFrame(self.other)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)

        self.gridLayout_3.addWidget(self.frame_9, 1, 0, 1, 1)

        self.ipInfo = QLabel(self.other)
        self.ipInfo.setObjectName(u"ipInfo")
        self.ipInfo.setMinimumSize(QSize(150, 20))
        self.ipInfo.setMaximumSize(QSize(150, 20))
        self.ipInfo.setFont(font3)
        self.ipInfo.setIndent(2)

        self.gridLayout_3.addWidget(self.ipInfo, 2, 0, 1, 1)


        self.horizontalLayout_3.addWidget(self.other)


        self.horizontalLayout_2.addWidget(self.infoFrame)


        self.horizontalLayout.addWidget(self.headerInfoFrame)


        self.verticalLayout.addWidget(self.headerFrame, 0, Qt.AlignTop)

        self.bodyFrame = QWidget(self.centralwidget)
        self.bodyFrame.setObjectName(u"bodyFrame")
        self.verticalLayout_5 = QVBoxLayout(self.bodyFrame)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.bodyFrame)
        self.tabWidget.setObjectName(u"tabWidget")
        self.autoTab = QWidget()
        self.autoTab.setObjectName(u"autoTab")
        self.horizontalLayout_6 = QHBoxLayout(self.autoTab)
        self.horizontalLayout_6.setSpacing(5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(5, 0, 0, 0)
        self.scrollArea = QScrollArea(self.autoTab)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1193, 541))
        self.verticalLayout_7 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.dutGridLayout = QGridLayout()
        self.dutGridLayout.setObjectName(u"dutGridLayout")
        self.dutGridLayout.setHorizontalSpacing(0)
        self.dutGridLayout.setVerticalSpacing(3)

        self.verticalLayout_7.addLayout(self.dutGridLayout)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_6.addWidget(self.scrollArea)

        self.tabWidget.addTab(self.autoTab, "")
        self.dataTab = QWidget()
        self.dataTab.setObjectName(u"dataTab")
        self.horizontalLayout_8 = QHBoxLayout(self.dataTab)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.select = QWidget(self.dataTab)
        self.select.setObjectName(u"select")
        self.verticalLayout_3 = QVBoxLayout(self.select)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.select)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 20))
        self.label.setMaximumSize(QSize(16777215, 30))
        font4 = QFont()
        font4.setPointSize(10)
        font4.setBold(True)
        self.label.setFont(font4)

        self.verticalLayout_3.addWidget(self.label)

        self.frame = QFrame(self.select)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setVerticalSpacing(25)
        self.selectModelBtn = QPushButton(self.frame)
        self.selectModelBtn.setObjectName(u"selectModelBtn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.selectModelBtn.sizePolicy().hasHeightForWidth())
        self.selectModelBtn.setSizePolicy(sizePolicy2)
        self.selectModelBtn.setMinimumSize(QSize(80, 20))
        self.selectModelBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_4.addWidget(self.selectModelBtn, 0, 2, 1, 1)

        self.label_14 = QLabel(self.frame)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_4.addWidget(self.label_14, 0, 0, 1, 1)

        self.modelFileLine = QLineEdit(self.frame)
        self.modelFileLine.setObjectName(u"modelFileLine")
        sizePolicy2.setHeightForWidth(self.modelFileLine.sizePolicy().hasHeightForWidth())
        self.modelFileLine.setSizePolicy(sizePolicy2)
        self.modelFileLine.setMinimumSize(QSize(300, 0))

        self.gridLayout_4.addWidget(self.modelFileLine, 0, 1, 1, 1)

        self.label_15 = QLabel(self.frame)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_4.addWidget(self.label_15, 1, 0, 1, 1)

        self.fetureFileLine = QLineEdit(self.frame)
        self.fetureFileLine.setObjectName(u"fetureFileLine")
        sizePolicy2.setHeightForWidth(self.fetureFileLine.sizePolicy().hasHeightForWidth())
        self.fetureFileLine.setSizePolicy(sizePolicy2)
        self.fetureFileLine.setMinimumSize(QSize(300, 0))

        self.gridLayout_4.addWidget(self.fetureFileLine, 1, 1, 1, 1)

        self.selectFeatureBtn = QPushButton(self.frame)
        self.selectFeatureBtn.setObjectName(u"selectFeatureBtn")
        sizePolicy2.setHeightForWidth(self.selectFeatureBtn.sizePolicy().hasHeightForWidth())
        self.selectFeatureBtn.setSizePolicy(sizePolicy2)
        self.selectFeatureBtn.setMinimumSize(QSize(80, 20))
        self.selectFeatureBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_4.addWidget(self.selectFeatureBtn, 1, 2, 1, 1)


        self.verticalLayout_3.addWidget(self.frame, 0, Qt.AlignLeft|Qt.AlignTop)


        self.horizontalLayout_8.addWidget(self.select)

        self.config = QWidget(self.dataTab)
        self.config.setObjectName(u"config")
        self.verticalLayout_10 = QVBoxLayout(self.config)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_16 = QLabel(self.config)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(0, 20))
        self.label_16.setMaximumSize(QSize(16777215, 30))
        self.label_16.setFont(font4)

        self.verticalLayout_10.addWidget(self.label_16)

        self.frame_3 = QFrame(self.config)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setVerticalSpacing(25)
        self.lineEdit_2 = QLineEdit(self.frame_3)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(300, 0))
        self.lineEdit_2.setMaximumSize(QSize(300, 16777215))

        self.gridLayout_5.addWidget(self.lineEdit_2, 3, 1, 1, 1)

        self.lineEdit = QLineEdit(self.frame_3)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(300, 0))
        self.lineEdit.setMaximumSize(QSize(300, 16777215))

        self.gridLayout_5.addWidget(self.lineEdit, 2, 1, 1, 1)

        self.comboBox = QComboBox(self.frame_3)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(300, 0))
        self.comboBox.setMaximumSize(QSize(300, 16777215))

        self.gridLayout_5.addWidget(self.comboBox, 1, 1, 1, 1)

        self.label_18 = QLabel(self.frame_3)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_5.addWidget(self.label_18, 2, 0, 1, 1)

        self.label_19 = QLabel(self.frame_3)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_5.addWidget(self.label_19, 3, 0, 1, 1)

        self.label_17 = QLabel(self.frame_3)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_5.addWidget(self.label_17, 1, 0, 1, 1)

        self.label_4 = QLabel(self.frame_3)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_5.addWidget(self.label_4, 0, 0, 1, 1)

        self.dutNumber = QLineEdit(self.frame_3)
        self.dutNumber.setObjectName(u"dutNumber")

        self.gridLayout_5.addWidget(self.dutNumber, 0, 1, 1, 1)


        self.verticalLayout_10.addWidget(self.frame_3, 0, Qt.AlignLeft|Qt.AlignTop)


        self.horizontalLayout_8.addWidget(self.config)

        self.frame_6 = QFrame(self.dataTab)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(200, 16777215))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.saveConfigBtn = QPushButton(self.frame_6)
        self.saveConfigBtn.setObjectName(u"saveConfigBtn")
        self.saveConfigBtn.setMinimumSize(QSize(0, 20))
        self.saveConfigBtn.setMaximumSize(QSize(150, 30))

        self.verticalLayout_6.addWidget(self.saveConfigBtn)

        self.restartBtn = QPushButton(self.frame_6)
        self.restartBtn.setObjectName(u"restartBtn")
        self.restartBtn.setMinimumSize(QSize(0, 20))
        self.restartBtn.setMaximumSize(QSize(150, 16777215))

        self.verticalLayout_6.addWidget(self.restartBtn)


        self.horizontalLayout_8.addWidget(self.frame_6, 0, Qt.AlignTop)

        self.tabWidget.addTab(self.dataTab, "")
        self.settingTab = QWidget()
        self.settingTab.setObjectName(u"settingTab")
        self.horizontalLayout_9 = QHBoxLayout(self.settingTab)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.viewSetting = QWidget(self.settingTab)
        self.viewSetting.setObjectName(u"viewSetting")
        sizePolicy1.setHeightForWidth(self.viewSetting.sizePolicy().hasHeightForWidth())
        self.viewSetting.setSizePolicy(sizePolicy1)
        self.gridLayout_7 = QGridLayout(self.viewSetting)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.viewSettingLabel = QLabel(self.viewSetting)
        self.viewSettingLabel.setObjectName(u"viewSettingLabel")
        sizePolicy.setHeightForWidth(self.viewSettingLabel.sizePolicy().hasHeightForWidth())
        self.viewSettingLabel.setSizePolicy(sizePolicy)
        self.viewSettingLabel.setMinimumSize(QSize(0, 0))
        self.viewSettingLabel.setMaximumSize(QSize(100000, 99997))
        self.viewSettingLabel.setScaledContents(True)

        self.gridLayout_7.addWidget(self.viewSettingLabel, 0, 0, 1, 1)


        self.horizontalLayout_9.addWidget(self.viewSetting)

        self.adjust = QWidget(self.settingTab)
        self.adjust.setObjectName(u"adjust")
        self.adjust.setMinimumSize(QSize(450, 0))
        self.verticalLayout_11 = QVBoxLayout(self.adjust)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_21 = QLabel(self.adjust)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMinimumSize(QSize(30, 0))
        self.label_21.setMaximumSize(QSize(16777215, 30))
        self.label_21.setFont(font4)

        self.verticalLayout_11.addWidget(self.label_21)

        self.frame_4 = QFrame(self.adjust)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_4)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setVerticalSpacing(12)
        self.lightLevelSlider = QSlider(self.frame_4)
        self.lightLevelSlider.setObjectName(u"lightLevelSlider")
        sizePolicy2.setHeightForWidth(self.lightLevelSlider.sizePolicy().hasHeightForWidth())
        self.lightLevelSlider.setSizePolicy(sizePolicy2)
        self.lightLevelSlider.setMinimumSize(QSize(140, 0))
        self.lightLevelSlider.setMaximumSize(QSize(140, 16777215))
        self.lightLevelSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_6.addWidget(self.lightLevelSlider, 1, 1, 1, 1)

        self.lightLevelLabel = QLabel(self.frame_4)
        self.lightLevelLabel.setObjectName(u"lightLevelLabel")
        self.lightLevelLabel.setMinimumSize(QSize(60, 20))
        self.lightLevelLabel.setMaximumSize(QSize(60, 20))
        self.lightLevelLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.lightLevelLabel, 1, 2, 1, 1)

        self.label_22 = QLabel(self.frame_4)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout_6.addWidget(self.label_22, 1, 0, 1, 1)

        self.lightSaveBtn = QPushButton(self.frame_4)
        self.lightSaveBtn.setObjectName(u"lightSaveBtn")
        self.lightSaveBtn.setMinimumSize(QSize(80, 20))

        self.gridLayout_6.addWidget(self.lightSaveBtn, 1, 3, 1, 1)

        self.exposureValLabel = QLabel(self.frame_4)
        self.exposureValLabel.setObjectName(u"exposureValLabel")
        self.exposureValLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.exposureValLabel, 0, 2, 1, 1)

        self.exposSaveBtn = QPushButton(self.frame_4)
        self.exposSaveBtn.setObjectName(u"exposSaveBtn")
        self.exposSaveBtn.setMinimumSize(QSize(80, 20))

        self.gridLayout_6.addWidget(self.exposSaveBtn, 0, 3, 1, 1)

        self.label_20 = QLabel(self.frame_4)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_6.addWidget(self.label_20, 0, 0, 1, 1)

        self.exposureSlider = QSlider(self.frame_4)
        self.exposureSlider.setObjectName(u"exposureSlider")
        sizePolicy2.setHeightForWidth(self.exposureSlider.sizePolicy().hasHeightForWidth())
        self.exposureSlider.setSizePolicy(sizePolicy2)
        self.exposureSlider.setMinimumSize(QSize(140, 0))
        self.exposureSlider.setMaximumSize(QSize(140, 16777215))
        self.exposureSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_6.addWidget(self.exposureSlider, 0, 1, 1, 1)

        self.toggleLightBtn = QPushButton(self.frame_4)
        self.toggleLightBtn.setObjectName(u"toggleLightBtn")
        self.toggleLightBtn.setMinimumSize(QSize(80, 20))
        self.toggleLightBtn.setMaximumSize(QSize(80, 20))

        self.gridLayout_6.addWidget(self.toggleLightBtn, 2, 3, 1, 1)


        self.verticalLayout_11.addWidget(self.frame_4, 0, Qt.AlignTop)

        self.frame_5 = QFrame(self.adjust)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_5)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.manualBtn = QPushButton(self.frame_5)
        self.manualBtn.setObjectName(u"manualBtn")
        self.manualBtn.setMinimumSize(QSize(80, 20))

        self.gridLayout_2.addWidget(self.manualBtn, 0, 0, 1, 1)

        self.stopBtn = QPushButton(self.frame_5)
        self.stopBtn.setObjectName(u"stopBtn")
        self.stopBtn.setMinimumSize(QSize(80, 20))

        self.gridLayout_2.addWidget(self.stopBtn, 0, 1, 1, 1)


        self.verticalLayout_11.addWidget(self.frame_5)


        self.horizontalLayout_9.addWidget(self.adjust, 0, Qt.AlignRight)

        self.tabWidget.addTab(self.settingTab, "")

        self.verticalLayout_5.addWidget(self.tabWidget)


        self.verticalLayout.addWidget(self.bodyFrame)

        self.footerFrame = QWidget(self.centralwidget)
        self.footerFrame.setObjectName(u"footerFrame")
        self.horizontalLayout_4 = QHBoxLayout(self.footerFrame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.footerFrame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setSpacing(2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(2, 2, 0, 2)
        self.autoTabBtn = QPushButton(self.frame_2)
        self.autoTabBtn.setObjectName(u"autoTabBtn")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.autoTabBtn.sizePolicy().hasHeightForWidth())
        self.autoTabBtn.setSizePolicy(sizePolicy3)
        self.autoTabBtn.setMinimumSize(QSize(100, 50))
        font5 = QFont()
        font5.setPointSize(11)
        font5.setBold(True)
        self.autoTabBtn.setFont(font5)
        self.autoTabBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.autoTabBtn.setMouseTracking(False)
        icon = QIcon()
        icon.addFile(u":/blueIcon/assets/icons/blue/airplay.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.autoTabBtn.setIcon(icon)
        self.autoTabBtn.setIconSize(QSize(26, 26))

        self.horizontalLayout_5.addWidget(self.autoTabBtn)

        self.dataTabBtn = QPushButton(self.frame_2)
        self.dataTabBtn.setObjectName(u"dataTabBtn")
        self.dataTabBtn.setMinimumSize(QSize(100, 50))
        self.dataTabBtn.setFont(font5)
        self.dataTabBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/blueIcon/assets/icons/blue/refresh-ccw.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.dataTabBtn.setIcon(icon1)
        self.dataTabBtn.setIconSize(QSize(26, 26))

        self.horizontalLayout_5.addWidget(self.dataTabBtn)

        self.settingTabBtn = QPushButton(self.frame_2)
        self.settingTabBtn.setObjectName(u"settingTabBtn")
        self.settingTabBtn.setMinimumSize(QSize(100, 50))
        self.settingTabBtn.setFont(font5)
        self.settingTabBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/blueIcon/assets/icons/blue/sliders.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.settingTabBtn.setIcon(icon2)
        self.settingTabBtn.setIconSize(QSize(26, 26))

        self.horizontalLayout_5.addWidget(self.settingTabBtn)


        self.horizontalLayout_4.addWidget(self.frame_2, 0, Qt.AlignLeft)


        self.verticalLayout.addWidget(self.footerFrame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Vision Program", None))
        self.logoMeg.setText(QCoreApplication.translate("MainWindow", u"SEVT-MEG", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Vision Inspection Program", None))
        self.exeVer.setText(QCoreApplication.translate("MainWindow", u"PGM_V0010", None))
        self.mdFile.setText(QCoreApplication.translate("MainWindow", u"A123_V001", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u2022 Execute:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u2022 Model file:", None))
        self.timeInfo.setText(QCoreApplication.translate("MainWindow", u"\u2022 Time: 12:12:11", None))
        self.ipInfo.setText(QCoreApplication.translate("MainWindow", u"\u2022 IP: 107.114.123.123", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.autoTab), QCoreApplication.translate("MainWindow", u"Auto", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u25a0 Select Model file", None))
        self.selectModelBtn.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u2022 Model file  :", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"\u2022 Feature file:", None))
        self.selectFeatureBtn.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u25a0 Configuration", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\u2022 Camera ID of TOP", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"\u2022 Camera ID of BTM", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\u2022 Serial COM no.", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u2022 DUT number", None))
        self.saveConfigBtn.setText(QCoreApplication.translate("MainWindow", u"Save Config", None))
        self.restartBtn.setText(QCoreApplication.translate("MainWindow", u"Restart App.", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.dataTab), QCoreApplication.translate("MainWindow", u"Data", None))
        self.viewSettingLabel.setText("")
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"\u25a0 Adjustment", None))
        self.lightLevelLabel.setText(QCoreApplication.translate("MainWindow", u"Val", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u". Light level", None))
        self.lightSaveBtn.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.exposureValLabel.setText(QCoreApplication.translate("MainWindow", u"Val", None))
        self.exposSaveBtn.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u". Exposure", None))
        self.toggleLightBtn.setText(QCoreApplication.translate("MainWindow", u"Toggle Light", None))
        self.manualBtn.setText(QCoreApplication.translate("MainWindow", u"Manual Test", None))
        self.stopBtn.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.settingTab), QCoreApplication.translate("MainWindow", u"Setting", None))
        self.autoTabBtn.setText(QCoreApplication.translate("MainWindow", u"Auto", None))
        self.dataTabBtn.setText(QCoreApplication.translate("MainWindow", u"Data", None))
        self.settingTabBtn.setText(QCoreApplication.translate("MainWindow", u"Setting", None))
    # retranslateUi

