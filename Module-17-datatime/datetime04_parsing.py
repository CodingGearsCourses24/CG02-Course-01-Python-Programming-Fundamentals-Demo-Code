# Working with dates
# Module: datetime

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

dt_string1 = "12-04/2001"
dt_string2 = "12/2001/04"
dt_string3 = "01-04-12"
dt_string4 = "2001-04-12 10:30:25"

my_date_from_dt_string1 = datetime.strptime(dt_string1,"%m-%d/%Y")
print(my_date_from_dt_string1)
my_date_from_dt_string2 = datetime.strptime(dt_string2,"%m/%Y/%d")
print(my_date_from_dt_string2)
my_date_from_dt_string3 = datetime.strptime(dt_string3,"%y-%d-%m")
print(my_date_from_dt_string3)
my_date_from_dt_string4 = datetime.strptime(dt_string4, "%Y-%d-%m %H:%M:%S")
print(my_date_from_dt_string4)

print(type(my_date_from_dt_string4))