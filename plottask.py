# Weekly Task 08
# Write a program called plottask.py that displays:
# a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2, and a plot of the function  h(x)=x3 in the range 0 to 10, on the one set of axes.

#Importing libraries
import matplotlib.pyplot as plt
import numpy as np

#Normal distribution histogram
my_plot_array = np.random.normal(loc=5, scale=2, size=1000) #Generating normal distribution with defined mean and deviation

plt.hist(my_plot_array) #Generating plot
plt.title('Normal Distribution histogram') #Adding title
plt.xlabel('X values') #Adding X axis lable
plt.ylabel('Y values') #Adding Y axis lable
plt.grid(axis = 'y', linestyle = '--', linewidth = 0.7) #Horizontal grid lines
plt.show() #Show plot

#Plot h(x) = x^3
x = np.linspace(0,10,201) #Generating array 0 to 10 range x values
y = x**3 #Y values X^3

plt.plot(x,y, label='h(x) = $x^3$') #Plot function and label
plt.title('Plotting $x^3$') #Adding title
plt.xlabel('x') #Adding X axis lable
plt.ylabel('$x^3$') #Adding Y axis lable
plt.grid(axis = 'y', linestyle = '--', linewidth = 0.7) #Horizontal grid lines
plt.legend() #Adding legend to plot
plt.show() #Show plot

#Resources: https://www.w3schools.com/python/matplotlib_grid.asp
#https://numpy.org/doc/stable/reference/generated/numpy.linspace.html
#https://www.w3schools.com/python/matplotlib_labels.asp
#https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html
#https://matplotlib.org/stable/users/explain/text/mathtext.html
#https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html



