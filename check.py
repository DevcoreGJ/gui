from tkinter import *
from PIL import ImageTk,Image

global message

root = Tk()
root.title('title')
root.iconbitmap('c:/gui/ico.png')
root.geometry("400x400")

var = IntVar()

state = var.get()


def valid():
	if var.get() == 0:
		message = Label (root, text="The checkbox is empty...")
		message.pack()
	else:
		message = Label(root, text="You checked the box!").pack()
	#checkValidation = Label(root, text=var.get()).pack()



check =Checkbutton(root, text="Check this box, I dare you!", variable = var, command=valid)
check.pack()

clickToVerify = Button(root, text="Print checkbox state",command=valid).pack()

message = Label (root, text="The checkbox is empty...").pack()

root.mainloop()

