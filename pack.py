from tkinter import *

window = Tk()
window.geometry('400x400+100+200')


label1 = Label(window, text="Label 1", bg="#E74C3C", fg="white").pack(fill=X, padx=10)
label2 = Label(window, text="Label 2", bg="#2ECC71", fg="black").pack(fill=X, padx=10)
label3 = Label(window, text="Label 3", bg="#F1C40F", fg="white").pack(fill=X, padx=10)
window.mainloop
