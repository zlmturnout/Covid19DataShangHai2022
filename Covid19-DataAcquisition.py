# coding=utf-8
import datetime
import os
import re
import sqlite3

import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup
# plot by matplotlib or plotnine
from plotnine import *

# import functions for data process among <pandas pd_data>||<dict_data>||<SQL_table>
from Dict_DataFrame_Sqlite import dict_to_DataFrame, create_path

"""
source url:http://m.sh.bendibao.com/mip/233243.html
datatable:

"""

header = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0'


def download(url, num_retries=2, user_agent=header, proxies=None):
    """ Download a given URL and return the page content
        args:
            url (str): URL
        kwargs:
            user_agent (str): user agent (default: wswp)
            proxies (dict): proxy dict w/ keys 'http' and 'https', values
                            are strs (i.e. 'http(s)://IP') (default: None)
            num_retries (int): # of retries if a 5xx error is seen (default: 2)
    """
    print('Downloading:', url)
    headers = {'User-Agent': user_agent}
    try:
        resp = requests.get(url, headers=headers, proxies=proxies)
        # encoding chinese by code UTF-8
        # print(resp.encoding)
        # resp.encoding='utf-8'
        resp.encoding = resp.apparent_encoding
        print('successful', resp)
        html = resp.text
        if resp.status_code >= 400:
            print('Download error:', resp.text)
            html = None
            if num_retries and 500 <= resp.status_code < 600:
                # recursively retry 5xx HTTP errors
                return download(url, num_retries - 1)
    except requests.exceptions.RequestException as e:
        print('Download error:', e)
        html = None
    else:
        if resp.text:
            os.makedirs('./html') if not os.path.isdir('./html') else print(os.path.abspath('./html'))
            html_name = ''.join(re.findall(r"[a-zA-Z0-9]", url)) + '.html'
            filename = os.path.join(os.path.abspath('./html'), html_name)
            print(filename)
            with open(filename, 'wb') as f:
                f.write(resp.text.encode())
    return html


"""
SH_COVID19_DATA structure
    SH_COVID19_DATA = {"Date":list[date], "NewInfection": list[int], "NewAsymptomatic": list[int], 
    "AllInfection": list[int], "AllAsymptomatic": list[int], "Death": list[int] }
    
"""
Example = {"Date": ["2022-05-11"], "NewInfection": [144], "NewAsymptomatic": [1305], "AllInfection": [56527],
           "AllAsymptomatic": [579553], "Death": [5]}


