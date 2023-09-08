import tkinter as tk
from tkinter import ttk
import string
import secrets
from ttkthemes import ThemedTk


def generate_password():
    # Get the password length from the user input
    password_length = int(length_entry.get())

    # Define character sets for the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a secure random password
    secure_password = ''.join(secrets.choice(characters) for _ in range(password_length))

    # Display the generated password in the result label
    result_label.config(text=secure_password)

# Create the main window
window = ThemedTk(theme="arc")
window.title("Password Generator")

# Create a frame for the content
frame = ttk.Frame(window)
frame.grid(column=0, row=0, padx=20, pady=20, sticky=(tk.W, tk.E, tk.N, tk.S))
frame.columnconfigure(0, weight=1)
frame.rowconfigure(0, weight=1)

# Label and Entry for password length
length_label = ttk.Label(frame, text="Password Length:")
length_label.grid(column=0, row=0, sticky=tk.W)

length_entry = ttk.Entry(frame)
length_entry.grid(column=1, row=0, sticky=(tk.W, tk.E))

# Button to generate password
generate_button = ttk.Button(frame, text="Generate Password", command=generate_password)
generate_button.grid(column=0, row=1, columnspan=2, pady=(10, 0))

# Label to display the generated password
result_label = ttk.Label(frame, text="", wraplength=300)
result_label.grid(column=0, row=2, columnspan=2, pady=(10, 0))

# Start the GUI main loop
window.mainloop()