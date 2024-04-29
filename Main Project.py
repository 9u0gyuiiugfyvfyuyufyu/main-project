import tkinter as tk
from tkinter import messagebox
window = tk.Tk()
window.title("TOTAL MONEY")
window.geometry("400x400")

def addition():

    num1 = number1_entry.get()
    num2 = number2_entry.get()
    print(num1 + num2)
    messagebox.showinfo("Result", int(num1) + int(num2))

number1_label = tk.Label(window, text="Number 1:")
number1_label.grid(row=0,column=0)
number2_label = tk.Label(window, text="Number 2:")
number2_label.grid(row=1,column=0)
number1_entry = tk.Entry(window)
number2_entry = tk.Entry(window)
number1_entry.grid(row=0, column=1)
number2_entry.grid(row=1, column=1)


my_button = tk.Button(window, text="Add", command= addition)
my_button.grid(row=5, column=0)

def subtraction():
    num1 = number1_entry.get()
    num2 = number2_entry.get()
    print(num1 - num2)
    messagebox.showinfo("Result", int(num1) - int(num2))

 
my_button = tk.Button(window, text="subtract", command= subtraction)
my_button.grid(row=2, column=0)

def multiplication():
    num1 = number1_entry.get()
    num2 = number2_entry.get()
    print(num1 * num2)
    messagebox.showinfo("Result", int(num1) * int(num2))

my_button = tk.Button(window, text="multiply", command= multiplication)
my_button.grid(row=5, column=3)

def divition():
    num1 = number1_entry.get()
    num2 = number2_entry.get()
    print(num1 / num2)
    messagebox.showinfo("Result", int(num1) / int(num2))

my_button = tk.Button(window, text="divide", command= divition)
my_button.grid(row=5, column=4)



window.mainloop()