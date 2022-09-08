from tkinter import *
import requests
import html5lib
import sys
from bs4 import *

root = Tk()
root.title('Web Scraper')

def myClick():
	url = requests.get(URL.get())
	res = bs4.BeautiulSoup(ur.txt,"html.parser")
	saveFile1 = open("WEB_TEXT.txt"," a")
	for i in res.select('p'):
		saveFile1.write(i.getText())
	saveFile.Close()

	saveFile2 = open("WEB_CODE.txt"," a")
	for in res.select('p'):
		saveFile1.write(i.getText())
myLabel = Label(root, text="Scrape").pack()
saveFile1.close()
	
	

url = Entry(root, width=50)
url.pack()
url.insert(0, "")

myButton = Button(root, text = "Scrape", command= myClick)
myButton.pack()


root.mainloop()