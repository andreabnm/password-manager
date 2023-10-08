from tkinter import *
from tkinter import messagebox
from random import shuffle, randint, choice
import pyperclip

FONT = ("Arial", 12, "bold")
EMAIL = 'email@email.com'


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    pwd_input.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]
    shuffle(password_list)
    password = ''.join(password_list)
    pwd_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = ws_input.get()
    email = email_input.get()
    psw = pwd_input.get()

    if (website == '') or (psw == ''):
        messagebox.showerror('Error', 'Please don''t leave any fields empty')
    else:
        is_ok = messagebox.askokcancel(title=website, message=f'These are the details entered: \nEmail: {email} "'
                                                              f'\nPassword: {psw} \nIs it ok to save?')
        if is_ok:
            with open('passwords.txt', 'a') as data_file:
                data_file.write(f'{website} | {email} | {psw}\n')
            ws_input.delete(0, END)
            pwd_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)

# Labels
ws_label = Label(text="Website:", font=FONT)
ws_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:", font=FONT)
email_label.grid(column=0, row=2)
pwd_label = Label(text="Password:", font=FONT)
pwd_label.grid(column=0, row=3)

# Inputs
ws_input = Entry(width=35)
ws_input.grid(column=1, row=1, columnspan=2)
ws_input.focus()
email_input = Entry(width=35)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, EMAIL)
pwd_input = Entry(width=21)
pwd_input.grid(column=1, row=3)

# Buttons
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)
window.mainloop()
