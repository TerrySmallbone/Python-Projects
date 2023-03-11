from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_pw():
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_numbers + password_letters + password_symbols
    shuffle(password_list)

    password = "".join(password_list)
    # password = str(password)
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_data():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    # if len(website) == 0 or len(password) == 0:
    #     messagebox.showinfo(title="Oops", message="1 or more fields are empty, please review entires.")
    #     return

    if messagebox.askokcancel(title=website, message=f"These are the details you entered. \nEmail {email} \n"
                                                     f"Password: {password} \n\nContinue?"):

        try:
            with open("saved_data.json", "r") as data_file:
                # reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("saved_data.json", "w") as data_file: #code repeated in else statement line 62, could imprement a method but left to make reading easier
                json.dump(new_data, data_file, indent=4) #code repeated in else statement line 64, could imprement a method but left to make reading easier
        else:
            with open("saved_data.json", "r") as data_file:
                # updating old data
                data.update(new_data)

            with open("saved_data.json", "w") as data_file: #code repeated in except statement line 55, could imprement a method but left to make reading easier
                # saving new data
                json.dump(data, data_file, indent=4) #code repeated in except statement line 56, could imprement a method but left to make reading easier

        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #

def search_data():
    website = website_input.get()
    try:
        with open("saved_data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found")
    else:
        if website in data:
            messagebox.showinfo(title=website, message=f"Email: {data[website]['email']}\n"
                                                       f"Password: {data[website]['password']}")
        else:
            messagebox.showinfo(title="Website not found", message="The Website entered was not found.\n"
                                                               "Please check and try again")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# inputs
website_input = Entry(width=33)
website_input.focus()
website_input.grid(column=1, row=1)
email_input = Entry(width=43)
email_input.insert(0, "terrysmallbone@hotmail.co.uk")
email_input.grid(column=1, row=2, columnspan=2)
password_input = Entry(width=33)
password_input.grid(column=1, row=3)

# buttons
generate_pw_button = Button(text="Generate", command=generate_pw)
generate_pw_button.grid(column=2, row=3)
search_button = Button(text="Search", command=search_data)
search_button.grid(column=2, row=1)
add_button = Button(text="Add", width=36, command=save_data)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
