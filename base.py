from tkinter import *
from PIL import ImageTk,Image


root = Tk()
root.title('main window')
root.iconbitmap('c:/gui/ico.png')

def openWindow():
	global my_img #needed to make global so sub window can access it.
	top = Toplevel() #new windows
	top.title('2nd window')
	top.iconbitmap('c:/gui/ico.png')
	lbl = Label(top, text="Hello World!!").pack() #makes label on new window
	my_img = ImageTk.PhotoImage(Image.open("images/budapestResized.jpg")) #load image in 2nd window
	my_label = Label(top, image=my_img).pack() #make image appear
	closeTop = Button(top, text="close window", command=top.destroy).pack()#closes top

Button(root, text="open in new window", command=openWindow).pack()
closeRoot = Button(root, text="close window", command=root.destroy).pack()#closes root
mainloop()