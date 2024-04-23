## Made by: Carson White
## Due Date: 4/22/2024
## Problem: 20.8.3

## This program creates a new text file containing an alphabetical list of
## all the words that occur in the text and their occurences. 


def word_frequency(file_name):
    frequency_count = {}
    
    with open(file_name, 'r', encoding='utf-8') as file:
        for line in file:
            words = line.lower().split() ## This statement seperates the words read in from the text file 
            
            for word in words:
                cleaned_word = ''
                
                for char in word:
                    if char.isalpha():  ## This checks if a letter is alphabetic removing any 
                                        ## punctuation or anything that is not a letter
                        cleaned_word += char
                
                if cleaned_word: 
                    frequency_count[cleaned_word] = frequency_count.get(cleaned_word, 0) + 1
                    ## This adds 1 to the frequency count if the word is cleaned

    
    sorted_items = sorted(frequency_count.items())
    ## This statement stores the frequency count that has been sorted into
    ## the sorted_items variable

    return sorted_items

def write_frequencies(frequencies, output_file):  ## The code below writes the output to the file with the correct spacing and format
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write("Word              Count\n")
        file.write("=======================\n")
        for word, count in frequencies:
            file.write(f"{word:<16}{count:>4}\n")
            
## Below are the statements to intake the input and output file and then
## creating a variable frequencies that is passeed the result of word_frequency
## on the input file. The frequencies variable is then passed into write_frequencies to
## output the frequencies to the user

input_file = input("Please enter the name of the input file: ")
output_file = input("Please enter the name of the output file: ")

frequencies = word_frequency(input_file)
write_frequencies(frequencies, output_file)
