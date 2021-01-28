# Working with dates
# Module: datatime

"""
%d - Day
%m - Month
%y - YY Year
%Y - YYYY Year
%H - Hour (24hr format)
%M - Minute
%S - Second
"""
from datetime import date, time, datetime

date_today = date.today()

print(date_today)
print(date_today.strftime("%Y/%m/%d"))
print(date_today.strftime("%m/%d/%y"))