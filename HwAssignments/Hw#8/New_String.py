## Made by Carson White
## Due Date: 4/8/24
## Problem: 11.22.10

## This problem is designed to replace all occurences of old in string
## to new using split and join methods

## Below is the replace function which takes in the parameters s(the string, old, and new)
## The replace function below utilizes the split method to split the string up where the word old is
## The function then uses the join method to replace the instances of old with new and rejoins all the substrings together


def replace(s, old, new):
    temporary_string = s.split(old)
    
    return new.join(temporary_string)

def main():
    s = "There was an old man who owned the old house in the old neighbourhood. One day while driving an old car, he decided he wanted to buy a new car"

    new_string = replace(s, "old", "new")
    
    print(new_string)
    
main()