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
    "2004 A) The Aviator B) Finding Neverland C) Million Dollar Baby": "C",
    "2005 A) Capote B) Brokeback Mountain C) Crash": "C" }


CATEGORY_3_Q_AND_A = {
    "The fear of snakes A) Ophidiophobia B) Entomophobia C) Selachophobia": "B",
    "The fear of crowds A) Chiroptophobia B) Enochlophobia C) Oneirophobia": "B",
    "The fear of being robbed A) Aurophobia B) Harpaxophobia C) Ichthyophobia": "B",
    "The fear of isolation A) Zelophobia B) Urophobia C) Autophobia": "C",
    "The fear of freedom A) Myrmecophobia B) Dendrophobia C) Eleutherophobia": "C",
    "The fear of mice A) Herpetophobia B) Musophobia C) Neophobia": "B" }


def calculate_score(current_score, number_of_guesses):
    new_score = current_score + (4 - number_of_guesses)
    return new_score


def choose_category():
    print "\nCategories: \n1) Pokemon, Big Data, or Prescription Drug? \n2) Oscar Winning Movies (2000s) \n3) Phobias"
    user_category_choice = int(raw_input("\nPlease choose a category: "))
    if user_category_choice == 1:
        print "\nCategory 1: Is it a Pokemon, big data technology, or prescription drug?"
        chosen_category = CATEGORY_1_Q_AND_A
    elif user_category_choice == 2:
        print "\nCategory 2: Which movie won the Oscar for Best Picture in each year?"
        chosen_category = CATEGORY_2_Q_AND_A
    elif user_category_choice == 3:
        print "\nCategory 3: Can you identify the phobia by its definition?"
        chosen_category = CATEGORY_3_Q_AND_A
    return chosen_category


def play_trivia():
    user_score = 0
    chosen_category = choose_category()
    for question in chosen_category:
        user_answer = (raw_input("\n" + question + "\nYour answer: ")).upper()
        user_guesses = 1
        while user_answer != chosen_category[question]:
            print "\nSorry, try again "
            user_answer = (raw_input("\n" + question + "\nYour answer: ")).upper() # make this a function
            user_guesses = user_guesses + 1
            continue
        print "\nThat's right!"
        user_score = calculate_score(user_score, user_guesses)
        print "Your score is " + str(user_score)
    print "Thanks for playing!\n"


def start_game():
    while True:
        user_choice = raw_input("Do you want to play trivia? Y/N: ")
        if user_choice.upper() == "Y":
            print "\nGreat, let's get started!"
            play_trivia()
        elif user_choice.upper() == "N":
            print "Maybe next time. Goodbye!"
            break


start_game()
 
# random question order
# high scores - save names & scores in a file
# use an api to get the questions & answers?
# rounds?
# timers?
