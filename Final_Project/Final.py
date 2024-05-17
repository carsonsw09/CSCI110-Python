## Made by Carson White
## Due Date: 5/13/24
## Final Project

## Bio: I am Carson White currently a junior at Colorado Mesa University who is pursuing
## a degree in computer science. I have a background in c++ and I am enjoying learning Python.

## This program is loosely based on the "Are you smarter then a 5th grader?" game. Questions, options, and answers are
## read in from the input file and then user input is compared with the answer read in from the text file. A total socre is
## then calculated and then compared with a percentage to determine if the user is smarter then a 5th grader. The results are
## then displayed in the output file. Unit testing is done on multiple fruitful functions throughout the program as well. 
import os

## The quiz reader function creates a dict to store the quiz info, reads in the input file and then stores the information into
## the dict. This is accomplished through creating a temporary storage for the question blocks, reading in the three different lines,
## and then appending them to the quiz dict based off the three different types

def Quiz_Reader(input_file):
    Quiz = [] 
    with open(input_file, 'r') as file:
        lines = file.readlines()
    
    question_block = [] 
    for line in lines:
        line = line.strip()
        if line:  
            
            question_block.append(line)
            
            if line.startswith('Answer:'):
                
                if len(question_block) == 3:
                    question = question_block[0]
                    options = question_block[1]
                    answer = question_block[2].split(': ', 1)[1]
                    Quiz.append({'question': question, 'options': options, 'answer': answer})
                question_block = []
    return Quiz


## The function below displays the output and returns true or false
## depending on the comparison between the user input and the recorded
## answer stored in the quiz dicitionary

def Quiz_Output(question):
    print(question['question'])
    print(question['options'])
    user_answer = input(" Please enter your answer and make sure it matches the option ")
    return user_answer.strip() == question['answer']

## This function runs the game comparing the result of Quiz_Output with the question
## and if correct the score is increased and if not, then a wrong message is displayed

def Run_Quiz(questions):
    print("Welcome to are you smarter than a 5th grader. My girlfriend is not, so good luck.")
    print("--------------------------------------------------------------------------------")
    score = 0
    incorrect_questions = []
    for question in questions:
        
        if Quiz_Output(question):
            print("Correct!")
            score += 1
            
        else:
            print("Wrong!")
            incorrect_questions.append(question['question'])
            
        if input("Do you want to continue? (yes/no): ") != 'yes':
            break

    return score, incorrect_questions

## Calculates the percentage based off the score and total questions
def Smartness_Calculator(score,toatl_questions):
    percentage = (score/toatl_questions)* 100
    return percentage

## Calculates what message to return based off the quiz percentage
def Smartness_Decider(percentage):
    if percentage >= 80:
        return "Congratulations! You are smarter than a 5th grader!"
    else:
        return "Unfortunately, you are not smarter than a 5th grader."
    
## Writes the score, percentage, and the message calculated by the function above
## to the output file and displays the questions that the user got incorrect
def Output_Writing(score, total_questions, incorrect_questions, output_file_path):
    percentage = Smartness_Calculator(score, total_questions)
    message = Smartness_Decider(percentage)
    
    with open(output_file_path, 'w') as file:
        file.write("Are you smarter than a 5th grader?")
        file.write(f"Score: {score}/{total_questions} ({percentage}%)")
        file.write(message)
        if incorrect_questions:
            file.write(" You got the following questions wrong:")
            for question in incorrect_questions:
                file.write(f"- {question}\n")
    
## Using assert statements the fruitful functions above our checked
## making sure these functions are returning the correct value      
def Test_Cases():
    assert(Smartness_Calculator(4,10) == 40)
    assert(Smartness_Calculator(10,10) == 100)
    assert(Smartness_Calculator(1,10) == 10)
    
    assert(Smartness_Decider(80) == 'Congratulations! You are smarter than a 5th grader!')
    assert(Smartness_Decider(10) == 'Unfortunately, you are not smarter than a 5th grader.')
    assert(Smartness_Decider(40) == 'Unfortunately, you are not smarter than a 5th grader.')
    

    
    
## The main aquires the input and output path files, uses try and except blocks for error catching, and calls 
## upon the functions used to run this quiz game.
def main():
    print("Please enter the path to your quiz file:")
    input_file_path = input("Input file path: ")  
    print("Please enter the path for the output results file:")
    output_file_path = input("Output file path: ")  

    try:
        questions = Quiz_Reader(input_file_path)  
        if not questions:
             
            print("No questions found in the file.")
            return
        score, incorrect_questions = Run_Quiz(questions)
        Output_Writing(score, len(questions), incorrect_questions, output_file_path)  
        print(f"Your final score is {score}/{len(questions)}")
        print(f"Results have been written to '{output_file_path}'.")
    except FileNotFoundError:
        print(f"Error: The file '{input_file_path}' was not found. Please check the path and try again.")
    
    
    Test_Cases()

if __name__ == "__main__":
    main()