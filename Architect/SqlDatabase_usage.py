# coding=utf-8
from calendar import c
from email import header
from re import T
import sys,requests,os
from tkinter import INSERT
from numpy import insert

from matplotlib.pyplot import get, table
import random, json
import time, datetime
import pandas as pd
import sqlite3


"""
This is the library of SQL CMD for python
"""
table_name = 'SH_COVID19_DATA'
date = '2021-06-18'
insert_record = []
start_date='2022-05-16'
end_date='2022-07-01'

# find and list all tables
sql_find_tables = f"SELECT count(name) FROM sqlite_master WHERE type= 'table' AND name='{table_name}'"
sql_list_tables = "SELECT name FROM sqlite_master WHERE type= 'table' order by name"

# find table info
sql_table_info = f"PRAGMA table_info({table_name})"
# create table
sql_create_table = f'CREATE TABLE IF NOT EXISTS {table_name} (ID integer primary key autoincrement,Date text UNIQUE,' \
                   f'Fund_value numeric,' \
                   f'Value_accumulate numeric,Rate_by_day numeric) '
# insert data
sql_insert_data = f'INSERT or REPLACE INTO {table_name} (Date,Fund_value,Value_accumulate,Rate_by_day) ' \
                  f'VALUES {insert_record} '
# find a record by date
sql_find_record = f"SELECT * From {table_name} WHERE Date='{date}'"

# find records by date range
sql_range_record = f"SELECT * From {table_name} WHERE Date between '{start_date}' and '{end_date}'"

"""
                     database format 
Table_name:SH_COVID19_DATA
    id        Date  NewInfection  NewAsymptomatic  AllInfection  AllAsymptomatic  Death
0    2  2022-06-30             0                0         58137           591518      0
1    3  2022-06-29             0                0         58137           591518      0
2    4  2022-06-28             0                0         58137           591518      0
3    5  2022-06-27             0                0         58137           591518      0
4    6  2022-06-26             2                2         58137           591518      0
5    7  2022-06-25             0                0         58135           591516      0
6    8  2022-06-24             0                0         58135           591516      0
7    9  2022-06-23             2                1         58135           591516      0
"""

def sql_query(query_cmd:str,table_name:str='SH_COVID19_DATA',db_path:str=os.getcwd(), db_name: str = 'Covid19_SH_db.db'):
    """perform one qurey cmd 
    and return the fected results
    Args:
        query (_type_): sql query cmd
        table_name (str, optional): Defaults to 'SH_COVID19_DATA'.
        db_path (str, optional):  Defaults to os.getcwd().
        db_name (str, optional): Defaults to 'Covid19_SH_db.db'.
    """
    database = os.path.join(db_path, db_name)
    # connect data base
    resp = []
    try:
        cxn = sqlite3.connect(database)
        cursor = cxn.cursor()
        cursor.execute(query_cmd)
        resp = cursor.fetchall()
        # find or not
        if not resp:
            print(f'cannot find any records of {table_name} at {date}')
        else:
            print(f'find record: {resp}')
        cxn.close()
    except sqlite3.OperationalError as e:
        print(e)
    return resp

def get_one_day_record(date, table_name:str='SH_COVID19_DATA',db_path:str=os.getcwd(), db_name: str = 'Covid19_SH_db.db'):
    """
    Acquire the fund info of one day from the fund database
    :param table_name: etc 'SH_COVID19_DATA'
    :param date: etc '2022-06-18'
    :param db_path: working path of the database file
    :param db_name: name of the database
    :return:[list]
    """
    print(f'table_name: {table_name} at date: {date}')
    database = os.path.join(db_path, db_name)
    # connect data base
    resp = []
    try:
        cxn = sqlite3.connect(database)
        cursor = cxn.cursor()
        sql_find_record = f"SELECT * From {table_name} WHERE Date='{date}'"
        cursor.execute(sql_find_record)
        resp = cursor.fetchall()
        # find or not
        if not resp:
            print(f'cannot find any records of {table_name} at {date}')
        else:
            print(f'find record: {resp}')
        cxn.close()
    except sqlite3.OperationalError as e:
        print(e)
    return resp

def get_latest_record(table_name:str='SH_COVID19_DATA',db_path:str=os.getcwd(), db_name: str = 'fund_db.db'):
    """
    get the latest record of this fund code from  database
    :param fund_code:
    :param db_path:
    :param db_name:
    :return: ('2021-06-18', 1.748, 2.245, 0.0133)
    """
    database = os.path.join(db_path, db_name)
    # resp from sql operation
    resp = []
    record_latest = []
    try:
        # connect data base
        cxn = sqlite3.connect(database)
        cursor = cxn.cursor()
        sql_find_date = f"SELECT Date From {table_name}"
        cursor.execute(sql_find_date)
        date_all = cursor.fetchall()
        date_list = [date[0] for date in date_all]
        #print(date_list)
        date_latest = latest_date(date_list)
        record_latest = get_one_day_record(date_latest,table_name, db_path, db_name)
        cxn.close()
        # sql_find_lasted_record=
    except sqlite3.OperationalError as e:
        print(e)
    return record_latest

