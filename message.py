from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title('MessageBox')
root.iconbitmap('c:/gui/ico.png')

def popup():
	response = messagebox.askyesno("This is my popup!", "Hello World!")
	Label(root, text=response).pack() #if yes it prints 1 if no it prints 0
	if response == 1:
		Label(root, text="you clicked yes!!").pack()
	else:
		Label(root, text="you clicked no!!").pack()

Button(root, text="popup", command=popup).pack()




mainloop()

'''
diferent types of popup boces
showinfo
showwarning
showerror
askquestion
askoktocancel
askyesno
'''
