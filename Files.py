def main(): #Makes main function 
    file = open("inp_file.txt", "w") #Opens the file
    file.write("Python is an interpreted, high-level, and general-purpose programming language.\n") #Writes this in the file
    file.close() #Closes the file

    #Askes user for file name they want
    Inputfile = input("Enter the input file name (e.g: inp_file.txt): ")
    OutputfileTwo = input("Enter the output file name (e.g: out_file.txt): ")

    file = open("inp_file.txt", 'r') #Displays the informaion in the inputed file
    print("\nDisplaying the contents of the input file.....\n")
    print(file.read())
    file.close() #Closes file

    try:
        file = open("out_file.txt", 'r') #Opens file
        content = file.read() #Reads the file
        print(content) #
    except FileNotFoundError: #If file is not found
        print("The file out_file.txt does not exist.") #Prints this
        
    fileOne = open('inp_file.txt', "r") #opens fie in reading mode
    fileTwo = open('out_file.txt', "w") #opens file in writing mode

    linecount = 0 #Makes line count 0
    charcount = 0 #Makes charachter count 0
    for i in fileOne:
        linecount += 1 #iterements the line count
        charcount += len(i) #iterements the character count
        fileTwo.write(i) #writes the content from fileOne to fileTwo

    print("################## After copy from input to output file ##################\n")
    print(f"{linecount} line and {charcount} chars have been copied to the output file\n") #Prints the lines and characters in the file
    fileOne.close() #closes the file
    fileTwo.close() #closes the file

    fileTwo = open('out_file.txt', 'a')
    fileTwo.write("It was created by Guido van Rossum and first released in 1991.\n")
    fileTwo.close()
    print("################## After append to the output file ##################\n")

    fileTwo = open('out_file.txt', 'r') #opens the file
    line2count = 0 #Makes line count 0
    char2count = 0 #Makes charachter count 0

    for j in fileTwo:
        line2count += 1 #iterements the line count
        char2count += len(j) #iterements the character count

    #Prints the information
    print(f"Updated count of lines in the output file is: {line2count}")
    print(f"Updated count of characters in the output file is: {char2count}")
    print("\nDisplaying the contents of the output file.....\n")
    fileTwo.close() #Closes the file

    fileTwo = open('out_file.txt', 'r') #opens the file
    print(fileTwo.read())
    fileTwo.close()

main()



