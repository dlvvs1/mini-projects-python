import datetime as dt

def is_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def month_days(month, leap_year):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2 and leap_year:
        return 29
    elif month == 2 and (not leap_year):
        return 28

print("Welcome to the Age Calculator!")
name = input("Please enter your name: ")
dob_input = input("Please enter your date of birth (YYYY-MM-DD): ")
time = input("Please enter your time of birth (HH:MM:SS): ")

print(f"Hello {name}!")

try:
    dob_object = dt.datetime.strptime(dob_input, "%Y-%m-%d")
    # print(f"Your date of birth is {dob_input}")
    print(f"Your formatted date of birth is: {dob_object.strftime('%B %d, %Y')}")
except ValueError:
    print("Invalid date format! Please use YYYY-MM-DD (e.g., 1995-05-15)")

try:
    time_object = dt.datetime.strptime(time, "%H:%M:%S")
    print(f"Time: {time_object.strftime('%I : %M : %S %p')}")
except ValueError:
    print("Invalid time format! Please use HH:MM:SS (e.g., 14:30:00)")  

birth_year = dob_object.year
birth_month = dob_object.month
birth_day = dob_object.day

birth_hour = time_object.hour
birth_minute = time_object.minute
birth_second = time_object.second

now = dt.datetime.now()

year = now.year
month = now.month
day = now.day

hour = now.hour
minute = now.minute
second = now.second


age_second = second - birth_second
if age_second < 0:
    age_second += 60
    minute -= 1


age_minute = minute - birth_minute
if age_minute < 0:
    age_minute += 60
    hour -= 1

age_hour = hour - birth_hour
if age_hour < 0:
    age_hour += 24
    day -= 1


leap = is_leap(year)
age_day = day - birth_day
if age_day < 0:
    month -= 1

    if month == 0:
        month = 12
        year -= 1

    leap = is_leap(year)
    age_day += month_days(month, leap)


age_month = month - birth_month
if age_month < 0:
    age_month += 12
    year -= 1
current_month = age_month

current_age = year - birth_year
# age_year = year - birth_year

print(f"You are {current_age} years, {current_month} months, and {age_day} days and {age_hour} hours and {age_minute} minutes and {age_second} seconds old.")
print(f"Your age in months is: {current_age * 12 + current_month}")

birth_datetime = dt.datetime(
    birth_year,
    birth_month,
    birth_day,
    birth_hour,
    birth_minute,
    birth_second
)

difference = now - birth_datetime

print("Exact total days:", difference.days)
print("Exact total seconds:", difference.total_seconds())
total_seconds = int(difference.total_seconds())
total_hours = int(total_seconds // 3600)
total_minutes = int(total_seconds // 60)