**Programming and scripting Weekly Tasks**

_Author Vanessa Lyra_

**Weekly Task 2** - bank.py

First, I used 'input()' function to prompt the message to the user and stored both values as integers in two different variables: 'amount1' and 'amount2' and printed both values back to the user.
Both values were then summed up and divided by 100 to transform the value from cent to Euro, new value in Euro stored in variable 'new_amount'.

GeeksforGeeks, was my source to print out the last statement containing the total value in Euro, I have added F-string to format the text and be able to call my variable 'new_amount' and add decimal places using '{.2f}'
_https://www.geeksforgeeks.org/formatted-string-literals-f-strings-python/_
_https://www.geeksforgeeks.org/how-to-get-two-decimal-places-in-python/_


**Weekly Task 3** - accounts.py

In task 3, I also used 'input()' function to prompt both messages to the user and stored the account numbers as string stored in variables: 'account_number' and 'account_number2'.

To print the last 4 digits of each account number I have used array slicing:
- 10 digits account number: as the first array value is always index 0, I've used [6:10], prints values from index 6 to index 9, the second value in array slicing is not included.

- Numbers of any length: Slicing [-4:], the negative value tells Python to work from the end of the array. Python prints the last four values of the array.
  

**Weekly Task 4** - collatz.py
Again 'input()' function to prompt the message to the user and store values as integers in variable 'my_integer'.
In this program, I used a 'while' loop to run the program while the integer value is not 1. 

A subsequent if/else employed:
If statement will find even numbers: I've used modulus '% 2 == 0', the program divides my integer by 2  and gives me the remainder, if remainder is equal to 0, the number is positive and it is divided by 2.
Else statement: if integer is not even, multiply it by three and add one.
The program will print each value until integer is 1.

I have based my even and odd calculations from Toppr Python guides
_https://www.toppr.com/guides/python-guide/examples/python-examples/python-program-to-check-if-a-number-is-odd-or-even/#:~:text=num%20%3D%20int%20(input%20(%E2%80%9C,even%3A%20887%20887%20is%20odd._

**Weekly Task 5** - weekday.py  M
In task 5, I've imported datetime library, the library which manipulates dates in Python and retrieved today's by calling function datetime.datetime.today().
Each day of the week is an interger, 0 - 4 Monday to Thursday and 5 - 6 Saturday and Sunday. I've used an If/else statement to read the current date and print message to user.

I took the idea for this exercise from Shecodes:
_https://www.shecodes.io/athena/10185-how-to-check-what-day-of-the-week-it-is-in-python#:~:text=date%20using%20datetime.-,datetime.,)%20to%206%20(Sunday)_


**Weekly Task 6** - squareroot.py
To ensure user input is positive, I've added a while loop to input a new message to user until the number typed was > 0.
I've created a function to calculate the squared root and store the result in a variable called my_float. How the function works:
1. Function calculates the root square aproximation multipliyng the user input by 0.5 nd store value in first_root
2. Calculates square root using Newnton's method: square_root = 0.5 * (X + (N / X)) from W3Schools
3. While loop runs program while both variable values first_root and square_root are different



 Newton method formulas, approach and inspiration:
 _https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/_
_https://thirumalai2024.medium.com/python-program-to-find-square-root-of-the-number-using-newtons-method-937c0e732756_

**Weekly Task 7** - es.py

**Weekly Task 8** - plottask.py



