from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2,4))]
    password_numbers = [choice(numbers) for _ in range(randint(2,4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    password = password_entry.get()
    email = email_entry.get()
    new_data = {website:
        {
            "email": email,
            "password": password
        }
    }

    if len(website) != 0:
        if len(password) != 0:
            is_ok = messagebox.askokcancel(title="website", message=f"These are the details entered\nWebsite: {website}"f"\nPassword: {password} \nIs it ok to save?")
            if is_ok:
                try:
                    file = open("data.json", "r")
                except FileNotFoundError:
                    file = open("data.json", "w")
                    json.dump(new_data, file, indent=4)
                else:
                    data = json.load(file)
                    data.update(new_data)
                    file = open("data.json", "w")
                    json.dump(data, file, indent=4)

                website_entry.delete(0, END)
                password_entry.delete(0, END)
        else:
            messagebox.showinfo(title="website", message="password field is empty")
    else:
        messagebox.showinfo(title="website", message="website field is empty")
# ------------------------------- save password --------------------------#

def find_password():
    website = website_entry.get()
    try:
        file = open("data.json", "r")
    except FileNotFoundError:
        messagebox.showinfo(title="error", message="No data file found")
    else:
        data = json.load(file)
    a = 0
    try:
        for _ in data:
            if _ == website:
                inner_data = data[f"{website}"]
                email = inner_data["email"]
                password = inner_data["password"]
                messagebox.showinfo(title=f"{website}", message=f"Email: {email}\nPassword: {password}")
                a += 1
            else:
                continue
        if a == 0:
            raise FileNotFoundError
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No details for the website exists")
    except UnboundLocalError:
        pass

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="#dec3c3")

# Logo

canvas = Canvas(width=200, height=200, bg="#dec3c3", highlightthickness=0)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=1)

# Labels

website_label = Label(text="Website:", bg="#dec3c3")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:", bg="#dec3c3")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:", bg="#dec3c3")
password_label.grid(row=3, column=0)

# Entries

website_entry = Entry(width=32)
website_entry.grid(row=1, column=1, columnspan=2, sticky="W")
website_entry.focus()
email_entry = Entry(width=52)
email_entry.grid(row=2, column=1, columnspan=2, sticky="W")
email_entry.insert(0, "aditya2712singh@gmail.com")
password_entry = Entry(width=32)
password_entry.grid(row=3, column=1, sticky="W")

# Buttons

generate_password_button = Button(text="Generate Password",width=15, command=generate_password, bg="#f0e4e4")
generate_password_button.grid(row=3, column=2, sticky="E")
add_button = Button(text="Add", width=44, command=save, bg="#f0e4e4")
add_button.grid(row=4, column=1, columnspan=2, sticky="W")
search_button = Button(text="Search",width=15, command=find_password, bg="#f0e4e4")
search_button.grid(row=1, column=2, sticky="E")
window.mainloop()
