""""
Ahmad shah yawar
computer science class
5. Bank deposit
The user makes a deposit in the amount of a rubles for a period of years at 10% per annum
(each year the size of his deposit increases by 10%. This money is added to the deposit amount, and they will also have interest next year).
 Write a bank function that takes arguments a and years and returns the amount that will be in the user's account.

"""
import msvcrt
num = int(input("Enter the number please: "))
flag = False

if num > 1:
    for i in range(2, num):
        if(num % i) == 0:
            flag = True

            break
if flag:
    print("True")
else:
    print("False")



msvcrt.getch()