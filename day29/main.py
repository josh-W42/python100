import tkinter as tk
from tkinter import messagebox
import random


# Constants
WHITE = "#FFFFFF"

# Password Generating
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password() -> str:
    """
    Generates a random password using letters numbers and symbols.
    :return: A generated password
    """
    password_list = []

    password_list.extend(random.choices(letters, k=random.randint(8, 10)))
    password_list.extend(random.choices(symbols, k=random.randint(2, 4)))
    password_list.extend(random.choices(numbers, k=random.randint(2, 4)))

    random.shuffle(password_list)

    return "".join(password_list)


# Password Saving
def handle_generate_btn() -> None:
    """
    Handler function for when the "generate password" button is pressed.
    It clears the password entry and inserts a generated password.
    """
    password_entry.delete(0, tk.END)
    password_entry.insert(0, generate_password())


def save_password() -> None:
    """
    Get the values of the all the entries and store them into a csv file.
    """
    new_line = ",".join([website_entry.get(), username_entry.get(), password_entry.get()])

    # New Topic: dialog boxes!
    is_ok = messagebox.askokcancel(
        title=f"Save {website_entry.get()} Password?",
        message=f"These details will be saved: \nEmail: {username_entry.get()}\nPassword: {password_entry.get()}")

    if is_ok:
        website_entry.delete(0, tk.END)
        username_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)
        with open("db.csv", "a") as file:
            file.write(f"{new_line}\n")
#  UI Setup


window = tk.Tk()
window.title("Paasword Manager")
window.config(
    padx=20,
    pady=20,
    width=400,
    height=300,
    bg=WHITE,
)

canvas = tk.Canvas(width=110, height=220, bg=WHITE, highlightthickness=0)
logo_img = tk.PhotoImage(file="logo.png")
canvas.create_image(50, 110, image=logo_img)

website_entry = tk.Entry(width=40)
website_entry.focus()
website_label = tk.Label(text="Website:", bg=WHITE)

username_entry = tk.Entry(width=40, highlightthickness=0)
username_label = tk.Label(text="Email/Username:", bg=WHITE, highlightthickness=0)
username_entry.insert(0, "email@gmail.com")

password_entry = tk.Entry(width=21)
password_label = tk.Label(text="Password:", bg=WHITE)
gen_password_btn = tk.Button(text="Generate Password", command=handle_generate_btn)

submit_btn = tk.Button(text="Add", width=35, command=save_password)

# Rendering
canvas.grid(row=0, column=1)
website_entry.grid(row=1, column=1, columnspan=2)
website_label.grid(row=1, column=0)
username_entry.grid(row=2, column=1, columnspan=2)
username_label.grid(row=2, column=0)
password_entry.grid(row=3, column=1)
password_label.grid(row=3, column=0)
gen_password_btn.grid(row=3, column=2)
submit_btn.grid(row=4, column=1, columnspan=2)


window.mainloop()