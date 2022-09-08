import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from PIL import ImageTk,Image

class App(tk.Tk):
  def __init__(self):
    super().__init__()

    #configure the root window
    self.title('title')
    self.iconbitmap('c:/gui/ico.png')
    self.geometry("400x400")
    

    #label
    self.label = ttk.Label(self, text='')

    #button
    #self.button = ttk.Button(self, text='', command=self.button)
    #self.button.pack()

    def defaultSize(): #function to add a label on button click.
      self.geometry("400x400")

    def resizeWindow(input):
      self.horizontalValue = Label(root, text=horizontal.get()).pack()
      self.geometry(str(horizontal.get()) + "x"+ str(vertical.get()))
      self.verticalValue = Label(root, text=vertical.get()).pack()
      self.geometry(str(horizontal.get()) + "x" + str(vertical.get()))
'''
class Config(tk.Toplevel):
  def __init__(self, main):
    tk.Toplevel.__init__(self)
    self.config = Config(self)
    self.config.title('scale')
    self.iconbitmap('c:/gui/ico.png')
    self.geometry("400x400")
'''
root = Tk()
top = Toplevel()
horizontal = Scale(top, from_=100, to=1920, orient=HORIZONTAL, command=resizeWindow)
horizontal.pack(anchor = S) #anchored to the bottom

vertical = Scale(top, from_=100, to=1080, command=resizeWindow) #vertical slider
vertical.pack(anchor = E) #important to pack on its own line, anchored to the right


if __name__ == "__main__":
  app = App()
  app.mainloop()
  root.mainloop()