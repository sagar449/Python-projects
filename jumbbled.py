from tkinter import *
import random
from tkinter import messagebox

answers = [
    "python",
    "java",
    "swift",
    "canada",
    "india",
    "america",
    "london",
]

words = [
    "nptoyh",
    "avja",
    "wfsit",
    "cdanaa",
    "aidin",
    "aiearcm",
    "odnlon",
]

num = random.randrange(0,7,1)

def default():
    global words,answers,num

    lbl.config(text=words[num])

def checkans():
    global words, answers, num
    var = e1.get()
    if var == answers[num]:
        messagebox.showinfo("Sucess!","This is correct answer")
        res()
    else:
        messagebox.showerror("Error","Answer is incorrect try another.")
        e1.delete(0,END)

def res():
    global words,answers,num
    num = random.randrange(0,7,1)
    lbl.config(text=words[num])
    e1.delete(0,END)



root = Tk()
root.title("Jumbbled words game")
root.geometry("300x300")

root.config(background = "Black")

lbl = Label(root,text="Your here",font=("Vardana",20),fg="blue",bg="black")
lbl.pack(padx=10,pady=20)


# ans1 = StringVar()
e1 = Entry(root,font="Vardana,15")
e1.pack()


buttn1 = Button(root,text="Check",font=("comic sans ms",16),width=7,height=0,bg="#616C6F",fg="#6AB04A",relief=GROOVE,command=checkans)
buttn1.pack(pady=20)


buttn2 = Button(root,text="Reset",font=("comic sans ms",16),width=7,height=0,bg="#616C6F",fg="#D63031",relief=GROOVE,command=res)
buttn2.pack()

default()

root.mainloop()

