#Assignment 1 Python
#Section      : Task #2
#Name         : Enrico Junior
#Student's ID : E2100297

#Display introduction message
print("\nThis is a 2-player mode guessing number program")
print("Created by Enrico Junior, E2100297\n")

#Importing the random module, to generate random numbers for the guessing #-number game program
import random

#This will be used as the main function, to start the game program
def main():
    #This shows the list of the variables that are available for the 2p 
    #-guessing game program

    #It will display player 1, this player will get the first turn for the 
    #-guessing game
    player1 = "Player 1"

    #It will display player 2, this player will get his/her turn as player 
    #-1's turn is over
    player2 = "Player 2"

    #This will display the minimum limit of the given number below
    min_limit = 0

    #This will display the maximum limit of the given number below
    max_limit = 100

    #This shows player 1 is getting the first attempt for guessing the 
    #-generated number
    player_role = player1

    #It will be generating the number that is determined from the range of
    #-the minimum limit and maximum limit
    generated_number = random.randint(min_limit,max_limit)

    #It displays the current guess number count for the guessing game 
    #-program
    guess_numbercount = 1

    #It will print out the player role, that is player 1
    print(player_role)

    #This formula display that player 1 is given the chance to guess the 
    #-number for the first attempt
    guess = int(input("Number ranges from " + str(min_limit) + " to " + str(max_limit) + "\nWhat is your guess? "))

    #Initiate the loop to ensure either player 1 or player 2 can repeat any
    #-guesses
    while guess_numbercount:

        #This message will be shown if any player between player 1 or 
        #-player 2, guessed the number correctly
        if guess == generated_number:
            print("\nCongratulation! " + str(player_role) + " wins!")

            #It will end the program as the guessing number game finishes
            break

        #Player 1 will take turn to guess
        if player_role == player1:

            #It will switch to player 2 turn if player 1 guessed the number		
            #-incorrectly
            player_role = player2
            if guess < min_limit:

                #This message will be shown if player 1 guessed the number
                #-lower than the minimum limit
                print("Incorrect!\n")
                print(player_role)

                #This message will be displayed in the screen, asks player		    
                #-to guess the number between minimum limit and maximum limit
                print("Please guess the number between " + str(min_limit) + " to " + str(max_limit))

                #It will switch to player 2, player 2 is given a chance to
                #-guess
                guess = eval(input("Number ranges from " + str(min_limit) + " to " + str(max_limit) + "\nWhat is your guess? "))
            elif guess > max_limit:

                #This message will be shown if player 1 guessed the number 
                #-higher than the maximum limit
                print("Incorrect!\n")
                print(player_role)

                #This message will be shown in the screen, asks player to
                #-guess the number between minimum limit and maximum limit
                print("Please guess the number between " + str(min_limit) + " to " + str(max_limit))

                #It will switch to player 2, player 2 is given a chance to 
                #-guess
                guess = eval(input("Number ranges from " + str(min_limit) + " to " + str(max_limit)) + "\nWhat is your guess? ")
            elif guess < generated_number:

                #It will display this message if player 1 guessed the
                #-number higher than generated number
                print("Incorrect!\n")
                print(player_role)

                #The value of the minimum limit will be modified, according
                #-to the guessed number and increases by 1
                min_limit = guess + 1

                #It will switch to player 2, player 2 is given a chance to 
                #-guess
                guess = eval(input("Number ranges from " + str(min_limit) + " to " + str(max_limit) + "\nWhat is your guess? "))
            else:
                #It will display the message below, as player 1 guessed the		    
                #-number lower than generated number
                print("Incorrect!\n")
                print(player_role)

                #The value of the maximum limit will be modified, according
                #-to the gueesed number and decreases by 1
                max_limit = guess - 1

                #It will switch to player 2, player 2 is given a chance to 
                #-guess
                guess = eval(input("Number ranges from " + str(min_limit) + " to " + str(max_limit) + "\nWhat is your guess? "))
        
        #Player 2 will take turn to guess
        elif player_role == player2:

            #It will switch to player 1 if player 2 guessed the number 
            #-incorrectly 
            player_role = player1
            if guess < min_limit:

                #This message will be shown if player 2 guessed the number
                #-lower than the minimum limit
                print("Incorrect!\n")
                print(player_role)

                #This message will be displayed in the screen, asks player 
                #-to guess the number between minimum limit and maximum 
                #-limit
                print("Please guess the number between " + str(min_limit) + " to " + str(max_limit))

                #It will switch to player 1, player 1 is given a chance to 
                #-guess
                guess = eval(input("Number ranges from " + str(min_limit) + " to " + str(max_limit) + "\nWhat is your guess? "))
            elif guess > max_limit:

                #This message will be shown if player 2 guessed the number 
                #-higher than the maximum limit
                print("Incorrect!\n")
                print(player_role)
                
                #This message will be displayed in the screen, asks player 
                #-to guess the number between minimum limit and maximum 
                #-limit
                print("Please guess the number between " + str(min_limit) + " to " + str(max_limit))

                #It will switch to player 1, player 1 is given a chance to 
                #-guess
                guess = eval(input("Number ranges from " + str(min_limit) + " to " + str(max_limit) + "\nWhat is your guess? "))
            elif guess < generated_number:

                #It will display this message if player 2 guessed the 
                #-number lower than generated number
                print("Incorrect!\n")
                print(player_role)

                #The value of the minimum limit will be modified, according	          
                #-to the guessed number and increases by 1
                min_limit = guess + 1

                #It will switch to player 1, player 1 is given a chance to
                #-guess
                guess = eval(input("Number ranges from " + str(min_limit) + " to " + str(max_limit) + "\nWhat is your guess? "))
            else:
                #It will display this message if player 2 guessed the 
                #-number higher than generated number
                print("Incorrect!\n")
                print(player_role)

                #The value of the maximum limit will be modified, according	          
                #-to the guessed number and decreases by 1
                max_limit = guess - 1

                #It will switch to player 1, player 1 is given chance to
                #-guess 
                guess = eval(input("Number ranges from " + str(min_limit) + " to " + str(max_limit) + "\nWhat is your guess? "))
                    
                    
main()