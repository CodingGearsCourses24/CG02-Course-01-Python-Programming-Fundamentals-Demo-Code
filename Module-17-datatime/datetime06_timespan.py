# Working with dates
# Module: datetime


from datetime import date, time, datetime
from datetime import timedelta

vacation_duration = timedelta(days=21)
vacation_start_date = datetime(2020, 6, 20)
vacation_end_date = vacation_start_date + vacation_duration

width = 25
print("Vacation Start Date".ljust(width), ":", vacation_start_date)
print("Vacation End Date".ljust(width),  ":", vacation_end_date)

flight_duration = timedelta(days=1, hours=2, minutes=10)
flight_take_off = datetime(2020, 6, 20, 17, 30)
flight_landing_time = flight_take_off + flight_duration
print("flight_take_off".ljust(width), ":", flight_take_off)
print("flight_landing_time".ljust(width), ":", flight_landing_time)

print("-"*30)

seminar_start_time = datetime(2020, 7, 10, 9, 30)
seminar_end_time = datetime(2020, 7, 15, 10, 30)
seminar_duration = seminar_end_time - seminar_start_time

print(seminar_duration.days)
print(seminar_duration.seconds)
print(seminar_duration.microseconds)
print(seminar_duration.total_seconds())