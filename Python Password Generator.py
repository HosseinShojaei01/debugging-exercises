from tkinter import *
import random

def Random():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    length = 8
    new_password = ""
    for i in range(length):
        next_index = random.randrange(len(alphabet))
        new_password = new_password + alphabet[next_index]
        if len(new_password) >= 2:
            for i in range(random.randrange(1,3)):
                replace_index = random.randrange(len(new_password)//2)
                new_password = new_password[0:replace_index] + str(random.randrange(10)) + new_password[replace_index+1:]
            for i in range(random.randrange(1,3)):
                replace_index = random.randrange(len(new_password)//2,len(new_password))
                new_password = new_password[0:replace_index] + new_password[replace_index].upper() + new_password[replace_index+1:]
    PASSWORD.set(new_password)


root = Tk()
root.title("Password Generator")
width = 400
height = 200
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))

PASSWORD = StringVar()

Top = Frame(root, width=width)
Top.pack(side=TOP)
Form = Frame(root, width=width)
Form.pack(side=TOP)

lbl_title = Label(Top, width=width, font=('arial', 16), text="Password Generator", bd=1, relief=SOLID)
lbl_title.pack(fill=X)
lbl_password = Label(Form, font=('arial', 18), text="Password", bd=10)
lbl_password.grid(row=0, pady=15)

password = Entry(Form, textvariable=PASSWORD, font=(18), width=16)
password.grid(row=0, column=1)

btn_generate = Button(Form, text="Generate", width=20, command=Random)
btn_generate.grid(row=1, columnspan=2)

root.mainloop()
