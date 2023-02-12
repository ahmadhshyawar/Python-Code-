""""
Ahmad shah Yawar
Task 7
7. Correct date
Write a date function that takes 3 arguments - day, month and year.
 Return True if such a date is in our calendar, and False otherwise.

"""


import msvcrt

day = int(input("please enter the day: "))
month = int(input("please enter the month: "))
year = int(input("please enter the year: "))
is_year = True
if day <= 30 and 0 < day and month <= 12 and month > 0 and year > 0:
    is_year = True
else:
    is_year = False
print(is_year)

msvcrt.getch()