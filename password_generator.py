import tkinter as tk
from tkinter import ttk
import string
import secrets
from ttkthemes import ThemedTk

def generate_password():
    # Get the password length from the slider as an integer
    password_length = int(password_length_slider.get())

    # Update the label to show the current password length
    password_length_label.config(text=f"Password Length: {password_length}")

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

# Label for minimum password length
min_length_label = ttk.Label(frame, text="Min: 5")
min_length_label.grid(column=0, row=1, padx=(0, 10), sticky=tk.E)

# Slider for password length
password_length_slider = ttk.Scale(frame, from_=5, to=30, orient="horizontal", length=200)
password_length_slider.grid(column=1, row=1, columnspan=2, pady=(10, 0))

# Label for maximum password length
max_length_label = ttk.Label(frame, text="Max: 30")
max_length_label.grid(column=3, row=1, padx=(10, 0), sticky=tk.W)

# Label to display the current password length
password_length_label = ttk.Label(frame, text="Password Length: 5")
password_length_label.grid(column=0, row=2, columnspan=4)

# Button to generate password
generate_button = ttk.Button(frame, text="Generate Password", command=generate_password)
generate_button.grid(column=0, row=3, columnspan=4, pady=(10, 0))

# Label to display the generated password
result_label = ttk.Label(frame, text="", wraplength=300)
result_label.grid(column=0, row=4, columnspan=4, pady=(10, 0))

# Start the GUI main loop
window.mainloop()