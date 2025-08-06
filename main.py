import random as rand
from tkinter import *
from tkinter import ttk
wordList = []
#testWordList = ["girls", "boys", "tongue", "titan", "maist", "malam", "fenks"]
startingWords = ["crane", "crate", "trace"]
blackLetters = []
greenLetters = ["_", "_", "_", "_", "_"]
yellowLetters = []
ALPHABET = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "w", "x", "y", "z"]
VOWELS = ["a", "e", "i", "o", "u", "y"]
def findWordByCharsPos(letters: list, inList: list = wordList): # Finds words containing given letters at given positions. _ indicates irrelevant position. Requires list exactly 5 items long. Returns list containing all matching words
    outlist = []
    if len(letters) != 5:
        return None
    lettersDict = dict()
    for i in range(len(letters)):
        tempLet = letters[i]
        lettersDict[i] = tempLet
    for word in inList:
        hasChars = True
        for i in range(5):
            if lettersDict[i] == "_":
                continue
            else:
                if word[i] != lettersDict[i]:
                    hasChars = False
        if hasChars == True:
            outlist.append(word)
    return outlist

def findWordByCharAny(letters: list, inList: list = wordList): # Finds words containing given letters at any position. Returns list containing all matching words
    outlist = []
    for word in inList:
        lettersInWord = True
        for letter in letters:
            if letter not in word:
                lettersInWord = False
        if lettersInWord == True:
            outlist.append(word)

    return outlist

def removeWordByChar(letters: list, inList: list = wordList): # Removes words containing given letters at any position from list. Returns list minus words with any given characters.
    outlist = []
    for word in inList:
        inWord = False
        for letter in letters:
            if letter in word:
                inWord = True
        if inWord == False:
            outlist.append(word)
    return outlist

def loadWords(path: str, outlist: list): # Loads a text file containing one word per line into a List datatype
    with open(path, "r") as inFile:
        for line in inFile:
            outlist.append(line.strip())
    return None

def processInputStr(instr: str): # Converts input string to list with each letter followed by its board state.

    outDict = [instr[i:i+2] for i in range(0, len(instr), 2)]
    return outDict

def updateLetterLists(inList: list): # Updates blackLetters, greenletters, yellowLetters based on user input.
    inLetters = []
    inStates = []
    global blackLetters
    global yellowLetters
    global greenLetters
    for x in inList:
        inLetters.append(x[0])
        inStates.append(x[1])
    if len(inLetters) != len(inStates):
        return None
    for x in range(len(inLetters)):
        if inStates[x] == "B":
            if str.lower(inLetters[x]) not in blackLetters:
                if str.lower(inLetters[x]) not in yellowLetters:
                    blackLetters.append(str.lower(inLetters[x]))
        elif inStates[x] == "Y":
            if str.lower(inLetters[x]) not in yellowLetters:
                yellowLetters.append(str.lower(inLetters[x]))
        elif inStates[x] == "G":
            greenLetters[x] = str.lower(inLetters[x])
    for x in greenLetters:
        if x != "_":
            while x in blackLetters:
                blackLetters.remove(x)
    return None

def guess(): # Produces the next guess list using blackLetters, yellowletters, greenLetters.
    global blackLetters
    global yellowLetters
    global greenLetters
    firstPass = []
    secondPass = []
    result = []
    if len(blackLetters) > 0:
        firstPass = removeWordByChar(blackLetters)
    else:
        firstPass = wordList
    
    secondPass = findWordByCharAny(yellowLetters, firstPass)
    result = findWordByCharsPos(greenLetters, secondPass)
    return result

"""def sortGuessList(guessList: list): # Sorts a list of guess words and returns the top 10 results in the sorted list
    vowelWeight = 2
    consonantWeight = 1
    global blackLetters
    global yellowLetters
    global greenLetters
    usedLetters = []
    for x in blackLetters:
        usedLetters.append(x)
    for x in yellowLetters:
        usedLetters.append(x)
    for x in greenLetters:
        if x != "_":
            usedLetters.append(x)
    print(usedLetters)
    return None"""

loadWords("wordle_words.txt", wordList)


startWord = startingWords[rand.randint(0, len(startingWords)-1)]
print("Wordle output format is X(G/Y/B) X(G/Y/B) X(G/Y/B) X(G/Y/B) X(G/Y/B) where X is letter, (G/Y/B) indicates that position being green, yellow, or black.")
print("Starting word: " + startWord)

while True:
    wordleOutputRaw = "" # str containing wordle output. Letter followed by uppercase G, Y, B to indicate state. Space seperated.
    wordleOutputRaw = input("Wordle Output: ")
    wordleOutput = processInputStr(wordleOutputRaw)

    updateLetterLists(wordleOutput)
    print(guess())