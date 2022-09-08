from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Using Icons, Images and Exit Buttons')

'''
<a target="_blank" href="https://icons8.com/icon/80695/certificate">Certificate</a> icon by <a target="_blank" href="https://icons8.com">Icons8</a>
'''
# link to icon
root.iconbitmap('C:/gui/ico.png')

buttonQuit = Button(root, text="Exit Program", command=root.quit)

myImg = ImageTk.PhotoImage(Image.open("C:/gui/budapest.jpg"))
myLabel = Label(image=myImg).pack()








root.mainloop()