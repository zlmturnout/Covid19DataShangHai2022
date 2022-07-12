import os,sys,time,datetime,traceback
from this import s
# QT for python import
import PySide6
from PySide6.QtCore import QTimer, Slot, QThread, Signal, Qt,QTime,QDate
from PySide6.QtGui import QDoubleValidator, QIntValidator, QTextCursor,QAction
from PySide6.QtGui import QIcon,QAction,QPixmap,QPainter,QColor
from PySide6.QtWidgets import QWidget, QPushButton, QStyle, QFileDialog, QApplication, QMainWindow, QGridLayout, \
    QMessageBox
# data process
import sqlite3
import numpy as np
import pandas as pd
# UI import
from UI.UI_select_calendar import Ui_Form
from UI.UI_Covid19SH_view import Ui_Dialog

class RunQThread(QThread):
    """
    run any time consuming operation of func(*args,**kwargs)
    :argument can provide keyword args <timeout:float=1000.0>ms
    :return the signal will send function's return value in list form (return=funcs())
    Notice: if run exception occurs,will emit the <Exception info>
    """
    run_sig = Signal(list)

    def __init__(self, func, *args, timeout: float = 1000.0, **kwargs):
        super(RunQThread, self).__init__()
        self.args = args
        self.kwargs = kwargs
        self.run_flag = True
        self.run_time = timeout
        self.func = func
        self.result = None

    def run(self):
        t0 = time.time()
        print('QThread start')
        while self.run_flag and time.time() - t0 < self.run_time:
            try:
                self.result = self.func(*self.args, **self.kwargs)
            except Exception as e:
                # print(e)
                error_info = traceback.format_exc() + str(e) + '\n'
                self.run_sig.emit([error_info])
            else:
                self.run_flag = False
                self.run_sig.emit([self.result])

    def __del__(self):
        self.run_time = False


def msg_box(title, text, details):
    msg_box = QMessageBox()
    msg_box.setWindowTitle(title)
    msg_box.setText(text)
    msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
    msg_box.setDetailedText(details)
    close_event = msg_box.exec_()
    if close_event == QMessageBox.Yes:
        return 1
    else:
        return 0


class SelectDate(QWidget, Ui_Form):
    """
        select date from calendar in frameless window and return
    """
    date_sig = Signal(str)

    def __init__(self):
        super(SelectDate, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Select date')
        now = QDate.currentDate()
        self.Calendar.setSelectedDate(now.addDays(-1))
        self.Calendar.setMinimumDate(QDate(2022,3,1))
        self.Calendar.setMaximumDate(now)
        self.Calendar.setGridVisible(True)
        self.Calendar.clicked.connect(self.date_selected)
        self.setWindowFlags(Qt.FramelessWindowHint)

    def date_selected(self):
        date = self.Calendar.selectedDate().toString(Qt.ISODate)
        #print(date)
        self.Show_date.setText(date)

    @Slot()
    def on_Confirm_date_btn_clicked(self):
        sel_date = self.Calendar.selectedDate().toString(Qt.ISODate)
        print(sel_date)
        self.date_sig.emit(sel_date)
        self.close()

class VieWDataCovid19SH(QWidget,Ui_Dialog):
	"""View Covid19 data in ShangHai@2022

	data start from 2022-03-01
	"""
	def __init__(self, *args, **kwargs):
		super(VieWDataCovid19SH, self).__init__()
		self.setupUi(self)
		self.setWindowTitle("ViewCovid19data-ShangHai@2022")
		self.Covid19Data=pd.DataFrame()
		self.__init__connections()
	
	def __init__connections(self):
		self.Select_date_btn.clicked.connect(self.get_input_date)

	@Slot()
	def get_input_date(self):
		self.start_calender = SelectDate()
		self.start_calender.show()
		self.start_calender.date_sig.connect(self.set_update_date)
	
	@Slot(str)
	def set_update_date(self, date: str):
        # print(f'get date:{date}')
		self.update_date = date
		self.Select_date_btn.setText(date)

if __name__ == '__main__':
	app = QApplication(sys.argv)
	win = VieWDataCovid19SH()
	win.show()
	sys.exit(app.exec())
