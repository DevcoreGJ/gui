from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo


#configure the root window
root = Tk()
root.title('My Awesome App')
root.geometry("300x50")

#method
def button_clicked():
	showinfo(title='Information', message='Hello, Tkinter!')

#label
greeting = Label(root, text='hello,Tkinter!').pack()

#button
action = ttk.Button(root, text='Click Me', command=button_clicked)
action.pack()

root.mainloop()