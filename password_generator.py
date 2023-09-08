import tkinter as tk
import random
import string
import secrets

def generate_password():
    # Get the password length from the user input
    password_length = int(length_entry.get())

    # Define character sets for the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a secure random password
    secure_password = ''.join(secrets.choice(characters) for _ in range(password_length))

    # Display the generated password in the result label
    result_label.config(text=secure_password)


window = tk.Tk()
window.title("Password Generator")

# Label and Entry for password length
length_label = tk.Label(window, text="Password Length:")
length_label.pack()

length_entry = tk.Entry(window)
length_entry.pack()

# Button to generate password
generate_button = tk.Button(window, text="Generate Password", command=generate_password)
generate_button.pack()

# Label to display the generated password
result_label = tk.Label(window, text="", wraplength=300)
result_label.pack()

# Start GUI main loop
window.mainloop()