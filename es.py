# Weekly Task 07
# Author Vanessa Lyra

#Write a program that reads in a text file and outputs the number of e's it contains. Think about what is being asked here, document any assumptions you are making.
#he program should take the filename from an argument on the command line. I have not shown you how to do this, you need to look it up.

import sys #Module imported to access command-line arguments

def counting_e(read_file): #Defining function name with file as parameter
    try: #try/except block to handle possible errors
        file = open(read_file,'r',encoding='utf-8') #opening file in read mode 
        file_content = file.read() #Read file and store content in variable
        file.close() 

        my_counter = file_content.lower().count('e') ##converting letters to lower case (making code case insensitive) and counting e´s
        return my_counter #Returning count of E
    
    except FileNotFoundError: #Exception warning user if file is not found
        print("ERROR!! File not found") #User warning
        sys.exit(1) #Exiting program, issue encountered
        
def my_program (): #Defining main function
    if len(sys.argv) != 2: #If the number of arguments is not 2 (.py and .txt file)
        print("Please provide a second argument (file) to run the program") #User warning
        sys.exit(1)
        
    read_file = sys.argv[1] #read the second argument and store in variable
    if not read_file.lower().endswith('.txt'): #if file extension is not .txt
            print ("ERROR!! File is not in .txt format") #User warning incorrect file extension
            sys.exit(1)

    my_counter = counting_e(read_file) #Calling counting_e function
    print(f"Number of E's in file '{read_file}' is:{my_counter}") #Print number of Es, return file name and counter

my_program() #call function

#Resources: 
#https://sqlpey.com/python/top-4-methods-to-handle-exceptions-when-reading-files-in-python/#google_vignette
#https://dnmtechs.com/using-endswith-to-check-for-multiple-file-extensions-in-python-3/
#https://ostechnix.com/count-characters-and-words-in-text-files-using-python/