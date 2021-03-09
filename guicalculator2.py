from tkinter import *
import tkinter.font as TkFont


#hello test for github commit from visual studio :)
# learning git in vscode

class myButton(Button):
    def __init__(self, text):
        self.text = text
        super().__init__()
        self['bg'] = 'white'
        self['text'] = self.text
        self['activebackground'] = 'darkgray'
        self['width'] = 5
        self['height'] = 2
        if self.text == ("1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9" or "0"):
            self['command'] = lambda:press(int(text))
        else:
            self['command'] = lambda:press(text)

result = ""

def press(num):
    global result
    result = result + str(num)
    #update the equation
    equation.set(result)


def calculate():
    try:
        global result
        summary = str(eval(result))

        equation.set(summary)
    except:
        equation.set("Error.")
        result = ""


def cleared():
    global result
    equation.set("")
    result = ""


if __name__ == "__main__":

    gui = Tk()

    gui.configure(background="gray")
    gui.title("Simplistic Calculator")
    gui.geometry("220x260")

    equation = StringVar()

    result_field = Entry(gui, textvariable=equation, bg="white", bd=8)
    result_field.config(font=('Courier', 20), width=11)
    result_field.place(x=10, y=1)

    add = myButton("+")
    substract = myButton("-")
    division = myButton("/")
    multiply = myButton("*")
    clear = Button(text="C", command=cleared, width=5, height=2, activebackground='darkgray', bg='white')
    equal = Button(text="=", command=calculate, width=5, height=2, activebackground='darkgray', bg='white')

    oneButton = myButton("1")
    twoButton = myButton("2")
    threeButton = myButton("3")
    fourButton = myButton("4")
    fiveButton = myButton("5")
    sixButton = myButton("6")
    sevenButton = myButton("7")
    eightButton = myButton("8")
    nineButton = myButton("9")
    zeroButton = myButton("0")

    #first row
    oneButton.place(x=10, y=58)
    twoButton.place(x=60, y=58)
    threeButton.place(x=110, y=58)
    add.place(x=160, y=58)

    #second row
    fourButton.place(x=10, y=108)
    fiveButton.place(x=60, y=108)
    sixButton.place(x=110, y=108)
    substract.place(x=160, y=108)

    #third row
    sevenButton.place(x=10, y=158)
    eightButton.place(x=60, y=158)
    nineButton.place(x=110, y=158)
    division.place(x=160, y=158)
    
    #fourth row
    clear.place(x=10, y=208)
    zeroButton.place(x=60, y=208)
    equal.place(x=110, y=208)
    multiply.place(x=160, y=208)

    gui.mainloop()
# To DO, set all configs into separate classes