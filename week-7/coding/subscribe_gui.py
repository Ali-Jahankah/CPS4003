import tkinter as tk
from tkinter import messagebox

components = {
    "email_entry": None
}

def run():
    window = create_window()
    add_email(window)
    add_input(window)
    add_button(window)
    window.mainloop()


def clicked(e):
    val=components["email_entry"].get()
    if len(val):
        messagebox.showinfo('Successful',F"Successfully subscribed with {val}")
    else:
        messagebox.showerror('showerror',"No email is entered")    

def create_window():
    window = tk.Tk()
    window.geometry("300x100")
    window.title("Subscribe")
    window.config(bg="#626161",cursor="hand2",padx=10,pady=10)
    window.columnconfigure(0,weight=1)
    window.columnconfigure(0,weight=3)

    return window
    
def add_email(window):
    add_email_label(window)

def add_email_label(window):
    email_label=tk.Label(window)
    email_label.config(text="Email: ",bg="#626161",font=("Arial",12))
    email_label.grid(row=0,column=0,sticky="W",pady=10)

def add_input(window):
    add_email_input(window)

def add_email_input(window):
    email_input=tk.Entry(window)
    email_input.config(bg="#fff",font=("Arial",12))
    email_input.grid(row=0,column=1,sticky="EW")
    components["email_entry"] = email_input


def add_button(window):
    add_email_button(window)

def add_email_button(window):
    button=tk.Button(window)
    button.config(bg="#fff",font=("Arial",12),text="Subscribe!")
    button.grid(row=1,column=0,columnspan=2, sticky='EW')
    button.bind("<Button-1>",clicked)

run()