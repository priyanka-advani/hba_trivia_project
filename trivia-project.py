TRIVIA_Q_AND_A = {
    "Q1? A) B) C)": "A",
    "Q2? A) B) C)": "B",
    "Q3? A) B) C)": "C" }

def calculate_score(current_score, number_of_guesses):
    new_score = current_score + (4 - number_of_guesses)
    return new_score

def play_trivia():
    user_score = 0
    for question in TRIVIA_Q_AND_A:
        user_answer = (raw_input(question + " ")).upper()
        user_guesses = 1
        while user_answer != TRIVIA_Q_AND_A[question]:
            print "Sorry, try again "
            user_answer = (raw_input(question + " ")).upper() # make this a function
            user_guesses = user_guesses + 1
            continue
        print "That's right!"
        user_score = calculate_score(user_score, user_guesses)
        print "Your score is " + str(user_score)
    print "Thanks for playing!"

def start_game():
    while True:
        user_choice = raw_input("Do you want to play trivia? Y/N: ")
        if user_choice.upper() == "Y":
            print "Let's get started!"
            play_trivia()
        elif user_choice.upper() == "N":
            print "Maybe next time"
            break

start_game()
 
# random question order
# high scores - save names & scores in a file
# use an api to get the questions & answers?
# rounds?
# timers?
