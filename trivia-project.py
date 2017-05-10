trivia_q_and_a = {
    "Q1": "A1",
    "Q2": "A2",
    "Q3": "A3" }

trivia_questions = trivia_q_and_a.keys()

def calculate_score(current_score):
    new_score = current_score + 1
    return new_score

def play_trivia():
    user_score = 0
    i = 0 # represents index for trivia_questions list
    while i < len(trivia_questions):
        user_answer = (raw_input(trivia_questions[i] + " ")).upper()
        if user_answer == trivia_q_and_a[trivia_questions[i]]:
            print "Correct"
            user_score = calculate_score(user_score)
        else:
            print "Incorrect"
        i = i + 1
        print "Your score is " + str(user_score)

def start_game():
    user_choice = raw_input("Do you want to play trivia? Y/N: ")
    if user_choice.upper() == "Y":
        print "Let's get started!"
        play_trivia()
    elif user_choice.upper() == "N":
        print "Maybe next time"

start_game()














# define a function play_trivia() # takes no arguments
#     create variable i and assign value of 0 # represents index
#     create variable score and assign value of 0
#     create a while loop to loop through questions list while i is less than length of questions list
#         ask user to input answer to questions at i
#         if user input evaluates to answers at i
#             print "correct"
#             add one to the score
#         else
#             print "incorrect"
#         print "your score is " + score # score needs to be a string

# ask user for raw input to the question "Do you want to play trivia? Y/N: "
#     if the user inputs "Y"
#         print "let's get started"
#         call play_trivia()
#     else if the user inputs "N"
#         print "maybe next time"