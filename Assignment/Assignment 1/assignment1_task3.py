#Assignment 1 Python
#Section      : Task #3
#Name         : Enrico Junior
#Student's ID : E2100297

#Display introduction message
print("\nThis is a guessing number program as Human play against Computer")
print("Created by Enrico Junior, E2100297\n")

#Importing the random module, in order generating the random number for 
#-guessing number Player vs Computer program
import random

#This will be used as the main function, to start the guessing number game #-program
def main():
    #List of the variables

    #Displaying the minimum limit of the number given below
    minimized_limit = 0

    #Displating the maximum limit of the number given below
    maximized_limit = 100

    #This shows the first player as Human, first player needs to guess the 
    #-number manually
    firstplayer = "Human"

    #This shows the second player as Computer, second player will guess the
    #-number automatically
    secondplayer = "Computer"

    #The formula below will generate the random number between minimized 
    #-limit and the maximized limit
    random_generated_number=random.randint(minimized_limit,maximized_limit)

    #First player will get the first turn to guess the number
    player_guess_role = firstplayer

    #This shows that first player is asked to guess the random generated 
    #-number
    print("Player : " + str(player_guess_role))
    firstplayer_guess = eval(input("Number ranges from " + str(minimized_limit) + " to " + str(maximized_limit) + "\nWhat is your guess? "))
    
    #This function is used for activating the given codes below
    #Furthermore, this function will give as many chances for human and 
    #-computer to guess, if both players guessed incorrectly
    while True:

        #First player or as known as Human will take turn to guess
        if player_guess_role == firstplayer:

            #It will switch to computer, if human guessed the random 
            #-generated number incorrectly
            player_guess_role = secondplayer

            #This message will be shown if human guessed the random number 
            #-correctly
            if firstplayer_guess == random_generated_number:
                player_guess_role = firstplayer

                print(str(player_guess_role) + " wins!")
                #This section is used to end the game program
                break

            elif firstplayer_guess < minimized_limit:
                #This message will be displayed on the screen, if human 
                #-guessed the number lower than minimum limit
                print("Incorrect!")

                #This message will be shown to human, asked human to guess
                #-the number between minimum limit and maximum limit
                print("Please guess the number between " + str(minimized_limit) + " to " + str(maximized_limit) + "\n")

                #Switch to second player, computer
                print("Player : " + str(player_guess_role))
            elif firstplayer_guess > maximized_limit:
                #This message will be displayed on the screen, if human 
                #-guessed the number higher than maximum limit
                print("Incorrect!")

                #This message will be shown to human, asked human to guess
                #-the number between minimum limit and maximum limit
                print("Please guess the number between " + str(minimized_limit) + " to " + str(maximized_limit) + "\n")

                #Switch to second player, computer
                print("Player : " + str(player_guess_role))
            elif firstplayer_guess < random_generated_number:
                #This message will be displayed on the screen, if human 
                #-guessed the number lower than random generated number
                print("Incorrect!\n")

                #The value of the minimized limit will change, according to
                #-the first player guess and increases the value by 1
                minimized_limit = firstplayer_guess + 1

                #Switch to second player, computer
                print("Player : " + str(player_guess_role))
            else:
                #This message will be displayed on the screen if human 
                #-guessed the number higher than random generated number
                print("Incorrect!\n")

                #The value of the maximized number will change, according 
                #-to the first player guess and decreases the value by 1
                maximized_limit = firstplayer_guess - 1

                #Switch to second player, computer
                print("Player : " + str(player_guess_role))

        #Second player or as known as Computer, will take turn to guess
        if player_guess_role == secondplayer:

            #It would switch back to first player, if computer guessed the 
            #-number incorrectly
            player_guess_role = firstplayer
            
            #This shows how the computer will generate any number 
            #-automatically
            secondplayer_guess = random.randint(minimized_limit,maximized_limit)

            #This message displays what number that will be guessed by the 
            #-computer
            print("Number ranges from " + str(minimized_limit) + " to " + str(maximized_limit))
            print("Computer guess " + str(secondplayer_guess))

            #This message will be shown if computer guessed the number 
            #-correctly 
            if secondplayer_guess == random_generated_number:
                player_guess_role = secondplayer

                print(str(player_guess_role) + " wins!")               
                #This section is used to end/stop the game program
                break
            elif secondplayer_guess < random_generated_number:
                #This message will be displayed on the screen, if computer
                #-guess the number lower than random generated number
                print("Incorrect!\n")

                #The value of the minimized limit will change, according to
                #-second player guess and increases the value by 1
                minimized_limit = secondplayer_guess + 1

                #Switch back to first player, Human
                print("Player : " + str(player_guess_role))
            else:
                #This message will be displayed on the screen if computer 
                #-guess the number higher than random generated number
                print("Incorrect!\n")

                #The value of the maximized limit will change, according to	          
                #-second player guess and decreases the value by 1
                maximized_limit = secondplayer_guess - 1

                #Switch back to first player, Human
                print("Player : " + str(player_guess_role))

        #This formula is used for human to input any number, as long as
        #-it's player turn to guess the random generated number
        firstplayer_guess = eval(input("Number ranges from " + str(minimized_limit) + " to " + str(maximized_limit) + "\nWhat is your guess? "))

main()
