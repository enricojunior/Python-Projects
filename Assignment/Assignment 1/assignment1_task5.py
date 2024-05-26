#Assignment 1 Python
#Section      : Task #5
#Name         : Enrico Junior
#Student's ID : E2100297

#Display introduction message
print("\nThis is a guessing number program with multiple rounds and various def function")
print("Created by Enrico Junior, E2100297\n")

#Importing the random module, to generate the random number
import random

#This function is used to show input from both players (human, computer)
#-depending on the default turn and limitation of the number ranges 
def dealWithATurn(defaultplayer,minimum_limit,maximum_limit):

    #This will display the current player who's taking turn to guess
    print("Player : " + str(defaultplayer))

    #This will be shown on the screen, giving the number range from the 
    #-minimum value to maximum value statement
    print("Range " + str(minimum_limit) + " --> " + str(maximum_limit) + ".",end = ' ')

    if defaultplayer == "Human":

        #This code is used to ask player 1, Human to guess the random 
        #-generated number
        defaultguess = eval(input("Your guess? "))

    elif defaultplayer == "Computer":

        #This code shows how computer generates the number automatically
        defaultguess = random.randint(minimum_limit,maximum_limit)

        #This message shows what's the number will be guessed by the 
        #-computer
        print("Computer guess " + str(defaultguess))

    #This code's purpose is to get the default guess of both players and 
    #-returns the guess to main function
    return defaultguess

#This function is used to dispkay the result of both players from all 
#-rounds
#Whoever has already reached 3 points will be declared as the winner of the
#-random guessing game
def displayFinalResult(Firstplayer_scorecount,Secondplayer_scorecount):

    #This will be displayed as the scoreboard of human and computer, it 
    #-stores the score of both players from previous game rounds
    print("Score: 'Human': "+ str(Firstplayer_scorecount) + " 'Computer': " + str(Secondplayer_scorecount) + "." ,end = ' ')
    
    if Firstplayer_scorecount > Secondplayer_scorecount:

        #This message will be displayed on the screen, if Human's score is 
        #-higher than computer
        print("Winner is Human!")
    else:

        #Meanwhile, this message will be displayed on the screen, if 
        #-Computer's score is higher than human
        print("Winner is Computer!")     

#This will be used for the main function, the purpose is to run the 
#-guessing number game program
def main():
    #List of the variables

    #The variable below is the default number for the game count, since 
    #-both players haven't input any number
    game_counting_number = 1

    #This variable displays as player 1, as Human
    player1 = "Human"

    #This variable displays as player 2, as Computer
    player2 = "Computer"

    #The default score count for first player, Human
    Firstplayer_scorecount = 0

    #The default score count for second player, Computer
    Secondplayer_scorecount = 0

    #Victory role describes who will get the first turn to guess, that is,
    #-player 1, Human
    victory_role = player1

    #This function is to create an infinite loop, it will run without any 
    #-conditions unless there's a break statement to stop the program
    while True:
        
        #This shows the default guess number count as both players haven't 
        #-take any single turn
        guessnumber_count = 0

        #This displays the default guess of the random guessing number game
        defaultguess = -1

        #This shows the minimum value of the given number below
        minimum_limit = 0

        #This shows the maximum value of the given number below
        maximum_limit = 100

        #This function is used to generate the random number from the range
        #-of minimal value and maximal value
        random_generated_number = random.randint(minimum_limit,maximum_limit)

        #This will display as the default game round
        print("Game : " + str(game_counting_number))

        #Initiate the loop to repeat any default guess until the random 
        #-generated number was guessed correctly
        while defaultguess != random_generated_number:
            if victory_role == player1:
                if guessnumber_count%2 == 0:

                    #Human will take turn to guess, depending on the guess 
 		            #-number count
                    defaultplayer = player1
                else:

                    #It will switch to "Computer", if human guesses 
 		            #-incorrectly
                    defaultplayer = player2
            else:
                if guessnumber_count%2 == 0:

                    #Computer will take turn to guess, depending on the 
 			        #-guess number count
                    defaultplayer = player2
                else:

                    #It will switch back to "Human", if computer guesses 
 			        #-incorrectly
                    defaultplayer = player1

            #This function shows the final result of both players, either 
            #-human or computer
            #Moreover, it will determine one of the two players that will 
            #-be decided as the winner of the game
            defaultguess = dealWithATurn(defaultplayer,minimum_limit,maximum_limit)    

            if defaultguess < random_generated_number:

                #The minimum limit changes, depending on the previous 
 	            #-default guess and increases by 1
                minimum_limit = defaultguess + 1

            if defaultguess > random_generated_number:

                #The maximum limit changes, depending on the previous 
 	            #-default guess and decreases by 1
                maximum_limit = defaultguess - 1

            if defaultguess != random_generated_number:

                #This message will be displayed on the screen, if both 
 	            #-players guessed the number incorrectly
                print("Incorrect!\n")

            #The guess number count increases by 1, this will determine who
 	        #-will get turn to repeat guess
            guessnumber_count = guessnumber_count + 1
        
        #This message will be shown on the screen, to declare who wins the 
        #-game
        print(str(defaultplayer) + " wins!\n")

        #This shows that whoever wins the round before, will get the first
        #-turn to guess on the next round
        victory_role = defaultplayer

        if defaultplayer == player1:

            #This shows that first player, human will acquire one point, if
 	        #-first player wins from a game round
            Firstplayer_scorecount = Firstplayer_scorecount + 1

        elif defaultplayer == player2:

            #This shows that second player, computer will acquire one 
 		    #-point, if second player wins from a game round
            Secondplayer_scorecount = Secondplayer_scorecount + 1

        if Firstplayer_scorecount == 3 or Secondplayer_scorecount == 3:

            #This function is used to display the result of both players 
 		    #-from all rounds
            #Whoever has already reached 3 points will be declared as the
 	        #-winner of the random guessing game
            displayFinalResult(Firstplayer_scorecount,Secondplayer_scorecount)

            #This function is used to end the game program
            exit()

        #The game counting number will increase by 1, as the previous round	  #-is over
        game_counting_number = game_counting_number + 1

main()