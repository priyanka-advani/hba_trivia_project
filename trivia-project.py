CATEGORY_1_Q_AND_A = {
    "Q1? A) B) C)": "A",
    "Q2? A) B) C)": "B",
    "Q3? A) B) C)": "C" }

CATEGORY_2_Q_AND_A = {
    "Q1? A) B) C)": "A",
    "Q2? A) B) C)": "B",
    "Q3? A) B) C)": "C" }

CATEGORY_3_Q_AND_A = {
    "Q1? A) B) C)": "A",
    "Q2? A) B) C)": "B",
    "Q3? A) B) C)": "C" }

def calculate_score(current_score, number_of_guesses):
    new_score = current_score + (4 - number_of_guesses)
    return new_score

def choose_category():
    print "Category 1: ABC \nCategory 2: ABC \nCategory 3: ABC"
    user_category_choice = int(raw_input("Please choose a category: "))
    if user_category_choice = 1:
        chosen_category = CATEGORY_1_Q_AND_A
    elif user_category_choice = 2:
        chosen_category = CATEGORY_2_Q_AND_A
    elif user_category_choice = 3:
        chosen_category = CATEGORY_3_Q_AND_A

def play_trivia(): #need to change to accommodate categories
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
