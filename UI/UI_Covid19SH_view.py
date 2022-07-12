# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI_Covid19SH_view.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QTableView,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1000, 650)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(300, 40))
        self.lineEdit.setMaximumSize(QSize(16777215, 40))
        palette = QPalette()
        brush = QBrush(QColor(255, 85, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        brush1 = QBrush(QColor(0, 0, 0, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        brush2 = QBrush(QColor(120, 120, 120, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        self.lineEdit.setPalette(palette)
        font = QFont()
        font.setFamilies([u"Cambria"])
        font.setPointSize(12)
        font.setBold(True)
        self.lineEdit.setFont(font)
        self.lineEdit.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.lineEdit)

        self.tableView = QTableView(Dialog)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setMinimumSize(QSize(300, 400))

        self.verticalLayout_2.addWidget(self.tableView)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)

        self.Open_datebase_btn = QPushButton(Dialog)
        self.Open_datebase_btn.setObjectName(u"Open_datebase_btn")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Open_datebase_btn.sizePolicy().hasHeightForWidth())
        self.Open_datebase_btn.setSizePolicy(sizePolicy)
        self.Open_datebase_btn.setMinimumSize(QSize(120, 40))
        self.Open_datebase_btn.setMaximumSize(QSize(100, 40))
        self.Open_datebase_btn.setFont(font)
        self.Open_datebase_btn.setStyleSheet(u"QPushButton{background-color: rgb(0, 170, 127);selection-color: rgb(255, 85, 127);\n"
"color: rgb(255, 255, 255);}\n"
"\n"
"QPushButton:hover{background-color:rgb(0, 170, 255);}\n"
"\n"
"QPushButton:pressed{background-color:rgb(255, 91, 58);}")

        self.horizontalLayout_5.addWidget(self.Open_datebase_btn)

        self.Update_database__btn = QPushButton(Dialog)
        self.Update_database__btn.setObjectName(u"Update_database__btn")
        sizePolicy.setHeightForWidth(self.Update_database__btn.sizePolicy().hasHeightForWidth())
        self.Update_database__btn.setSizePolicy(sizePolicy)
        self.Update_database__btn.setMinimumSize(QSize(120, 40))
        self.Update_database__btn.setMaximumSize(QSize(100, 40))
        self.Update_database__btn.setFont(font)
        self.Update_database__btn.setStyleSheet(u"QPushButton{background-color: rgb(0, 170, 127);selection-color: rgb(255, 85, 127);\n"
"color: rgb(255, 255, 255);}\n"
"\n"
"QPushButton:hover{background-color:rgb(0, 170, 255);}\n"
"\n"
"QPushButton:pressed{background-color:rgb(255, 91, 58);}")

        self.horizontalLayout_5.addWidget(self.Update_database__btn)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)


        self.horizontalLayout_6.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMinimumSize(QSize(400, 40))
        self.label_6.setMaximumSize(QSize(500, 40))
        palette1 = QPalette()
        brush3 = QBrush(QColor(0, 170, 255, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        self.label_6.setPalette(palette1)
        font1 = QFont()
        font1.setFamilies([u"Cambria"])
        font1.setPointSize(14)
        font1.setBold(True)
        self.label_6.setFont(font1)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_6)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMinimumSize(QSize(100, 40))
        self.label_5.setMaximumSize(QSize(100, 40))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush3)
        brush4 = QBrush(QColor(0, 255, 255, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush4)
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        self.label_5.setPalette(palette2)
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(14)
        font2.setBold(True)
        self.label_5.setFont(font2)
        self.label_5.setFrameShape(QFrame.NoFrame)
        self.label_5.setFrameShadow(QFrame.Sunken)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_5)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QSize(100, 40))
        self.label_2.setMaximumSize(QSize(100, 40))
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush)
        palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette3.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        self.label_2.setPalette(palette3)
        self.label_2.setFont(font2)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QSize(100, 40))
        self.label_3.setMaximumSize(QSize(100, 40))
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette4.setBrush(QPalette.Active, QPalette.Text, brush)
        palette4.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette4.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette4.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette4.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        self.label_3.setPalette(palette4)
        self.label_3.setFont(font2)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_3)

        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QSize(100, 40))
        self.label_4.setMaximumSize(QSize(100, 40))
        palette5 = QPalette()
        palette5.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette5.setBrush(QPalette.Active, QPalette.Text, brush)
        palette5.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette5.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette5.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette5.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette5.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette5.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        self.label_4.setPalette(palette5)
        self.label_4.setFont(font2)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_4)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.Select_date_btn = QPushButton(Dialog)
        self.Select_date_btn.setObjectName(u"Select_date_btn")
        sizePolicy.setHeightForWidth(self.Select_date_btn.sizePolicy().hasHeightForWidth())
        self.Select_date_btn.setSizePolicy(sizePolicy)
        self.Select_date_btn.setMinimumSize(QSize(100, 40))
        self.Select_date_btn.setMaximumSize(QSize(100, 40))
        self.Select_date_btn.setFont(font)
        self.Select_date_btn.setStyleSheet(u"QPushButton{background-color: rgb(0, 170, 127);selection-color: rgb(255, 85, 127);\n"
"color: rgb(255, 255, 255);}\n"
"\n"
"QPushButton:hover{background-color:rgb(0, 170, 255);}\n"
"\n"
"QPushButton:pressed{background-color:rgb(255, 91, 58);}")

        self.horizontalLayout_2.addWidget(self.Select_date_btn)

        self.Infection_input = QLineEdit(Dialog)
        self.Infection_input.setObjectName(u"Infection_input")
        self.Infection_input.setMinimumSize(QSize(100, 40))
        self.Infection_input.setMaximumSize(QSize(100, 40))
        font3 = QFont()
        font3.setFamilies([u"Cambria Math"])
        font3.setPointSize(12)
        font3.setBold(False)
        self.Infection_input.setFont(font3)
        self.Infection_input.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.Infection_input)

        self.Asymptom_input = QLineEdit(Dialog)
        self.Asymptom_input.setObjectName(u"Asymptom_input")
        self.Asymptom_input.setMinimumSize(QSize(100, 40))
        self.Asymptom_input.setMaximumSize(QSize(100, 40))
        font4 = QFont()
        font4.setFamilies([u"Cambria Math"])
        font4.setPointSize(14)
        self.Asymptom_input.setFont(font4)
        self.Asymptom_input.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.Asymptom_input)

        self.Death_input = QLineEdit(Dialog)
        self.Death_input.setObjectName(u"Death_input")
        self.Death_input.setMinimumSize(QSize(100, 40))
        self.Death_input.setMaximumSize(QSize(100, 40))
        self.Death_input.setFont(font4)
        self.Death_input.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.Death_input)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer = QSpacerItem(188, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.Confirm_btn = QPushButton(Dialog)
        self.Confirm_btn.setObjectName(u"Confirm_btn")
        sizePolicy.setHeightForWidth(self.Confirm_btn.sizePolicy().hasHeightForWidth())
        self.Confirm_btn.setSizePolicy(sizePolicy)
        self.Confirm_btn.setMinimumSize(QSize(100, 40))
        self.Confirm_btn.setMaximumSize(QSize(100, 40))
        self.Confirm_btn.setFont(font)
        self.Confirm_btn.setStyleSheet(u"QPushButton{background-color: rgb(0, 170, 127);selection-color: rgb(255, 85, 127);\n"
"color: rgb(255, 255, 255);}\n"
"\n"
"QPushButton:hover{background-color:rgb(0, 170, 255);}\n"
"\n"
"QPushButton:pressed{background-color:rgb(255, 91, 58);}")

        self.horizontalLayout_3.addWidget(self.Confirm_btn)

        self.Cancel_btn = QPushButton(Dialog)
        self.Cancel_btn.setObjectName(u"Cancel_btn")
        sizePolicy.setHeightForWidth(self.Cancel_btn.sizePolicy().hasHeightForWidth())
        self.Cancel_btn.setSizePolicy(sizePolicy)
        self.Cancel_btn.setMinimumSize(QSize(100, 40))
        self.Cancel_btn.setMaximumSize(QSize(100, 40))
        self.Cancel_btn.setFont(font)
        self.Cancel_btn.setStyleSheet(u"QPushButton{background-color: rgb(0, 170, 127);selection-color: rgb(255, 85, 127);\n"
"color: rgb(255, 255, 255);}\n"
"\n"
"QPushButton:hover{background-color:rgb(0, 170, 255);}\n"
"\n"
"QPushButton:pressed{background-color:rgb(255, 91, 58);}")

        self.horizontalLayout_3.addWidget(self.Cancel_btn)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.Plot_frame = QFrame(Dialog)
        self.Plot_frame.setObjectName(u"Plot_frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Plot_frame.sizePolicy().hasHeightForWidth())
        self.Plot_frame.setSizePolicy(sizePolicy1)
        self.Plot_frame.setMinimumSize(QSize(400, 300))
        self.Plot_frame.setMaximumSize(QSize(500, 16777215))
        self.Plot_frame.setFrameShape(QFrame.StyledPanel)
        self.Plot_frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.Plot_frame)


        self.horizontalLayout_6.addLayout(self.verticalLayout)


        self.gridLayout.addLayout(self.horizontalLayout_6, 0, 0, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Dialog", u"Sqlite database file", None))
        self.Open_datebase_btn.setText(QCoreApplication.translate("Dialog", u"Open database", None))
        self.Update_database__btn.setText(QCoreApplication.translate("Dialog", u"Update&&Plot", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Input daily report", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Date", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Infection", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"asymptom", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Death", None))
        self.Select_date_btn.setText(QCoreApplication.translate("Dialog", u"Select Date", None))
        self.Infection_input.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.Asymptom_input.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.Death_input.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.Confirm_btn.setText(QCoreApplication.translate("Dialog", u"add", None))
        self.Cancel_btn.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
    # retranslateUi

