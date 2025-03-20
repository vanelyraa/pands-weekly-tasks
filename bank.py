#Weekly Tasks 02
#When Banks are storing currency figures, they store them as integers (usually in cent).This is to avoid rounding errors. 
#The program should:
    #Prompt the user and read in two money amounts (in cent)
    #Add the two amounts
    #Print out the answer in a human readable format with a euro sign and decimal point between the euro and cent of the amount 
# Author Vanessa Lyra

amount1 = int(input("Please enter first amount(in cents): ")) #User input 1 stored as integer
print ('First amount is:', amount1,' cents') #Printing user input 1 

amount2 = int(input("Please enter second amount(in cents): "))#User input 2 stored as integer
print ('Second amount is:', amount2,' cents') #Printing user input 2

new_amount = (amount1 + amount2)/100 #Sum values and divide by 100 for value in €
print (f'The sum of these is € {new_amount:.2f}') #Printing result, added F-string to print 2 decimal places

#Source: https://www.geeksforgeeks.org/formatted-string-literals-f-strings-python/