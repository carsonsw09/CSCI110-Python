# Made by Carson White 
# Due Date: 2/24/2024
# Problem: 5.14.1

import sys

def Day_Converter(x):# This function checks what the input value is then
                     # prints the day of the week based off the corresponding
                     # input value
    if x == 0:
        print("The day of the week is Monday")
    elif x == 1:
        print("The day of the week is Tuesday")
    elif x == 2:
        print("The day of the week is Wednesday")
    elif x == 3:
        print("The day of the week is Thursday")
    elif x == 4:
        print("The day of the week is Friday")
    elif x == 5:
        print("The day of the week is Saturday")
    elif x == 6:
        print("The day of the week is Sunday")
        
    # The elif statements will check through the values in descending order until
    # the input value is found, if not found, then there was an error with the user input

if __name__ == '__main__':
    x = int(input("Please enter a integer from 0-6 and this program will return the day of the week: "))
    
    # The statement above stores the user input into the x-variable
    
    Day_Converter(x)
    
    # Above the Day_Converter function is called passing the variable x into the function