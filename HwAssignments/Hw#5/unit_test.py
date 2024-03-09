## Made by Carson White
## Due Date 3/11/24
## Problem 6.9.7

## The program below runs a unit test on a function that converts
## hours, minutes, and seconds to a total number of seconds


import sys

## The function below uses the threee inputs, converts them to seconds, and 
## then adds them together to return the total amount of seconds

def to_secs(input_a, input_b, input_c):
    hour_seconds = input_a * 3600
    minute_seconds = input_b * 60
    total_seconds = hour_seconds + minute_seconds + input_c
    return total_seconds

## The function below returns a message on wheter the test case failed or passed
## based off the did_pass parameter

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno  # This gets the callers line number
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)
    
## The function below tests the to_secs function by calling it with three inputs
## and verifying that the correct answer is achieved
def test_group():
    """ Run the suite of tests for code in this module (this file).
    """
    test(to_secs(2, 30, 11) == 9011)
    test(to_secs(2, 0, 0) == 7200)
    test(to_secs(0, 2, 0) == 120)
    test(to_secs(0, 0, 42) == 42)
    test(to_secs(0, -10, 10) == -590)

test_group()  # Here is the call to test_group which will return whether
              # or not the test passed  



    
    