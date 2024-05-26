#Assignment 1 Python
#Section      : Task #4
#Name         : Enrico Junior
#Student's ID : E2100297

#Display introduction message
print("\nThis is a guessing number game program with multiple rounds, Human vs Computer")
print("Created by Enrico Junior, E2100297\n")

#Importing the random module, this will activate the generated random 
#-number for the number guessing game
import random

#This will be used for the main function, the purpose is to run the 
#-guessing number game program
def main():
    #List of the variables:

    #The variable below is the default number for the game count, since 
    #-both players haven't input any number
    game_counting_number = 1

    #This will display as the first player of the game, Human
    first_player = "Human"

    #This will display as the second player of the game, Computer
    second_player = "Computer"

    #The default score count for the first player, Human
    firstplayer_scorecount = 0

    #The default score count for the second player, Computer
    secondplayer_scorecount = 0

    #Victory role describes who will get the first turn to play the 
    #-guessing number game, that is, first player "Human"
    victory_role = first_player

    #This function is to create an infinite loop, it will run without any 
    #-conditions unless there's a break statement to stop the program
    while True:
        #This shows the default guess number count as both players haven't
        #-take any single turn
        guessnumber_count = 0

        #This displays the default guess of the random guessing number game
        default_guess = -1

        #This shows the minimum value of the given number below
        minimal_limitation = 0

        #This shows the maximum value of the given number below
        maximal_limitation = 100

        #This function is used to generate the random number from the range
        #-of minimal value and maximal value
        random_generated_number = random.randint(minimal_limitation,maximal_limitation)

        #This message displays the round/stage
        print("Game : " + str(game_counting_number))

        #Initiate the loop to repeat any default guess until the random 
        #-generated number was guessed correctly
        while default_guess != random_generated_number:
            if victory_role == first_player:
                if guessnumber_count%2 == 0:

                    #Human will take turn to guess, depending on the guess
                    #-number count
                    player_role = first_player
                else:

                    #It would switch to "Computer", if human guessed 
                    #-incorrectly
                    player_role = second_player
            else:
                if guessnumber_count%2 == 0:

                    #Computer will take turn to guess, depending on the 
                    #-guess number count
                    player_role = second_player
                else:

                    #It would switch back to "Human", if computer guessed 
 			        #-incorrectly
                    player_role = first_player

            #This will display on the screen, to show the player’s name, to
 		    #-prevent confusion who will take turn to guess
            print("Player : " + str(player_role))

            #This will print out the number ranges from the minimal 
 		    #-limitation to maximal limitation statement
            print("Range " + str(minimal_limitation) + " --> " + str(maximal_limitation) + ".", end = ' ')

            if player_role == first_player:

                #This function shows that player will input any number 
 		        #-manually
                default_guess = eval(input("Your guess? "))

            elif player_role == second_player:

                #This function shows how computer will generate the number 
 	            #-automatically
                default_guess = random.randint(minimal_limitation,maximal_limitation)

                #This message shows what number will be guessed by the 
 		        #-computer
                print("Computer guess " + str(default_guess))

            if default_guess < random_generated_number:

                #The minimal limitation will be modified, according to the 
 		        #-default guess value and increases by 1
                minimal_limitation = default_guess + 1

            if default_guess > random_generated_number:

                #The maximal limitation will be modified, according to the 
 		        #-default guess value and decreases by 1
                maximal_limitation = default_guess - 1

            if default_guess != random_generated_number:

                #This message will be displayed if both players guessed the
 	            #-number incorrectly
                print("Incorrect!\n")
            
            #The guess number count will increase by 1, this will determine
 	        #-who will get the turn to guess
            guessnumber_count = guessnumber_count + 1

        #This message will be shown on the screen, if one of the two 
        #-players input the right number
        print(str(player_role) + " wins!\n") 

        #This shows whoever wins the previous round will get the first turn
        #-for the next round
        victory_role = player_role

        if player_role == first_player:
            
            #First player will get one point as first player wins
            firstplayer_scorecount = firstplayer_scorecount + 1
        else:

            #Meanwhile, second player will get one point as second player 
            #-wins
            secondplayer_scorecount = secondplayer_scorecount + 1

        if firstplayer_scorecount == 3 or secondplayer_scorecount == 3:

            #This message will be displayed as the scoreboard of both 
 		    #-players score count
            print("Score : " + "'" + str(first_player) + "': " +  str(firstplayer_scorecount) + " '" + str(second_player) + "': " + str(secondplayer_scorecount) + ".", end = ' ')

            if firstplayer_scorecount > secondplayer_scorecount:

                #This message will be displayed on the screen if human wins
 		        #-the game
                print("Winner is Human!")

                #This function is used to end the game program
                break
            else:

                #While this message will be displayed on the screen if 
 	            #-computer wins the game
                print("Winner is Computer!")

                #This function is used to end the game program
                break

        #The game counting number increases by 1, as a certain round has 
        #-finished
        game_counting_number = game_counting_number + 1

main()
