CATEGORY_1_Q_AND_A = {
    "Crebase A) Pokemon B) Big Data C) Prescription Drug": "A",
    "Tokutek A) Pokemon B) Big Data C) Prescription Drug": "B",
    "Adabas A) Pokemon B) Big Data C) Prescription Drug": "B",
    "Feebas A) Pokemon B) Big Data C) Prescription Drug": "A",
    "Actos A) Pokemon B) Big Data C) Prescription Drug": "C",
    "Decadron A) Pokemon B) Big Data C) Prescription Drug": "C" }

CATEGORY_2_Q_AND_A = {
    "2000 A) Crouching Tiger, Hidden Dragon B) Gladiator C) Traffic": "B",
    "2001 A) A Beautiful Mind B) Moulin Rouge! C) LOTR: The Fellowship of the Ring": "A",
    "2002 A) Chicago B) Gangs of New York C) The Pianist": "A",
    "2003 A) Lost in Translation B) LOTR: The Return of the King C) Seabiscuit": "B",
    "2004 A) The Aviator B) Finding Neverland C) Million Dollar Baby": "C" }

CATEGORY_3_Q_AND_A = {
    "The fear of snakes A) Entomophobia B) Ophidiophobia C) Selachophobia": "B",
    "The fear of crowds A) Chiroptophobia B) Enochlophobia C) Oneirophobia": "B",
    "The fear of being robbed A) Aurophobia B) C)": "C" }

def calculate_score(current_score, number_of_guesses):
    new_score = current_score + (4 - number_of_guesses)
    return new_score

def choose_category():
    print "1) Pokemon, Big Data, or Prescription Drug? \n2) Oscar Winning Movies (2000s) \n3) Phobias"
    user_category_choice = int(raw_input("Please choose a category: "))
    if user_category_choice == 1:
        print "Is it a Pokemon, big data technology, or prescription drug?"
        chosen_category = CATEGORY_1_Q_AND_A
    elif user_category_choice == 2:
        print "Which movie won the Oscar for Best Picture in each year?"
        chosen_category = CATEGORY_2_Q_AND_A
    elif user_category_choice == 3:
        print "Can you identify the phobia by its definition?"
        chosen_category = CATEGORY_3_Q_AND_A
    return chosen_category

def play_trivia(): #need to change to accommodate categories
    user_score = 0
    chosen_category = choose_category()
    for question in chosen_category:
        user_answer = (raw_input(question + " ")).upper()
        user_guesses = 1
        while user_answer != chosen_category[question]:
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
