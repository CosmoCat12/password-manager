from re import search
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_password():
    #Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_get = site_entry.get()
    email_get = email_entry.get()
    password_get = password_entry.get()
    new_data = {website_get: {
        "email": email_get,
        "password": password_get,

    }}

    if len(website_get) == 0 or len(password_get) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure to fill in all fields.")
    else:
        try:
            with open("data.json", mode="w") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)
                site_entry.delete(0, END)
                password_entry.delete(0, END)
        finally:
            site_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- SEARCH  ------------------------------- #
def search():
    website_get = site_entry.get()
    website_title = website_get.title()
    try:
        with open("data.json", mode="r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found.")
    else:
        if website_title in data:
            email = data[website_title]["email"]
            password = data[website_title]["password"]
            messagebox.showinfo(title=website_title, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details found for {website_title}.")

# ------- UI SETUP ------------------------------- #

window = Tk()
canvas = Canvas(height=200, width=200)

window.config(pady=50,padx=50)
window.title("Password Manager")
photo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=photo)
canvas.grid(column=2, row=1)

website = Label(text="Website:")
website.grid(column=1, row=2)

site_entry = Entry(width=26)
site_entry.grid(column=2, row=2)
site_entry.focus()

email = Label(text="Email/Username:")
email.grid(column=1, row=3)

email_entry = Entry(width=35)
email_entry.grid(column=2, row=3, columnspan=2)
email_entry.insert(0, "tulyaganov.azamat@gmail.com")

password = Label(text="Password:")
password.grid(column=1, row=4)

password_entry = Entry(width=26)
password_entry.grid(column=2, row=4)

generate_button = Button(text="Generate Password:", command=gen_password, width=15)
generate_button.grid(column=3, row=4)

add_button = Button(text="Add", width=30, command=save)
add_button.grid(column=2, row=5, columnspan=2)

search_button = Button(text="Search", width=15, command=search)
search_button.grid(column=3, row=2)



window.mainloop()