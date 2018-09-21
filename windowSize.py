from tkinter import *
 
window = Tk()
 
window.title("Welcome to BMK")
 
lbl = Label(window, text="Hello")
 
lbl.grid(column=0, row=0)

window.geometry('350x200')

window.mainloop()
