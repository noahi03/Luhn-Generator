import os

# put your 8 digit BIN here
starting = "48472212"


i = 0
file = open("luhns_output.txt", 'a')

while i <= 9999999:
    length = len(str(i))
    amountOfZerosToAdd = "0" * (7 - length)
    fullCardNumber = starting + amountOfZerosToAdd + str(i)
    
    
    #perform checksum calculation
    totalSum = 0
    for idx, z in enumerate(fullCardNumber):
        sum = 0
        if idx%2==0:
            initialSum = int(z) * 2
            if initialSum >= 10:
                sum = int(str(initialSum)[0]) + int(str(initialSum)[1]) 
            else:
                sum = initialSum
        else:
            sum = int(z)
        
        totalSum += sum


    checksum = (10 - (totalSum%10))%10

    fullCardNumber += str(checksum)

    file.write(fullCardNumber + "\n")
    

    i += 1

file.close()
    
