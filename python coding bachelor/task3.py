""""""""""
taks 3.
3. Square
Write a function square that takes 1 argument, the side of the square, and returns 3 values (using a tuple):
 the perimeter of the square, the area of the square, and the diagonal of the square.
"""""
import math
import msvcrt
Side_of_square = int(input("enter one side of a square: "))
Area = Side_of_square ** 2
primeter = Side_of_square * 4
diagonal = math.isqrt(2 * Area)

print("Area of square is eqaul to: ", Area)
print("Primeter of square is eqaul to: ", primeter)
print("diagonal of square is equal to: ", diagonal)
msvcrt.getch()