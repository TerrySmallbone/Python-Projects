from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_pw():
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_numbers + password_letters + password_symbols
    shuffle(password_list)

    password = 0, "".join(password_list)
    password=str(password)
    password_input.insert(0, password)
    pyperclip.copy(password)
    
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_data():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="1 or more fields are empty, please review entires.")
        return

    if messagebox.askokcancel(title=website, message=f"These are the details you entered. \nEmail {email} \n"
                                                 f"Password: {password} \n\nContinue?"):
        with open("saved_data.txt", "a") as data_file:
            data_file.write(f"{website} | {email} | {password} |\n")
            website_input.delete(0, END)
            password_input.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx= 50, pady= 50)

canvas = Canvas(width= 200, height= 200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image= logo_img)
canvas.grid(column=1, row=0)

#labels
website_label = Label(text= "Website:")
website_label.grid(column=0, row= 1)
email_label = Label(text= "Email/Username:")
email_label.grid(column=0, row=2)
password_label = Label(text= "Password:")
password_label.grid(column=0, row=3)

#inputs
website_input = Entry(width= 43)
website_input.focus()
website_input.grid(column=1, row=1, columnspan=2)
email_input = Entry(width=43)
email_input.insert(0, "terrysmallbone@hotmail.co.uk")
email_input.grid(column=1, row=2, columnspan=2)
password_input = Entry(width= 33)
password_input.grid(column=1, row=3)

#buttons
generate_pw_button = Button(text="Generate", command=generate_pw)
generate_pw_button.grid(column=2, row=3)
add_button = Button(text="Add", width=36, command= save_data)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()
