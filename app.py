# Import UI packages
import re
import tkinter as tk
from tkinter import *

# Import Genetic Algorithm
from src.algorithm import geneticAlgorithm


class SudokuApp:
    """Need to put description here"""

    def __init__(self, window):
        self.window = window
        # Run the window
        window.title('Word Sudoku')
        window.geometry("600x500")
        window.configure(bg="#ADD8E6")

        self.pixelVirtual = PhotoImage(width=1, height=1)

        # Add title to application
        self.label_one = Label(window,
                               text="Enter at least four different letters into the grid...",
                               fg='black',
                               font=("Helvetica", 10),
                               image=self.pixelVirtual,
                               height=30,
                               width=400,
                               compound="c")

        self.label_one.place(x=100, y=30)

        # Create and place input boxes
        format = ("Helvetica", 18)
        self.input_1 = Text(window, font=format, height=1, width=3)
        self.input_2 = Text(window, font=format, height=1, width=3)
        self.input_3 = Text(window, font=format, height=1, width=3)
        self.input_4 = Text(window, font=format, height=1, width=3)
        self.input_5 = Text(window, font=format, height=1, width=3)
        self.input_6 = Text(window, font=format, height=1, width=3)
        self.input_7 = Text(window, font=format, height=1, width=3)
        self.input_8 = Text(window, font=format, height=1, width=3)
        self.input_9 = Text(window, font=format, height=1, width=3)
        self.input_10 = Text(window, font=format, height=1, width=3)
        self.input_11 = Text(window, font=format, height=1, width=3)
        self.input_12 = Text(window, font=format, height=1, width=3)
        self.input_13 = Text(window, font=format, height=1, width=3)
        self.input_14 = Text(window, font=format, height=1, width=3)
        self.input_15 = Text(window, font=format, height=1, width=3)
        self.input_16 = Text(window, font=format, height=1, width=3)

        inputs = [(self.input_1, self.input_2, self.input_3, self.input_4),
                  (self.input_5, self.input_6, self.input_7, self.input_8),
                  (self.input_9, self.input_10, self.input_11, self.input_12),
                  (self.input_13, self.input_14, self.input_15, self.input_16)]

        x = 220
        y = 100
        for i in range(4):
            for j in range(4):
                self.table = inputs[i][j]
                self.table.place(x=x+i*40, y=y+j*40)

        # Generate the result from the grid
        def generateSudoku():
            self.show_result.configure(text="Calculating solution...")

            input_1 = self.input_1.get(1.0, "end-1c")
            input_2 = self.input_2.get(1.0, "end-1c")
            input_3 = self.input_3.get(1.0, "end-1c")
            input_4 = self.input_4.get(1.0, "end-1c")
            input_5 = self.input_5.get(1.0, "end-1c")
            input_6 = self.input_6.get(1.0, "end-1c")
            input_7 = self.input_7.get(1.0, "end-1c")
            input_8 = self.input_8.get(1.0, "end-1c")
            input_9 = self.input_9.get(1.0, "end-1c")
            input_10 = self.input_10.get(1.0, "end-1c")
            input_11 = self.input_11.get(1.0, "end-1c")
            input_12 = self.input_12.get(1.0, "end-1c")
            input_13 = self.input_13.get(1.0, "end-1c")
            input_14 = self.input_14.get(1.0, "end-1c")
            input_15 = self.input_15.get(1.0, "end-1c")
            input_16 = self.input_16.get(1.0, "end-1c")
            coords = [[input_1, input_5, input_9, input_13],
                      [input_2, input_6, input_10, input_14],
                      [input_3, input_7, input_11, input_15],
                      [input_4, input_8, input_12, input_16]]

            def getPositions(list):
                for i in range(0, 4):
                    for j in range(0, 4):
                        if list[i][j] == '':
                           list[i][j] = ' '
                return(list)

            initial = getPositions(coords)

            result = geneticAlgorithm(1000, initial)
            solution = str(result)
            self.show_result.config(text="Finished calculating.")

            self.final_result = Label(window, text="Result: " + str(solution))
            self.final_result.place(relx=0.5, y=400, anchor=CENTER)

        self.submit_button = Button(window, text="Submit",
                                    command=generateSudoku)
        self.submit_button.place(relx=0.5, y=350, anchor=CENTER)
        self.show_result = Label(window, text="Click submit to see results.")
        self.show_result.place(relx=0.5, y=300, anchor=CENTER)


root = Tk()
app = SudokuApp(root)
root.mainloop()