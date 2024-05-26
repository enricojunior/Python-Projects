from propertyApp import * 

propName = input("What's the name of your property company? ")
myProperty = PropertyList(propName)

def main():
    choiceSelection = propertyMenu()
    while(choiceSelection != 0):
        if(choiceSelection == 1):
            addNewProperty()
        elif(choiceSelection == 2):
            if(myProperty.noOfProperties() == 0):
                print("No property has been registered yet")
            else:
                showAllProperties()
        elif(choiceSelection == 3):
            if(myProperty.noOfProperties() == 0):
                print("No property has been registered yet")
            else:
                summaryInformation()
        elif(choiceSelection == 4):
            if(myProperty.noOfProperties() == 0):
                print("No property has been registered yet")
            else:
                displaySpecifiedProperties()
        else:
            print("Invalid choice! Try again!")

        print()
        choiceSelection = propertyMenu()

def addNewProperty():
    print("Adding a new property")
    Location = input("Location: ")
    Price = float(input("Price: "))
    Type = input("Property type ('A'partemen, 'B'ungalow, 'C'ondominium): ")
    Size = int(input("Size (in square feet, eg. 1438): "))
    newProperty = Property(Location, Price, Type, Size)

    # Additional validation purpose for the property type selection
    if(newProperty.getType().lower() == "a" or newProperty.getType().lower() == "b" or newProperty.getType().lower() == "c"):
        myProperty.addProperty(newProperty)
        print("... added successfully")
    else:
        print("Invalid Property Type! Failed to add the new property.. ")

def showAllProperties():
    print("Details of all properties: ")
    print(myProperty.allProperties())

def summaryInformation():
    print("Summary Information")
    print("Number of registered properties: " + str(myProperty.noOfProperties()))
    print("Total price: $" + '{:.2f}'.format(myProperty.totalPrice()))
    print("Most expensive property: " + str(myProperty.mostExpensiveProperty()))

def displaySpecifiedProperties():
    userType = input("Property type ('A'partment, 'B'ungalow, 'C'ondominimum): ")
    if(userType.lower() == "a" or userType.lower() == "b" or userType.lower() == "c"):
        print("The properties are:")
        print(myProperty.findPropertyByType(userType))
    else:
        print("Invalid property type entered! Returning to the main menu..")

def propertyMenu():
    print(str(myProperty.getCompanyName()))
    print("-" * 22)
    print("1 Add a property\n2 Display all properties\n3 Display summary information about property list")
    print("4 Display properties with user-specified type\n5 Sell a property based on given index")
    print("6 Display all properties, sorted according to Property values")
    print("7 Read properties information from file\n8 Write properties information to file\n")
    print("0 Quit")
    response = int(input("Your choice: "))
    return response

main()