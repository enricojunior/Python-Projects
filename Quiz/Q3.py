def hasConnect(firstString, secondString):
    lwrFirst = firstString.lower()
    lwrSecond = secondString.lower()

    if(lwrFirst[-1] == lwrSecond[0]):
        return "true"
    else:
        return "false"

def entranceFee(adults, children, seniors):
    totalFee = 0
    
    if(adults <= 5):
        totalFee += adults * 50
    else:
        totalFee += 5 * 50 + (adults - 5) * 45

    if(children <= 5):
        totalFee += children * 25
    else:
        totalFee += 5 * 25 + (children - 5) * 20

    totalFee += seniors * 30
    return '${:.2f}'.format(totalFee)

def computeInts(firstInteger, secondInteger):
    num = 0
    if(firstInteger >= 0 and secondInteger >= 0):
        if(firstInteger % 2 != 0 and secondInteger % 2 != 0):
            num += (firstInteger - secondInteger)
        elif(firstInteger % 2 == 0 and secondInteger % 2 == 0):
            num += (firstInteger + secondInteger)
        else:
            num += (firstInteger * secondInteger)
    elif(firstInteger < 0 and secondInteger < 0):
        num += ((firstInteger ** 2) - (secondInteger ** 2))
    else:
        num += ((firstInteger ** 2) + (secondInteger ** 2))

    return num

def main():
    print(hasConnect("James", "Sammy"))
    print(entranceFee(5,0,0))
    print(computeInts(-3,5))
    
main()