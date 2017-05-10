trivia_q_and_a = {} #add questions as keys, answers as values













define a function play_trivia() # takes no arguments
    create variable i and assign value of 0 # represents index
    create variable score and assign value of 0
    create a while loop to loop through questions list while i is less than length of questions list
        ask user to input answer to questions at i
        if user input evaluates to answers at i
            print "correct"
            add one to the score
        else
            print "incorrect"
        print "your score is " + score # score needs to be a string

ask user for raw input to the question "Do you want to play trivia? Y/N: "
    if the user inputs "Y"
        print "let's get started"
        call play_trivia()
    else if the user inputs "N"
        print "maybe next time"