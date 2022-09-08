from tkinter import *
from PIL import ImageTk,Image


root = Tk()
root.title('title')
root.iconbitmap('c:/gui/ico.png')
root.geometry("400x400")
top = Toplevel()
top.geometry("400x400")

#vertical = Scale(root, from_=100, to=1080) #vertical slider
#vertical.pack(anchor = E) #important to pack on its own line, anchored to the right

#horizontalValue = Label(root, text=horizontal.get())
#horizontalValue.pack() # superfluous label as now attached to button function.

def defaultSize(): #function to add a label on button click.
		root.geometry("400x400")


def resizeWindow(input):
	horizontalValue = Label(root, text=horizontal.get()).pack()
	root.geometry(str(horizontal.get()) + "x"+ str(vertical.get()))
	verticalValue = Label(root, text=vertical.get()).pack()
	root.geometry(str(horizontal.get()) + "x" + str(vertical.get()))

horizontal = Scale(top, from_=100, to=1920, orient=HORIZONTAL, command=resizeWindow)
horizontal.pack(anchor = S) #anchored to the bottom

vertical = Scale(top, from_=100, to=1080, command=resizeWindow) #vertical slider
vertical.pack(anchor = E) #important to pack on its own line, anchored to the right

# button to activate above function
#valueBtn = Button(root, text="Click Me!", command=updateValue) button from old function
#valueBtn.pack()

resizeBtn = Button(top, text="Default Size!!", command=defaultSize)
resizeBtn.pack()

mainloop()
