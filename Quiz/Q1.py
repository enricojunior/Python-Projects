# isValidUsername function
def isValidUsername(Username):
    lengthValidator = False
    usernameLength = len(Username)
    if(usernameLength >= 8 and usernameLength <= 15):
        lengthValidator = True

    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    digits = "0123456789"
    chars = "!@$%&"

    # Method to validate the whole operation
    capitalValidator = False
    for i in Username:
        if(i in uppercase):
            capitalValidator = True

    digitValidator = False
    for i in Username:
        if(i in digits):
            digitValidator = True

    # Method to validate the number of small letters, where a username must contain at least two small letters
    LetterValidator = False
    smallLettersNum = 0
    for i in Username:
        if(i in lowercase):
            smallLettersNum += 1
            if(smallLettersNum >= 2):
                LetterValidator = True

    # Method to validate digit, where a username must not begin with a digit
    FirstDigitValidator = True
    for i in Username[0]:
        if(i in digits):
            FirstDigitValidator = False

    # Method to validate special characters
    CharsValidator = False
    for i in Username:
        if(i in chars):
            CharsValidator = True 
    
    if(lengthValidator and digitValidator and FirstDigitValidator and CharsValidator and LetterValidator and capitalValidator):
        return True 
    else:
        return False

# Main Function
def main():
    totalCount = 0
    validCount = 0
    usernameInput = "test"

    while(usernameInput != ""):
        usernameInput = input("Enter a username (<Enter>) to quit: ")

        if(usernameInput == ""):
            break

        if(isValidUsername(usernameInput)):
            print("... is valid username\n")
            validCount += 1
        else:
            print("... is invalid username\n")
        totalCount += 1

    if(totalCount == 0):
        print("\nNo username entered!")
    else:
        print("\n" + str(validCount) + " valid username(s) out of " + str(totalCount) + " entered")
main()