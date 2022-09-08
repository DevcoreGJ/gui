from tkinter import *

root = Tk()

#creating a label widget
myLabel1 = Label(root, text =  "Hello World!").grid(row= 0, column = 0)
myLabel2 = Label(root, text =  "My Name Is Nic Ledger").grid(row= 1, column = 5)
myLabel3 = Label(root, text =  "                     ").grid(row= 1, column = 1)
# here we are shoving it onto the screen

'''
myLabel.pack()
# event loop
'''

#myLabel1.grid(row= 0, column = 0)

#myLabel2.grid(row= 1, column = 5)

#myLabel3.grid(row= 1, column = 1)

root.mainloop()