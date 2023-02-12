"""
Name: Ahmad Shah Yawar
cmputer science studnet
5. Bank deposit
The user makes a deposit in the amount of a rubles for a period of years at 10% per annum
(each year the size of his deposit increases by 10%. This money is added to the deposit amount, and they will also have interest next year).
 Write a bank function that takes arguments a and years and returns the amount that will be in the user's account.

"""
import msvcrt

Acount_money = int(input("Enter the amount of money you want to invest: "))
ten_percentage_of_money = (Acount_money * 10) / 100
Amount_of_year = int(input("please enter the amount of year that you want your money to be in:  "))
print("your account money would be ", Acount_money + ten_percentage_of_money * Amount_of_year, "After ", Amount_of_year, "years")



msvcrt.getch()