def get_Covid19Data_SH(local_url: str, dict_daily_data=None):
    """
    # get the Covid19_SH data from the table in the url
    ## SH_COVID19_DATA structure
    SH_COVID19_DATA:
        {"Date":list[date], "NewInfection": list[int], "NewAsymptomatic": list[int],
        "AllInfection": list[int], "AllAsymptomatic": list[int], "Death": list[int] }
    Example:
        {"Date":["2022-05-11"], "NewInfection": [144], "NewAsymptomatic": [1305], "AllInfection": [56527],
        "AllAsymptomatic": [579553],"Death": [5]}
    noted
    :param dict_data: Covid19Data in dict form
    :param url:2022-05-12 page: "http://m.sh.bendibao.com/mip/233243.html"
    :return: Covid19Data in dict form: dict_data
    """
    list_daily_data = []
    if dict_daily_data is None:
        dict_daily_data = {"Date": [], "NewInfection": [], "NewAsymptomatic": [],
                           "AllInfection": [], "AllAsymptomatic": [], "Death": []}
    today = str(datetime.datetime.now().strftime('%Y-%m-%d'))
    print(f'taday is {today}')
    # acquire html
    html_resp = download(local_url)
    assert html_resp, '数据获取错误'
    html_soup = BeautifulSoup(html_resp, 'html.parser')
    tr = html_soup.find('table').find_all('tr')  # 查找表格内所有内容
    table_info = tr[0].find_all('td')[0].text.replace('\t', '').replace('\n', '').split('\r')
    table_name = table_info[0]
    update_time = table_info[1]
    print(f'{table_name}-{update_time}')
    [the_date, local_source, new_cases, all_cases] = [item.text.strip() for item in tr[1].find_all('td')]
    print(the_date, local_source, new_cases, all_cases)
    # get everyday data by row even[2,4,6,...] and odd[3,5,7,...]
    # start from row 2 namely tr[2]
    table_row = tr[2:]
    all_daily_data = []
    for index, row_data in enumerate(table_row):
        # from evev rows get 日期-date 本土确诊-NewInfection 累计确诊-AllInfection
        # print(f'\nCovid-19 in ShangHai daily info:')
        if index % 2 == 0:
            cn_date = row_data.find_all('td')[0].text.strip('\n')
            # change to datetime string
            date = deal_cn_date(cn_date, 2022)  # add later
            NewInfection = int(row_data.find_all('td')[-2].text.replace('\n', '').replace('\r', ''))
            AllInfection = int(row_data.find_all('td')[-1].text.replace('\n', '').replace('\r', ''))
            # print(f'date: {date}, NewInfection: {NewInfection}, AllInfection: {AllInfection}')
            # from odd rows get 本土无症状-NewAsymptomatic 累计无症状-AllAsymptomatic
            NewAsymptomatic = int(table_row[index + 1].find_all('td')[-2].text.replace('\n', '').replace('\r', ''))
            AllAsymptomatic = int(table_row[index + 1].find_all('td')[-1].text.replace('\n', '').replace('\r', ''))
            # print(f'NewAsymptomatic: {NewAsymptomatic}, AllAsymptomatic: {AllAsymptomatic}')
            all_daily_data.append([date, NewInfection, AllInfection, NewAsymptomatic, AllAsymptomatic])
            # add to dict_daily_data
            dict_daily_data["Date"].append(date)
            dict_daily_data["NewInfection"].append(NewInfection)
            dict_daily_data["AllInfection"].append(AllInfection)
            dict_daily_data["NewAsymptomatic"].append(NewAsymptomatic)
            dict_daily_data["AllAsymptomatic"].append(AllAsymptomatic)
            dict_daily_data["Death"].append(0)  # no death data in this table
    return all_daily_data, dict_daily_data


def deal_cn_date(cn_date: str = '5月11日(0-24时)', year: int = 2022):
    """
    change '5月11日(0-24时)' to '2022-05-11'
    :param year: default 2022
    :param cn_date: '5月11日(0-24时)'
    :return: datetime.string
    """
    month = int(cn_date.split('月')[0])
    day = int(cn_date.split('月')[-1].split('日')[0])
    return datetime.date(year, month, day).strftime("%Y-%m-%d")


def create_Covid19_SH_sql(db_path, db_name: str = 'Covid19_SH_db.db', table_name='SH_COVID19_DATA'):
    """
    create a sqlite database to save all_daily_data into sql database
    :param table_name: default='SH_COVID19_DATA'
    :param db_path: path to database
    :param db_name: default='Covid19_SH_db.db'
    :return:
    """
    if not os.path.exists(db_path):
        db_path = os.getcwd()
    sql_db = os.path.join(db_path, db_name)
    cxn = sqlite3.connect(sql_db)
    cursor = cxn.cursor()
    sql_table = f'CREATE TABLE IF NOT EXISTS Fund{table_name} (ID integer primary key autoincrement,Date text UNIQUE,' \
                f'NewInfection integer,AllInfection integer,' \
                f'NewAsymptomatic integer,AllAsymptomatic integer,Death,integer) '
    try:
        cursor.execute(sql_table)
    except sqlite3.OperationalError as e:
        print(f'Create Table{table_name} failed')
        print(e)
        return False
    cxn.commit()
    cxn.close()
    return sql_db


