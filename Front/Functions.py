# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 20:44:54 2023

@author: chang
"""

import pandas as pd
import sqlite3
from datetime import date
from icalendar import Calendar, Event
import requests
from pandas.tseries.offsets import BDay
import datetime
import pytz

def isHolidays(date):
    url = "https://www.officeholidays.com/ics-clean/indonesia"
    gcal = Calendar.from_ical(requests.get(url).text)
    temp = []
    for component in gcal.walk():
        if component.name == "VEVENT":
            temp.append({
                'Name': component.get('summary'),
                'Start': str(component.get('DTSTART').dt)
            })
            
    holidays = pd.DataFrame(temp)
    if date in holidays['Start'].values:
        return True
    else:
        return False
    
def isWeekend(date):
    if datetime.datetime.strptime(
    date, '%Y-%m-%d').weekday() > 4:
        return True
    else:
        return False

def shiftDate(date):
    curYear = datetime.datetime.now().strftime("%Y")
    shift = 0
    year_date = str(curYear) + "-" + date
    while isHolidays(year_date) or isWeekend(year_date):
        shift += 1
        temp_sub = str((datetime.datetime.strptime(year_date, '%Y-%m-%d') - datetime.timedelta(days = shift)).date())
        temp_add = str((datetime.datetime.strptime(year_date, '%Y-%m-%d') + datetime.timedelta(days = shift)).date())
        if isHolidays(temp_sub) == False or isWeekend(temp_sub) == False:
            year_date = temp_sub
        elif isHolidays(temp_add) == False or isWeekend(temp_add) == False:
            year_date = temp_add
    return year_date

def createUser(userid, username, password):
    """function to create user, need to input 
    userid: text
    username: text
    password: text
    """
    conn = sqlite3.connect('pelitaAirDB')
    c = conn.cursor()
    insert = 'INSERT INTO Users Values (?,?,?,"user")'
    conn.executemany(insert, [(userid, username, password)])
    conn.commit()
    # you also need to close  the connection
    conn.close() 

def yearlyRun(data):
    """function to shift date and save old data to csv"""
    #Connect to database
    conn = sqlite3.connect('pelitaAirDB')
    table_name = "Schedule"
    #Save old data as CSV
    try:
        a = conn.execute(f'SELECT * FROM {table_name}')
        results = a.fetchall()
        old_data = pd.DataFrame(results)
        old_data.columns = ["Activity", "SKH", "Type", "Date", "base", "year_date", "execution_date"]
        curYear = datetime.datetime.now().strftime("%Y")
        old_data.to_csv('../data/{}.csv'.format(str(curYear)))
    except:
        #First time running function, need to create table first
        print("Creating Table")
    #Shift Date
    data['year_date'] = data['Date'].apply(shiftDate)
    #add execution_date
    data['execution_date'] = None
    #create schedule table if not exists, if exists then replace
    query = f'Create table if not Exists {table_name} (Activity text, SKH text, Type text, Date text, base text, year_date text, execution_date text)'
    conn.execute(query)
    data.to_sql(table_name,conn,if_exists='replace',index=False)
    conn.commit()
    conn.close()

def updateSchedule(activity, SKH, Type, year_date, base, exc_date):
    """update schedule to done"""
    conn = sqlite3.connect('pelitaAirDB')
    table_name = "Schedule"
    a = conn.execute(f'UPDATE {table_name} SET execution_date = "{exc_date}" WHERE activity = "{activity}" AND SKH = "{SKH}" AND Type = "{Type}" AND year_date = "{year_date}" AND base = "{base}"')
    conn.commit()
    conn.close()