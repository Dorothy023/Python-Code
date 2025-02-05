import random 

num = random.randint(1, 100) #Theres a ranbom number assigned to num

userInt = int(input("Enter your guess of the number (between 1 and 100): ")) #User enter there guess to guess the random number

while userInt != num: #Will keep looping till user get guess right
    if userInt < num: #If the guessed number is lower then random number, prints too low
        print("The number is too low.")
    elif userInt > num:#If the guessed number is higher then random number, prints too high
        print("The number is too high.")
    
    userInt = int(input("Enter your guess of the number (between 1 and 100): ")) #Will ask user to enter another number if incorrect guess before
    
#If user gets it right, will print this
print("You guessed right!")
