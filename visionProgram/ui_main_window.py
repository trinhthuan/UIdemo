# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLineEdit,
    QPushButton, QScrollArea, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(355, 141)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(MainWindow)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.num_duts_input = QLineEdit(MainWindow)
        self.num_duts_input.setObjectName(u"num_duts_input")

        self.horizontalLayout.addWidget(self.num_duts_input)

        self.save_config_button = QPushButton(MainWindow)
        self.save_config_button.setObjectName(u"save_config_button")

        self.horizontalLayout.addWidget(self.save_config_button)

        self.restart_button = QPushButton(MainWindow)
        self.restart_button.setObjectName(u"restart_button")

        self.horizontalLayout.addWidget(self.restart_button)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.scroll_area = QScrollArea(MainWindow)
        self.scroll_area.setObjectName(u"scroll_area")
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area_widget_contents = QWidget()
        self.scroll_area_widget_contents.setObjectName(u"scroll_area_widget_contents")
        self.scroll_area_widget_contents.setGeometry(QRect(0, 0, 335, 85))
        self.grid_layout = QGridLayout(self.scroll_area_widget_contents)
        self.grid_layout.setObjectName(u"grid_layout")
        self.scroll_area.setWidget(self.scroll_area_widget_contents)

        self.verticalLayout.addWidget(self.scroll_area)


        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        self.num_duts_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Number of DUTs", None))
        self.save_config_button.setText(QCoreApplication.translate("MainWindow", u"Save Config", None))
        self.restart_button.setText(QCoreApplication.translate("MainWindow", u"Restart App", None))
        pass
    # retranslateUi

