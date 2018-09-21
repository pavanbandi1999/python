from tkinter import *
 
window = Tk()
 
window.title("Welcome to BMK ")
 
window.geometry('350x200')
 
var =IntVar()
 
var.set(36)#Set default value for Spinbox
 
spin = Spinbox(window, from_=0, to=50, width=5, textvariable=var)

spin.grid(column=0,row=0)
 
window.mainloop()
