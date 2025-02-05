import string
words = ("HeLlO wOrLd!!11", "Did you hear about the one-eyed one-horned Flying Purple People Eater?") #Words we use to test the function

def getStringInfo(*args): #Makes function
    #loops though each string
    for combineWords in args: 

        #Splits the string into a list
        separatedWord = combineWords.split() 

        print('\n',"##################################################################", '\n')
        print(combineWords) #Prints the word

        print('{:31} {}'.format("# of words - ", len(separatedWord))) # Calculate number of words
 
        print('{:31} {}'.format("# of chars - ", len(combineWords.replace(" ", "")))) # Calculates number of characters excluding spaces

        numLetters = len([c for c in combineWords if c.isalpha()]) # Calculates number of letters
        print('{:31} {}'.format("# of letters - ", numLetters))

        numDigits = len([d for d in combineWords if d.isdigit()]) # Calculates number of digits
        print('{:31} {}'.format("# of numbers - ", numDigits))

        numPunctuation = len([p for p in combineWords if p in string.punctuation]) # Calculates number of punctuation marks
        print('{:31} {}'.format("# of punctuations - ", numPunctuation))

        isStringNumeric = combineWords.isdigit() # Sees the string is digits only
        print('{:31} {}'.format("Is number - ", isStringNumeric))

        numUppercase = len([u for u in combineWords if u.isupper()]) # Calculates number of uppercase characters
        print('{:31} {}'.format("# of uppercase chars - ", numUppercase))

        numLowercase = len([l for l in combineWords if l.islower()]) # Calculates number of lowercase characters
        print('{:31} {}'.format("# of lowercase chars - ", numLowercase))

        print('{:31} {}'.format("Lowercase:", combineWords.lower())) # Converts to lowercase
        print('{:31} {}'.format("Uppercase:", combineWords.upper())) # Converts to uppercase
        print('{:31} {}'.format("Reversed case:", combineWords.swapcase())) # Swaps case
        print('{:31} {}'.format("No spaces:", combineWords.replace(" ", ""))) # Removes spaces
        print('{:31} {}'.format("Title case:", combineWords.title())) # Converts to title
        print('{:31} {}'.format("Reversed:", combineWords[::-1])) # Reverses the string

getStringInfo(*words) # Calls function and passes the words though the funtion
