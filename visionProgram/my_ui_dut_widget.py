# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'my_dut_widget.ui'
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
    QHeaderView, QLabel, QPushButton, QSizePolicy,
    QTabWidget, QTableWidget, QTableWidgetItem, QTextBrowser,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(571, 496)
        Form.setStyleSheet(u"/*{\n"
"  border: none;\n"
"}*/\n"
"#dutFrame, #viewResultFrame{\n"
"	border: 2px solid #D5EEF7;\n"
"	border-radius: 10px;\n"
"	background-color: #EBF7FB;\n"
"}\n"
"\n"
"#logViewTabWidget{\n"
"	background-color: #000;\n"
"}\n"
"\n"
"\n"
"#frame, #frame_2, #frame_3, #frame_4, #frame_5, #frame_6{\n"
"    background-color: rgba(38, 200, 255, 80); /* m\u00e0u \u0111en m\u1edd (opacity 50/255) */\n"
"    max-height: 1px;   /* ch\u1ec9 d\u00e0y 1 pixel */\n"
"    min-height: 1px;\n"
"    border: none;\n"
"\n"
"}\n"
"\n"
"#viewResultFrame{\n"
"	border: 2px solid #D5EEF7;\n"
"	border-radius: 10px;\n"
"	background-color: #fff;\n"
"\n"
"}\n"
"\n"
"#dutNameLabel{\n"
"	background-color: #26eaff;\n"
"	border-top-left-radius: 10px;\n"
"    border-top-right-radius: 10px;\n"
"}\n"
"\n"
"\n"
"\n"
"QTextBrowser{\n"
"	background-color: #ffffff;\n"
"}\n"
"\n"
"#dutImageLabel{\n"
"	background-color: #D5EEF7;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"    /*border: 1px solid #26eaff;*/\n"
"    background: #ebf7"
                        "fb;\n"
"	color: rgb(235, 247, 251);\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    background: #e0e0e0;\n"
"   /* border: 1px solid #26eaff;*/\n"
"    border-top-left-radius: 8px;\n"
"    padding: 3px ;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background: #ebf7fb;\n"
"    border-bottom-color: #26eaff; /* N\u1ed1i li\u1ec1n v\u1edbi n\u1ed9i dung */\n"
"}\n"
"\n"
"#tableWidget{\n"
"	background-color: #fff;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.dutFrame = QFrame(Form)
        self.dutFrame.setObjectName(u"dutFrame")
        self.dutFrame.setFrameShape(QFrame.StyledPanel)
        self.dutFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.dutFrame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.dutNameLabel = QLabel(self.dutFrame)
        self.dutNameLabel.setObjectName(u"dutNameLabel")
        font = QFont()
        font.setPointSize(9)
        font.setBold(True)
        self.dutNameLabel.setFont(font)
        self.dutNameLabel.setAlignment(Qt.AlignCenter)
        self.dutNameLabel.setMargin(2)

        self.verticalLayout.addWidget(self.dutNameLabel)

        self.inspData = QFrame(self.dutFrame)
        self.inspData.setObjectName(u"inspData")
        self.inspData.setFrameShape(QFrame.StyledPanel)
        self.inspData.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.inspData)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.dutStatusLabel = QLabel(self.inspData)
        self.dutStatusLabel.setObjectName(u"dutStatusLabel")
        self.dutStatusLabel.setFont(font)
        self.dutStatusLabel.setAlignment(Qt.AlignCenter)
        self.dutStatusLabel.setMargin(2)
        self.dutStatusLabel.setIndent(1)

        self.verticalLayout_7.addWidget(self.dutStatusLabel, 0, Qt.AlignTop)

        self.btn_start = QPushButton(self.inspData)
        self.btn_start.setObjectName(u"btn_start")

        self.verticalLayout_7.addWidget(self.btn_start)

        self.inspDetailFrame = QFrame(self.inspData)
        self.inspDetailFrame.setObjectName(u"inspDetailFrame")
        self.inspDetailFrame.setFrameShape(QFrame.StyledPanel)
        self.inspDetailFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.inspDetailFrame)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.resultLabel = QLabel(self.inspDetailFrame)
        self.resultLabel.setObjectName(u"resultLabel")
        font1 = QFont()
        font1.setBold(True)
        self.resultLabel.setFont(font1)
        self.resultLabel.setAlignment(Qt.AlignCenter)
        self.resultLabel.setMargin(2)
        self.resultLabel.setIndent(1)

        self.gridLayout_2.addWidget(self.resultLabel, 0, 1, 1, 1)

        self.label_10 = QLabel(self.inspDetailFrame)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(200, 16777215))
        self.label_10.setMargin(2)
        self.label_10.setIndent(1)

        self.gridLayout_2.addWidget(self.label_10, 4, 0, 1, 1)

        self.frame_3 = QFrame(self.inspDetailFrame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.HLine)
        self.frame_3.setFrameShadow(QFrame.Raised)

        self.gridLayout_2.addWidget(self.frame_3, 3, 0, 1, 1)

        self.rateLabel = QLabel(self.inspDetailFrame)
        self.rateLabel.setObjectName(u"rateLabel")
        self.rateLabel.setFont(font1)
        self.rateLabel.setAlignment(Qt.AlignCenter)
        self.rateLabel.setMargin(2)
        self.rateLabel.setIndent(1)

        self.gridLayout_2.addWidget(self.rateLabel, 4, 1, 1, 1)

        self.frame = QFrame(self.inspDetailFrame)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.HLine)
        self.frame.setFrameShadow(QFrame.Raised)

        self.gridLayout_2.addWidget(self.frame, 1, 0, 1, 1)

        self.frame_2 = QFrame(self.inspDetailFrame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.HLine)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.gridLayout_2.addWidget(self.frame_2, 1, 1, 1, 1)

        self.tTimeLabel = QLabel(self.inspDetailFrame)
        self.tTimeLabel.setObjectName(u"tTimeLabel")
        self.tTimeLabel.setFont(font1)
        self.tTimeLabel.setAlignment(Qt.AlignCenter)
        self.tTimeLabel.setMargin(2)
        self.tTimeLabel.setIndent(1)

        self.gridLayout_2.addWidget(self.tTimeLabel, 2, 1, 1, 1)

        self.frame_4 = QFrame(self.inspDetailFrame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.HLine)
        self.frame_4.setFrameShadow(QFrame.Raised)

        self.gridLayout_2.addWidget(self.frame_4, 3, 1, 1, 1)

        self.label_6 = QLabel(self.inspDetailFrame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(200, 16777215))
        self.label_6.setMargin(2)
        self.label_6.setIndent(1)

        self.gridLayout_2.addWidget(self.label_6, 0, 0, 1, 1)

        self.label_8 = QLabel(self.inspDetailFrame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(200, 16777215))
        self.label_8.setMargin(2)
        self.label_8.setIndent(1)

        self.gridLayout_2.addWidget(self.label_8, 2, 0, 1, 1)

        self.frame_5 = QFrame(self.inspDetailFrame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.HLine)
        self.frame_5.setFrameShadow(QFrame.Raised)

        self.gridLayout_2.addWidget(self.frame_5, 5, 0, 1, 1)

        self.frame_6 = QFrame(self.inspDetailFrame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.HLine)
        self.frame_6.setFrameShadow(QFrame.Raised)

        self.gridLayout_2.addWidget(self.frame_6, 5, 1, 1, 1)


        self.verticalLayout_7.addWidget(self.inspDetailFrame, 0, Qt.AlignTop)


        self.verticalLayout.addWidget(self.inspData)

        self.viewResultFrame = QFrame(self.dutFrame)
        self.viewResultFrame.setObjectName(u"viewResultFrame")
        self.viewResultFrame.setFrameShape(QFrame.StyledPanel)
        self.viewResultFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.viewResultFrame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.logViewTabWidget = QTabWidget(self.viewResultFrame)
        self.logViewTabWidget.setObjectName(u"logViewTabWidget")
        self.logViewTabWidget.setMaximumSize(QSize(250, 16777215))
        self.logViewTabWidget.setTabPosition(QTabWidget.West)
        self.testResultTab = QWidget()
        self.testResultTab.setObjectName(u"testResultTab")
        self.verticalLayout_13 = QVBoxLayout(self.testResultTab)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.tableWidget = QTableWidget(self.testResultTab)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        font2 = QFont()
        font2.setFamilies([u"MS Shell Dlg 2"])
        font2.setPointSize(7)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font2);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font2);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        font3 = QFont()
        font3.setPointSize(7)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font3);
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font2);
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font2);
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidget.setObjectName(u"tableWidget")
        font4 = QFont()
        font4.setFamilies([u"Arial"])
        font4.setPointSize(6)
        self.tableWidget.setFont(font4)
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(47)

        self.verticalLayout_13.addWidget(self.tableWidget)

        icon = QIcon()
        icon.addFile(u":/blueIcon/assets/icons/blue/grid.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.logViewTabWidget.addTab(self.testResultTab, icon, "")
        self.serialTab = QWidget()
        self.serialTab.setObjectName(u"serialTab")
        self.verticalLayout_15 = QVBoxLayout(self.serialTab)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.serial_textBrowser = QTextBrowser(self.serialTab)
        self.serial_textBrowser.setObjectName(u"serial_textBrowser")

        self.verticalLayout_15.addWidget(self.serial_textBrowser)

        icon1 = QIcon()
        icon1.addFile(u":/blueIcon/assets/icons/blue/minimize-2.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.logViewTabWidget.addTab(self.serialTab, icon1, "")
        self.stageTab = QWidget()
        self.stageTab.setObjectName(u"stageTab")
        self.verticalLayout_14 = QVBoxLayout(self.stageTab)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.state_textBrowser = QTextBrowser(self.stageTab)
        self.state_textBrowser.setObjectName(u"state_textBrowser")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.state_textBrowser.sizePolicy().hasHeightForWidth())
        self.state_textBrowser.setSizePolicy(sizePolicy1)
        self.state_textBrowser.setMinimumSize(QSize(150, 200))
        self.state_textBrowser.setMaximumSize(QSize(250, 16777215))

        self.verticalLayout_14.addWidget(self.state_textBrowser)

        icon2 = QIcon()
        icon2.addFile(u":/blueIcon/assets/icons/blue/chevrons-right.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.logViewTabWidget.addTab(self.stageTab, icon2, "")

        self.horizontalLayout.addWidget(self.logViewTabWidget, 0, Qt.AlignLeft)

        self.dutImageLabel = QLabel(self.viewResultFrame)
        self.dutImageLabel.setObjectName(u"dutImageLabel")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.dutImageLabel.sizePolicy().hasHeightForWidth())
        self.dutImageLabel.setSizePolicy(sizePolicy2)
        self.dutImageLabel.setMinimumSize(QSize(200, 200))
        self.dutImageLabel.setStyleSheet(u"")
        self.dutImageLabel.setScaledContents(False)
        self.dutImageLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.dutImageLabel)


        self.verticalLayout.addWidget(self.viewResultFrame)


        self.verticalLayout_2.addWidget(self.dutFrame)


        self.retranslateUi(Form)

        self.logViewTabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.dutNameLabel.setText(QCoreApplication.translate("Form", u"DUT Name", None))
        self.dutStatusLabel.setText(QCoreApplication.translate("Form", u"Status: Idle", None))
        self.btn_start.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.resultLabel.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"\u2022 Fail rate", None))
        self.rateLabel.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.tTimeLabel.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u2022 Result", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"\u2022 Test time", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Items", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Values", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Result", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"LSL", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"USL", None));
        self.logViewTabWidget.setTabText(self.logViewTabWidget.indexOf(self.testResultTab), QCoreApplication.translate("Form", u"Test Result", None))
        self.logViewTabWidget.setTabText(self.logViewTabWidget.indexOf(self.serialTab), QCoreApplication.translate("Form", u"Serial Log", None))
        self.logViewTabWidget.setTabText(self.logViewTabWidget.indexOf(self.stageTab), QCoreApplication.translate("Form", u"Stage Log", None))
        self.dutImageLabel.setText("")
    # retranslateUi

