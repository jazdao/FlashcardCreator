import random

print("Flashcard Creator\n-----------------------------------------------------------------")

q_number = 1      # question number
questions = []    # list of questions
answers = []      # list of answers

print("Enter 'done' when you have finished registering your flash cards.")

question = "N/A"
answer = "N/A"

while question != "done" and answer != "done":     # loop entry of flashcards until input = 'done'
    print("\nEnter the question for flashcard #", q_number, sep="", end="")
    print(":")
    question = str(input())
    while question == "done" and q_number == 1:    # if input = 'done' at the first entry
        print("Please create at least one flashcard entry:")
        question = str(input())
    if question == "done" and q_number != 1:       # break out of loop if input = 'done' after first entry
        q_number = q_number - 1                    # revert q_number value because no new question added
        break
    else:
        questions.append(question)                 # add input to question list

    print("Enter the answer for flashcard #", q_number, sep="", end="")
    print(":")
    answer = str(input())
    while answer == "done":                        # cannot create question without answer
        print("Please first enter the answer for flashcard #", q_number, sep="", end="")
        print(":")
        answer = str(input())
    answers.append(answer)                         # add input to answer list

    q_number += 1


print("\nWould you like to review the flashcards (yes/no)?")

test = str(input())
while test != "yes" and test != "no":              # if non-answer
    print("\nPlease enter either 'yes' or 'no':", end=" ")
    test = str(input())

if test == "yes":                                  # review flashcards
    print("\nEnter 'show' to reveal the answer, 'next' to move on to the next card, and 'exit' to quit the program.")
    flashcards = "next"
    while flashcards != "quit":                    # loop through flashcard entries until input = 'quit'
        if flashcards == "show":                   # show answer
            print("Answer:   " + answers[ran])
            print()
            flashcards = str(input())
        elif flashcards == "next":                 # display random flashcard question
            ran = random.randint(0, q_number-1)
            print("Question:   " + questions[ran])
            flashcards = str(input())
        else:                                      # if non-answer
            print("\nPlease enter one of the following:")
            print("'show' = reveal the answer\n'next' = move on to the next card\n'quit' = exit the program\n")
            flashcards = str(input())

    print("Exiting program...")                     # if input = 'quit'

elif test == "no":                                  # quit program
    print("\nExiting program...")







