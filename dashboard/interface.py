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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

from Custom_Widgets.QCustomSlideMenu import QCustomSlideMenu
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1187, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"*{\n"
"	color: #000;\n"
"	border: none;\n"
"}\n"
"\n"
"#centralwidget{\n"
"	background-color: #eff9fe;\n"
"}\n"
"\n"
"#frame_12{\n"
"	background-color: #2596be;\n"
"}\n"
"\n"
"QLineEdit{\n"
"	background-color: transparent;\n"
"	color: #2596be;\n"
"}\n"
"\n"
"#searchFrame{\n"
"	border-radius: 10px;\n"
"	border: 2px solid #2596be;\n"
"}\n"
"\n"
"#appHeader{\n"
"	color: #2596be;\n"
"}\n"
"\n"
"#viewMoreBtn, #viewMoreBtn2{\n"
"	background-color: #2596be;\n"
"	color: #fff;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"#card1, #card2, #card3, #card4{\n"
"	background-color: #fefeff;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"#widget_4, #widget_5, #headerFrame, #profileCont, #frame_15{\n"
"	background-color: #fefeff;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"#homeBtn{\n"
"	background-color: #1efeff;\n"
"	padding: 5px;\n"
"	text-align: left;\n"
"	color: #000;\n"
"	border-top-left-radius: 10px;\n"
"}\n"
"#monitorBtn, #settingBtn, #extentBtn{\n"
"	padding: 5px;\n"
"	text-align: left;\n"
"	color: #000;\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, 0, -1)
        self.leftMenu = QCustomSlideMenu(self.centralwidget)
        self.leftMenu.setObjectName(u"leftMenu")
        self.leftMenu.setMinimumSize(QSize(215, 0))
        self.leftMenu.setMaximumSize(QSize(215, 16777215))
        self.verticalLayout_8 = QVBoxLayout(self.leftMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_12 = QFrame(self.leftMenu)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_12)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_13 = QFrame(self.frame_12)
        self.frame_13.setObjectName(u"frame_13")
        font = QFont()
        font.setPointSize(9)
        font.setBold(True)
        self.frame_13.setFont(font)
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_13)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_44 = QLabel(self.frame_13)
        self.label_44.setObjectName(u"label_44")
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(True)
        self.label_44.setFont(font1)

        self.verticalLayout_10.addWidget(self.label_44)


        self.verticalLayout_9.addWidget(self.frame_13, 0, Qt.AlignLeft|Qt.AlignTop)

        self.frame_14 = QFrame(self.frame_12)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_14)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(-1, -1, 0, -1)
        self.homeBtn = QPushButton(self.frame_14)
        self.homeBtn.setObjectName(u"homeBtn")
        self.homeBtn.setMinimumSize(QSize(0, 40))
        self.homeBtn.setMaximumSize(QSize(16777215, 40))
        icon = QIcon()
        icon.addFile(u":/whiteIcon/assets/icons/whiteIcon/home.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.homeBtn.setIcon(icon)
        self.homeBtn.setIconSize(QSize(20, 20))

        self.verticalLayout_11.addWidget(self.homeBtn)

        self.monitorBtn = QPushButton(self.frame_14)
        self.monitorBtn.setObjectName(u"monitorBtn")
        self.monitorBtn.setMinimumSize(QSize(0, 40))
        self.monitorBtn.setMaximumSize(QSize(16777215, 40))
        icon1 = QIcon()
        icon1.addFile(u":/whiteIcon/assets/icons/whiteIcon/map.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.monitorBtn.setIcon(icon1)
        self.monitorBtn.setIconSize(QSize(20, 20))

        self.verticalLayout_11.addWidget(self.monitorBtn)

        self.settingBtn = QPushButton(self.frame_14)
        self.settingBtn.setObjectName(u"settingBtn")
        self.settingBtn.setMinimumSize(QSize(0, 40))
        self.settingBtn.setMaximumSize(QSize(16777215, 40))
        icon2 = QIcon()
        icon2.addFile(u":/whiteIcon/assets/icons/whiteIcon/minimize.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.settingBtn.setIcon(icon2)
        self.settingBtn.setIconSize(QSize(20, 20))

        self.verticalLayout_11.addWidget(self.settingBtn)

        self.extentBtn = QPushButton(self.frame_14)
        self.extentBtn.setObjectName(u"extentBtn")
        self.extentBtn.setMinimumSize(QSize(0, 40))
        self.extentBtn.setMaximumSize(QSize(16777215, 40))
        icon3 = QIcon()
        icon3.addFile(u":/whiteIcon/assets/icons/whiteIcon/battery-charging.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.extentBtn.setIcon(icon3)
        self.extentBtn.setIconSize(QSize(20, 20))

        self.verticalLayout_11.addWidget(self.extentBtn)


        self.verticalLayout_9.addWidget(self.frame_14)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_2)


        self.verticalLayout_8.addWidget(self.frame_12)


        self.horizontalLayout.addWidget(self.leftMenu)

        self.mainBody = QWidget(self.centralwidget)
        self.mainBody.setObjectName(u"mainBody")
        self.verticalLayout = QVBoxLayout(self.mainBody)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.headerFrame = QWidget(self.mainBody)
        self.headerFrame.setObjectName(u"headerFrame")
        self.horizontalLayout_2 = QHBoxLayout(self.headerFrame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 4)
        self.widget = QWidget(self.headerFrame)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_3 = QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.menuBtn = QPushButton(self.widget)
        self.menuBtn.setObjectName(u"menuBtn")
        icon4 = QIcon()
        icon4.addFile(u":/blueIcon/assets/icons/blueIcon/menu.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.menuBtn.setIcon(icon4)
        self.menuBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.menuBtn)

        self.appHeader = QLabel(self.widget)
        self.appHeader.setObjectName(u"appHeader")
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.appHeader.setFont(font2)

        self.horizontalLayout_3.addWidget(self.appHeader)


        self.horizontalLayout_2.addWidget(self.widget, 0, Qt.AlignLeft)

        self.widget_2 = QWidget(self.headerFrame)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.searchFrame = QFrame(self.widget_2)
        self.searchFrame.setObjectName(u"searchFrame")
        self.searchFrame.setMinimumSize(QSize(160, 0))
        self.searchFrame.setFrameShape(QFrame.StyledPanel)
        self.searchFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.searchFrame)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.searchFrame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(30, 30))
        self.label_2.setMaximumSize(QSize(30, 30))
        self.label_2.setAutoFillBackground(False)
        self.label_2.setPixmap(QPixmap(u":/blueIcon/assets/icons/blueIcon/search.svg"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout_5.addWidget(self.label_2)

        self.lineEdit = QLineEdit(self.searchFrame)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_5.addWidget(self.lineEdit)


        self.horizontalLayout_4.addWidget(self.searchFrame, 0, Qt.AlignTop)


        self.horizontalLayout_2.addWidget(self.widget_2, 0, Qt.AlignHCenter)

        self.widget_3 = QWidget(self.headerFrame)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.accountBtn = QPushButton(self.widget_3)
        self.accountBtn.setObjectName(u"accountBtn")
        icon5 = QIcon()
        icon5.addFile(u":/blueIcon/assets/icons/blueIcon/user.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.accountBtn.setIcon(icon5)
        self.accountBtn.setIconSize(QSize(32, 32))

        self.horizontalLayout_6.addWidget(self.accountBtn)


        self.horizontalLayout_2.addWidget(self.widget_3, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.headerFrame, 0, Qt.AlignTop)

        self.cardFrame = QWidget(self.mainBody)
        self.cardFrame.setObjectName(u"cardFrame")
        self.horizontalLayout_7 = QHBoxLayout(self.cardFrame)
        self.horizontalLayout_7.setSpacing(20)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(5, 5, 5, 5)
        self.card1 = QFrame(self.cardFrame)
        self.card1.setObjectName(u"card1")
        self.card1.setMinimumSize(QSize(160, 0))
        self.card1.setFrameShape(QFrame.StyledPanel)
        self.card1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.card1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.card1)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        font3 = QFont()
        font3.setPointSize(13)
        font3.setBold(True)
        self.label_3.setFont(font3)

        self.horizontalLayout_8.addWidget(self.label_3)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(40, 40))
        font4 = QFont()
        font4.setPointSize(8)
        font4.setBold(True)
        self.label_4.setFont(font4)
        self.label_4.setPixmap(QPixmap(u":/blueIcon/assets/icons/blueIcon/shopping-cart.svg"))
        self.label_4.setScaledContents(True)

        self.horizontalLayout_8.addWidget(self.label_4)


        self.verticalLayout_2.addWidget(self.frame)

        self.label = QLabel(self.card1)
        self.label.setObjectName(u"label")
        font5 = QFont()
        font5.setPointSize(10)
        self.label.setFont(font5)

        self.verticalLayout_2.addWidget(self.label, 0, Qt.AlignTop)


        self.horizontalLayout_7.addWidget(self.card1)

        self.card2 = QFrame(self.cardFrame)
        self.card2.setObjectName(u"card2")
        self.card2.setMinimumSize(QSize(160, 0))
        self.card2.setFrameShape(QFrame.StyledPanel)
        self.card2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.card2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_2 = QFrame(self.card2)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font3)

        self.horizontalLayout_9.addWidget(self.label_5)

        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(40, 40))
        self.label_6.setFont(font4)
        self.label_6.setPixmap(QPixmap(u":/blueIcon/assets/icons/blueIcon/credit-card.svg"))
        self.label_6.setScaledContents(True)

        self.horizontalLayout_9.addWidget(self.label_6)


        self.verticalLayout_3.addWidget(self.frame_2)

        self.label_7 = QLabel(self.card2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font5)

        self.verticalLayout_3.addWidget(self.label_7, 0, Qt.AlignTop)


        self.horizontalLayout_7.addWidget(self.card2)

        self.card3 = QFrame(self.cardFrame)
        self.card3.setObjectName(u"card3")
        self.card3.setMinimumSize(QSize(160, 0))
        self.card3.setFrameShape(QFrame.StyledPanel)
        self.card3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.card3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_3 = QFrame(self.card3)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_8 = QLabel(self.frame_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font3)

        self.horizontalLayout_10.addWidget(self.label_8)

        self.label_9 = QLabel(self.frame_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(40, 40))
        self.label_9.setFont(font4)
        self.label_9.setPixmap(QPixmap(u":/blueIcon/assets/icons/blueIcon/shopping-bag.svg"))
        self.label_9.setScaledContents(True)

        self.horizontalLayout_10.addWidget(self.label_9)


        self.verticalLayout_4.addWidget(self.frame_3)

        self.label_10 = QLabel(self.card3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font5)

        self.verticalLayout_4.addWidget(self.label_10, 0, Qt.AlignTop)


        self.horizontalLayout_7.addWidget(self.card3)

        self.card4 = QFrame(self.cardFrame)
        self.card4.setObjectName(u"card4")
        self.card4.setMinimumSize(QSize(160, 0))
        self.card4.setFrameShape(QFrame.StyledPanel)
        self.card4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.card4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_4 = QFrame(self.card4)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_11 = QLabel(self.frame_4)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font3)

        self.horizontalLayout_11.addWidget(self.label_11)

        self.label_12 = QLabel(self.frame_4)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMaximumSize(QSize(40, 40))
        self.label_12.setFont(font4)
        self.label_12.setPixmap(QPixmap(u":/blueIcon/assets/icons/blueIcon/truck.svg"))
        self.label_12.setScaledContents(True)

        self.horizontalLayout_11.addWidget(self.label_12)


        self.verticalLayout_5.addWidget(self.frame_4)

        self.label_13 = QLabel(self.card4)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font5)

        self.verticalLayout_5.addWidget(self.label_13, 0, Qt.AlignTop)


        self.horizontalLayout_7.addWidget(self.card4)


        self.verticalLayout.addWidget(self.cardFrame)

        self.mainFrame = QWidget(self.mainBody)
        self.mainFrame.setObjectName(u"mainFrame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainFrame.sizePolicy().hasHeightForWidth())
        self.mainFrame.setSizePolicy(sizePolicy)
        self.horizontalLayout_12 = QHBoxLayout(self.mainFrame)
        self.horizontalLayout_12.setSpacing(10)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(5, 5, 5, 5)
        self.widget_4 = QWidget(self.mainFrame)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_6 = QVBoxLayout(self.widget_4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_5 = QFrame(self.widget_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_14 = QLabel(self.frame_5)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font1)

        self.horizontalLayout_13.addWidget(self.label_14, 0, Qt.AlignLeft)

        self.viewMoreBtn = QPushButton(self.frame_5)
        self.viewMoreBtn.setObjectName(u"viewMoreBtn")
        font6 = QFont()
        font6.setBold(True)
        self.viewMoreBtn.setFont(font6)
        icon6 = QIcon()
        icon6.addFile(u":/whiteIcon/assets/icons/whiteIcon/arrow-right.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.viewMoreBtn.setIcon(icon6)
        self.viewMoreBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_13.addWidget(self.viewMoreBtn, 0, Qt.AlignRight)


        self.verticalLayout_6.addWidget(self.frame_5, 0, Qt.AlignTop)

        self.frame_6 = QFrame(self.widget_4)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_6)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_20 = QLabel(self.frame_6)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout.addWidget(self.label_20, 1, 3, 1, 1)

        self.label_18 = QLabel(self.frame_6)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout.addWidget(self.label_18, 1, 1, 1, 1)

        self.label_23 = QLabel(self.frame_6)
        self.label_23.setObjectName(u"label_23")

        self.gridLayout.addWidget(self.label_23, 2, 3, 1, 1)

        self.label_17 = QLabel(self.frame_6)
        self.label_17.setObjectName(u"label_17")
        font7 = QFont()
        font7.setPointSize(10)
        font7.setBold(True)
        self.label_17.setFont(font7)

        self.gridLayout.addWidget(self.label_17, 0, 3, 1, 1)

        self.label_19 = QLabel(self.frame_6)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout.addWidget(self.label_19, 1, 2, 1, 1)

        self.label_22 = QLabel(self.frame_6)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout.addWidget(self.label_22, 2, 2, 1, 1)

        self.label_15 = QLabel(self.frame_6)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font7)

        self.gridLayout.addWidget(self.label_15, 0, 1, 1, 1)

        self.label_21 = QLabel(self.frame_6)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout.addWidget(self.label_21, 2, 1, 1, 1)

        self.label_16 = QLabel(self.frame_6)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font7)

        self.gridLayout.addWidget(self.label_16, 0, 2, 1, 1)

        self.label_24 = QLabel(self.frame_6)
        self.label_24.setObjectName(u"label_24")

        self.gridLayout.addWidget(self.label_24, 3, 1, 1, 1)

        self.label_25 = QLabel(self.frame_6)
        self.label_25.setObjectName(u"label_25")

        self.gridLayout.addWidget(self.label_25, 3, 2, 1, 1)

        self.label_26 = QLabel(self.frame_6)
        self.label_26.setObjectName(u"label_26")

        self.gridLayout.addWidget(self.label_26, 3, 3, 1, 1)


        self.verticalLayout_6.addWidget(self.frame_6)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer)


        self.horizontalLayout_12.addWidget(self.widget_4)

        self.widget_5 = QWidget(self.mainFrame)
        self.widget_5.setObjectName(u"widget_5")
        self.verticalLayout_7 = QVBoxLayout(self.widget_5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_7 = QFrame(self.widget_5)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_27 = QLabel(self.frame_7)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font1)

        self.horizontalLayout_14.addWidget(self.label_27, 0, Qt.AlignLeft)

        self.viewMoreBtn2 = QPushButton(self.frame_7)
        self.viewMoreBtn2.setObjectName(u"viewMoreBtn2")
        self.viewMoreBtn2.setFont(font6)
        self.viewMoreBtn2.setIcon(icon6)
        self.viewMoreBtn2.setIconSize(QSize(24, 24))

        self.horizontalLayout_14.addWidget(self.viewMoreBtn2, 0, Qt.AlignRight)


        self.verticalLayout_7.addWidget(self.frame_7, 0, Qt.AlignTop)

        self.frame_10 = QFrame(self.widget_5)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_36 = QLabel(self.frame_10)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setMinimumSize(QSize(50, 50))
        self.label_36.setMaximumSize(QSize(50, 50))
        self.label_36.setPixmap(QPixmap(u":/images/assets/images/Pro.jpg"))
        self.label_36.setScaledContents(True)

        self.horizontalLayout_17.addWidget(self.label_36)

        self.label_37 = QLabel(self.frame_10)
        self.label_37.setObjectName(u"label_37")

        self.horizontalLayout_17.addWidget(self.label_37)

        self.label_38 = QLabel(self.frame_10)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setMinimumSize(QSize(30, 30))
        self.label_38.setMaximumSize(QSize(30, 30))
        self.label_38.setPixmap(QPixmap(u":/blueIcon/assets/icons/blueIcon/message-circle.svg"))
        self.label_38.setScaledContents(True)

        self.horizontalLayout_17.addWidget(self.label_38)

        self.label_39 = QLabel(self.frame_10)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setMinimumSize(QSize(30, 30))
        self.label_39.setMaximumSize(QSize(30, 30))
        self.label_39.setPixmap(QPixmap(u":/blueIcon/assets/icons/blueIcon/phone-call.svg"))
        self.label_39.setScaledContents(True)

        self.horizontalLayout_17.addWidget(self.label_39)


        self.verticalLayout_7.addWidget(self.frame_10, 0, Qt.AlignTop)

        self.frame_11 = QFrame(self.widget_5)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_40 = QLabel(self.frame_11)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setMinimumSize(QSize(50, 50))
        self.label_40.setMaximumSize(QSize(50, 50))
        self.label_40.setPixmap(QPixmap(u":/images/assets/images/Pro.jpg"))
        self.label_40.setScaledContents(True)

        self.horizontalLayout_18.addWidget(self.label_40)

        self.label_41 = QLabel(self.frame_11)
        self.label_41.setObjectName(u"label_41")

        self.horizontalLayout_18.addWidget(self.label_41)

        self.label_42 = QLabel(self.frame_11)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setMinimumSize(QSize(30, 30))
        self.label_42.setMaximumSize(QSize(30, 30))
        self.label_42.setPixmap(QPixmap(u":/blueIcon/assets/icons/blueIcon/message-circle.svg"))
        self.label_42.setScaledContents(True)

        self.horizontalLayout_18.addWidget(self.label_42)

        self.label_43 = QLabel(self.frame_11)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setMinimumSize(QSize(30, 30))
        self.label_43.setMaximumSize(QSize(30, 30))
        self.label_43.setPixmap(QPixmap(u":/blueIcon/assets/icons/blueIcon/phone-call.svg"))
        self.label_43.setScaledContents(True)

        self.horizontalLayout_18.addWidget(self.label_43)


        self.verticalLayout_7.addWidget(self.frame_11, 0, Qt.AlignTop)

        self.frame_8 = QFrame(self.widget_5)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_28 = QLabel(self.frame_8)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMinimumSize(QSize(50, 50))
        self.label_28.setMaximumSize(QSize(50, 50))
        self.label_28.setPixmap(QPixmap(u":/images/assets/images/Pro.jpg"))
        self.label_28.setScaledContents(True)

        self.horizontalLayout_15.addWidget(self.label_28)

        self.label_29 = QLabel(self.frame_8)
        self.label_29.setObjectName(u"label_29")

        self.horizontalLayout_15.addWidget(self.label_29)

        self.label_30 = QLabel(self.frame_8)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMinimumSize(QSize(30, 30))
        self.label_30.setMaximumSize(QSize(30, 30))
        self.label_30.setPixmap(QPixmap(u":/blueIcon/assets/icons/blueIcon/message-circle.svg"))
        self.label_30.setScaledContents(True)

        self.horizontalLayout_15.addWidget(self.label_30)

        self.label_31 = QLabel(self.frame_8)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setMinimumSize(QSize(30, 30))
        self.label_31.setMaximumSize(QSize(30, 30))
        self.label_31.setPixmap(QPixmap(u":/blueIcon/assets/icons/blueIcon/phone-call.svg"))
        self.label_31.setScaledContents(True)

        self.horizontalLayout_15.addWidget(self.label_31)


        self.verticalLayout_7.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.widget_5)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_32 = QLabel(self.frame_9)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setMinimumSize(QSize(50, 50))
        self.label_32.setMaximumSize(QSize(50, 50))
        self.label_32.setPixmap(QPixmap(u":/images/assets/images/Pro.jpg"))
        self.label_32.setScaledContents(True)

        self.horizontalLayout_16.addWidget(self.label_32)

        self.label_33 = QLabel(self.frame_9)
        self.label_33.setObjectName(u"label_33")

        self.horizontalLayout_16.addWidget(self.label_33)

        self.label_34 = QLabel(self.frame_9)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setMinimumSize(QSize(30, 30))
        self.label_34.setMaximumSize(QSize(30, 30))
        self.label_34.setPixmap(QPixmap(u":/blueIcon/assets/icons/blueIcon/message-circle.svg"))
        self.label_34.setScaledContents(True)

        self.horizontalLayout_16.addWidget(self.label_34)

        self.label_35 = QLabel(self.frame_9)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setMinimumSize(QSize(30, 30))
        self.label_35.setMaximumSize(QSize(30, 30))
        self.label_35.setPixmap(QPixmap(u":/blueIcon/assets/icons/blueIcon/phone-call.svg"))
        self.label_35.setScaledContents(True)

        self.horizontalLayout_16.addWidget(self.label_35)


        self.verticalLayout_7.addWidget(self.frame_9, 0, Qt.AlignTop)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_3)


        self.horizontalLayout_12.addWidget(self.widget_5)


        self.verticalLayout.addWidget(self.mainFrame)


        self.horizontalLayout.addWidget(self.mainBody)

        self.profileCont = QCustomSlideMenu(self.centralwidget)
        self.profileCont.setObjectName(u"profileCont")
        sizePolicy.setHeightForWidth(self.profileCont.sizePolicy().hasHeightForWidth())
        self.profileCont.setSizePolicy(sizePolicy)
        self.profileCont.setMinimumSize(QSize(150, 0))
        self.profileCont.setMaximumSize(QSize(150, 16777215))
        self.verticalLayout_12 = QVBoxLayout(self.profileCont)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.frame_15 = QFrame(self.profileCont)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_15)
        self.verticalLayout_13.setSpacing(6)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.label_45 = QLabel(self.frame_15)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setFont(font6)
        self.label_45.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_45)

        self.label_46 = QLabel(self.frame_15)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_46)

        self.label_47 = QLabel(self.frame_15)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setMinimumSize(QSize(50, 50))
        self.label_47.setMaximumSize(QSize(50, 50))
        self.label_47.setPixmap(QPixmap(u":/images/assets/images/Pro.jpg"))
        self.label_47.setScaledContents(True)
        self.label_47.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_47, 0, Qt.AlignHCenter)

        self.profileBtn = QPushButton(self.frame_15)
        self.profileBtn.setObjectName(u"profileBtn")
        self.profileBtn.setIcon(icon5)

        self.verticalLayout_13.addWidget(self.profileBtn)

        self.logoutBtn = QPushButton(self.frame_15)
        self.logoutBtn.setObjectName(u"logoutBtn")
        icon7 = QIcon()
        icon7.addFile(u":/blueIcon/assets/icons/blueIcon/log-out.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.logoutBtn.setIcon(icon7)

        self.verticalLayout_13.addWidget(self.logoutBtn)


        self.verticalLayout_12.addWidget(self.frame_15, 0, Qt.AlignTop)


        self.horizontalLayout.addWidget(self.profileCont, 0, Qt.AlignTop)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Learn Programming", None))
        self.homeBtn.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.monitorBtn.setText(QCoreApplication.translate("MainWindow", u"Monitoring", None))
        self.settingBtn.setText(QCoreApplication.translate("MainWindow", u"Setting", None))
        self.extentBtn.setText(QCoreApplication.translate("MainWindow", u"Extention", None))
        self.menuBtn.setText("")
        self.appHeader.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.label_2.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search something", None))
        self.accountBtn.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"2,000,000", None))
        self.label_4.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"USD", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"+300", None))
        self.label_6.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Stock", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"2,000,000", None))
        self.label_9.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"USD", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"2,000,000", None))
        self.label_12.setText("")
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"something", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Lastest Products", None))
        self.viewMoreBtn.setText(QCoreApplication.translate("MainWindow", u"View more", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Store", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Products", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Price", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Clients", None))
        self.viewMoreBtn2.setText(QCoreApplication.translate("MainWindow", u"View more", None))
        self.label_36.setText("")
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Trinh Thuan</span></p><p><span style=\" font-size:7pt;\">TS part</span></p></body></html>", None))
        self.label_38.setText("")
        self.label_39.setText("")
        self.label_40.setText("")
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Trinh Thuan</span></p><p><span style=\" font-size:7pt;\">TS part</span></p></body></html>", None))
        self.label_42.setText("")
        self.label_43.setText("")
        self.label_28.setText("")
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Trinh Thuan</span></p><p><span style=\" font-size:7pt;\">TS part</span></p></body></html>", None))
        self.label_30.setText("")
        self.label_31.setText("")
        self.label_32.setText("")
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Trinh Thuan</span></p><p><span style=\" font-size:7pt;\">TS part</span></p></body></html>", None))
        self.label_34.setText("")
        self.label_35.setText("")
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Trinh Thuan", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Admin", None))
        self.label_47.setText("")
        self.profileBtn.setText(QCoreApplication.translate("MainWindow", u"My Profile", None))
        self.logoutBtn.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
    # retranslateUi

