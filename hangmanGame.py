import random

def guessNew (guessedFreq):
    guessedLetter = input("Please enter your letter guess: ")
    guessedLetter = guessedLetter.lower()

    while not guessedLetter.isalpha():
        print("Only letters allowed.\n")
        guessedLetter = input("Please enter your letter guess: ")
        guessedLetter = guessedLetter.lower()


    while guessedLetter in guessedFreq.keys():
        print("Already guessed that one! Try again.\n")
        guessedLetter = input("Please enter your letter guess: ")
        guessedLetter = guessedLetter.lower()


    if guessedLetter not in guessedFreq.keys():
            guessedFreq[guessedLetter] = 1
            return guessedLetter

def printHangman(numOfFails):
    if numOfFails == 0:
        print("-----")
        print("|   |    ")
        print("|")
        print("|")
        print("|")
        print("|")
        print("---------\n")

    elif numOfFails == 1:
        print("-----")
        print("|   |    ")
        print("|   O")
        print("|")
        print("|")
        print("|")
        print("---------\n")
    elif numOfFails == 2:
        print("-----")
        print("|   |    ")
        print("|   O")
        print("|   -")
        print("|")
        print("|")
        print("---------\n")

    elif numOfFails == 3:
        print("-----")
        print("|   |    ")
        print("|   O")
        print("|  >-")
        print("|")
        print("|")
        print("---------\n")

    elif numOfFails == 4:
        print("-----")
        print("|   |    ")
        print("|   O")
        print("|  >-<")
        print("|")
        print("|")
        print("---------\n")
    else:
        print("-----")
        print("|   |    ")
        print("|   O")
        print("|  >-<")
        print("|   ^")
        print("|")
        print("---------\n")

def randomWord(l):
    with open('words.txt') as f:
        all_words = f.read().splitlines()
        return random.choice([i for i in all_words if len(i) == l])
    
def playHangman():
    lenOfWord = input("Please how many letters you would like the word to have (between 2 and 14): ")
    while int(lenOfWord) < 2 or int(lenOfWord) > 14:
        print("Length of word must be between 2 and 14 characters.")
        lenOfWord = input("Please how many letters you would like the word to have (between 2 and 14): ")

    goalWord = randomWord(int(lenOfWord))

    guesses = []
    guessedLetter = ""
    failureCounter = 0
    alreadyGuessed = {}

    for char in goalWord: #populate guesses list
        guesses.append("_")

    while guesses != list(goalWord):
        print(guesses) #print guessing loop, exit when found a new letter to check

        guessedLetter = guessNew(alreadyGuessed)

        if guessedLetter in goalWord: 
            occurenceOfLetter = goalWord.count(guessedLetter) #find how often the letter appears
            
            if occurenceOfLetter == 1:
                indexToChange = goalWord.find(guessedLetter)
                guesses.pop(indexToChange)
                guesses.insert(indexToChange, guessedLetter)

            else: #loop for mutiple occureces
                prevIndex = -1
                while occurenceOfLetter > 0:
                    indexToChange = goalWord.find(guessedLetter, prevIndex+1)
                    guesses.pop(indexToChange)
                    guesses.insert(indexToChange, guessedLetter)
                    prevIndex = indexToChange
                    occurenceOfLetter -= 1
            print("Great job! You got one!\n")
        else:
            print("Aw, not quite.")
            printHangman(failureCounter)
            failureCounter+= 1
            if failureCounter > 5:
                print(f"Game Over X. Correct word was '{goalWord}'\n")
                return

    print(f"Congrats! You guessed the word! It was '{goalWord}'")


playHangman()
