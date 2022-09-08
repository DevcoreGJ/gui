from tkinter import *

root = Tk()
global errInvOp
errInvOp = "Not a valid operator please choose from the buttons provided."
root.title("Simple Calculator") # might not work come back later.

#e.insert(0, "Enter your name") don't need an entry box text
'''
def myClick():
	hello = "Hello " + e.get()
	myLabel = Label(root, text=hello)
	myLabel.pack()
'''
def buttonClick(number):
	#e.delete(0, END)
	current = e.get() # get current stuff inputted
	e.delete(0, END)
	e.insert(0, str(current) + str(number))

def buttonClear():
	e.delete(0, END)

def buttonPlus():
	num1 = e.get()
	global num01
	global math
	math = "plus"
	num01 = int(num1)
	e.delete(0, END)

def buttonEqual():
	num2 = e.get()
	e.delete(0, END)
	if math == "plus":
		e.insert(0, num01 + int(num2))
	elif math == "minus":
		e.insert(0, num01 - int(num2))
	elif math == "times":
		e.insert(0, num01 * int(num2))
	elif math == "divide":
		e.insert(0, num01 / int(num2))
	else:
		return err1InvOp

def buttonMinus():
	num1 = e.get()
	global num01
	global math
	math = "minus"
	num01 = int(num1)
	e.delete(0, END)

def buttonTimes():
	num1 = e.get()
	global num01
	global math
	math = "times"
	num01 = int(num1)
	e.delete(0, END)

def buttonDivide():
	num1 = e.get()
	global num01
	global math
	math = "divide"
	num01 = int(num1)
	e.delete(0, END)


#myButton = Button(root, text = "Submit", command = myClick)

# e define entry box

e = Entry(root, width=35, borderwidth = 5)

# define buttons

button1 = Button(root, text = "1", padx=40, pady=20, command=lambda: buttonClick(1))
button2 = Button(root, text = "2", padx=40, pady=20, command=lambda: buttonClick(2))
button3 = Button(root, text = "3", padx=40, pady=20, command=lambda: buttonClick(3))

button4 = Button(root, text = "4", padx=40, pady=20, command=lambda: buttonClick(4))
button5 = Button(root, text = "5", padx=40, pady=20, command=lambda: buttonClick(5))
button6 = Button(root, text = "6", padx=40, pady=20, command=lambda: buttonClick(6))

button7 = Button(root, text = "7", padx=40, pady=20, command=lambda: buttonClick(7))
button8 = Button(root, text = "8", padx=40, pady=20, command=lambda: buttonClick(8))
button9 = Button(root, text = "9", padx=40, pady=20, command=lambda: buttonClick(9))

button0 = Button(root, text = "0", padx=138, pady=20, command=lambda: buttonClick(0))
buttonClear = Button(root, text = "Clear",padx=31,pady=20,command= buttonClear)

buttonPlus = Button(root, text = "+", padx=39, pady=52, command= buttonPlus)
buttonEquals = Button(root, text = "=", padx=39, pady=52, command= buttonEqual)

buttonMinus = Button(root, text = "-", padx=39, pady=20, command= buttonMinus)
buttonTimes = Button(root, text = "x", padx=39, pady=20, command= buttonTimes)
buttonDivide = Button(root, text = "÷", padx=39, pady=20, command= buttonDivide)

# put buttons on the screen

e.grid(row = 0, column = 0, columnspan = 5, padx=10, pady=10)

buttonClear.grid(row = 1, column = 0)
buttonDivide.grid(row = 1, column = 1)
buttonTimes.grid(row = 1, column = 2)
buttonMinus.grid(row = 1, column = 3)

buttonPlus.grid(row = 2, column = 3, rowspan = 2)
buttonEquals.grid(row = 4, column = 3, rowspan = 2)

button9.grid(row = 2, column = 2)
button8.grid(row = 2, column = 1)
button7.grid(row = 2, column = 0)

button6.grid(row = 3, column = 2)
button5.grid(row = 3, column = 1)
button4.grid(row = 3, column = 0)

button3.grid(row = 4, column = 2)
button2.grid(row = 4, column = 1)
button1.grid(row = 4, column = 0)

button0.grid(row = 5, column = 0, columnspan = 3)


root.mainloop()
