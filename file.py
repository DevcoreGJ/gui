from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog


root = Tk()
root.title('open file')
root.iconbitmap('c:/gui/ico.png')

def open():
	global my_img
#creates an open file dialog and can filter by file type.
	root.filename = filedialog.askopenfilename(initialdir="/gui/images", title="Select A File", filetypes=(("jpg files", "*jpg"),("all files", "*.*")))

	my_label = Label(root, text=root.filename).pack() #returns location of file.
#image variable parses location from filename variable through a function to open images
	my_img = ImageTk.PhotoImage(Image.open(root.filename)) 
#attaches above functions to a label to display
	my_img_lbl= Label(image=my_img).pack()
#added a buton to control file dialog opening
my_btn = Button(root, text="open file", command=open).pack()

root.mainloop()