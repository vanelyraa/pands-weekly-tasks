# ***Programming and Scripting Weekly Tasks***

_Author Vanessa Lyra_

### **Weekly Task 2** - bank.py

In this task, I've utilized 'input()' function to prompt the message to the user. Both user inputs were stored as integers in two different variables: 'amount1' and 'amount2' and both values were prompted back to the user.
I summed both values in cents and to convert from cent to Euro, I divided the result by 100. New value in Euro was stored in variable 'new_amount' and prompted to user.

[GeeksforGeeks](https://www.geeksforgeeks.org/formatted-string-literals-f-strings-python/), was my inspiration to format the last statement of my code, I have added F-string to format print statement, call my variable 'new_amount' and again [GeeksforGeeks](https://www.geeksforgeeks.org/how-to-get-two-decimal-places-in-python/) to display decimal places using '{.2f}'  

  
### **Weekly Task 3** - accounts.py

In task 3, I have employed 'input()' function to prompt message to the user and stored the user input as string in variables: 'account_number' and 'account_number2'.  
To print the last 4 digits of each account number I have used array slicing:
- 10 digits account number: as the first array value is always index 0, I've used [6:10], prints values from index 6 to index 9, the second value in array slicing non inclusive.
- Numbers of any length: Slicing [-4:], the negative value tells Python to work from the end of the array, the empty side of the slicing means 'until the end of the array'. The starting point for Python in this case is the 4th number from the end the end of the array, Python will print the last 4 digits of the user's bank account.
  

### **Weekly Task 4** - collatz.py
Again 'input()' function utilized to prompt the message to the user and values stored as integers in variable 'my_integer'.  
In this program, I chose a 'while' loop to run the program while the integer value is different then 1.   
A subsequent if/else employed:  
- If statement will find even numbers: I've used a very common way to determine if a number is positive: modulus '% 2 == 0'. The program divides the integer input by 2, if remainder is equal to 0, the integer is positive. This number is then divided by 2 and stored in variable my_integer.
- Else statement: if remainder is not 0, number is odd, multiplied by three and added one. The result is stored in variable my_integer.
The program will print each value until the integer is equals to 1.

I have based even and odd numbers calculation from 
[Toppr Python guides](https://www.toppr.com/guides/python-guide/examples/python-examples/python-program-to-check-if-a-number-is-odd-or-even)

### **Weekly Task 5** - weekday.py 
In task 5, I've imported datetime library, the library which manipulates dates in Python and retrieved today's by calling function datetime.datetime.today().  
Each day of the week is an integer, 0 - 4 Monday to Thursday and 5 - 6 Saturday and Sunday. I've used an If/else statement to read the current date and print message to user.

[Shecodes](https://www.shecodes.io/athena/10185-how-to-check-what-day-of-the-week-it-is-in-python) provided me with the inspiration for this task.


### **Weekly Task 6** - squareroot.py
In this task, to ensure user input is positive, I've added a while loop to input a new message to user until the number typed is > 0.  
I've created a function 'Sqrt' to calculate the squared root and store the result in a variable called my_float.  
How the function works:  
1. Function calculates the root square aproximation multipliyng the user input by 0.5. Result is stored in variable 'first_root'.
2. Newton's square root method is calculated using : square_root = 0.5 * (X + (N / X)) formula from W3Schools, where X = 'first_root' and N = user input
3. A While loop runs program while variables 'first_root' and 'square_root' are different. If both variables are different the program will assign the value stored in 'square_root' to variable 'square_root' and the Newton's method is applied again. When both value are equal, the function will return value stored in 'first root'.
4. I've added two print statements (commented out) to check the function results of each loop iteration.

 Newton method formula from [GeeksforGeeks](https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/), approach and inspiration from [Medium](https://thirumalai2024.medium.com/python-program-to-find-square-root-of-the-number-using-newtons-method-937c0e732756).

### **Weekly Task 7** - es.py
This program is divided in two functions:  

1. My_program()
The first block of this function (If statement) checks if user is passing the two necessary arguments to run  the program: a python script .py and second file, if not, a error message will be printed out to user and python will exit the program.  
The second block (If statement) checks if the second argument passed by user is a text file .txt, if not, a error message will be prompted to user and python will exit the program.  
If no issues encountered, the function will call 'counting_e()' and store it's result in variable 'my_counter'

2. Counting_e()
Divided by a try/except block
Try block will open the file in read mode. Read the file and store it in variable file_content and close the file. My program wouldn't read the file at first, I've used ChatGPT to debug this line of code, I had to specify the encoding 'UTF-8' in statement 'file = open(read_file,'r',_encoding='utf-8_')'   
Subsequently, the funtion will convert the file content to lower case 'file_content.lower()' and count the number of letter 'E's' using 'count('e') and store the count in vaialble 'my_counter'.  
The Except block will display an error in case Python can't open or access the text file.

Resources for this exercise and where I've applied:  
Handling exceptions, helped me estructure the try/except from my code [SQLPEY](https://sqlpey.com/python/top-4-methods-to-handle-exceptions-when-reading-files-in-python)  
How to check a file extension [DNM](https://dnmtechs.com/using-endswith-to-check-for-multiple-file-extensions-in-python-3/)  
How to count characters, define and call functions: [OStechnix](https://ostechnix.com/count-characters-and-words-in-text-files-using-python/)  
I am currently reading this book, thought it would be fun to use it for the exercise _Fitzgerald, F. Scott. The Great Gatsby. Scribner, 2004_

### **Weekly Task 8** - plottask.py
1. Plotting the histogram of a normal distribution  
First I generated a random array using numpy function 'random.normal', where I could define: loc=mean and scale = standard deviation. Array generated stored in variable my_plot_array. I generated the plot using 'plt.hist', added a title, labels for both axis and horizontal grid lines.

2. Plotting of the function  h(x)= $X^3$  
X axis: I've generated a random array using numpy function 'linspace', where I could define asked range of 0 to 10, I've added a random 201 values to the array.  
Y axis: Added to function $X^3$, I generated the plot using 'plt.plot', added a title, labels for both axis, horizontal grid lines and a legend. Also added LaTex function '$$' to display the function $X^3$ as a mathematical expression.

Resources for this exercise and where I've applied:  
To add the horizontal grid lines to plot: [W3Schools](https://www.w3schools.com/python/matplotlib_grid.asp)  
Generate the array to plot histogram: [Numpy documentation](https://numpy.org/doc/2.1/reference/random/generated/numpy.random.normal.html)  
Generate the array to plot function h(x)=x3: [Numpy documentation](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html)  
To add labels and title to plot: [W3Schools](https://www.w3schools.com/python/matplotlib_labels.asp)  
To add a legend to the plot: [Matplolib documentation](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html)  
To add the mathematical expressions using LaTex: [Matplolib documentation](https://matplotlib.org/stable/users/explain/text/mathtext.html)  
Library to plot the histogram: [Matplolib documentation](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html)  


