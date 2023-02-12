"""
Name: Ahmad Shah Yawar
cmputer science studnet
2. Leap year
Write a function is_year_leap that takes 1 argument - the year, and returns True if the year is a leap year, and False otherwise.

"""
import msvcrt
yearnnum = int(input("enter the year number if it is leap year you will see ture if not you will see false: "))
def is_leap_year(yearnnum):
    if yearnnum % 400 == 0:
        return True
    if yearnnum % 100 == 0:
        return False
    if yearnnum % 4 == 0:
        return True
    else:
        return False
print(is_leap_year(yearnnum))
msvcrt.getch()
