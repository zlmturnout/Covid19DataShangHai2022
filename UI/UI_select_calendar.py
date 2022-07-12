# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI_select_calendar.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
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
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QGridLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(685, 474)
        self.gridLayout_2 = QGridLayout(Form)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.Show_date = QLabel(Form)
        self.Show_date.setObjectName(u"Show_date")
        self.Show_date.setMinimumSize(QSize(120, 30))
        palette = QPalette()
        brush = QBrush(QColor(0, 170, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(255, 85, 0, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush1)
        brush2 = QBrush(QColor(0, 255, 255, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        brush3 = QBrush(QColor(255, 85, 0, 128))
        brush3.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush3)
#endif
        brush4 = QBrush(QColor(0, 0, 0, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush4)
        brush5 = QBrush(QColor(0, 0, 0, 128))
        brush5.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush5)
#endif
        brush6 = QBrush(QColor(120, 120, 120, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush5)
#endif
        self.Show_date.setPalette(palette)
        font = QFont()
        font.setFamilies([u"Cambria"])
        font.setPointSize(14)
        font.setBold(True)
        self.Show_date.setFont(font)
        self.Show_date.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.Show_date, 0, 0, 1, 2)

        self.Calendar = QCalendarWidget(Form)
        self.Calendar.setObjectName(u"Calendar")

        self.gridLayout.addWidget(self.Calendar, 1, 0, 1, 2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 2, 0, 1, 1)

        self.Confirm_date_btn = QPushButton(Form)
        self.Confirm_date_btn.setObjectName(u"Confirm_date_btn")
        self.Confirm_date_btn.setMinimumSize(QSize(100, 40))
        palette1 = QPalette()
        brush7 = QBrush(QColor(255, 255, 255, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush7)
        brush8 = QBrush(QColor(0, 170, 127, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush8)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush7)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush7)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush8)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush8)
        brush9 = QBrush(QColor(255, 85, 127, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.HighlightedText, brush9)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush7)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush7)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush8)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush7)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush7)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush8)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush8)
        palette1.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush9)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush7)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush7)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush8)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush7)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush7)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush8)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush8)
        palette1.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush9)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush7)
#endif
        self.Confirm_date_btn.setPalette(palette1)
        self.Confirm_date_btn.setFont(font)
        self.Confirm_date_btn.setStyleSheet(u"QPushButton{background-color: rgb(0, 170, 127);selection-color: rgb(255, 85, 127);\n"
"color: rgb(255, 255, 255);}\n"
"\n"
"QPushButton:hover{background-color:rgb(0, 170, 255);}\n"
"\n"
"QPushButton:pressed{background-color:rgb(255, 91, 58);}")

        self.gridLayout.addWidget(self.Confirm_date_btn, 2, 1, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.Show_date.setText(QCoreApplication.translate("Form", u"Select date", None))
        self.Confirm_date_btn.setText(QCoreApplication.translate("Form", u"Confirm", None))
    # retranslateUi

