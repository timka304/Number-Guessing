from tkinter import *
from tkinter import messagebox
import random

screen = Tk()
screen.config(background="white")
screen.geometry("400x600")
screen.title("Number Guessing Game")

heading_label = Label(screen, text="Number Guessing Game", font=("Arial", 20, 'bold'), bg="white", fg="black")
heading_label.pack(pady=20)

name_label = Label(screen, text="Enter your name:", font=("Arial", 20, 'bold'), bg="white", fg="black")
name_label.pack(pady=20)

name_entry = Entry(screen, font=("Arial", 20, 'bold'), bg="white", fg="black")
name_entry.pack(pady=20)

greeting_label = Label(screen, text="Welcome to the Number Guessing Game!", font=("Arial", 20, 'bold'), bg="white", fg="black")
greeting_label.pack(pady=20)

#Greeting message box with their name
def greet_user():
    name = name_entry.get()
    if name:
        messagebox.showinfo("Welcome", f"Hello {name}! Let's play the Number Guessing Game!")
    else:
        messagebox.showwarning("Input Error", "Please enter your name.")


greet_button = Button(screen, text="Start Game", command=greet_user, font=("Arial", 20, 'bold'), bg="white", fg="black")
greet_button.pack(pady=20)

#Entry field for the user to enter a number
number_entry = Entry(screen, font=("Arial", 20, 'bold'), bg="white", fg="black")
number_entry.pack(pady=20)



#Label to generate a random range of numbers that the user has to enter in between
number_label = Label(screen, text="Enter a number between 1 and 10", font=("Arial", 20, 'bold'), bg="white", fg="black")
number_label.pack(pady=20)

#Function to check if the number entered by the user is correct or not, if not tell the user if the number is too high or too low and let them try again
def check_number():
    try:
        user_number = int(number_entry.get())
        random_number = random.randint(1, 10)

        if user_number < 1 or user_number > 10:
            messagebox.showinfo("Error", "Please enter a number between 1 and 10")
        elif user_number == random_number:
            messagebox.showinfo("Success", f"Congratulations {name_entry.get()}! You guessed the correct number: {user_number}")
        elif user_number < random_number:
            messagebox.showinfo("Try Again", f"Too low!")
        else:
            messagebox.showinfo("Try Again", f"Too high!")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")

#button to check the number entered by the user
check_button = Button(screen, text="Check Number", command=check_number, font=("Arial", 20, 'bold'), bg="white", fg="black")
check_button.pack(pady=20)

screen.mainloop()

