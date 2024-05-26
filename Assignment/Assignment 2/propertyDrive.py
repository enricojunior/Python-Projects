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
        elif(choiceSelection == 5):
            if(myProperty.noOfProperties() == 0):
                print("No property has been registered yet")
            else:
                sellPropertyController()
        elif(choiceSelection == 6):
            if(myProperty.noOfProperties() == 0):
                print("No property has been registered yet")
            else:
                showSortedProperties()
        elif(choiceSelection == 7):
            if(myProperty.noOfProperties() == 0):
                print("No property has been registered yet")
            else:
                loadFile()
        elif(choiceSelection == 8):
            if(myProperty.noOfProperties() == 0):
                print("No property has been registered yet")
            else:
                saveFile()
        else:
            print("Invalid choice! Try again!")

        choiceSelection = propertyMenu()

    print("Sayonara...")

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
        print(myProperty.findPropertyByType(userType))
    else:
        print("Invalid property type entered! Returning to the main menu..")

def sellPropertyController():
    indexRange = int(input("Property to sell (1.." + str(myProperty.noOfProperties()) + ")? "))
    if(indexRange <= 0):
        print("Out of range....")
    elif(indexRange > myProperty.noOfProperties()):
        print("Out of range....")
    else:
        print(str(myProperty.getPropertyList()[indexRange-1]) + " has been sold.")
        myProperty.sellProperty(indexRange-1)

def showSortedProperties():
    print("Sorting properties")
    criteria = input("- criteria (price, tax, or size): ")
    if(criteria.lower() == "price"):
        for i in myProperty.sortedProperties("price"):
            print(str(i))
    elif(criteria.lower() == "tax"):
        for i in myProperty.sortedProperties("tax"):
            print(str(i) + " with annual tax $" + '{:.2f}'.format(i.annualTax()))
    elif(criteria.lower() == "size"):
        for i in myProperty.sortedProperties("size"):
            print(str(i))
    else:
        print("Invalid criteria! Please try again!")

def loadFile():
    LoadfileName = input("File name to load from: ")
    myProperty.loadFromFile(LoadfileName)

def saveFile():
    SavefileName = input("File name to save to: ")
    myProperty.saveToFile(SavefileName)

def propertyMenu():
    print("")
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