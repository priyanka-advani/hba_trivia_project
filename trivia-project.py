CATEGORY_1_Q_AND_A = {
    "Crebase\nA) Pokemon B) Big Data C) Prescription Drug": "A",
    "Tokutek\nA) Pokemon B) Big Data C) Prescription Drug": "B",
    "Adabas\nA) Pokemon B) Big Data C) Prescription Drug": "B",
    "Feebas\nA) Pokemon B) Big Data C) Prescription Drug": "A",
    "Actos\nA) Pokemon B) Big Data C) Prescription Drug": "C",
    "Decadron\nA) Pokemon B) Big Data C) Prescription Drug": "C" }


CATEGORY_2_Q_AND_A = {
    "2000\nA) Crouching Tiger, Hidden Dragon B) Gladiator C) Traffic": "B",
    "2001\nA) A Beautiful Mind B) Moulin Rouge! C) LOTR: The Fellowship of the Ring": "A",
    "2002\nA) Chicago B) Gangs of New York C) The Pianist": "A",
    "2003\nA) Lost in Translation B) LOTR: The Return of the King C) Seabiscuit": "B",
    "2004\nA) The Aviator B) Finding Neverland C) Million Dollar Baby": "C",
    "2005\nA) Capote B) Brokeback Mountain C) Crash": "C" }


CATEGORY_3_Q_AND_A = {
    "Fear of snakes\nA) Ophidiophobia B) Entomophobia C) Selachophobia": "B",
    "Fear of crowds\nA) Chiroptophobia B) Enochlophobia C) Oneirophobia": "B",
    "Fear of being robbed\nA) Aurophobia B) Harpaxophobia C) Ichthyophobia": "B",
    "Fear of isolation\nA) Zelophobia B) Urophobia C) Autophobia": "C",
    "Fear of freedom\nA) Myrmecophobia B) Dendrophobia C) Eleutherophobia": "C",
    "Fear of mice\nA) Herpetophobia B) Musophobia C) Neophobia": "B" }


# for printing in color
color_gray = "\033[1;30m{}\033[1;m"
color_blue = "\033[1;34m{}\033[1;m"
color_green = "\033[1;32m{}\033[1;m"
color_red = "\033[1;31m{}\033[1;m"
highlight_gray = "\033[1;47m{}\033[1;m"


def calculate_score(original_score, number_of_guesses):
    """ Calculates user score after each question """

    # score for each question starts at 3 and bottoms out at 0
    # negative scores are not possible
    if number_of_guesses <= 4:
        current_question_score = (4 - number_of_guesses)
    
    else:
        current_question_score = 0
    
    new_score = original_score + current_question_score
    
    return new_score


def choose_category():
    """ Asks user to choose a category, validates input,
    and returns the chosen category """

    while True:

        print color_gray.format("\nCategories: \n1) Pokemon, Big Data, or Prescription Drug? \n2) Oscar Winning Movies (2000s) \n3) Phobias")
        user_category_choice = raw_input(color_blue.format("\nPlease choose a category: "))
        
        if user_category_choice.isdigit():
            
            if int(user_category_choice) == 1:
                print highlight_gray.format("\nCategory 1: Is it a Pokemon, big data technology, or prescription drug?")
                chosen_category = CATEGORY_1_Q_AND_A
                return chosen_category
            
            elif int(user_category_choice) == 2:
                print highlight_gray.format("\nCategory 2: Which movie won the Oscar for Best Picture in each year?")
                chosen_category = CATEGORY_2_Q_AND_A
                return chosen_category
            
            elif int(user_category_choice) == 3:
                print highlight_gray.format("\nCategory 3: Can you identify the phobia by its definition?")
                chosen_category = CATEGORY_3_Q_AND_A
                return chosen_category
            
            else:
                print color_red.format("\nSorry, that is not a valid category")
        
        else:
            print color_red.format("\nSorry, that is not a valid category")


def play_trivia():
    """ Takes user category choice and loops through questions for that category """
    
    # user score starts at 0 at the beginning of each instance of game play
    user_score = 0

    # use choose_category function to assign the user's choice to chosen_category
    chosen_category = choose_category()

    # iterate through dictionary of Q&As for the chosen question
    for question in chosen_category:
        
        user_answer = (raw_input(color_gray.format("\n" + question) + color_blue.format("\nYour answer: "))).upper()
        user_guesses = 1
        
        while user_answer != chosen_category[question]:
            print color_red.format("\nSorry, try again")
            user_answer = (raw_input(color_gray.format("\n" + question) + color_blue.format("\nYour answer: "))).upper() # make this a function
            user_guesses = user_guesses + 1
            continue
        
        print color_green.format("\nThat's right!")
        user_score = calculate_score(user_score, user_guesses)
        print color_gray.format("Your score is " + str(user_score))
    
    print highlight_gray.format("\nThanks for playing! Your final score is " + str(user_score))


def start_game():
    """ Asks the user if they want to play, validates input,
    and either starts game or exits """

    while True:
        user_choice = raw_input(color_blue.format("\nDo you want to play trivia? Y/N: "))
        
        if user_choice.upper() == "Y":
            print color_gray.format("\nGreat, let's get started!")
            print color_gray.format("\nRules:")
            print color_gray.format("- You must choose one of the available categories")
            print color_gray.format("- Getting it right on the first guess is worth 3 points, on the second guess is worth 2 points, and so on")
            print color_gray.format("- If it takes you four or more guesses to get the answer right, you will get 0 points")
            print color_gray.format("- Invalid answer choices count towards your number of guesses")
            print color_gray.format("- You must answer each question in order to get to the next question")
            
            # starts game play
            play_trivia()
        
        elif user_choice.upper() == "N":
            print color_gray.format("\nMaybe next time. Goodbye!\n")
            break
        
        else:
            print color_red.format("\n Sorry, that is not a valid choice")


start_game()
 
# random question order
# high scores - save names & scores in a file
# use an api to get the questions & answers?
# rounds?
# timers?
