sentence = input("Enter a sentence with special characters: ") 
sentenceWords = sentence.split() 
print(sentenceWords)


vowels = ['A','E','I','O','U','a','e','i','o','u']
consonants = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 
    'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z', 'b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
vowelCount = 0
consonantCount = 0

def checkvowelsConsonants(sentenceWords):
    global vowelCount, consonantCount 
    for word in sentenceWords:
        for letter in word:  
            if letter in vowels:
                vowelCount += 1
            elif letter in consonants:
                consonantCount += 1
                break
                
checkvowelsConsonants(sentenceWords)

    
printOrExit = input("Do you want to know the vowel & consonant count (1), or want to exit program? (2) ")
if int(printOrExit) == 1:  
    print(f"There are {vowelCount} vowels and {consonantCount} consonants.")
else:
    print("Thanks for playing")
