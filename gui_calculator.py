import tkinter as tk



def summ():
    num1,num2 = entry1.get().split()
    label1 = tk.Label(gui, text = int(num1) + int(num2))
    canvas1.create_window(150,50,window=label1)

def substract():
    num1,num2 = entry1.get().split()
    label1 = tk.Label(gui, text = int(num1) - int(num2))
    canvas1.create_window(150,50,window=label1)

def divide():
    num1,num2 = entry1.get().split()
    label1 = tk.Label(gui, text = int(num1) / int(num2))
    canvas1.create_window(150,50,window=label1)

def multiply():
    num1,num2 = entry1.get().split()
    label1 = tk.Label(gui, text = int(num1) * int(num2))
    canvas1.create_window(150,50,window=label1)

if __name__ == "__main__":

    gui = tk.Tk(className = 'Calculator')
    gui.geometry('300x280')
    canvas1 = tk.Canvas(gui, width = 400, height = 70, bg='black')
    
    canvas1.pack()
    entry1 = tk.Entry(gui)

    canvas1.create_window(150,20,window=entry1)

    summ_button = tk.Button(text='summ', command=summ, width=30, height=2, bg='gray', fg='white', font='Helvetica')
    subs_button = tk.Button(text='substract', command=substract, width=30, height=2, bg='gray', fg='white', font='Helvetica')
    divide_button = tk.Button(text='divide', command=divide, width=30, height=2, bg='gray', fg='white', font='Helvetica') 
    multiply_button = tk.Button(text='multiply', command=multiply, width=30, height=2, bg='gray', fg='white', font='Helvetica')

    canvas1.create_window(30,40,window=summ_button)
    canvas1.create_window(30,60,window=subs_button)
    canvas1.create_window(30,70,window=divide_button)
    canvas1.create_window(30,50,window=multiply_button)

    summ_button.pack()
    subs_button.pack()
    multiply_button.pack()
    divide_button.pack()


    gui.mainloop()