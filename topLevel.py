from tkinter import *
 
class TopLevelWindow():
    def __init__(self, master, width, height):
        self.master = master
        self.master.geometry("%sx%s+400+400" % (width, height))
        self.master.title("Toplevel Window")
        
root = Tk()
root.title('Main Window')
root.iconbitmap('c:/gui/ico.png')
root.geometry("400x400")

def defaultSize(): #function to add a label on button click.
        root.geometry("400x400")

def resizeWindow(input):
    horizontalValue = Label(root, text=horizontal.get()).pack()
    root.geometry(str(horizontal.get()) + "x" + str(vertical.get()))
    verticalValue = Label(root, text=vertical.get()).pack()
    root.geometry(str(horizontal.get()) + "x" + str(vertical.get()))

top1 = Toplevel()
TopLevelWindow(top1, "400", "400")

horizontal = Scale(top1, from_=100, to=1920, orient=HORIZONTAL, command=resizeWindow)
horizontal.pack(anchor = N) #anchored to the bott(root, "400", "400")om

vertical = Scale(top1, from_=100, to=1080, command=resizeWindow) #vertical slider.pack(anchor = E) #important to pack on its own line, anchored to the right
vertical.pack(anchor = E)

resizeBtn = Button(top1, text="Default Size!!", command=defaultSize).pack()

root.mainloop()