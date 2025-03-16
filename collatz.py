# Weekly Task 04
# Author Vanessa Lyra

#Write a program, called collatz.py, that asks the user to input any positive integer and outputs the successive values of the following calculation.
#At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one.
#Have the program end if the current value is one.

print("Please enter a positive integer")
my_integer = 15

while my_integer != 1:
    if (my_integer % 2) == 0:
        my_integer = my_integer // 2
    else:
        my_integer = 3 * my_integer + 1
    print (my_integer)

    #Source even and odd numbers: https://www.toppr.com/guides/python-guide/examples/python-examples/python-program-to-check-if-a-number-is-odd-or-even/#:~:text=num%20%3D%20int%20(input%20(%E2%80%9C,even%3A%20887%20887%20is%20odd.