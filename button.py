from tkinter import *
 
window = Tk()
 
window.title("Welcome to BMK")
 
window.geometry('350x200')
 
lbl = Label(window, text="Hello")
 
lbl.grid(column=0, row=0)
 
btn = Button(window, text="Click Me")
btn1 = Button(window, text="Click Me", bg="orange", fg="red")#Change button foreground and background colors
 
btn.grid(column=1, row=0)
btn1.grid(column=1, row=1)

window.mainloop()
