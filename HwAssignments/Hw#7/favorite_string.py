## Made by Carson White
## Due Date:
## Problem: 8.18.5

## This program operates by taking a string quote and then figuring out the total amount of words
## as well as the amount of words that contain an e, then returning a print statement that mentions the 
## total words, words with e in it, and the percentage of words with e in it


import string

## This function belows removes punctuation from the quote using
## the string library provided by Python

def remove_punctuation(x):
    punctiation = ",.-"
    quote = ""
    for char in x:
        if char not in string.punctuation:
            quote += char
    return quote

## The function below is the find function and will be used for the search of the letter e below

def find(strng, ch, start=0, end=None):
    ix = start
    if end is None:
        end = len(strng)
    while ix < end:
        if strng[ix] == ch:
            return ix
        ix += 1
    return -1

## The function below uses the find function above to iterate through the words in quote using an if loop
## according to the conditions set above by the find function if e can not be be found then the function returns -1,
## so the condition set in the if loop is to run until the find function comes up with -1 ( The find function can't find any more e's)

def EWord_Count(words):
    e_words = 0
    for x in words:
        if find(x, 'e') != -1:
            e_words += 1
    return e_words

quote = "Four score and seven years ago our fathers brought forth on this continent a new nation, conceived in liberty, and dedicated to the proposition that all men are created equal. “Now we are engaged in a great civil war, testing whether that nation, or any nation so conceived and so dedicated, can long endure. We are met on a great battlefield of that war. We have come to dedicate a portion of that field as a final resting place for those who here gave their lives that that nation might live. It is altogether fitting and proper that we should do this. “But in a larger sense we cannot dedicate, we cannot consecrate, we cannot hallow this ground. The brave men, living and dead, who struggled here have consecrated it, far above our poor power to add or detract. The world will little note, nor long remember, what we say here, but it can never forget what they did here. It is for us the living, rather, to be dedicated here to the unfinished work which they who fought here have thus far so nobly advanced. It is rather for us to be here dedicated to the great task remaining before us,that from these honored dead we take increased devotion to that cause for which they gave the last full measure of devotion, that we here highly resolve that these dead shall not have died in vain, that this nation, under God, shall have a new birth of freedom, and that government of the people, by the people, for the people, shall not perish from the earth."
removed_quote = remove_punctuation(quote)
fav_string = removed_quote.split()
total_words = len(fav_string)
e_words = EWord_Count(fav_string)
   
## Above are some crucial operations for this program including the split which splits the string into seperate words
## so the words can be viewed for other operations


def print_statement(total_words, e_words):
    e_percentage = (e_words/total_words) * 100
    
    print("Your text contains " + str( total_words)  + " words, of which " + str( e_words) + "( " + str(e_percentage) + " %) contain an e. ")
    
def main():
    
    
    print_statement(total_words, e_words)
    
main()