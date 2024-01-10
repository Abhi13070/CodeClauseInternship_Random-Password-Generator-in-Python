import tkinter as tk
from tkinter import Entry, Button, Label, StringVar
import random
import string

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Random Password Generator App")

        # Set up GUI elements
        self.root.geometry("600x600")  # Increase window size
        self.root.configure(bg='#3498db')  # Set background color

        self.label = Label(root, text="Password Length:", font=('Helvetica', 14), bg='#3498db', fg='#ffffff')
        self.label.pack(pady=15)

        self.length_entry = Entry(root, font=('Helvetica', 12))
        self.length_entry.pack(pady=10)

        self.password_var = StringVar()
        self.password_label = Label(root, textvariable=self.password_var, font=('Helvetica', 14), wraplength=350, bg='#3498db', fg='#ffffff')
        self.password_label.pack(pady=20)

        self.generate_button = Button(root, text="Generate Password", command=self.generate_password, font=('Helvetica', 12), bg='#2ecc71', fg='#ffffff')
        self.generate_button.pack(pady=15)

    def generate_password(self):
        try:
            password_length = int(self.length_entry.get())
        except ValueError:
            self.password_var.set("Invalid input. Please enter a valid number.")
            return

        if password_length <= 0:
            self.password_var.set("Password length must be greater than 0.")
            return

        characters = string.ascii_letters + string.digits + string.punctuation
        # Filter out characters that are not alphabets, numbers, or special characters
        valid_characters = [char for char in characters if char.isalnum() or char in string.punctuation]

        password = ''.join(random.choice(valid_characters) for _ in range(password_length))

        self.password_var.set(f"Generated Password:\n{password}")

# Create the main window
root = tk.Tk()
app = PasswordGenerator(root)

# Run the main loop
root.mainloop()
