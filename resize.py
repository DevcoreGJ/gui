from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("reisze images")

image = Image.open("C:/gui/images/parliament.jpg")
'''
myImg1 = ImageTk.PhotoImage(Image.open("C:/gui/images/castle.jpg"))
myImg2 = ImageTk.PhotoImage(Image.open("C:/gui/images/parliament.jpg"))
myImg3 = ImageTk.PhotoImage(Image.open("C:/gui/images/statue.jpg"))
myImg4 = ImageTk.PhotoImage(Image.open("C:/gui/images/street.jpg"))
'''
budapestResized = image.resize((400, 266))
budapestResized.save("C:/gui/images/pariamentResized.jpg")
'''
myImg1.thumbnail((400, 400))image.save("castle-aspect.jpg")
myImg2.thumbnail((400, 400))image.save("parliament-aspect.jpg")
myImg3.thumbnail((400, 400))image.save("statue-aspect.jpg")
myImg4.thumbnail((400, 400))image.save("street-aspect.jpg")
'''

print(f"Original size : {image.size}")







root.mainloop()