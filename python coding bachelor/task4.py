""""""""""
task 4.
4. Seasons
Write a season function that takes 1 argument - the number of the month (from 1 to 12) and returns the time of year to 
which this month belongs (winter, spring, summer, or autumn).
"""""
import msvcrt
Month_Numbuer = int(input(" Enther the month number and I will tell you the season: "))

if Month_Numbuer <= 3 and Month_Numbuer >= 1:
    print("spring")
elif  Month_Numbuer <= 6 and  Month_Numbuer >= 4 :
    print("summer")
elif Month_Numbuer <= 9 and Month_Numbuer > 6 :
    print("autumn")
elif Month_Numbuer <= 12 and Month_Numbuer > 9 :
    print("winter")
else:
    print("wrong number")

msvcrt.getch()