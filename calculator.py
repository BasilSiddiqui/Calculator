"""
  F27SQ - Coursework 4 - Task 2

  @author: Basil

  This is simple calculator GUI program. It includes buttons for the four main
  mathematical operators, a clear button, an input box to get the values from
  the user and a lable to display the result of calculations.

"""

import tkinter as tk #To build the GUI.
import math #For using root method.

class Calculator(tk.Tk): #Defining a class for the window.
    def __init__(self):
        super().__init__()

        self.title("Calculator") #Naming it calculator.
        self.accumulator = 0 #Start the calculator with 0.
        self.configure(bg="black") #Making the theme dark mode.
        self.create_widgets() #To make the buttons on the display.

    def create_widgets(self):
        self.accumulator_label = tk.Label(self, text=self.accumulator, font=("Ariel", 16), bg="black", fg="white") #Black background and white font to match dark mode.
        self.accumulator_label.grid(row=0, column=5, columnspan=5, pady=10) #Placing it at the top right area.

        self.input_field = tk.Entry(self, width= 50) #Elongating the entry area for aesthethic.
        self.input_field.grid(row=1, column=1, columnspan=5, pady=5)

        dark_grey = "#444444"  # Hexadecimal color code for very dark grey (to be used for button color).

        self.clear_button = tk.Button(self, text=" CLR ", command=self.clear, font=("Ariel", 12), bg=dark_grey, fg="white", borderwidth=1, relief="solid")
        self.clear_button.grid(row=2, column=0, columnspan=1, padx=5, pady=5, sticky="ew") 

        self.add_button = tk.Button(self, text=" + ", command=self.addition, font=("Ariel", 12), bg=dark_grey, fg="white", borderwidth=1, relief="flat")
        self.add_button.grid(row=2, column=1, columnspan=1, padx=5, pady=5, sticky="ew")

        self.subtract_button = tk.Button(self, text=" - ", command=self.subtraction, font=("Ariel", 12), bg=dark_grey, fg="white", borderwidth=1, relief="flat")
        self.subtract_button.grid(row=2, column=2, columnspan=1, padx=5, pady=5, sticky="ew")

        self.multiply_button = tk.Button(self, text=" * ", command=self.multiplication, font=("Ariel", 12), bg=dark_grey, fg="white", borderwidth=1, relief="flat")
        self.multiply_button.grid(row=2, column=3, columnspan=1, padx=5, pady=5, sticky="ew")

        self.divide_button = tk.Button(self, text=" / ", command=self.division, font=("Ariel", 12), bg=dark_grey, fg="white", borderwidth=1, relief="flat")
        self.divide_button.grid(row=2, column=4, columnspan=1, padx=5, pady=5, sticky="ew")

        self.sqrt_button = tk.Button(self, text="√", command=self.square_root, font=("Ariel", 12), bg=dark_grey, fg="white", borderwidth=1, relief="flat")
        self.sqrt_button.grid(row=2, column=5, columnspan=1, padx=5, pady=5, sticky="ew")

    def clear(self):
        self.accumulator = 0 #Initial value to be 0.
        self.update_display() #Refresh display.
        self.input_field.delete(0, tk.END) #Clear the input feild back to 0.

    def addition(self):
            self.accumulator += float(self.input_field.get()) #Adding input value.
            self.update_display() #Updating with new value.
            self.input_field.delete(0, tk.END) #Emptying input field back to 0.

    def subtraction(self):
            self.accumulator -= float(self.input_field.get()) #Subtracting input value.
            self.update_display() #Updating with new value.
            self.input_field.delete(0, tk.END) #Emptying input field back to 0.

    def multiplication(self):
            self.accumulator *= float(self.input_field.get())
            self.update_display()
            self.input_field.delete(0, tk.END)
            
    def division(self):
            divisor = float(self.input_field.get()) #Keeping every number in float for decimals.
            if divisor != 0:                #If input is not 0,
                self.accumulator /= divisor #divide by input.
                self.update_display()
                self.input_field.delete(0, tk.END)
            else:
                self.input_field.insert(0, "Error") #Can not be divided by 0.

    def square_root(self):
        try:
            value = float(self.input_field.get())
            if value >= 0:                           #If value is above 0,
                self.accumulator = math.sqrt(value)  #Square root it (using math library).
                self.update_display()
                self.input_field.delete(0, tk.END)
            else:
                self.input_field.delete(0, tk.END)
                self.input_field.insert(0, "Error") #Negative value can not work in root (no imaginary numbers).
        except ValueError:
            self.input_field.delete(0, tk.END)
            self.input_field.insert(0, "Error")

    def update_display(self):
        self.accumulator_label.config(text=str(self.accumulator)) #To refresh display with new accumulator value4.

if __name__ == "__main__": #To run the application.
    app = Calculator()
    app.mainloop() #Loop for the application.