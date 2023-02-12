"""
Name: Ahmad Shah Yawar
cmputer science studnet
task.1 The simplest arithmetic operations.
Write an arithmetic function that takes 3 arguments: the first 2 are numbers, the third is the operation to be performed
 on them. If the third argument is +, add them up; if -, then subtract; * - multiply; / - divide (first to second).
  Otherwise, return the string "Unknown operation".
"""
import msvcrt
Num1 = input("enter first number: ")
Operation = input("enter operation: ")
Num2 = input("enter second number: ")
if (Operation == "+"):
    print(int(Num1) + int(Num2))
elif(Operation == "-"):
    print(int(Num1) - int(Num2))
elif(Operation == "*"):
    print(int(Num1) * int(Num2))
elif(Operation == "/"):
    print(int(Num1) / int(Num2))
else:
    print("Unkown Operation")

msvcrt.getch()