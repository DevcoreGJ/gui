from tkinter import *

root = Tk()

def myClick():
	myLabel = Label(root, text="look I clicked a button!!").pack()

myButton = Button(root, text = "Click Me!", command = myClick,fg ="blue", bg="red").pack()


root.mainloop()