def plot_Covid19_SH_data(pd_data: pd.DataFrame):
    """
    plot the SH_COVID19_DATA
    :param pd_data:
    :return:
    """
    pd_NewCases = pd_data.drop(columns=['Death', 'AllInfection', 'AllAsymptomatic'])
    melt_df = pd.melt(pd_NewCases, id_vars=['Date'], var_name='variable', value_name='value')
    area_fill_plot = (ggplot(melt_df, aes(x='Date', y='value', group='variable', color='variable'))
                      + geom_area(aes(fill='variable'), alpha=0.7, position='identity')
                      + geom_line(aes(color='variable'), size=0.75) +  # color='black',
                      scale_x_date(date_labels="%m-%d", date_breaks='5 days')
                      + scale_fill_hue(s=0.9, l=0.65, h=0.0617, color_space='husl') + xlab("2022ShangHai")
                      + ylab("Covid-19 Cases")) + theme(legend_position=(0.25, 0.75))
    print(area_fill_plot)


if __name__ == '__main__':
    url = "http://m.sh.bendibao.com/mip/233243.html"
    All_daily_data, Dict_daily_data = get_Covid19Data_SH(url)
    database_path = create_path(os.path.join(os.getcwd(), "save"))
    print(All_daily_data)
    print(Dict_daily_data)
    pd_data = dict_to_DataFrame(Dict_daily_data)

    # print(pd_data)
    pd_NewCases = pd_data.drop(columns=['Death', 'AllInfection', 'AllAsymptomatic', 'NewInfection'])
    print(pd_NewCases)
    # save data to sql and excel csv,json file
    # dict_to_SQLTable(Dict_daily_data,table_name="SH_COVID19_DATA",db_path=database_path,db_name="Covid19_SH_db.db")
    # save_pd_data(pd_data,database_path,"SH_COVID19_DATA")
    melt_df = pd.melt(pd_NewCases, id_vars=['Date'], var_name='variable', value_name='value')
    # base_plot = (ggplot(melt_df, aes(x='Date', y='value', group='variable', color='variable')) + geom_line(size=1)
    #              + scale_x_date(date_labels="%m-%d", date_breaks='5 days')
    #             + scale_fill_hue(s=0.9, l=0.65, h=0.0417, color_space='husl') + xlab("Date")+ylab("Cases"))
    # print(base_plot)
    # plot_Covid19_SH_data(pd_data)

    # calender plot
    df = pd.melt(pd_NewCases, id_vars=['Date'], var_name='variable', value_name='value')
    df['Date'] = [datetime.datetime.strptime(d, "%Y-%m-%d").date() for d in df['Date']]
    df['year'] = [d.year for d in df['Date']]
    df = df[df['year'] == 2022]
    df['month'] = [d.month for d in df['Date']]
    month_label = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    df['monthf'] = df['month'].replace(np.arange(1, 13, 1), month_label)
    from pandas.api.types import CategoricalDtype

    cat_dtype = CategoricalDtype(categories=month_label, ordered=True)
    df['monthf'] = df['monthf'].astype(cat_dtype)
    df['week'] = [int(d.strftime('%W')) for d in df['Date']]
    df['weekay'] = [int(d.strftime('%u')) for d in df['Date']]
    week_label = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    df['weekdayf'] = df['weekay'].replace(np.arange(1, 8, 1), week_label)
    catWeek_dtype = CategoricalDtype(categories=week_label, ordered=True)
    df['weekdayf'] = df['weekdayf'].astype(catWeek_dtype)
    df['day'] = [d.strftime('%d') for d in df['Date']]
    df['monthweek'] = df.groupby('monthf')['week'].apply(lambda x: x - x.min() + 1)
    base_plot = (ggplot(df, aes('weekdayf', 'monthweek', fill='value')) +
                 geom_tile(colour="white", size=0.1) +
                 scale_fill_cmap(cmap_name='OrRd', name='Asymptomatic') +
                 geom_text(aes(label='day'), size=8) +
                 facet_wrap('~monthf', nrow=1) +
                 scale_y_reverse() +
                 xlab("COVID-19 2022@ShangHai") + ylab("Week") +
                 theme(strip_text=element_text(size=11, face="plain", color="black"),
                       text=element_text(family="SimHei"),
                       axis_title=element_text(size=14, face="plain", color="deepskyblue"),
                       axis_text=element_text(size=8, face="plain", color="#E7298A"),
                       legend_position='left',
                       legend_background=element_blank(),
                       aspect_ratio=0.85,
                       figure_size=(8, 4),
                       dpi=100))

    print(base_plot)
    print('get data done')
