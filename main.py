import random as rand
from tkinter import *
from tkinter import ttk
"""A small program, attempting to guess a Wordle answer in as few tries as possible."""
word_list = []
#testWordList = ["girls", "boys", "tongue", "titan", "maist", "malam", "fenks"]

startingWords = ["crane", "crate", "trace"]

black_letters = []
green_letters = ["_", "_", "_", "_", "_"]
yellow_letters = []

ALPHABET = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "w", "x", "y", "z"]
VOWELS = ["a", "e", "i", "o", "u", "y"]

root = Tk()
root.title("Wordle Guesser")
mainframe = ttk.Frame(root, padding="1")
mainframe.grid(column=0, row=0)

last_wordle_word = StringVar()

letter_state_1 = StringVar()
letter_state_2 = StringVar()
letter_state_3 = StringVar()
letter_state_4 = StringVar()
letter_state_5 = StringVar()

out_list = []

def find_word_by_chars_pos(letters: list, in_list: list):
    """Finds words containing given letters at given positions. _ indicates irrelevant position. 
    Requires list exactly 5 items long. Returns list containing all matching words"""
    output_list = []
    if len(letters) != 5:
        return None
    letters_dict = {}
    for i in range(len(letters)):
        temp_let = letters[i]
        letters_dict[i] = temp_let
    for word in in_list:
        has_chars = True
        for i in range(5):
            if letters_dict[i] == "_":
                continue
            else:
                if word[i] != letters_dict[i]:
                    has_chars = False
        if has_chars is True:
            output_list.append(word)
    return output_list

def find_word_by_chars_any(letters: list, in_list: list):
    """Finds words containing given letters at any position. 
    Returns list containing all matching words"""
    output_list = []
    for word in in_list:
        letters_in_word = True
        for letter in letters:
            if letter not in word:
                letters_in_word = False
        if letters_in_word is True:
            output_list.append(word)

    return output_list

def remove_word_by_char(letters: list, in_list: list):
    """Removes words containing given letters at any position from list. 
    Returns list minus words with any given characters."""
    output_list = []
    for word in in_list:
        in_word = False
        for letter in letters:
            if letter in word:
                in_word = True
        if in_word is False:
            output_list.append(word)
    return output_list

def load_words(path: str, output_list: list):
    """Loads a text file containing one word per line into a List datatype"""
    with open(path, "r", encoding=None) as in_file:
        for line in in_file:
            output_list.append(line.strip())

def process_input_str(instr: str):
    """Converts input string to list with each letter followed by its board state."""
    out_dict = [instr[i:i+2] for i in range(0, len(instr), 2)]
    return out_dict

def update_letter_lists(in_list: list):
    """Updates black_letters, green_letters, yellow_letters based on user input."""
    in_letters = []
    in_states = []
    #global black_letters
    #global yellow_letters
    #global green_letters
    for x in in_list:
        in_letters.append(x[0])
        in_states.append(x[1])
    if len(in_letters) != len(in_states):
        return None
    for x in range(len(in_letters)):
        if in_states[x] == "B":
            if str.lower(in_letters[x]) not in black_letters:
                if str.lower(in_letters[x]) not in yellow_letters:
                    black_letters.append(str.lower(in_letters[x]))
        elif in_states[x] == "Y":
            if str.lower(in_letters[x]) not in yellow_letters:
                yellow_letters.append(str.lower(in_letters[x]))
        elif in_states[x] == "G":
            green_letters[x] = str.lower(in_letters[x])
    for x in green_letters:
        if x != "_":
            while x in black_letters:
                black_letters.remove(x)
    return None

def guess():
    """Produces the next guess list using black_letters, yellow_letters, green_letters."""
    first_pass = []
    second_pass = []
    result = []
    if len(black_letters) > 0:
        first_pass = remove_word_by_char(black_letters, word_list)
    else:
        first_pass = word_list
    
    second_pass = find_word_by_chars_any(yellow_letters, first_pass)
    result = find_word_by_chars_pos(green_letters, second_pass)
    return result

def handle_run_button():
    """Initiates the main guess algorithm and handles its related components."""
    global out_list
    last_wordle_word_str = last_wordle_word.get()
    temp_list = [last_wordle_word_str[i:i+1] for i in range(0, len(last_wordle_word_str))]
    if len(temp_list) != 5:
        return None
    temp_list[0] = temp_list[0] + letter_state_1.get().upper()
    temp_list[1] = temp_list[1] + letter_state_2.get().upper()
    temp_list[2] = temp_list[2] + letter_state_3.get().upper()
    temp_list[3] = temp_list[3] + letter_state_4.get().upper()
    temp_list[4] = temp_list[4] + letter_state_5.get().upper()
    update_letter_lists(temp_list)
    out_list.clear()
    out_list = guess()
    outBox['state'] = 'normal'
    outBox.delete('1.0', 'end')
    for item in out_list:
        outBox.insert('end', item + "\n")
    outBox['state'] = 'disabled'
    return None

load_words("wordle_words.txt", word_list)

startWord = startingWords[rand.randint(0, len(startingWords)-1)]

wordEntryTitle = ttk.Label(mainframe, text='Wordle Word')
entryForm = ttk.Entry(mainframe, textvariable=last_wordle_word)

letterStateFrame = ttk.Frame(mainframe)
letterStateFrame.grid(column=2, row=2)

letterState1Combobox = ttk.Combobox(letterStateFrame, textvariable=letter_state_1, values=["G","Y","B"], width=1)
letterState1Combobox.state(["readonly"])

letterState2Combobox = ttk.Combobox(letterStateFrame, textvariable=letter_state_2, values=["G","Y","B"], width=1)
letterState2Combobox.state(["readonly"])

letterState3Combobox = ttk.Combobox(letterStateFrame, textvariable=letter_state_3, values=["G","Y","B"], width=1)
letterState3Combobox.state(["readonly"])

letterState4Combobox = ttk.Combobox(letterStateFrame, textvariable=letter_state_4, values=["G","Y","B"], width=1)
letterState4Combobox.state(["readonly"])

letterState5Combobox = ttk.Combobox(letterStateFrame, textvariable=letter_state_5, values=["G","Y","B"], width=1)
letterState5Combobox.state(["readonly"])

enterButton = ttk.Button(mainframe, text="Run Guess", command=handle_run_button)

outputFrame = ttk.Frame(root)
outputFrame.grid(column=1, row=0, sticky=(N,S,E))

outBox = Text(outputFrame, state="disabled", width=7, height=10)
outBox.grid()

outListBoxScroll = ttk.Scrollbar(outputFrame, orient=VERTICAL, command=outBox.yview)
outListBoxScroll.grid(column=1, row=0, sticky=(N,S))

outBox["yscrollcommand"] = outListBoxScroll.set

wordEntryTitle.grid(column=2, row=0)
entryForm.grid(column=2, row=1, sticky=(E,W))

letterState1Combobox.grid(column=0, row=0, padx="2")
letterState2Combobox.grid(column=1, row=0, padx="2")
letterState3Combobox.grid(column=2, row=0, padx="2")
letterState4Combobox.grid(column=3, row=0, padx="2")
letterState5Combobox.grid(column=4, row=0, padx="2")

enterButton.grid(column=2, row=3)

root.mainloop()
