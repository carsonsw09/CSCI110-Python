## Made by Carson White
## Due Date: 4/15/2024
## Problem: 13.10.1

## This problem is based around reading in an external file and then reversing
## the lines order. This program will open and then read the file. After that,
## the program will reverse the order of the lines and then write that to a new file

import os

input_file = input(" Please enter the file name. ")

output_file = input(" Please enter the output file name. ")

with open(input_file, 'r') as file:
    read_lines = file.readlines()
    
## The lines above open the input file entered by the user, then reads the text seperating it by lines
    
read_lines.reverse()

## The line above reverses the order of the lines that were read in 

with open(output_file,'w') as file:
    file.writelines(read_lines)

## The lines above open the output file and then writes the reversed order of the lines
## I opted for user innput as my VScode has troubles finding txt files stored in it
    
