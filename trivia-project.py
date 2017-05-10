trivia_q_and_a = {
    "Q1": "A1",
    "Q2": "A2",
    "Q3": "A3" }

# trivia_questions = trivia_q_and_a.keys()

def calculate_score(current_score):
    new_score = current_score + 1
    return new_score

def play_trivia():
    user_score = 0
    i = 0 # represents index for trivia_questions list
    for question in trivia_q_and_a:
        user_answer = (raw_input(question + " ")).upper()
        if user_answer == trivia_q_and_a[question]:
            print "Correct"
            user_score = calculate_score(user_score)
        else:
            print "Incorrect"
        print "Your score is " + str(user_score)

def start_game():
    user_choice = raw_input("Do you want to play trivia? Y/N: ")
    if user_choice.upper() == "Y":
        print "Let's get started!"
        play_trivia()
    elif user_choice.upper() == "N":
        print "Maybe next time"

start_game()