## Made by Carson White
## Due Date 3/18/24
## Problem 7.26.9

## This program is centered around a print triangle number function that 
## prints out the first n triangular numbers. The function can be called with inputs
## that will produce the correct result

import sys

## The function below incorporates the print_triangular_numbers which uses the formula
## provided to figure out the number of triangles

def print_triangular_numbers(n):
    
    ans = ((n*(n+1))/2)
    return int(ans)

## The main function below intakes user input, calls the print_triangular_numbers(n),
## and then displays the result to the user

def test_cases():
    assert(print_triangular_numbers(1)==1)
    assert(print_triangular_numbers(2)==3)
    assert(print_triangular_numbers(3)==6)
    assert(print_triangular_numbers(4)==10)
    assert(print_triangular_numbers(5)==15)
    

def main():
    n = int(input("Please enter a value: "))
    for i in range(1, n+1):
        
        ans = print_triangular_numbers(i)
        print(f"{i} {ans}")
    
    test_cases()
    
main()