# Made by Carson White 
# Due Date: 2/24/2024
# Problem: 5.14.1

import sys

def Day_Converter(x):
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

if __name__ == '__main__':
    x = int(input("Please enter a integer from 0-6 and this program will return the day of the week: "))
    Day_Converter(x)