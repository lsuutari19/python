from tkinter import *
import tkinter.font as TkFont


#hello test for github commit from visual studio :)
# learning git in vscode

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
 #       result = ""
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

    #all the buttons
    add = Button(text="+", command=lambda: press("+"), width=5, height=2, activebackground='darkgray', bg='white')
    substract = Button(text="-", command=lambda: press("-"), width=5, height=2, activebackground='darkgray', bg='white')
    division = Button(text="/", command=lambda: press("/"), width=5, height=2, activebackground='darkgray', bg='white')
    multiply = Button(text="*", command=lambda: press("*"), width=5, height=2, activebackground='darkgray', bg='white')
    clear = Button(text="C", command=cleared, width=5, height=2, activebackground='darkgray', bg='white')
    equal = Button(text="=", command=calculate, width=5, height=2, activebackground='darkgray', bg='white')

    oneButton = Button(text="1", command=lambda: press(1), width=5, height=2, activebackground='darkgray', bg='white')
    twoButton = Button(text="2", command=lambda: press(2), width=5, height=2, activebackground='darkgray', bg='white')
    threeButton = Button(text="3", command=lambda: press(3), width=5, height=2, activebackground='darkgray', bg='white')
    fourButton = Button(text="4", command=lambda: press(4), width=5, height=2, activebackground='darkgray', bg='white')
    fiveButton = Button(text="5", command=lambda: press(5), width=5, height=2, activebackground='darkgray', bg='white')
    sixButton = Button(text="6", command=lambda: press(6), width=5, height=2, activebackground='darkgray', bg='white')
    sevenButton = Button(text="7", command=lambda: press(7), width=5, height=2, activebackground='darkgray', bg='white')
    eightButton = Button(text="8", command=lambda: press(8), width=5, height=2, activebackground='darkgray', bg='white')
    nineButton = Button(text="9", command=lambda: press(9), width=5, height=2, activebackground='darkgray', bg='white')
    zeroButton = Button(text="0", command=lambda: press(0), width=5, height=2, activebackground='darkgray', bg='white')

    
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