def latest_date(date_list: list):
    """
    find the latest date in the date_list
    :param date_list: ['2011-06-18','2020-08-28','2011-11-02']
    :return:
    """
    max_date_index = 0
    date_max = datetime.datetime.strptime('1970-01-01', '%Y-%m-%d')
    for index, day in enumerate(date_list):
        date = datetime.datetime.strptime(day, '%Y-%m-%d')
        if date > date_max:
            date_max = date
            max_date_index = index
        else:
            pass
    return date_list[max_date_index]

def get_date_range_record(start_date, end_date, table_name:str='SH_COVID19_DATA',db_path:str=os.getcwd(), db_name: str = 'fund_db.db'):
    """
    get the record from start date to end date
    :param fund_code:
    :param start_date: str='2022-06-01'
    :param end_date: str='2022-07-01'
    :param db_path:os.getcwd()
    :param db_name:
    :return:
    """
    database = os.path.join(db_path, db_name)
    resp = []
    pd_data = pd.DataFrame()
    # connect data base
    try:
        cxn = sqlite3.connect(database)
        sql_range_record = f"SELECT * From {table_name} WHERE Date>'" \
                           f"{start_date}'and Date<'{end_date}' "
        pd_data = pd.read_sql(sql=sql_range_record, con=cxn)
        if pd_data.empty:
            print(f'cannot find any tables name{table_name} in:{database} ')
        else:
            print(f'find record,will return')
        cxn.close()
    except sqlite3.OperationalError as e:
        print(e)
    return pd_data

def get_db_table_headers(table_name,db_path,db_name)->list:
    """get all the table headers for a given table name

    Args:
        table_name (str): specific one table name
        db_path (str): database path default=os.getcwd()
        db_name (str): database name
    Returns:
        [list]:list of all table headers
    """
    if not os.path.exists(db_path):
        db_path = os.getcwd()
    sql_db = os.path.join(db_path, db_name)
    table_headers=[]
    try:
        cxn = sqlite3.connect(sql_db)
        # cursor = cxn.cursor()
    except Exception as e:
        print(e)
    else:
        sql_table_info = f"PRAGMA table_info({table_name})"
        cursor = cxn.cursor()
        cursor.execute(sql_table_info)
        resp = cursor.fetchall()
        # find or not
        if not resp:
            print(f'cannot find any table with name of {table_name}')
        else:
            print(f'find record: {resp}')
            for each_header in resp:
                table_headers.append(each_header[1])
        cxn.commit()
        cxn.close()
    return table_headers

def insert_one_record(insert_record:tuple,table_name,db_path, db_name):
    """insert one record
    insert data should be a tuple with values match the table headers
    Args:
        insert_record (tuple): like (0,'2022-05-12', 227, 1869, 56754, 581422, 0)
        table_name (str): specific one table name
        db_path (str): database path default=os.getcwd()
        db_name (str): database name
    Returns:
        bool: True if success else False
    """
    if not os.path.exists(db_path):
        db_path = os.getcwd()
    sql_db = os.path.join(db_path, db_name)
    table_headers=get_db_table_headers(table_name,db_path,db_name)[1:] # primary id not included
    if not table_headers and not insert_record: 
        return False
    insert_date=insert_record[1] # insert record like
    print(f'insert date: {insert_date}')
    # check if insert date is already in the table
    check_resp=get_one_day_record(insert_date,table_name,db_path,db_name)
    if check_resp:
        print(f'instert record already in table\n insert_record:{insert_record} '\
            f'\ninside table:{check_resp}')
        return False
    try:
        cxn = sqlite3.connect(sql_db)
        cursor = cxn.cursor()
        sql_insert_data=f'INSERT or REPLACE INTO {table_name} {tuple(table_headers)}' \
                  f'VALUES {insert_record} '
        print(sql_insert_data)
        cursor.execute(sql_insert_data)
    except Exception as e:
        print(e)
        return False
    else:
        cxn.commit()
        cxn.close()
        return True



if __name__ == '__main__':
    usr_name = os.getlogin()
    #path = os.path.join(os.getcwd(), 'save')
    path = os.getcwd()
    print(f'currentPath: {path}')
    db_name = 'Covid19_SH_db.db'
    table_name = 'SH_COVID19_DATA'
    date = '2022-05-01'
    result = get_one_day_record(date,table_name, path, db_name)
    latest_record = get_latest_record(table_name,path, db_name)
    print(f'table_name:{table_name},\n latesd record: \n{latest_record}')
    # date_range_record=get_date_range_record(start_date,end_date, table_name,path, db_name)
    # print(f'date range:\n{date_range_record}')
    # insert one record
    insert_record=(0,'2022-05-12', 227, 1869, 56754, 581422, 0)
    insert_one_record(insert_record,table_name,path,db_name)
    # get table info from database
    sql_table_info = f"PRAGMA table_info({table_name})"
    table_info=sql_query(sql_table_info,table_name,path,db_name)
    print(f'table:{table_name},\n latesd tabletable_info:\n{table_info}')
    # get table headers
    # table_headers=get_db_table_headers(table_name,path,db_name)
    # print(f'table_headers:{table_headers} \nat table {table_name}')