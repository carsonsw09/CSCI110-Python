## Made by: Carson White
## Due date: 5/6/2024
## Problem #:19.6.1

## The goal of this program is to take in user input for a positive integer
## and handle cases that do not match the input like negative numbers and
## edge cases

import os

def respoint():
    try:
        ## The statement below checks if not input was provided using the strip command
        
        positive_integer = input("Please enter a positive integer. ")
        if positive_integer.strip() == '':
            return ("No input was provided, please enter a positive integer. ")
        ## The statement below checks if the number entered is less than 0
        ## if so an error message is provided. If not then the number is a positive integer
        
        positive_integer = int(positive_integer)
        if positive_integer < 0:
            return("{0} is not a valid positive integer".format(positive_integer))   
        else:
            print("The input meets the requirements.", + positive_integer, "is a positive integer. ")
            
        ## The statment below raises an error if the input provided was not an integer by using the except ValueError
        ## if the input provided can not be converted into a positive integer then this exception is called
        
    except ValueError:
        print("The input provided was not an integer, please provide a positive integer for the input. ")
    
output = respoint()
print(output)