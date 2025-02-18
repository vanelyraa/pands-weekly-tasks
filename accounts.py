# Weekly Task 03
# Author Vanessa Lyra
#Bank account numbers can stored as 10 character strings, for security reasons some applications only display the last 4 characters (with the other other characters replaced with Xs).

#Write a python program called accounts.py that reads in a 10 character account number and outputs the account number with only the last 4 digits showing (and the first 6 digits replaced with Xs).

#$ python accounts.py
#Please enter an 10 digit account number: 1234567890
#XXXXXX7890
#Extra:
#M#odify the program to deal with account numbers of any length (yes that is a vague requirement, comment your assumptions)

print("Please enter an 10 digit account number")
account_number = "1098745638"
print ("XXXXXX" + account_number[6:10]) #Print from 6 digit until 9. Position 10 not included

#Modified version
print("Please enter an account number")
account_number = "1095878745638"
print ("Last 4 digits of your account number " + account_number[-4:]) #Print 4 digits from the end of the account number