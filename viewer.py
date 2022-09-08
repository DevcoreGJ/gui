from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Using Icons, Images and Exit Buttons')

'''
<a target="_blank" href="https://icons8.com/icon/80695/certificate">Certificate</a> icon by <a target="_blank" href="https://icons8.com">Icons8</a>
'''
# link to icon
root.iconbitmap('C:/gui/ico.png')

myImg = ImageTk.PhotoImage(Image.open("C:/gui/images/budapestResized.jpg"))
myImg1 = ImageTk.PhotoImage(Image.open("C:/gui/images/castleResized.jpg"))
myImg2 = ImageTk.PhotoImage(Image.open("C:/gui/images/parliamentResized.jpg"))
myImg3 = ImageTk.PhotoImage(Image.open("C:/gui/images/statueResized.jpg"))
myImg4 = ImageTk.PhotoImage(Image.open("C:/gui/images/streetResized.jpg"))

imgList = [myImg, myImg1, myImg2, myImg3, myImg4,]
myLabel = Label(image=myImg)
myLabel.grid(row=0, column=0, columnspan=3)

def forward(imgNum):
	global myLabel
	global buttonForward
	global buttonBack

	myLabel.grid_forget()
	myLabel = Label(image=imgList[imgNum-1])
	myLabel.grid(row=0, column=0, columnspan=3)
	buttonForward = Button(root, text=">>", command=lambda: forward(imgNum+1))
	buttonBack = Button(root, text="<<", command=lambda:back(imgNum-1))

	if imgNum == 5:
		buttonForward = Button(root, text=">>", state=DISABLED)

	myLabel.grid(row=0, column=0, columnspan=3)
	buttonBack.grid(row =1, column=0)
	buttonForward.grid(row=1,column=2)



def back(imgNum):
	global myLabel
	global buttonForward
	global buttonBack

	myLabel.grid_forget()
	myLabel = Label(image=imgList[imgNum-1])
	buttonForward = Button(root, text=">>", command=lambda: forward(imgNum+1))
	buttonBack = Button(root, text="<<", command=lambda: back(imgNum-1))

	if imgNum == 1:
		buttonBack = Button(root, text="<<", state=DISABLED)

	myLabel.grid(row=0, column=0, columnspan=3)
	buttonBack.grid(row =1, column=0)
	buttonForward.grid(row=1,column=2)
	#buttonForward = Button(root, text=">>", command=lambda: forward(imgNum+1))
	#buttonBack = Button(root, text="<<", command=lambda: back(imgNum-1))

buttonBack = Button(root, text="<<", command=back, state=DISABLED)
buttonQuit = Button(root, text="Exit Program", command=root.quit)
buttonForward = Button(root, text=">>", command=lambda: forward(2))


buttonBack.grid(row =1, column=0)
buttonQuit.grid(row=1,column=1)
buttonForward.grid(row=1,column=2)
root.mainloop()