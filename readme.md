# Installation
This program has been tested on Python 3.13.7, and requires Tkinter. Tkinter is installed by default with Python 3.X.X.
# Usage
Extract the source archive and run via `python main.py`.
The program will open with a window containing an input text box for the most recent Wordle guess, 5 dropdown boxes to indicate letter state as either green (G), yellow (Y), or black (B), and a scrollable box on the right for the program's output. After you have entered your most recent guess and input the state for each letter, press `Run Guess` to run the guessing algorithm. It will produce a list of possible words based on your input in the output box. To input subsequent Wordle guesses, replace the word in the input text box with your latest guess, update the letter state dropdown boxes, and press `Run Guess` again. The output box will update with new output based on all guesses made so far. When you have finished a Wordle puzzle and need to reset, simply close the window and restart it with `python main.py`. 
# Credits
https://github.com/tabatkins/wordle-list See LICENSE.md for copyright disclosure
