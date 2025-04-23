# Weekly task 6
# Author Vanessa Lyra

#Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.
#You should create a function called <tt>sqrt</tt> that does this.

#def pos_number():
#my_float = False
my_float = float(input("Please  enter a positive number ")) 
while my_float < 0: #while loop, number cannot be smaller than 0
    my_float = float(input ("This is not a positive number, try again: ")) #Asking user to input correct parameter (positive number)

def Sqrt(my_float): #function to calculate square root using Newton's method
    first_root = 0.5 * my_float #root square approximation 
    square_root = 0.5 * (first_root + my_float / first_root) #Newton's method
    while square_root != first_root: #Run loop while first Newton's root square is different from approximation 
        first_root = square_root #Define approximation square root as New Newton calculation result
        square_root = 0.5 * (first_root + my_float / first_root) # Newton's method While condition when both square roots are different 
        #print("square ", square_root) #checking results
        #print("First ", first_root)
    return first_root #function return value
print (Sqrt(my_float)) #Printing Square root

#Resources: 
#https://thirumalai2024.medium.com/python-program-to-find-square-root-of-the-number-using-newtons-method-937c0e732756
#https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method