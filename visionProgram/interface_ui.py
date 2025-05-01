# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface.ui'
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
    QPushButton, QSizePolicy, QSlider, QTabWidget,
    QTextBrowser, QVBoxLayout, QWidget)
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
"#centralwidget, #overviewData, #autoTab, #dataTab, #settingTab{\n"
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
"#selectFeatureBtn, #selectModelBtn, #exposSaveBtn, #lightSaveBtn, #manualBtn, #uploadBtn{\n"
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
"    border: 2px solid #2980b9;    /* Darker border on hover */\n"
"}\n"
"\n"
"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.headerFrame = QWidget(self.centralwidget)
        self.headerFrame.setObjectName(u"headerFrame")
        self.horizontalLayout = QHBoxLayout(self.headerFrame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.headerInfoFrame = QFrame(self.headerFrame)
        self.headerInfoFrame.setObjectName(u"headerInfoFrame")
        self.headerInfoFrame.setFrameShape(QFrame.StyledPanel)
        self.headerInfoFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.headerInfoFrame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.logo = QFrame(self.headerInfoFrame)
        self.logo.setObjectName(u"logo")
        self.logo.setFrameShape(QFrame.StyledPanel)
        self.logo.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.logo)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.logoMeg = QLabel(self.logo)
        self.logoMeg.setObjectName(u"logoMeg")
        self.logoMeg.setMinimumSize(QSize(200, 0))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.logoMeg.setFont(font)

        self.verticalLayout_2.addWidget(self.logoMeg)


        self.horizontalLayout_2.addWidget(self.logo, 0, Qt.AlignLeft)

        self.pgmName = QFrame(self.headerInfoFrame)
        self.pgmName.setObjectName(u"pgmName")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
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
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setPointSize(15)
        font1.setBold(True)
        self.label_2.setFont(font1)

        self.horizontalLayout_7.addWidget(self.label_2)


        self.horizontalLayout_2.addWidget(self.pgmName)

        self.infoFrame = QFrame(self.headerInfoFrame)
        self.infoFrame.setObjectName(u"infoFrame")
        self.infoFrame.setFrameShape(QFrame.StyledPanel)
        self.infoFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.infoFrame)
        self.horizontalLayout_3.setSpacing(30)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.version = QFrame(self.infoFrame)
        self.version.setObjectName(u"version")
        self.version.setFrameShape(QFrame.StyledPanel)
        self.version.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.version)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(22)
        self.gridLayout.setVerticalSpacing(4)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.exeVer = QLabel(self.version)
        self.exeVer.setObjectName(u"exeVer")
        font2 = QFont()
        font2.setPointSize(9)
        self.exeVer.setFont(font2)

        self.gridLayout.addWidget(self.exeVer, 0, 1, 1, 1)

        self.label_5 = QLabel(self.version)
        self.label_5.setObjectName(u"label_5")
        font3 = QFont()
        font3.setPointSize(8)
        font3.setBold(False)
        self.label_5.setFont(font3)

        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)

        self.mdFile = QLabel(self.version)
        self.mdFile.setObjectName(u"mdFile")
        self.mdFile.setFont(font2)

        self.gridLayout.addWidget(self.mdFile, 1, 1, 1, 1)

        self.label_3 = QLabel(self.version)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font3)

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)


        self.horizontalLayout_3.addWidget(self.version)

        self.other = QFrame(self.infoFrame)
        self.other.setObjectName(u"other")
        self.other.setFrameShape(QFrame.StyledPanel)
        self.other.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.other)
        self.verticalLayout_4.setSpacing(5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.timeInfo = QLabel(self.other)
        self.timeInfo.setObjectName(u"timeInfo")

        self.verticalLayout_4.addWidget(self.timeInfo)

        self.ipInfo = QLabel(self.other)
        self.ipInfo.setObjectName(u"ipInfo")

        self.verticalLayout_4.addWidget(self.ipInfo)


        self.horizontalLayout_3.addWidget(self.other)


        self.horizontalLayout_2.addWidget(self.infoFrame, 0, Qt.AlignRight)


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
        self.overviewData = QWidget(self.autoTab)
        self.overviewData.setObjectName(u"overviewData")
        self.overviewData.setMinimumSize(QSize(300, 0))
        self.overviewData.setMaximumSize(QSize(300, 16777215))
        self.verticalLayout_6 = QVBoxLayout(self.overviewData)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.inspData = QFrame(self.overviewData)
        self.inspData.setObjectName(u"inspData")
        self.inspData.setFrameShape(QFrame.StyledPanel)
        self.inspData.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.inspData)
        self.verticalLayout_7.setSpacing(10)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 10)
        self.label_4 = QLabel(self.inspData)
        self.label_4.setObjectName(u"label_4")
        font4 = QFont()
        font4.setPointSize(9)
        font4.setBold(True)
        self.label_4.setFont(font4)

        self.verticalLayout_7.addWidget(self.label_4, 0, Qt.AlignTop)

        self.inspDetailFrame = QFrame(self.inspData)
        self.inspDetailFrame.setObjectName(u"inspDetailFrame")
        self.inspDetailFrame.setFrameShape(QFrame.StyledPanel)
        self.inspDetailFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.inspDetailFrame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(0)
        self.gridLayout_2.setVerticalSpacing(15)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.tTimeLabel = QLabel(self.inspDetailFrame)
        self.tTimeLabel.setObjectName(u"tTimeLabel")
        font5 = QFont()
        font5.setBold(True)
        self.tTimeLabel.setFont(font5)
        self.tTimeLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.tTimeLabel, 1, 1, 1, 1)

        self.label_6 = QLabel(self.inspDetailFrame)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 0, 0, 1, 1)

        self.resultLabel = QLabel(self.inspDetailFrame)
        self.resultLabel.setObjectName(u"resultLabel")
        self.resultLabel.setFont(font5)
        self.resultLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.resultLabel, 0, 1, 1, 1)

        self.label_8 = QLabel(self.inspDetailFrame)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_2.addWidget(self.label_8, 1, 0, 1, 1)

        self.label_10 = QLabel(self.inspDetailFrame)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_2.addWidget(self.label_10, 2, 0, 1, 1)

        self.rateLabel = QLabel(self.inspDetailFrame)
        self.rateLabel.setObjectName(u"rateLabel")
        self.rateLabel.setFont(font5)
        self.rateLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.rateLabel, 2, 1, 1, 1)


        self.verticalLayout_7.addWidget(self.inspDetailFrame, 0, Qt.AlignTop)


        self.verticalLayout_6.addWidget(self.inspData, 0, Qt.AlignTop)

        self.logData = QFrame(self.overviewData)
        self.logData.setObjectName(u"logData")
        self.logData.setFrameShape(QFrame.StyledPanel)
        self.logData.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.logData)
        self.verticalLayout_8.setSpacing(10)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 18, 0, 0)
        self.label_12 = QLabel(self.logData)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font4)

        self.verticalLayout_8.addWidget(self.label_12)

        self.frame_6 = QFrame(self.logData)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_6)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.tabWidget_2 = QTabWidget(self.frame_6)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2.setTabPosition(QTabWidget.West)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_13 = QVBoxLayout(self.tab)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.items_textBrowser = QTextBrowser(self.tab)
        self.items_textBrowser.setObjectName(u"items_textBrowser")

        self.verticalLayout_13.addWidget(self.items_textBrowser)

        icon = QIcon()
        icon.addFile(u":/blueIcon/assets/icons/blue/grid.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tabWidget_2.addTab(self.tab, icon, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_15 = QVBoxLayout(self.tab_3)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.serial_textBrowser = QTextBrowser(self.tab_3)
        self.serial_textBrowser.setObjectName(u"serial_textBrowser")

        self.verticalLayout_15.addWidget(self.serial_textBrowser)

        icon1 = QIcon()
        icon1.addFile(u":/blueIcon/assets/icons/blue/minimize-2.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tabWidget_2.addTab(self.tab_3, icon1, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_14 = QVBoxLayout(self.tab_2)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.state_textBrowser = QTextBrowser(self.tab_2)
        self.state_textBrowser.setObjectName(u"state_textBrowser")

        self.verticalLayout_14.addWidget(self.state_textBrowser)

        icon2 = QIcon()
        icon2.addFile(u":/blueIcon/assets/icons/blue/chevrons-right.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tabWidget_2.addTab(self.tab_2, icon2, "")

        self.verticalLayout_9.addWidget(self.tabWidget_2)


        self.verticalLayout_8.addWidget(self.frame_6)


        self.verticalLayout_6.addWidget(self.logData)


        self.horizontalLayout_6.addWidget(self.overviewData)

        self.runningData = QWidget(self.autoTab)
        self.runningData.setObjectName(u"runningData")
        self.gridLayout_3 = QGridLayout(self.runningData)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.image1Label = QLabel(self.runningData)
        self.image1Label.setObjectName(u"image1Label")
        sizePolicy1.setHeightForWidth(self.image1Label.sizePolicy().hasHeightForWidth())
        self.image1Label.setSizePolicy(sizePolicy1)
        self.image1Label.setScaledContents(True)

        self.gridLayout_3.addWidget(self.image1Label, 0, 1, 1, 1)

        self.image2Label = QLabel(self.runningData)
        self.image2Label.setObjectName(u"image2Label")
        sizePolicy1.setHeightForWidth(self.image2Label.sizePolicy().hasHeightForWidth())
        self.image2Label.setSizePolicy(sizePolicy1)
        self.image2Label.setScaledContents(True)

        self.gridLayout_3.addWidget(self.image2Label, 0, 3, 1, 1)

        self.image3Label = QLabel(self.runningData)
        self.image3Label.setObjectName(u"image3Label")
        sizePolicy1.setHeightForWidth(self.image3Label.sizePolicy().hasHeightForWidth())
        self.image3Label.setSizePolicy(sizePolicy1)
        self.image3Label.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.image3Label.setScaledContents(True)

        self.gridLayout_3.addWidget(self.image3Label, 1, 1, 1, 1)

        self.image4Label = QLabel(self.runningData)
        self.image4Label.setObjectName(u"image4Label")
        sizePolicy1.setHeightForWidth(self.image4Label.sizePolicy().hasHeightForWidth())
        self.image4Label.setSizePolicy(sizePolicy1)
        self.image4Label.setScaledContents(True)

        self.gridLayout_3.addWidget(self.image4Label, 1, 3, 1, 1)


        self.horizontalLayout_6.addWidget(self.runningData)

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
        font6 = QFont()
        font6.setPointSize(10)
        font6.setBold(True)
        self.label.setFont(font6)

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
        self.label_16.setFont(font6)

        self.verticalLayout_10.addWidget(self.label_16)

        self.frame_3 = QFrame(self.config)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setVerticalSpacing(25)
        self.label_19 = QLabel(self.frame_3)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_5.addWidget(self.label_19, 2, 0, 1, 1)

        self.comboBox = QComboBox(self.frame_3)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(300, 0))
        self.comboBox.setMaximumSize(QSize(300, 16777215))

        self.gridLayout_5.addWidget(self.comboBox, 0, 1, 1, 1)

        self.label_18 = QLabel(self.frame_3)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_5.addWidget(self.label_18, 1, 0, 1, 1)

        self.lineEdit = QLineEdit(self.frame_3)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(300, 0))
        self.lineEdit.setMaximumSize(QSize(300, 16777215))

        self.gridLayout_5.addWidget(self.lineEdit, 1, 1, 1, 1)

        self.label_17 = QLabel(self.frame_3)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_5.addWidget(self.label_17, 0, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.frame_3)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(300, 0))
        self.lineEdit_2.setMaximumSize(QSize(300, 16777215))

        self.gridLayout_5.addWidget(self.lineEdit_2, 2, 1, 1, 1)


        self.verticalLayout_10.addWidget(self.frame_3, 0, Qt.AlignLeft|Qt.AlignTop)


        self.horizontalLayout_8.addWidget(self.config)

        self.tabWidget.addTab(self.dataTab, "")
        self.settingTab = QWidget()
        self.settingTab.setObjectName(u"settingTab")
        self.horizontalLayout_9 = QHBoxLayout(self.settingTab)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.viewSetting = QWidget(self.settingTab)
        self.viewSetting.setObjectName(u"viewSetting")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.viewSetting.sizePolicy().hasHeightForWidth())
        self.viewSetting.setSizePolicy(sizePolicy3)
        self.gridLayout_7 = QGridLayout(self.viewSetting)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.viewSettingLabel = QLabel(self.viewSetting)
        self.viewSettingLabel.setObjectName(u"viewSettingLabel")
        sizePolicy1.setHeightForWidth(self.viewSettingLabel.sizePolicy().hasHeightForWidth())
        self.viewSettingLabel.setSizePolicy(sizePolicy1)
        self.viewSettingLabel.setMinimumSize(QSize(0, 0))
        self.viewSettingLabel.setMaximumSize(QSize(100000, 99997))
        self.viewSettingLabel.setScaledContents(True)

        self.gridLayout_7.addWidget(self.viewSettingLabel, 0, 0, 1, 1)


        self.horizontalLayout_9.addWidget(self.viewSetting)

        self.adjust = QWidget(self.settingTab)
        self.adjust.setObjectName(u"adjust")
        self.adjust.setMinimumSize(QSize(400, 0))
        self.verticalLayout_11 = QVBoxLayout(self.adjust)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_21 = QLabel(self.adjust)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMinimumSize(QSize(30, 0))
        self.label_21.setMaximumSize(QSize(16777215, 30))
        self.label_21.setFont(font6)

        self.verticalLayout_11.addWidget(self.label_21)

        self.frame_4 = QFrame(self.adjust)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_4)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setVerticalSpacing(12)
        self.exposSaveBtn = QPushButton(self.frame_4)
        self.exposSaveBtn.setObjectName(u"exposSaveBtn")
        self.exposSaveBtn.setMinimumSize(QSize(80, 20))

        self.gridLayout_6.addWidget(self.exposSaveBtn, 0, 2, 1, 1)

        self.label_20 = QLabel(self.frame_4)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_6.addWidget(self.label_20, 0, 0, 1, 1)

        self.horizontalSlider = QSlider(self.frame_4)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        sizePolicy2.setHeightForWidth(self.horizontalSlider.sizePolicy().hasHeightForWidth())
        self.horizontalSlider.setSizePolicy(sizePolicy2)
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_6.addWidget(self.horizontalSlider, 0, 1, 1, 1)

        self.label_22 = QLabel(self.frame_4)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout_6.addWidget(self.label_22, 1, 0, 1, 1)

        self.horizontalSlider_2 = QSlider(self.frame_4)
        self.horizontalSlider_2.setObjectName(u"horizontalSlider_2")
        sizePolicy2.setHeightForWidth(self.horizontalSlider_2.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_2.setSizePolicy(sizePolicy2)
        self.horizontalSlider_2.setOrientation(Qt.Horizontal)

        self.gridLayout_6.addWidget(self.horizontalSlider_2, 1, 1, 1, 1)

        self.lightSaveBtn = QPushButton(self.frame_4)
        self.lightSaveBtn.setObjectName(u"lightSaveBtn")
        self.lightSaveBtn.setMinimumSize(QSize(80, 20))

        self.gridLayout_6.addWidget(self.lightSaveBtn, 1, 2, 1, 1)


        self.verticalLayout_11.addWidget(self.frame_4, 0, Qt.AlignTop)

        self.frame_5 = QFrame(self.adjust)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_5)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.manualBtn = QPushButton(self.frame_5)
        self.manualBtn.setObjectName(u"manualBtn")
        self.manualBtn.setMinimumSize(QSize(80, 20))

        self.verticalLayout_12.addWidget(self.manualBtn)

        self.uploadBtn = QPushButton(self.frame_5)
        self.uploadBtn.setObjectName(u"uploadBtn")
        self.uploadBtn.setMinimumSize(QSize(80, 20))

        self.verticalLayout_12.addWidget(self.uploadBtn)


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
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.autoTabBtn.sizePolicy().hasHeightForWidth())
        self.autoTabBtn.setSizePolicy(sizePolicy4)
        self.autoTabBtn.setMinimumSize(QSize(100, 50))
        font7 = QFont()
        font7.setPointSize(11)
        font7.setBold(True)
        self.autoTabBtn.setFont(font7)
        self.autoTabBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.autoTabBtn.setMouseTracking(False)
        icon3 = QIcon()
        icon3.addFile(u":/blueIcon/assets/icons/blue/airplay.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.autoTabBtn.setIcon(icon3)
        self.autoTabBtn.setIconSize(QSize(26, 26))

        self.horizontalLayout_5.addWidget(self.autoTabBtn)

        self.dataTabBtn = QPushButton(self.frame_2)
        self.dataTabBtn.setObjectName(u"dataTabBtn")
        self.dataTabBtn.setMinimumSize(QSize(100, 50))
        self.dataTabBtn.setFont(font7)
        self.dataTabBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/blueIcon/assets/icons/blue/refresh-ccw.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.dataTabBtn.setIcon(icon4)
        self.dataTabBtn.setIconSize(QSize(26, 26))

        self.horizontalLayout_5.addWidget(self.dataTabBtn)

        self.settingTabBtn = QPushButton(self.frame_2)
        self.settingTabBtn.setObjectName(u"settingTabBtn")
        self.settingTabBtn.setMinimumSize(QSize(100, 50))
        self.settingTabBtn.setFont(font7)
        self.settingTabBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/blueIcon/assets/icons/blue/sliders.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.settingTabBtn.setIcon(icon5)
        self.settingTabBtn.setIconSize(QSize(26, 26))

        self.horizontalLayout_5.addWidget(self.settingTabBtn)


        self.horizontalLayout_4.addWidget(self.frame_2, 0, Qt.AlignLeft)


        self.verticalLayout.addWidget(self.footerFrame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Vision Program", None))
        self.logoMeg.setText(QCoreApplication.translate("MainWindow", u"SEVT-MEG", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Vision Inspection Program", None))
        self.exeVer.setText(QCoreApplication.translate("MainWindow", u"PGM_V0010", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u2022 Model file_", None))
        self.mdFile.setText(QCoreApplication.translate("MainWindow", u"A123_V001", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u2022 Execute__", None))
        self.timeInfo.setText(QCoreApplication.translate("MainWindow", u"\u2022 Time: 12:12:11", None))
        self.ipInfo.setText(QCoreApplication.translate("MainWindow", u"\u2022 IP Adress: 107.114.123.123", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u25a0 Inspection Data__________________", None))
        self.tTimeLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u". Result", None))
        self.resultLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u". Test time", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u". Fail rate", None))
        self.rateLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u25a0 Detailed Log____________________", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Test Result", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Serial Log", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Stage Log", None))
        self.image1Label.setText("")
        self.image2Label.setText("")
        self.image3Label.setText("")
        self.image4Label.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.autoTab), QCoreApplication.translate("MainWindow", u"Auto", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u25a0 Select Model file", None))
        self.selectModelBtn.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u2022 Model file  :", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"\u2022 Feature file:", None))
        self.selectFeatureBtn.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u25a0 Configuration", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"\u2022 Camera ID of BTM", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\u2022 Camera ID of TOP", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\u2022 Serial COM no.", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.dataTab), QCoreApplication.translate("MainWindow", u"Data", None))
        self.viewSettingLabel.setText("")
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"\u25a0 Adjustment", None))
        self.exposSaveBtn.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u". Exposure", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u". Light level", None))
        self.lightSaveBtn.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.manualBtn.setText(QCoreApplication.translate("MainWindow", u"Manual Test", None))
        self.uploadBtn.setText(QCoreApplication.translate("MainWindow", u"Upload", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.settingTab), QCoreApplication.translate("MainWindow", u"Setting", None))
        self.autoTabBtn.setText(QCoreApplication.translate("MainWindow", u"Auto", None))
        self.dataTabBtn.setText(QCoreApplication.translate("MainWindow", u"Data", None))
        self.settingTabBtn.setText(QCoreApplication.translate("MainWindow", u"Setting", None))
    # retranslateUi

