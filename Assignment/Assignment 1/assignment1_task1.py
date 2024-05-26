#Assignment 1 Python
#Section      : Task #1
#Name         : Enrico Junior
#Student's ID : E2100297

#This is a guessing number game program to guess the random generated 
#-number, and it will count the number of user guess
#Created by Enrico Junior, E2100297

#Display introduction message
print("\nThis is a guessing number game program to guess the random generated number, and it will count the number of user guess")
print("Created by Enrico Junior, E2100297\n")

#Importing the random module, to generate random numbers for the guessing number game program
import random

#This will be displayed as the main function, the purpose is to start the game program
def main():

    #Displaying the current number of guessing count since the player/user 
    #-haven't decided to input any number
    guess_number_count = 1
    
    #The minimum limit of the given number below
    minlimit = 0
    
    #The maximum limit of the given number below
    maxlimit = 100
    
    #Generating number that is determined between the minimum limit and 
    #-maximum limit, that is between 0 and 100
    number = random.randint(minlimit,maxlimit)
    
    #Players/Users are asked to input any number from the range of minimum
    #-limit to maximum limit
    #From the formula below, using function 'int' as integer is appropriate
    #-formula, since there will be no decimal number involved
    guess = int(input("Number ranges from " + str(minlimit) + " to " + str(maxlimit) + "\nWhat is your guess?? "))
    
    #Initiate the loop to ensure for all the Players/Users are able to 
    #-repeat guess, whenever they're guessing the number incorrectly
    while guess != number:
        #Expressing with boolean logic, with function "or"
        if guess < minlimit or guess > maxlimit:
            #This message will be shown to all Players/Users if they 
            #-guessed incorrectly
            print("Not correct. Try again!")

            #This message will be shown, if Players/Users guessed the 
 		    #-number lower than minimum limit or higher than maximum limit
            #Players/Users asked to type any numbers, as long as the number		
            #-is between 0 and 100
            print("Please type a number between " + str(minlimit) + " to " + str(maxlimit) + "!\n")

            #Players/Users are given another chance to guess, if they 
            #-guessed the number incorrectly
            guess = eval(input("Number ranges from " + str(minlimit) + " to " + str(maxlimit) + "\nWhat is your guess?? "))
        
        #This message will be shown to all Players/Users if they input the 
        #-number is lower than the generated number
        elif guess < number:
            print("Not correct. Try again!\n")
            
            #The value of the minlimit (left section) will change, based 
            #-from the guessed number and add the value by 1 
            minlimit = guess + 1 

            #Players/Users are given another chance to guess if they 
            #-guessed the number incorrectly
            guess = eval(input("Number ranges from " + str(minlimit) + " to " + str(maxlimit) + "\nWhat is your guess?? "))
        
        #This message will be shown to all Players/Users if they input the 
        #-number is higher than the generated number
        else:
            print("Not correct. Try again!\n")
            
            #The value of the maxlimit (right section) will change, based 
	        #-from the guessed number and minus the value by 1
            maxlimit = guess - 1
            
            #Players/Users are given another chance to guess, if they 
            #-guessed the number incorrectly
            guess = eval(input("Number ranges from " + str(minlimit) + " to " + str(maxlimit) + "\nWhat is your guess?? "))

        #The number of guess increased by 1 as the user guessed the number	  
        #-incorrectly
        guess_number_count = guess_number_count + 1

    if guess == number:

        #This message will be shown to Players/Users for guessing the 
        #-number correctly less than five times
        if guess_number_count < 5:
            print("\nCongratulations! you have done it in " + str(guess_number_count) + " tries!")
            print("You are lucky today!")
        #On the other hand, this message will be shown to Players/Users for
        #-guessing the number correctly more than five times
        else:
            print("\nCongratulations, you have done it in " + str(guess_number_count) + " tries!")

    #It will display the text below, if user moved on to the next stage, 
    #-stage 2
    print("\nNext, is the second section of the random guessing number game, Stage 2!")

    #Displaying the current number of guessing count since the player/user 
    #-haven't decided to input any number
    guess_number_count = 1

    #The minimum limit of the given number below
    min_limit = 0

    #The maximum limit of the given number below
    max_limit = 100

    #Generating number that is determined between the minimum limit and 
    #-maximum limit, that is between 0 and 100
    number = random.randint(min_limit,max_limit)

    #Players/Users are asked to input any number from the range of minimum
    #-limit to maximum limit
    #From the formula below, using function 'int' as integer is appropriate
    #-formula, since there will be no decimal number involved
    guess = int(input("Range : " + str(min_limit) + " ---> " + str(max_limit) + " Your guess?? "))

    #Initiate the loop to ensure for all the Players/Users are able to 
    #-repeat guess, whenever they're guessing the number incorrectly
    while guess != number:
        #Expressing with boolean logic with function "or"
        if guess < min_limit or guess > max_limit:
            #This message will be shown to all Players/Users if they 
            #-guessed incorrectly
            print("Incorrect!")

            #This message will be shown, if Players/Users guessed the 
            #-number lower than minimum limit or higher than maximum limit
            #Players/Users asked to type any numbers, as long as the number		
            #-is between 0 and 100
            print("Note : The number that should be guessed is between " + str(min_limit) + " to " + str(max_limit) + "!\n")

            #Players/Users are given another chance to guess, if they 
            #-guessed the number incorrectly
            guess = eval(input("Range : " + str(min_limit) + " ---> " + str(max_limit) + " Your guess?? "))
        elif guess < number:

            #This message will be shown to all Players/Users if they 
            #-guessed incorrectly
            print("Incorrect!\n")

            #The value of the min_limit (left section) will change, based 
            #-from the guessed number and add the value by 1
            min_limit = guess + 1

            #Players/Users are given another chance to guess, if they 
            #-guessed the number incorrectly
            guess = eval(input("Range : " + str(min_limit) + " ---> " + str(max_limit) + " Your guess?? "))
        else:

            #This message will be shown to all Players/Users if they 
            #-guessed incorrectly
            print("Incorrect!\n")

            #The value of the max_limit (right section) will change, based
            #-from the guessed number and minus the value by 1
            max_limit = guess - 1

            #Players/Users are given another chance to guess if they 
            #-guessed the number incorrectly
            guess = eval(input("Range : " + str(min_limit) + " ---> " + str(max_limit) + " Your guess?? "))

        #The number of guess increased by 1 as the user guessed the number
        #-incorrectly
        guess_number_count = guess_number_count + 1

    if guess == number:

        #This message will be shown to Players/Users for guessing the 
        #-number correctly less than five times
        if guess_number_count < 5:
            print("\nCongratulations, you have done it in " + str(guess_number_count) + " tries!")
            print("You are lucky today!")

        #On the other hand, this message will be shown to Players/Users for	  
        #-guessing the number correctly more than five times
        else:
            print("\nCongratulations, you have done it in " + str(guess_number_count) + " tries!")

main()