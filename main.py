import tkinter
from tkinter import *
import random

ran = 0


def btn_range():

    global ran
    num = rang.get()
    r, r1 = map(int, num.split(','))
    ran = random.randint(r, r1)


def btn_entry():

    a = 1
    while a == 1:
        per = number.get()
        per = int(per)
        if ran == per:
            tex.configure(state='normal')
            tex.delete(0, END)
            tex.insert(0, "Вы угадали)")
            tex.configure(state='disabled')
            break

        elif ran < per:
            tex.configure(state='normal')
            tex.delete(0, END)
            tex.insert(0, "число меньше вашего")
            number.delete(0, END)
            tex.configure(state='disabled')
            return

        elif ran > per:
            tex.configure(state='normal')
            tex.delete(0, END)
            tex.insert(0, "число больше вашего")
            number.delete(0, END)
            tex.configure(state='disabled')
            return


root = Tk()

root.title("Guess the number")

f_range = LabelFrame(text='Range (1,10)')
f_range.pack()

f_person = LabelFrame(text="Your number")
f_person.pack()

btn = Button(f_person, text="Guess", bg='white', command=btn_entry, width=8, height=2)
btn.pack(side=tkinter.LEFT, padx=10, pady=10)
btn = Button(f_range, text="Set range", bg='white', command=btn_range, width=8, height=2)
btn.pack(side=tkinter.LEFT, padx=10, pady=10)

rang = Entry(f_range, bg='white', width=10, borderwidth=5)
rang.pack(side=LEFT, padx=10, pady=10)

tex = Entry(root, bg='white', width=25, borderwidth=5)
tex.configure(state='disabled')
tex.pack(side=TOP, padx=10, pady=10)

number = Entry(f_person, bg='white', width=10, borderwidth=5)
number.pack(side=LEFT, padx=10, pady=10)

root.mainloop()
