from tkinter import *
 
from tkinter.ttk import *
 
window = Tk()
 
window.title("Welcome to BMK")
 
window.geometry('350x200')
 
chk_state = BooleanVar()
 
chk_state.set(True) #set check state
 
chk = Checkbutton(window, text='Choose', var=chk_state)
 
chk.grid(column=0, row=0)
 
window.mainloop()
