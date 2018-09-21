from tkinter import *
window = Tk()

window.geometry('200x200+100+200')

Label(window, text="Label 1 : x=0, y=0", bg="#FFFF00", fg="blue").place(x=0, y=0)
Label(window, text="Label 2 : x=50, y=40", bg="#3300CC", fg="orange").place(x=50, y=40)
Label(window, text="Label 3 : x=75, y=80", bg="#FF0099", fg="green").place(x=75, y=80)
Label(window, text="Label 4 : x=25, y=100", bg="#00FFFF", fg="white").place(x=25, y=100)

mainloop()
