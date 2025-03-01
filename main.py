from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password(): 
    """ generate a password """
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    pass_letters = [random.choice(letters) for _ in range(random.randint(8,10))]
    pass_numbers = [random.choice(numbers) for _ in range(random.randint(2,4))]
    pass_symbols = [random.choice(symbols) for _ in range(2,4)]

    password_list = pass_letters + pass_numbers + pass_symbols 
    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(END,password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def update_json(app,user,password): 
    """ update json file with password, user, and app informatikon"""
    new_data = {
            app:{
                "user": user,
                "password": password
        }
    }
        
    try: 
        with open(file='passwords.json', mode='r') as file: 
            data = json.load(file)
    except FileNotFoundError:
        with open(file='passwords.json',mode='w') as file:  
            json.dump(new_data,file,indent=4)
    else: 
        data.update(new_data)
        with open(file='passwords.json',mode='w') as file:  
            json.dump(data,file,indent=4)
    finally:
        app_entry.delete(0,END)
        user_entry.delete(0,END)
        password_entry.delete(0,END)
            
def add_password():
    """ add password to json file"""
    app = app_entry.get() 
    user = user_entry.get() 
    password = password_entry.get()

    # confirmation popup
    add = messagebox.askyesno(title='Add password', message=f'Do you want to this to your list \n Service: {app} \n Username: {user} \n Password: {password}' )
    
    if add == True: 
        pyperclip.copy(password) # copy to clipboard automatically
        update_json(app,user,password)

# ---------------------------- PASSWORD SEARCH ------------------------------- #

def search_password(): 
    """ Search for application on"""
    app = app_entry.get()
 
    with open(file='passwords.json',mode='r') as file: 
        data = json.load(file)
    
    try:
        password = data[app]
        messagebox.showinfo('Password Info', f"Application: {app} \n Email: {password["user"]} \n Password: {password["password"]}" )
    except KeyError: 
        messagebox.showinfo('Password Info', f"Application: '{app}' not found" )
    finally:
        app_entry.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #

root = Tk() 
root.title("Password Manager")
root.config(padx=50, pady=50)

# --- Logo --- # 
logo_canvas = Canvas(height=200,width=200)
logo = PhotoImage(file="logo.png") # size 200x189
logo_canvas.create_image(100,100,image=logo)
logo_canvas.grid(row=0,column=1)

# --- Entrys --- # 
# app 
app_entry = Entry(width=20)
app_entry.grid(row=1,column=1)

# username 
user_entry = Entry(width=40)
user_entry.grid(row=2,column=1,columnspan=2)

# password 3,1
password_entry = Entry(width=20)
password_entry.grid(row=3,column=1)


# --- Buttons --- # 
# search username
search_password = Button(text='Search',command=search_password)
search_password.grid(row=1,column=2)

# password generator
pass_gen = Button(text='Generate Password',command=generate_password)
pass_gen.grid(row=3,column=2)

# add to file 
add = Button(text='Add Password',width=40,command=add_password)
add.grid(row=4,column=1,columnspan=2)


# --- Labels --- # 
# labels 
label_app = Label(text='Website/Application:',font=('Arial',15)) 
label_app.grid(row=1,column=0,pady=5)

# username 
label_user = Label(text='Username/Email:',font=('Arial',15))
label_user.grid(row=2,column=0,pady=5)

# password
pass_label = Label(text="Password:",font=('Arial',15))
pass_label.grid(row=3,column=0,pady=5)


root.mainloop()