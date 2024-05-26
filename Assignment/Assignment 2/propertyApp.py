class Property:
    def __init__(self, location, price, Type, size):
        self.location = location
        self.price = price
        self.Type = Type
        self.size = size

    def setLocation(self, location):
        self.location = location

    def setPrice(self, price):
        self.price = price

    def setType(self, Type):
        self.Type = Type

    def setSize(self, size):
        self.size = size
        
    def getLocation(self):
        return self.location

    def getPrice(self):
        return self.price

    def getType(self):
        return self.Type

    def getSize(self):
        return self.size

    def typeString(self):
        confirmedType = ""
        if(self.Type.lower() == "a"):
            confirmedType = "apartment"
        elif(self.Type.lower() == "b"):
            confirmedType = "bungalow"
        elif(self.Type.lower() == "c"):
            confirmedType = "condominium"
        else:
            confirmedType = "Invalid"

        return confirmedType

    def annualTax(self):
        confirmedCost = 0.0
        if(self.Type.lower() == "a"):
            confirmedCost = self.price * 2.5 / 100
        elif(self.Type.lower() == "b"):
            confirmedCost = self.price * 4.5 / 100
        elif(self.Type.lower() == "c"):
            confirmedCost = self.price * 3.5 / 100
        else:
            confirmedCost = 0

        return confirmedCost
    
    def __eq__(self, obj):
        if(self.location == obj.location and self.Type == obj.Type and self.size == obj.size):
            return True
        else:
            return False

    def __lt__(self, obj):
        if(self.size < obj.size):
            return True
        else:
            return False

    def __le__(self, obj):
        if(self.size <= obj.size):
            return True
        else:
            return False

    def __str__(self):
        return str(self.typeString().capitalize()) + ", " + str(self.size) + " square feet, at " + str(self.location) + ", costing $" + "{:.2f}".format(self.price)

class PropertyList:
    def __init__(self, companyName):
        self.companyName = companyName
        self.propertyList = []

    def getCompanyName(self):
        return self.companyName

    def getPropertyList(self):
        return self.propertyList

    def setCompanyName(self, companyName):
        self.companyName = companyName

    def addProperty(self, obj):
        self.propertyList.append(obj)
    
    def noOfProperties(self):
        return len(self.propertyList)

    def allProperties(self):
        strAllProperties = ""
        for Property in self.propertyList:
            strAllProperties += str(Property) + "\n"
        return strAllProperties

    def totalPrice(self):
        ttlPrices = 0.0
        for Property in self.propertyList:
            ttlPrices += Property.getPrice()
        return ttlPrices

    def mostExpensiveProperty(self):
        mostExpensiveProperty = self.propertyList[0]
        for Property in self.propertyList:
            if(Property.getPrice() > mostExpensiveProperty.getPrice()):
                mostExpensiveProperty = Property
        return mostExpensiveProperty

    def findPropertyByType(self, Type):
        filteredList = []
        strDisplayPropertiesByType = ""
        for Property in self.propertyList:
            if(Property.getType().lower() == Type.lower()):
                filteredList.append(Property)
                
        if not filteredList:
            strDisplayPropertiesByType += "No property of that specific type yet"
        else:
            strDisplayPropertiesByType += "The properties are:\n"
            for Property in filteredList:
                strDisplayPropertiesByType += "At " + Property.getLocation() + " with " + str(Property.getSize()) + " square feet, cost $" + '{:.2f}'.format(Property.getPrice()) + "\n"
        return strDisplayPropertiesByType
        
    def sellProperty(self, obj):
        if(obj >= self.noOfProperties()):
            return "Empty"
        else:
            del self.propertyList[obj]

    def sortedProperties(self, param):
        sortedList = []

        if(param == "price"):
            for i in range(len(self.propertyList)):
                sortedList.append(self.propertyList[i])
            for i in range(len(sortedList)):
                key = sortedList[i]
                j = i - 1
                while(j >= 0 and key.getPrice() < sortedList[j].getPrice()):
                    sortedList[j+1] = sortedList[j]
                    j -= 1
                sortedList[j+1] = key

        if(param == "tax"):
            for i in range(len(self.propertyList)):
                sortedList.append(self.propertyList[i])
            for i in range(len(sortedList)):
                key = sortedList[i]
                j = i - 1
                while(j >= 0 and key.annualTax() < sortedList[j].annualTax()):
                    sortedList[j+1] = sortedList[j]
                    j -= 1
                sortedList[j+1] = key
        
        if(param == "size"):
            for i in range(len(self.propertyList)):
                sortedList.append(self.propertyList[i])
            for i in range(len(sortedList)):
                key = sortedList[i]
                j = i - 1
                while(j >= 0 and key.getSize() < sortedList[j].getSize()):
                    sortedList[j+1] = sortedList[j]
                    j -= 1
                sortedList[j+1] = key

        return sortedList

    def saveToFile(self, fileName):
        strDetails = ""
        for Property in self.propertyList:
            propLocation = Property.getLocation()
            propPrice = Property.getPrice()
            propType = Property.getType()
            propSize = Property.getSize()

            strDetails += propLocation + "," + str(propPrice) + "," + propType + "," + str(propSize) + "\n"

        fileAccess = open(fileName, 'w')
        fileAccess.write(strDetails)
        fileAccess.close()

    def loadFromFile(self, fileName):
        self.propertyList = []
        fileAccess = open(fileName, 'r') 
        for line in fileAccess:
            strDetails = line.split(",")
            propLocation = strDetails[0]
            propPrice = float(strDetails[1])
            propType = strDetails[2]
            propSize = int(strDetails[3])

            propObj = Property(propLocation, propPrice, propType, propSize)
            self.addProperty(propObj)
        
        fileAccess.close()