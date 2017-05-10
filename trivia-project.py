TRIVIA_Q_AND_A = {
    "Q1? A) B) C)": "A",
    "Q2? A) B) C)": "B",
    "Q3? A) B) C)": "C" }

def calculate_score(current_score, user_guesses):
    new_score = current_score + (4 - user_guesses)
    return new_score

def play_trivia():
    user_score = 0
    for question in TRIVIA_Q_AND_A:
        user_answer = (raw_input(question + " ")).upper()
        while user_answer != TRIVIA_Q_AND_A[question]:
            print "Sorry, try again "
            user_answer = (raw_input(question + " ")).upper() # make this a function
            continue
        print "That's right!"
        user_guesses = 
        user_score = calculate_score(user_score)
        print "Your score is " + str(user_score)

def start_game():
    user_choice = raw_input("Do you want to play trivia? Y/N: ")
    if user_choice.upper() == "Y":
        print "Let's get started!"
        play_trivia()
    elif user_choice.upper() == "N":
        print "Maybe next time"

start_game()
 
# play again
# tiered scoring
# random question order
# high scores - save names & scores in a file
# use an api to get the questions & answers?
# rounds?
# timers?
