from msilib import Table
import os,sys,time,datetime,traceback
from re import S
# QT for python import
import PySide6
from PySide6.QtCore import QTimer, Slot, QThread, Signal, Qt,QTime,QDate
from PySide6.QtCore import QModelIndex
from PySide6.QtGui import QDoubleValidator, QIntValidator, QTextCursor,QAction
from PySide6.QtGui import QIcon,QAction,QPixmap,QPainter,QColor,QBrush
from PySide6.QtWidgets import QWidget, QPushButton, QStyle, QFileDialog, QApplication, QMainWindow, QGridLayout, \
    QMessageBox,QAbstractItemView
# QSql support
from PySide6.QtSql import QSqlDatabase,QSqlError,QSqlTableModel,QSqlDriver,QSqlField
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

class SQLCustomModel(QSqlTableModel):
	"""Customed QSqlTableModel
	"""
	def __init__(self,parent,db:QSqlDatabase):
		super(SQLCustomModel, self).__init__(parent,db)
		print(f'parent:{parent} db:{db}')
		#SQLCustomModel.__init__(self,parent,db)
		self.db=db
		self.parent=parent
		self.table_model=QSqlTableModel(self.parent,self.db)

	# override
	def data(self,idx:QModelIndex,role:int):
		if role== 8 and self.table_model.isDirty(idx):
			return QBrush(QColor(Qt.yellow))
		return self.table_model.data(idx,role)

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
		self.Select_date_btn.clicked.connect(self.get_input_date)
		self.__init__sqlconnection()
	
	# **************************************VerTicaL@zlm**************************************
	# start of  data input  part

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
	# end of  data input  part
	# **************************************VerTicaL@zlm**************************************


	# **************************************VerTicaL@zlm**************************************
	# start of SQL data part

	def __init__sqlconnection(self):
		self.dbconnect_N=0
		self.current_dbTable=''
		# show table data when db_table in treeView activated
		self.treeView.tableActivated_sig.connect(self.show_tabledata)


	@Slot()
	def on_Open_datebase_btn_clicked(self):
		"""open filedialog to connect to a SQLite database
		"""
		database_file,filetype=QFileDialog.getOpenFileName(self, "Open database file",os.getcwd(), "databasefile(*.db)")
		if database_file:
			print(f'get database file: {database_file}')
			self.Database_txt.setText(database_file)
			# connect database by SQLite driver
			qError=self.sqlite_connect(database_file)
			if qError.type() != QSqlError.NoError:
				self.msgbox=msg_box('open database failed',f'error while connecting to database{database_file}',qError.text())
				self.msgbox.show()
			else:
				# database connected refresh database in treeView
				self.treeView.refresh()
	
	def sqlite_connect(self, db_name:str,driver:str="QSQLITE"):
		"""connect to sqlite database

		Args:
			db_name (str): 
			driver (str, optional): driver name,Defaults to "QSQLITE".
		"""
		qerror=QSqlError()
		self.dbconnect_N+=1
		connection_name=f'DBconnect{self.dbconnect_N}'
		db=QSqlDatabase.addDatabase(driver,connection_name)
		db.setDatabaseName(db_name)

		# db is not open,reomve connection and return error
		if not db.open():
			qerror=db.lastError()
			db=QSqlDatabase()
			QSqlDatabase.removeDatabase(connection_name)
		return qerror
	
	@Slot(str)
	def show_tabledata(self,tableName:str):
		print(f'get table name:{tableName}')
		self.current_dbTable=tableName
		Table_model=SQLCustomModel(self.tableView,self.treeView.currentDatabase())
		#Table_model=QSqlTableModel(self.tableView,self.treeView.currentDatabase())
		print(f'current driver:{self.treeView.currentDatabase().driver().escapeIdentifier(tableName,QSqlDriver.TableName)}')

		Table_model.setTable(self.treeView.currentDatabase().driver().escapeIdentifier(tableName,QSqlDriver.TableName))
		Table_model.select()

		if Table_model.lastError().type()!=QSqlError.NoError:
			print(f'last error: {Table_model.lastError().text()}')

		Table_model.setEditStrategy(QSqlTableModel.OnRowChange)
		# set table model in table view
		self.tableView.setModel(Table_model)
		self.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)

	# end of SQL data  part	
	# **************************************VerTicaL@zlm**************************************

if __name__ == '__main__':
	app = QApplication(sys.argv)
	win = VieWDataCovid19SH()
	win.show()
	sys.exit(app.exec())
