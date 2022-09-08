from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Using Icons, Images and Exit Buttons')

'''
<a target="_blank" href="https://icons8.com/icon/80695/certificate">Certificate</a> icon by <a target="_blank" href="https://icons8.com">Icons8</a>
'''
# link to icon
root.iconbitmap('C:/gui/ico.png')
#locate images
myImg = ImageTk.PhotoImage(Image.open("C:/gui/images/budapestResized.jpg"))
myImg1 = ImageTk.PhotoImage(Image.open("C:/gui/images/castleResized.jpg"))
myImg2 = ImageTk.PhotoImage(Image.open("C:/gui/images/parliamentResized.jpg"))
myImg3 = ImageTk.PhotoImage(Image.open("C:/gui/images/statueResized.jpg"))
myImg4 = ImageTk.PhotoImage(Image.open("C:/gui/images/streetResized.jpg"))
#collate image list
imgList = [myImg, myImg1, myImg2, myImg3, myImg4,]

#statusChecker = imgList.Str(index(x[, start[, end]]))


#define status counter
status = Label(root, text="Image " + "1" + " of " + str(len(imgList)), bd=1, relief=SUNKEN, anchor=E) # anchor uses compass diretions

myLabel = Label(image=myImg)
myLabel.grid(row=0, column=0, columnspan=3)

def forward(imgNum): #refer to back function block comments
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

	status = Label(root, text="Image " + str(imgNum) + " of " + str(len(imgList)), bd=1, relief=SUNKEN, anchor=E)
	status.grid(row=2,column=0,columnspan=3, sticky=W+E)

def back(imgNum): # back button functionality
	# global variables
	global myLabel
	global buttonForward
	global buttonBack

	myLabel.grid_forget() # clear image before moving on to the next
	myLabel = Label(image=imgList[imgNum-1]) # subtract the list to previous image
	buttonForward = Button(root, text=">>", command=lambda: forward(imgNum+1)) # add list count to next image
	buttonBack = Button(root, text="<<", command=lambda: back(imgNum-1)) #quit app

	if imgNum == 1: #disable back button if count is exactly 1
		buttonBack = Button(root, text="<<", state=DISABLED)

#buttons printed

	myLabel.grid(row=0, column=0, columnspan=3)
	buttonBack.grid(row =1, column=0)
	buttonForward.grid(row=1,column=2)
# status bar prints indec from list for relevant image.
	status = Label(root, text="Image " + str(imgNum) + " of " + str(len(imgList)), bd=1, relief=SUNKEN, anchor=E)
	status.grid(row=2,column=0,columnspan=3, sticky=W+E) # sticky uses comapass directions


buttonBack = Button(root, text="<<", command=back, state=DISABLED)
buttonQuit = Button(root, text="Exit Program", command=root.quit)
buttonForward = Button(root, text=">>", command=lambda: forward(2))


buttonBack.grid(row =1, column=0)
buttonQuit.grid(row=1,column=1,pady=10)
buttonForward.grid(row=1,column=2)
status.grid(row=2,column=0,columnspan=3, sticky=W+E)
root.mainloop()