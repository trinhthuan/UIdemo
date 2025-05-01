# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dut_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_DUTWidget(object):
    def setupUi(self, DUTWidget):
        if not DUTWidget.objectName():
            DUTWidget.setObjectName(u"DUTWidget")
        self.verticalLayout = QVBoxLayout(DUTWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.title_label = QLabel(DUTWidget)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.title_label)

        self.image_label = QLabel(DUTWidget)
        self.image_label.setObjectName(u"image_label")
        self.image_label.setMinimumSize(QSize(320, 240))

        self.verticalLayout.addWidget(self.image_label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.start_button = QPushButton(DUTWidget)
        self.start_button.setObjectName(u"start_button")

        self.horizontalLayout.addWidget(self.start_button)

        self.stop_button = QPushButton(DUTWidget)
        self.stop_button.setObjectName(u"stop_button")

        self.horizontalLayout.addWidget(self.stop_button)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.status_label = QLabel(DUTWidget)
        self.status_label.setObjectName(u"status_label")
        self.status_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.status_label)


        self.retranslateUi(DUTWidget)

        QMetaObject.connectSlotsByName(DUTWidget)
    # setupUi

    def retranslateUi(self, DUTWidget):
        self.title_label.setText(QCoreApplication.translate("DUTWidget", u"DUT Name", None))
        self.title_label.setStyleSheet(QCoreApplication.translate("DUTWidget", u"font-weight: bold; font-size: 16px;", None))
        self.image_label.setStyleSheet(QCoreApplication.translate("DUTWidget", u"background-color: black;", None))
        self.start_button.setText(QCoreApplication.translate("DUTWidget", u"Start Camera", None))
        self.stop_button.setText(QCoreApplication.translate("DUTWidget", u"Stop Camera", None))
        self.status_label.setText(QCoreApplication.translate("DUTWidget", u"Status: Idle", None))
        pass
    # retranslateUi

