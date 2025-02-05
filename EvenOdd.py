evenlist = [] # Makes list
oddlist = [] # Makes list

while True:  #Make a loop for repeting loop if user wants
    while True:
        userInput = int(input("Enter a set of userInputbers. Enter -1 once all userInputbers are inputted: ")) #Askes user input
        if userInput == -1: #If user enters -1, then stops asking
            break
        if userInput % 2 == 0: # Sees if number is even, then add in list
            evenlist.append(userInput)
        else: # Sees if number is odd, then add in list
            oddlist.append(userInput)

    print("Even userInputbers:", evenlist) #Prints list 
    print("Odd userInputbers:", oddlist) #Prints list

    def SumOfEvenOdd(evenlist, oddlist): 
        evenSum = sum(evenlist)  # Adds all the numbers in the set
        oddSum = sum(oddlist)    # Adds all the numbers in the set
        return evenSum, oddSum #Return sun

    evenSum, oddSum = SumOfEvenOdd(evenlist, oddlist) 
    print("Sum of even user input:", evenSum) #Prints list
    print("Sum of odd user input:", oddSum) #Prints list

    def PrintResults(avgeven, avgodd):  # This function takes averages as input and prints them
        if len(evenlist) > 0:  # Checks if there are even numbers
           # avgeven = even_sum / len(evenlist)  # Calculates average of even numbers
            print("Average of even numbers:", avgeven)  # Prints average of even numbers

        if len(oddlist) > 0:  # Checks if there are odd numbers
          #  avgodd = odd_sum / len(oddlist)  # Calculates average of odd numbers
            print("Average of odd numbers:", avgodd)  # Prints average of odd numbers
    
        PrintResults(avgeven, avgodd)  # Calls the function to print results


    def CalculatePow(mylist): #makes power function
        for index in range(len(mylist)):
            mylist[index] = pow(mylist[index], index) #Adds the power calcaulton
        return mylist



    # Askes to repet the code
    repeat = input("Do you want to repeat the operation?: ")
    if repeat.lower() != "yes":
        print("Byee!")
        break
